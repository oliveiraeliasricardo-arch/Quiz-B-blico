import React, { useState, useEffect, useRef } from 'react';
import {
  Difficulty,
  Question,
  PlayerScore,
  DuelSlot,
  DuelParticipant,
} from './types/quiz';
import { getQuestionsForRound } from './data/questions';
import {
  getCurrentPlayer,
  saveCurrentPlayer,
  SavedPlayer,
} from './utils/storage';
import {
  getInitialCachedLeaderboard,
  saveOnlineScore,
  sortScores,
  subscribeToOnlineLeaderboard,
} from './utils/leaderboardService';
import { normalizeRoomCode } from './utils/duelService';
import { sound } from './utils/sound';
import { Navbar } from './components/Navbar';
import { PlayerSetup } from './components/PlayerSetup';
import { QuizScreen } from './components/QuizScreen';
import { ResultsScreen } from './components/ResultsScreen';
import { LeaderboardModal } from './components/LeaderboardModal';
import { OfflineIndicator } from './components/OfflineIndicator';
import { DuelLobby } from './components/DuelLobby';
import { DuelQuizScreen, DuelHistoryItem } from './components/DuelQuizScreen';
import { DuelResultsScreen } from './components/DuelResultsScreen';
import { BookOpen } from 'lucide-react';

type AppView =
  | 'setup'
  | 'quiz'
  | 'results'
  | 'duel-lobby'
  | 'duel-quiz'
  | 'duel-results';

function getInitialDuelInviteCode(): string {
  if (typeof window === 'undefined') return '';
  const params = new URLSearchParams(window.location.search);
  const raw = params.get('duel');
  return raw ? normalizeRoomCode(raw) : '';
}

export default function App() {
  const initialInvite = getInitialDuelInviteCode();

  const [view, setView] = useState<AppView>(
    initialInvite.length === 6 ? 'duel-lobby' : 'setup'
  );
  const [duelInviteCode, setDuelInviteCode] = useState<string>(initialInvite);
  const [player, setPlayer] = useState<SavedPlayer>(getCurrentPlayer());
  const [difficulty, setDifficulty] = useState<Difficulty | 'misto'>('medio');
  const [activeQuestions, setActiveQuestions] = useState<Question[]>([]);

  // Modais
  const [isLeaderboardOpen, setIsLeaderboardOpen] = useState(false);

  // Placar Geral Online (sincronizado em tempo real com Firestore)
  const [leaderboard, setLeaderboard] = useState<PlayerScore[]>(
    getInitialCachedLeaderboard()
  );

  useEffect(() => {
    const unsubscribe = subscribeToOnlineLeaderboard((onlineScores) => {
      setLeaderboard(onlineScores);
    });
    return () => unsubscribe();
  }, []);

  // Resultados da rodada solo de 20 questões
  const [roundResults, setRoundResults] = useState<{
    score: number;
    correctAnswers: number;
    totalQuestions: number;
    timeSpentSeconds: number;
    history: {
      question: Question;
      selectedOption: number;
      isCorrect: boolean;
    }[];
  } | null>(null);

  // Estado do Duelo 2 Jogadores
  const [duelSession, setDuelSession] = useState<{
    roomCode: string;
    slot: DuelSlot;
    difficulty: Difficulty | 'misto';
    questions: Question[];
  } | null>(null);

  const [duelFinalResults, setDuelFinalResults] = useState<{
    host: DuelParticipant;
    guest: DuelParticipant;
    myHistory: DuelHistoryItem[];
  } | null>(null);

  const savedDuelKeysRef = useRef<Set<string>>(new Set());

  const clearDuelQueryParam = () => {
    if (typeof window !== 'undefined' && window.location.search.includes('duel=')) {
      const url = new URL(window.location.href);
      url.searchParams.delete('duel');
      window.history.replaceState({}, '', url.pathname + url.search);
    }
  };

  // Iniciar Quiz Solo de 20 questões
  const handleStartQuiz = (
    playerName: string,
    avatar: string,
    chosenDifficulty: Difficulty | 'misto'
  ) => {
    const updatedPlayer = { name: playerName, avatar };
    setPlayer(updatedPlayer);
    saveCurrentPlayer(updatedPlayer);
    setDifficulty(chosenDifficulty);

    const round20Questions = getQuestionsForRound(chosenDifficulty, 20);
    setActiveQuestions(round20Questions);
    setRoundResults(null);
    setView('quiz');
  };

  // Concluir Quiz Solo de 20 questões
  const handleCompleteQuiz = async (results: {
    score: number;
    correctAnswers: number;
    totalQuestions: number;
    timeSpentSeconds: number;
    history: {
      question: Question;
      selectedOption: number;
      isCorrect: boolean;
    }[];
  }) => {
    setRoundResults(results);

    const payload = {
      playerName: player.name || 'Discípulo Anônimo',
      playerAvatar: player.avatar || '📜',
      score: results.score,
      correctAnswers: results.correctAnswers,
      totalQuestions: results.totalQuestions,
      accuracy: Math.round((results.correctAnswers / results.totalQuestions) * 100),
      difficulty,
      timeSpentSeconds: results.timeSpentSeconds,
    };

    const optimisticScore: PlayerScore = {
      id: `pending_${Date.now()}`,
      ...payload,
      date: new Date().toISOString(),
    };
    setLeaderboard((prev) => sortScores([optimisticScore, ...prev]));
    setView('results');

    try {
      await saveOnlineScore(payload);
    } catch (error) {
      console.error('Erro ao salvar pontuação online:', error);
    }
  };

  const handlePlayAgain = () => {
    const newQuestions = getQuestionsForRound(difficulty, 20);
    setActiveQuestions(newQuestions);
    setRoundResults(null);
    setView('quiz');
  };

  const handleReturnToSetup = () => {
    clearDuelQueryParam();
    setDuelInviteCode('');
    setDuelSession(null);
    setDuelFinalResults(null);
    setRoundResults(null);
    setView('setup');
  };

  const handleOpenDuel = () => {
    setDuelFinalResults(null);
    setDuelSession(null);
    setView('duel-lobby');
  };

  const handleStartDuel = (session: {
    roomCode: string;
    slot: DuelSlot;
    difficulty: Difficulty | 'misto';
    questions: Question[];
  }) => {
    clearDuelQueryParam();
    setDuelInviteCode('');
    setDuelSession(session);
    setDuelFinalResults(null);
    setView('duel-quiz');
  };

  const handleFinishDuel = async (result: {
    host: DuelParticipant;
    guest: DuelParticipant;
    myHistory: DuelHistoryItem[];
  }) => {
    setDuelFinalResults(result);
    setView('duel-results');

    if (duelSession) {
      const saveKey = `${duelSession.roomCode}_${duelSession.slot}`;
      if (!savedDuelKeysRef.current.has(saveKey)) {
        savedDuelKeysRef.current.add(saveKey);
        const me = duelSession.slot === 'host' ? result.host : result.guest;
        try {
          await saveOnlineScore({
            playerName: me.playerName,
            playerAvatar: me.playerAvatar,
            score: me.score,
            correctAnswers: me.correctAnswers,
            totalQuestions: 20,
            accuracy: Math.round((me.correctAnswers / 20) * 100),
            difficulty: duelSession.difficulty,
            timeSpentSeconds: Math.max(1, Math.round(me.totalTimeMs / 1000)),
          });
        } catch (error) {
          console.error('Erro ao registrar resultado do duelo no placar:', error);
        }
      }
    }
  };

  return (
    <div className="min-h-screen bg-stone-950 text-stone-100 flex flex-col selection:bg-amber-500 selection:text-amber-950 relative overflow-x-hidden">
      {/* Background Decorativo com Luz Celestial Dourada */}
      <div className="fixed inset-0 pointer-events-none z-0 overflow-hidden">
        <div className="absolute -top-40 left-1/2 -translate-x-1/2 w-[800px] h-[500px] bg-amber-600/10 rounded-full blur-[140px]" />
        <div className="absolute top-1/3 -left-40 w-[500px] h-[500px] bg-amber-700/5 rounded-full blur-[160px]" />
        <div className="absolute bottom-0 -right-40 w-[600px] h-[600px] bg-amber-600/10 rounded-full blur-[180px]" />
      </div>

      {/* Barra de Navegação */}
      <Navbar
        player={player}
        onOpenLeaderboard={() => setIsLeaderboardOpen(true)}
        onNewGame={handleReturnToSetup}
        isInGame={view === 'quiz' || view === 'duel-quiz'}
      />

      {/* Conteúdo Principal */}
      <main className="flex-1 relative z-10 flex flex-col justify-center">
        {view === 'setup' && (
          <PlayerSetup
            initialPlayer={player}
            onStartQuiz={handleStartQuiz}
            onOpenLeaderboard={() => setIsLeaderboardOpen(true)}
            onOpenDuel={handleOpenDuel}
          />
        )}

        {view === 'quiz' && activeQuestions.length > 0 && (
          <QuizScreen
            questions={activeQuestions}
            playerName={player.name}
            playerAvatar={player.avatar}
            difficulty={difficulty}
            onCompleteQuiz={handleCompleteQuiz}
          />
        )}

        {view === 'results' && roundResults && (
          <ResultsScreen
            score={roundResults.score}
            correctAnswers={roundResults.correctAnswers}
            totalQuestions={roundResults.totalQuestions}
            timeSpentSeconds={roundResults.timeSpentSeconds}
            playerName={player.name}
            playerAvatar={player.avatar}
            difficulty={difficulty}
            history={roundResults.history}
            leaderboard={leaderboard}
            onPlayAgain={handlePlayAgain}
            onOpenLeaderboard={() => setIsLeaderboardOpen(true)}
            onChangeSetup={handleReturnToSetup}
          />
        )}

        {view === 'duel-lobby' && (
          <DuelLobby
            initialPlayer={player}
            initialInviteCode={duelInviteCode}
            onUpdatePlayer={(updated) => {
              setPlayer(updated);
              saveCurrentPlayer(updated);
            }}
            onStartDuel={handleStartDuel}
            onBack={handleReturnToSetup}
          />
        )}

        {view === 'duel-quiz' && duelSession && (
          <DuelQuizScreen
            roomCode={duelSession.roomCode}
            slot={duelSession.slot}
            questions={duelSession.questions}
            playerName={player.name || 'Discípulo'}
            playerAvatar={player.avatar || '📜'}
            difficulty={duelSession.difficulty}
            onFinishDuel={handleFinishDuel}
          />
        )}

        {view === 'duel-results' && duelSession && duelFinalResults && (
          <DuelResultsScreen
            roomCode={duelSession.roomCode}
            mySlot={duelSession.slot}
            difficulty={duelSession.difficulty}
            questions={duelSession.questions}
            host={duelFinalResults.host}
            guest={duelFinalResults.guest}
            myHistory={duelFinalResults.myHistory}
            onNewDuel={handleOpenDuel}
            onReturnHome={handleReturnToSetup}
          />
        )}
      </main>

      {/* Rodapé Informativo */}
      <footer className="relative z-10 border-t border-amber-900/30 bg-amber-950/40 text-amber-300/60 text-xs py-6 mt-12">
        <div className="max-w-6xl mx-auto px-4 flex flex-col sm:flex-row items-center justify-between gap-3 text-center sm:text-left">
          <div className="flex items-center gap-2">
            <BookOpen className="w-4 h-4 text-amber-500" />
            <span className="font-serif font-bold text-amber-200">
              Quiz Bíblico da Bíblia Sagrada
            </span>
            <span>•</span>
            <span>1.000 Questões de Gênesis ao Apocalipse</span>
          </div>

          <div className="flex items-center gap-4 text-[11px]">
            <button
              onClick={() => {
                sound.playClick();
                setIsLeaderboardOpen(true);
              }}
              className="hover:text-amber-200 underline decoration-amber-700 underline-offset-4 cursor-pointer"
            >
              Ver Placar de Líderes
            </button>
          </div>
        </div>
      </footer>

      {/* Modais Globais */}
      <LeaderboardModal
        isOpen={isLeaderboardOpen}
        onClose={() => setIsLeaderboardOpen(false)}
        scores={leaderboard}
        currentPlayerName={player.name}
        onScoresReset={(newScores) => setLeaderboard(newScores)}
      />

      <OfflineIndicator />
    </div>
  );
}
