import React, { useEffect, useState } from 'react';
import confetti from 'canvas-confetti';
import { Question, Difficulty, PlayerScore } from '../types/quiz';
import { sound } from '../utils/sound';
import { formatTime } from '../utils/storage';
import { 
  Trophy, 
  RotateCcw, 
  Award, 
  CheckCircle2, 
  XCircle, 
  Clock, 
  Target, 
  BookOpen, 
  Share2, 
  ArrowRight,
  Filter
} from 'lucide-react';

interface ResultsScreenProps {
  score: number;
  correctAnswers: number;
  totalQuestions: number;
  timeSpentSeconds: number;
  playerName: string;
  playerAvatar: string;
  difficulty: Difficulty | 'misto';
  history: {
    question: Question;
    selectedOption: number;
    isCorrect: boolean;
  }[];
  leaderboard: PlayerScore[];
  onPlayAgain: () => void;
  onOpenLeaderboard: () => void;
  onChangeSetup: () => void;
}

export const ResultsScreen: React.FC<ResultsScreenProps> = ({
  score,
  correctAnswers,
  totalQuestions,
  timeSpentSeconds,
  playerName,
  playerAvatar,
  difficulty,
  history,
  leaderboard,
  onPlayAgain,
  onOpenLeaderboard,
  onChangeSetup,
}) => {
  const [filter, setFilter] = useState<'all' | 'correct' | 'wrong'>('all');
  const [copied, setCopied] = useState(false);

  const accuracy = Math.round((correctAnswers / totalQuestions) * 100);

  // Calcula a colocação/posição no placar
  const normalizedPlayerName =
    (playerName || 'Discípulo Anônimo').trim().slice(0, 32) || 'Discípulo';
  const roundedTime = Math.min(86400, Math.max(0, Math.round(timeSpentSeconds)));
  const exactRank = leaderboard.findIndex(
    (s) =>
      s.playerName === normalizedPlayerName &&
      s.score === score &&
      s.correctAnswers === correctAnswers &&
      s.timeSpentSeconds === roundedTime
  );
  const currentRank =
    (exactRank >= 0
      ? exactRank
      : leaderboard.findIndex(
          (s) =>
            s.playerName === normalizedPlayerName &&
            s.score === score &&
            s.correctAnswers === correctAnswers
        )) + 1;

  useEffect(() => {
    // Solta confetes se desempenho bom (>= 60%)
    if (accuracy >= 60) {
      try {
        confetti({
          particleCount: 80,
          spread: 70,
          origin: { y: 0.6 },
          colors: ['#f59e0b', '#fbbf24', '#d97706', '#10b981', '#ffffff'],
        });
      } catch {}
    }
  }, [accuracy]);

  // Título bíblico baseado na pontuação
  const getBiblicalTitle = () => {
    if (accuracy === 100) return { title: 'Mestre das Escrituras!', desc: 'Perfeito! Conhecimento digno de Esdras o escriba!' };
    if (accuracy >= 80) return { title: 'Bereano Exemplar!', desc: 'Examinou as Escrituras com diligência e sabedoria!' };
    if (accuracy >= 60) return { title: 'Discípulo Fiel!', desc: 'Bom conhecimento bíblico, continue crescendo na graça!' };
    if (accuracy >= 40) return { title: 'Peregrino Esforçado!', desc: 'Um bom começo! A Palavra é lâmpada para os teus pés!' };
    return { title: 'Buscador da Verdade!', desc: 'Continue lendo a Bíblia diariamente e tente novamente!' };
  };

  const titleInfo = getBiblicalTitle();

  const filteredHistory = history.filter((item) => {
    if (filter === 'correct') return item.isCorrect;
    if (filter === 'wrong') return !item.isCorrect;
    return true;
  });

  const handleShare = () => {
    sound.playClick();
    const text = `📖 Quiz Bíblico (1.000 Questões)
Jogador: ${playerName}
Acertos: ${correctAnswers}/${totalQuestions} (${accuracy}%)
Pontuação: ${score} pts
Dificuldade: ${difficulty.toUpperCase()}
Posição no Placar: #${currentRank > 0 ? currentRank : 1}º Lugar`;

    if (navigator.clipboard) {
      navigator.clipboard.writeText(text);
      setCopied(true);
      setTimeout(() => setCopied(false), 2500);
    }
  };

  const letters = ['A', 'B', 'C', 'D'];

  return (
    <div className="max-w-3xl mx-auto px-4 py-8 space-y-8">
      {/* Card Principal de Vitória / Conclusão */}
      <div className="bg-gradient-to-b from-amber-950/80 to-amber-950/40 backdrop-blur-md border border-amber-800/50 rounded-3xl p-6 sm:p-10 shadow-2xl text-center relative overflow-hidden">
        
        {/* Posicionamento no placar em destaque */}
        {currentRank > 0 && (
          <div className="inline-flex items-center gap-2 px-4 py-1.5 rounded-full bg-amber-500/20 border border-amber-400/40 text-amber-200 text-xs sm:text-sm font-bold mb-4 shadow-sm">
            <Trophy className="w-4 h-4 text-amber-400" />
            <span>Classificado em #{currentRank}º Lugar no Placar Geral!</span>
          </div>
        )}

        <div className="text-4xl sm:text-5xl mb-2">{playerAvatar}</div>
        <h1 className="text-2xl sm:text-4xl font-serif font-black text-amber-100 tracking-tight mb-2">
          {titleInfo.title}
        </h1>
        <p className="text-amber-200/80 text-sm sm:text-base max-w-md mx-auto mb-6">
          {titleInfo.desc}
        </p>

        {/* Grade de Estatísticas */}
        <div className="grid grid-cols-2 sm:grid-cols-4 gap-3 max-w-xl mx-auto mb-8 text-left">
          
          <div className="p-3.5 rounded-2xl bg-amber-900/30 border border-amber-700/40">
            <div className="flex items-center gap-1.5 text-xs text-amber-400/80 mb-1">
              <Award className="w-4 h-4 text-amber-400" />
              <span>Pontos</span>
            </div>
            <div className="text-2xl font-bold font-mono text-amber-100">{score}</div>
          </div>

          <div className="p-3.5 rounded-2xl bg-amber-900/30 border border-amber-700/40">
            <div className="flex items-center gap-1.5 text-xs text-amber-400/80 mb-1">
              <Target className="w-4 h-4 text-emerald-400" />
              <span>Acertos</span>
            </div>
            <div className="text-2xl font-bold font-mono text-emerald-300">
              {correctAnswers}/{totalQuestions}
            </div>
          </div>

          <div className="p-3.5 rounded-2xl bg-amber-900/30 border border-amber-700/40">
            <div className="flex items-center gap-1.5 text-xs text-amber-400/80 mb-1">
              <CheckCircle2 className="w-4 h-4 text-blue-400" />
              <span>Precisão</span>
            </div>
            <div className="text-2xl font-bold font-mono text-amber-200">{accuracy}%</div>
          </div>

          <div className="p-3.5 rounded-2xl bg-amber-900/30 border border-amber-700/40">
            <div className="flex items-center gap-1.5 text-xs text-amber-400/80 mb-1">
              <Clock className="w-4 h-4 text-amber-400" />
              <span>Tempo</span>
            </div>
            <div className="text-2xl font-bold font-mono text-amber-200">
              {formatTime(timeSpentSeconds)}
            </div>
          </div>

        </div>

        {/* Botões de Ação Principal */}
        <div className="flex flex-wrap items-center justify-center gap-3">
          <button
            onClick={() => {
              sound.playClick();
              onPlayAgain();
            }}
            className="px-6 py-3.5 rounded-xl font-bold text-sm text-amber-950 bg-gradient-to-r from-amber-400 to-amber-500 hover:from-amber-300 hover:to-amber-400 shadow-lg shadow-amber-950/40 border border-amber-200 flex items-center gap-2 cursor-pointer transition-all active:scale-95"
          >
            <RotateCcw className="w-4 h-4" />
            <span>Jogar Novamente (Novas 20 Questões)</span>
          </button>

          <button
            onClick={() => {
              sound.playClick();
              onOpenLeaderboard();
            }}
            className="px-5 py-3.5 rounded-xl font-semibold text-sm text-amber-200 bg-amber-900/50 hover:bg-amber-900/80 border border-amber-700/50 flex items-center gap-2 cursor-pointer transition-all active:scale-95"
          >
            <Trophy className="w-4 h-4 text-amber-400" />
            <span>Ver Placar com Posições</span>
          </button>

          <button
            onClick={handleShare}
            className="px-4 py-3.5 rounded-xl font-semibold text-sm text-amber-300 hover:text-white bg-amber-950/60 hover:bg-amber-900/40 border border-amber-800/40 flex items-center gap-1.5 transition-all"
            title="Copiar resumo do resultado"
          >
            <Share2 className="w-4 h-4" />
            <span>{copied ? 'Copiado!' : 'Compartilhar'}</span>
          </button>
        </div>
      </div>

      {/* Revisão Completa das 20 Questões Respondidas */}
      <div className="space-y-4">
        <div className="flex flex-wrap items-center justify-between gap-3">
          <div>
            <h2 className="text-xl font-serif font-bold text-amber-100 flex items-center gap-2">
              <BookOpen className="w-5 h-5 text-amber-400" />
              <span>Gabarito Completo da Partida (20 Questões)</span>
            </h2>
            <p className="text-xs text-amber-300/70">
              Revise suas respostas, verifique a opção correta e estude o contexto bíblico
            </p>
          </div>

          {/* Filtros de Revisão */}
          <div className="flex items-center gap-1.5 p-1 rounded-xl bg-amber-950/60 border border-amber-800/40 text-xs">
            <button
              onClick={() => setFilter('all')}
              className={`px-3 py-1 rounded-lg font-medium transition-all ${
                filter === 'all' ? 'bg-amber-600 text-white shadow-sm' : 'text-amber-300/70 hover:text-amber-200'
              }`}
            >
              Todas (20)
            </button>
            <button
              onClick={() => setFilter('correct')}
              className={`px-3 py-1 rounded-lg font-medium transition-all ${
                filter === 'correct' ? 'bg-emerald-600 text-white shadow-sm' : 'text-emerald-400/70 hover:text-emerald-300'
              }`}
            >
              Acertos ({correctAnswers})
            </button>
            <button
              onClick={() => setFilter('wrong')}
              className={`px-3 py-1 rounded-lg font-medium transition-all ${
                filter === 'wrong' ? 'bg-red-600 text-white shadow-sm' : 'text-red-400/70 hover:text-red-300'
              }`}
            >
              Erros ({totalQuestions - correctAnswers})
            </button>
          </div>
        </div>

        {/* Lista das Questões */}
        <div className="space-y-3">
          {filteredHistory.map((item, idx) => {
            const q = item.question;
            const correctOptText = q.options[q.correctIndex];
            const userOptText = q.options[item.selectedOption];

            return (
              <div
                key={idx}
                className={`p-5 rounded-2xl border transition-all ${
                  item.isCorrect
                    ? 'bg-amber-950/20 border-emerald-900/40 hover:border-emerald-700/50'
                    : 'bg-red-950/15 border-red-900/40 hover:border-red-700/50'
                }`}
              >
                <div className="flex items-start justify-between gap-3 mb-2">
                  <div className="flex items-center gap-2 text-xs">
                    <span className="font-mono text-amber-400/60">Q#{idx + 1}</span>
                    <span className="text-amber-300 font-semibold">{q.book}</span>
                    <span className="text-amber-500">•</span>
                    <span className="text-amber-300/80">{q.reference}</span>
                  </div>

                  {item.isCorrect ? (
                    <span className="inline-flex items-center gap-1 px-2.5 py-0.5 rounded-full text-xs font-bold bg-emerald-900/40 text-emerald-300 border border-emerald-500/30">
                      <CheckCircle2 className="w-3.5 h-3.5 text-emerald-400" />
                      Acertou
                    </span>
                  ) : (
                    <span className="inline-flex items-center gap-1 px-2.5 py-0.5 rounded-full text-xs font-bold bg-red-900/40 text-red-300 border border-red-500/30">
                      <XCircle className="w-3.5 h-3.5 text-red-400" />
                      Errou
                    </span>
                  )}
                </div>

                <h3 className="text-base font-serif font-bold text-amber-100 mb-3">
                  {q.question}
                </h3>

                {/* Resposta do usuário vs Resposta correta */}
                <div className="grid grid-cols-1 sm:grid-cols-2 gap-2 text-xs mb-3">
                  <div className={`p-2.5 rounded-lg border ${
                    item.isCorrect 
                      ? 'bg-emerald-950/40 border-emerald-700/50 text-emerald-200' 
                      : 'bg-red-950/40 border-red-700/50 text-red-200'
                  }`}>
                    <span className="text-[10px] font-bold uppercase tracking-wider block opacity-70 mb-0.5">
                      Sua Resposta:
                    </span>
                    <span className="font-medium">
                      Opção {letters[item.selectedOption]}: {userOptText}
                    </span>
                  </div>

                  {!item.isCorrect && (
                    <div className="p-2.5 rounded-lg border bg-emerald-950/40 border-emerald-600/50 text-emerald-200">
                      <span className="text-[10px] font-bold uppercase tracking-wider block text-emerald-400 mb-0.5">
                        Resposta Correta:
                      </span>
                      <span className="font-semibold text-emerald-100">
                        Opção {letters[q.correctIndex]}: {correctOptText}
                      </span>
                    </div>
                  )}
                </div>

                {/* Comentário Bíblico */}
                <div className="text-xs text-amber-200/80 italic bg-amber-900/20 p-3 rounded-lg border border-amber-800/30">
                  <strong className="text-amber-300 not-italic font-semibold">Contexto Bíblico: </strong>
                  {q.explanation}
                </div>
              </div>
            );
          })}
        </div>
      </div>
    </div>
  );
};
