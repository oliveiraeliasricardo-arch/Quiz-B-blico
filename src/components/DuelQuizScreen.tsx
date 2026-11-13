import React, { useEffect, useRef, useState } from 'react';
import {
  Difficulty,
  DuelParticipant,
  DuelRoom,
  DuelSlot,
  Question,
} from '../types/quiz';
import {
  formatResponseMs,
  markDuelFinished,
  submitDuelAnswerProgress,
  subscribeToDuelSession,
} from '../utils/duelService';
import { sound } from '../utils/sound';
import {
  ArrowRight,
  Award,
  BookOpen,
  CheckCircle2,
  Clock,
  Flame,
  Loader2,
  Swords,
  Target,
  XCircle,
} from 'lucide-react';

export interface DuelHistoryItem {
  question: Question;
  selectedOption: number;
  isCorrect: boolean;
  responseTimeMs: number;
}

interface DuelQuizScreenProps {
  roomCode: string;
  slot: DuelSlot;
  questions: Question[];
  playerName: string;
  playerAvatar: string;
  difficulty: Difficulty | 'misto';
  onFinishDuel: (result: {
    host: DuelParticipant;
    guest: DuelParticipant;
    myHistory: DuelHistoryItem[];
  }) => void;
}

export const DuelQuizScreen: React.FC<DuelQuizScreenProps> = ({
  roomCode,
  slot,
  questions,
  playerName,
  playerAvatar,
  difficulty,
  onFinishDuel,
}) => {
  const [countdown, setCountdown] = useState(3);
  const [currentIndex, setCurrentIndex] = useState(0);
  const [selectedOption, setSelectedOption] = useState<number | null>(null);
  const [isAnswered, setIsAnswered] = useState(false);

  const [score, setScore] = useState(0);
  const [streak, setStreak] = useState(0);
  const [correctCount, setCorrectCount] = useState(0);
  const [answerTimesMs, setAnswerTimesMs] = useState<number[]>([]);
  const [answersCorrect, setAnswersCorrect] = useState<boolean[]>([]);
  const [history, setHistory] = useState<DuelHistoryItem[]>([]);
  const [localFinished, setLocalFinished] = useState(false);

  const [roomState, setRoomState] = useState<DuelRoom | null>(null);
  const [hostData, setHostData] = useState<DuelParticipant | null>(null);
  const [guestData, setGuestData] = useState<DuelParticipant | null>(null);

  const [questionElapsedMs, setQuestionElapsedMs] = useState(0);
  const questionShownAtRef = useRef<number>(performance.now());
  const hasTransitionedToResultsRef = useRef(false);

  // Inscreve-se no progresso em tempo real dos dois jogadores
  useEffect(() => {
    const unsubscribe = subscribeToDuelSession(roomCode, {
      onRoom: (room) => setRoomState(room),
      onHost: (host) => setHostData(host),
      onGuest: (guest) => setGuestData(guest),
    });
    return () => unsubscribe();
  }, [roomCode]);

  // Contagem regressiva inicial sincronizada (3 -> 2 -> 1 -> Já!)
  useEffect(() => {
    if (countdown <= 0) {
      questionShownAtRef.current = performance.now();
      setQuestionElapsedMs(0);
      return;
    }
    const timer = setTimeout(() => {
      sound.playClick();
      setCountdown((prev) => prev - 1);
    }, 750);
    return () => clearTimeout(timer);
  }, [countdown]);

  // Cronômetro em tempo real da questão atual
  useEffect(() => {
    if (countdown > 0 || isAnswered || localFinished) return;
    const interval = setInterval(() => {
      setQuestionElapsedMs(Math.max(0, performance.now() - questionShownAtRef.current));
    }, 100);
    return () => clearInterval(interval);
  }, [countdown, isAnswered, localFinished, currentIndex]);

  // Transiciona para o comparativo final assim que ambos concluírem as 20 questões
  useEffect(() => {
    if (
      localFinished &&
      hostData?.finished &&
      guestData?.finished &&
      !hasTransitionedToResultsRef.current
    ) {
      hasTransitionedToResultsRef.current = true;
      if (roomState?.status === 'playing') {
        markDuelFinished(roomCode).catch(() => {});
      }
      sound.playVictory();
      onFinishDuel({
        host: hostData,
        guest: guestData,
        myHistory: history,
      });
    }
  }, [localFinished, hostData, guestData, roomState, roomCode, history, onFinishDuel]);

  const currentQ = questions[currentIndex];
  const isLastQuestion = currentIndex === questions.length - 1;
  const opponentData = slot === 'host' ? guestData : hostData;

  const totalMyTimeMs = answerTimesMs.reduce((acc, ms) => acc + ms, 0);
  const avgMyTimeMs =
    answerTimesMs.length > 0 ? Math.round(totalMyTimeMs / answerTimesMs.length) : 0;

  const handleSelectOption = (index: number) => {
    if (countdown > 0 || isAnswered || localFinished || !currentQ) return;

    const responseTimeMs = Math.min(
      3600000,
      Math.max(150, Math.round(performance.now() - questionShownAtRef.current))
    );
    setQuestionElapsedMs(responseTimeMs);
    setSelectedOption(index);
    setIsAnswered(true);

    const isCorrect = index === currentQ.correctIndex;
    let nextScore = score;
    let nextCorrect = correctCount;

    if (isCorrect) {
      sound.playCorrect();
      const streakBonus = Math.min(streak * 10, 50);
      nextScore = score + 100 + streakBonus;
      nextCorrect = correctCount + 1;
      setScore(nextScore);
      setCorrectCount(nextCorrect);
      setStreak((prev) => prev + 1);
    } else {
      sound.playWrong();
      setStreak(0);
    }

    const nextTimes = [...answerTimesMs, responseTimeMs];
    const nextCorrectList = [...answersCorrect, isCorrect];
    const nextAnsweredCount = nextTimes.length;

    setAnswerTimesMs(nextTimes);
    setAnswersCorrect(nextCorrectList);
    setHistory((prev) => [
      ...prev,
      {
        question: currentQ,
        selectedOption: index,
        isCorrect,
        responseTimeMs,
      },
    ]);

    submitDuelAnswerProgress({
      roomCode,
      slot,
      currentQuestionIndex: isLastQuestion ? questions.length : currentIndex + 1,
      answeredCount: nextAnsweredCount,
      correctAnswers: nextCorrect,
      score: nextScore,
      answerTimesMs: nextTimes,
      answersCorrect: nextCorrectList,
      finished: false,
    }).catch((err) => {
      console.error('Erro ao sincronizar resposta do duelo:', err);
    });
  };

  const handleNextQuestion = () => {
    sound.playClick();
    if (isLastQuestion) {
      setLocalFinished(true);
      submitDuelAnswerProgress({
        roomCode,
        slot,
        currentQuestionIndex: questions.length,
        answeredCount: answerTimesMs.length,
        correctAnswers: correctCount,
        score,
        answerTimesMs,
        answersCorrect,
        finished: true,
      }).catch((err) => {
        console.error('Erro ao finalizar duelo do jogador:', err);
      });
    } else {
      setCurrentIndex((prev) => prev + 1);
      setSelectedOption(null);
      setIsAnswered(false);
      setQuestionElapsedMs(0);
      questionShownAtRef.current = performance.now();
    }
  };

  // Atalhos de teclado (1-4 e Enter)
  useEffect(() => {
    const handleKeyDown = (e: KeyboardEvent) => {
      if (countdown > 0 || localFinished) return;
      if (!isAnswered) {
        if (['1', '2', '3', '4'].includes(e.key)) {
          handleSelectOption(parseInt(e.key, 10) - 1);
        }
      } else if (e.key === 'Enter' || e.key === ' ') {
        e.preventDefault();
        handleNextQuestion();
      }
    };
    window.addEventListener('keydown', handleKeyDown);
    return () => window.removeEventListener('keydown', handleKeyDown);
  });

  const letters = ['A', 'B', 'C', 'D'];
  const myAccuracy =
    answerTimesMs.length > 0
      ? Math.round((correctCount / answerTimesMs.length) * 100)
      : 0;
  const oppAccuracy =
    opponentData && opponentData.answeredCount > 0
      ? Math.round((opponentData.correctAnswers / opponentData.answeredCount) * 100)
      : 0;

  return (
    <div className="max-w-3xl mx-auto px-4 py-6 sm:py-8 relative">
      {/* Overlay de contagem regressiva inicial sincronizada */}
      {countdown > 0 && (
        <div className="fixed inset-0 z-50 bg-stone-950/90 backdrop-blur-md flex items-center justify-center p-4">
          <div className="text-center space-y-4 animate-fadeIn">
            <div className="inline-flex items-center gap-2 px-4 py-1.5 rounded-full bg-amber-500/20 border border-amber-400/40 text-amber-200 text-xs font-bold uppercase tracking-wider">
              <Swords className="w-4 h-4 text-amber-400" />
              <span>Sala {roomCode} • Duelo Simultâneo</span>
            </div>
            <h2 className="text-2xl sm:text-3xl font-serif font-bold text-amber-100">
              {playerName} vs {opponentData?.playerName || 'Oponente'}
            </h2>
            <div className="text-7xl sm:text-8xl font-mono font-black text-amber-400 drop-shadow-lg">
              {countdown}
            </div>
            <p className="text-sm text-amber-200/80">
              Mesmas 20 questões • Vence quem tiver maior precisão e menor tempo!
            </p>
          </div>
        </div>
      )}

      {/* Placar Ao Vivo Cabeça-a-Cabeça */}
      <div className="bg-amber-950/70 backdrop-blur-md border border-amber-800/50 rounded-2xl p-4 shadow-xl mb-6 space-y-3">
        <div className="flex items-center justify-between text-[11px] text-amber-300/80 border-b border-amber-800/40 pb-2">
          <div className="flex items-center gap-2 font-bold">
            <Swords className="w-3.5 h-3.5 text-amber-400" />
            <span>Duelo Simultâneo • Sala {roomCode}</span>
          </div>
          <span className="uppercase font-semibold px-2 py-0.5 rounded bg-amber-900/60 border border-amber-700/40 text-amber-200">
            {difficulty}
          </span>
        </div>

        <div className="grid grid-cols-1 sm:grid-cols-2 gap-3">
          {/* Card Você */}
          <div className="p-3 rounded-xl bg-amber-900/35 border border-amber-500/40 space-y-2">
            <div className="flex items-center justify-between gap-2">
              <div className="flex items-center gap-2 min-w-0">
                <span className="text-xl">{playerAvatar}</span>
                <div className="min-w-0">
                  <div className="text-xs font-bold text-amber-100 truncate">
                    {playerName} <span className="text-amber-400">(Você)</span>
                  </div>
                  <div className="text-[11px] text-amber-300/75 font-mono">
                    {answerTimesMs.length}/20 • {myAccuracy}% precisão
                  </div>
                </div>
              </div>
              <div className="text-right font-mono shrink-0">
                <div className="text-sm font-bold text-amber-200">{score} pts</div>
                <div className="text-[10px] text-amber-300/70">
                  Média: {answerTimesMs.length > 0 ? formatResponseMs(avgMyTimeMs) : '0.0s'}
                </div>
              </div>
            </div>
            <div className="grid grid-cols-20 gap-0.5 h-1.5 rounded-full overflow-hidden bg-amber-950/80">
              {questions.map((_, idx) => {
                let color = 'bg-amber-900/40';
                if (idx < answerTimesMs.length) {
                  color = answersCorrect[idx] ? 'bg-emerald-400' : 'bg-red-400';
                } else if (idx === currentIndex && !localFinished) {
                  color = 'bg-amber-400 animate-pulse';
                }
                return <div key={idx} className={`h-full ${color}`} />;
              })}
            </div>
          </div>

          {/* Card Oponente */}
          <div className="p-3 rounded-xl bg-stone-900/60 border border-amber-800/40 space-y-2">
            <div className="flex items-center justify-between gap-2">
              <div className="flex items-center gap-2 min-w-0">
                <span className="text-xl">{opponentData?.playerAvatar || '⚔️'}</span>
                <div className="min-w-0">
                  <div className="text-xs font-bold text-amber-100 truncate">
                    {opponentData?.playerName || 'Oponente'}{' '}
                    {opponentData?.finished && (
                      <span className="text-emerald-400 text-[10px]">• Concluiu!</span>
                    )}
                  </div>
                  <div className="text-[11px] text-amber-300/75 font-mono">
                    {opponentData?.answeredCount ?? 0}/20 • {oppAccuracy}% precisão
                  </div>
                </div>
              </div>
              <div className="text-right font-mono shrink-0">
                <div className="text-sm font-bold text-amber-200">
                  {opponentData?.score ?? 0} pts
                </div>
                <div className="text-[10px] text-amber-300/70">
                  Média:{' '}
                  {opponentData && opponentData.answeredCount > 0
                    ? formatResponseMs(opponentData.avgResponseMs)
                    : '0.0s'}
                </div>
              </div>
            </div>
            <div className="grid grid-cols-20 gap-0.5 h-1.5 rounded-full overflow-hidden bg-amber-950/80">
              {questions.map((_, idx) => {
                const oppCount = opponentData?.answeredCount ?? 0;
                const oppCorrect = opponentData?.answersCorrect?.[idx];
                let color = 'bg-amber-900/40';
                if (idx < oppCount) {
                  color = oppCorrect ? 'bg-emerald-500' : 'bg-red-500';
                } else if (idx === oppCount && !opponentData?.finished) {
                  color = 'bg-sky-400 animate-pulse';
                }
                return <div key={idx} className={`h-full ${color}`} />;
              })}
            </div>
          </div>
        </div>
      </div>

      {/* Estado de Espera quando o jogador terminou antes do oponente */}
      {localFinished ? (
        <div className="bg-amber-950/50 backdrop-blur-md border border-amber-700/50 rounded-3xl p-8 text-center shadow-2xl space-y-6">
          <div className="w-16 h-16 rounded-2xl bg-amber-500/20 border border-amber-400/40 flex items-center justify-center mx-auto">
            <Loader2 className="w-8 h-8 text-amber-300 animate-spin" />
          </div>
          <div className="space-y-2">
            <h2 className="text-2xl sm:text-3xl font-serif font-bold text-amber-100">
              Você concluiu as 20 questões!
            </h2>
            <p className="text-sm text-amber-200/80 max-w-md mx-auto">
              Aguardando <strong className="text-amber-100">{opponentData?.playerName || 'seu oponente'}</strong> responder às questões restantes ({opponentData?.answeredCount ?? 0}/20) para exibir o comparativo completo.
            </p>
          </div>

          <div className="grid grid-cols-3 gap-3 max-w-md mx-auto text-left">
            <div className="p-3 rounded-xl bg-amber-900/30 border border-amber-700/40">
              <div className="text-[11px] text-amber-300/75 flex items-center gap-1">
                <Target className="w-3.5 h-3.5 text-emerald-400" />
                <span>Sua Precisão</span>
              </div>
              <div className="text-xl font-mono font-bold text-emerald-300 mt-1">
                {myAccuracy}%
              </div>
            </div>
            <div className="p-3 rounded-xl bg-amber-900/30 border border-amber-700/40">
              <div className="text-[11px] text-amber-300/75 flex items-center gap-1">
                <Clock className="w-3.5 h-3.5 text-amber-400" />
                <span>Tempo Total</span>
              </div>
              <div className="text-xl font-mono font-bold text-amber-100 mt-1">
                {formatResponseMs(totalMyTimeMs)}
              </div>
            </div>
            <div className="p-3 rounded-xl bg-amber-900/30 border border-amber-700/40">
              <div className="text-[11px] text-amber-300/75 flex items-center gap-1">
                <Award className="w-3.5 h-3.5 text-amber-400" />
                <span>Pontos</span>
              </div>
              <div className="text-xl font-mono font-bold text-amber-200 mt-1">
                {score}
              </div>
            </div>
          </div>
        </div>
      ) : (
        /* Card da Questão Atual */
        currentQ && (
          <div className="bg-amber-950/40 backdrop-blur-md border border-amber-800/40 rounded-2xl p-6 sm:p-8 shadow-2xl space-y-6">
            <div className="flex flex-wrap items-center justify-between gap-2 border-b border-amber-800/30 pb-3">
              <div className="flex items-center gap-2 text-xs font-medium text-amber-300/90">
                <span className="px-2 py-0.5 rounded bg-amber-900/70 border border-amber-700/50 text-amber-200 font-bold">
                  Questão {currentIndex + 1}/20
                </span>
                <span className="text-amber-500">•</span>
                <span>{currentQ.testament === 'VT' ? 'Antigo Testamento' : 'Novo Testamento'}</span>
                <span className="text-amber-500">•</span>
                <span className="font-semibold text-amber-100">{currentQ.book}</span>
              </div>

              <div className="flex items-center gap-3 font-mono text-xs">
                {streak >= 2 && (
                  <span className="flex items-center gap-1 text-orange-400 font-bold">
                    <Flame className="w-3.5 h-3.5" />
                    {streak}x
                  </span>
                )}
                <span className="flex items-center gap-1 px-2.5 py-1 rounded-lg bg-amber-900/50 border border-amber-700/40 text-amber-200">
                  <Clock className="w-3.5 h-3.5 text-amber-400" />
                  {formatResponseMs(questionElapsedMs)}
                </span>
              </div>
            </div>

            <div className="py-1">
              <h2 className="text-lg sm:text-xl lg:text-2xl font-serif font-bold text-amber-50 leading-relaxed">
                {currentQ.question}
              </h2>
            </div>

            <div className="space-y-3">
              {currentQ.options.map((option, idx) => {
                const isSelected = selectedOption === idx;
                const isCorrectAnswer = idx === currentQ.correctIndex;

                let buttonStyle =
                  'bg-amber-900/20 border-amber-800/50 hover:bg-amber-900/40 hover:border-amber-600/60 text-amber-100';
                let badgeStyle =
                  'bg-amber-900/60 border-amber-700/60 text-amber-300';
                let iconElement = null;

                if (isAnswered) {
                  if (isCorrectAnswer) {
                    buttonStyle =
                      'bg-emerald-950/60 border-emerald-500 text-emerald-100 ring-2 ring-emerald-500/50';
                    badgeStyle = 'bg-emerald-600 text-white border-emerald-400';
                    iconElement = <CheckCircle2 className="w-5 h-5 text-emerald-400 shrink-0" />;
                  } else if (isSelected && !isCorrectAnswer) {
                    buttonStyle =
                      'bg-red-950/60 border-red-500 text-red-200 ring-2 ring-red-500/50';
                    badgeStyle = 'bg-red-600 text-white border-red-400';
                    iconElement = <XCircle className="w-5 h-5 text-red-400 shrink-0" />;
                  } else {
                    buttonStyle =
                      'bg-amber-950/20 border-amber-900/30 text-amber-300/40 opacity-40';
                    badgeStyle =
                      'bg-amber-950/50 border-amber-900/30 text-amber-500/40';
                  }
                }

                return (
                  <button
                    key={idx}
                    type="button"
                    disabled={isAnswered}
                    onClick={() => handleSelectOption(idx)}
                    className={`w-full p-4 rounded-xl border text-left flex items-center justify-between gap-3.5 transition-all text-sm sm:text-base cursor-pointer ${buttonStyle} ${
                      !isAnswered ? 'active:scale-[0.99] hover:shadow-md' : 'cursor-default'
                    }`}
                  >
                    <div className="flex items-center gap-3">
                      <span
                        className={`w-8 h-8 rounded-lg border flex items-center justify-center font-bold text-xs shrink-0 ${badgeStyle}`}
                      >
                        {letters[idx]}
                      </span>
                      <span className="font-medium leading-snug">{option}</span>
                    </div>
                    {iconElement}
                  </button>
                );
              })}
            </div>

            {isAnswered && (
              <div className="pt-2 animate-fadeIn space-y-4">
                {selectedOption === currentQ.correctIndex ? (
                  <div className="p-3.5 rounded-xl bg-emerald-950/40 border border-emerald-500/40 text-emerald-200 flex items-center justify-between gap-3 text-sm">
                    <div className="flex items-center gap-2.5">
                      <CheckCircle2 className="w-5 h-5 text-emerald-400 shrink-0" />
                      <span>
                        <strong className="text-emerald-300">Correta!</strong> Tempo de resposta:{' '}
                        <strong className="font-mono">{formatResponseMs(questionElapsedMs)}</strong>
                      </span>
                    </div>
                  </div>
                ) : (
                  <div className="p-3.5 rounded-xl bg-red-950/40 border border-red-500/40 text-red-200 flex items-center gap-2.5 text-sm">
                    <XCircle className="w-5 h-5 text-red-400 shrink-0" />
                    <span>
                      <strong className="text-red-300">Incorreta</strong> ({formatResponseMs(questionElapsedMs)}). Correta:{' '}
                      <strong className="text-emerald-300 underline">
                        {currentQ.options[currentQ.correctIndex]}
                      </strong>
                      .
                    </span>
                  </div>
                )}

                <div className="p-4 rounded-xl bg-amber-900/30 border border-amber-700/40 text-amber-200 space-y-1.5">
                  <div className="flex items-center gap-2 text-xs font-bold text-amber-300 uppercase tracking-wider">
                    <BookOpen className="w-4 h-4 text-amber-400" />
                    <span>Referência: {currentQ.reference}</span>
                  </div>
                  <p className="text-sm text-amber-100/90 leading-relaxed font-serif italic">
                    "{currentQ.explanation}"
                  </p>
                </div>

                <div className="pt-1 flex justify-end">
                  <button
                    type="button"
                    onClick={handleNextQuestion}
                    className="w-full sm:w-auto px-8 py-3.5 rounded-xl font-bold text-base text-amber-950 bg-gradient-to-r from-amber-400 via-amber-300 to-amber-500 hover:from-amber-300 hover:to-amber-400 shadow-xl border border-amber-200 flex items-center justify-center gap-2 transition-all cursor-pointer"
                  >
                    <span>
                      {isLastQuestion ? 'Ver Comparativo Final' : 'Próxima Questão'}
                    </span>
                    <ArrowRight className="w-5 h-5 text-amber-950" />
                  </button>
                </div>
              </div>
            )}
          </div>
        )
      )}
    </div>
  );
};
