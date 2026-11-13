import React, { useState, useEffect } from 'react';
import { Question, Difficulty } from '../types/quiz';
import { sound } from '../utils/sound';
import { 
  CheckCircle2, 
  XCircle, 
  ArrowRight, 
  BookOpen, 
  Flame, 
  Clock, 
  Award,
  Sparkles,
  Info
} from 'lucide-react';

interface QuizScreenProps {
  questions: Question[];
  playerName: string;
  playerAvatar: string;
  difficulty: Difficulty | 'misto';
  onCompleteQuiz: (results: {
    score: number;
    correctAnswers: number;
    totalQuestions: number;
    timeSpentSeconds: number;
    history: {
      question: Question;
      selectedOption: number;
      isCorrect: boolean;
    }[];
  }) => void;
}

export const QuizScreen: React.FC<QuizScreenProps> = ({
  questions,
  playerName,
  playerAvatar,
  difficulty,
  onCompleteQuiz,
}) => {
  const [currentIndex, setCurrentIndex] = useState(0);
  const [selectedOption, setSelectedOption] = useState<number | null>(null);
  const [isAnswered, setIsAnswered] = useState(false);
  const [score, setScore] = useState(0);
  const [streak, setStreak] = useState(0);
  const [maxStreak, setMaxStreak] = useState(0);
  const [correctCount, setCorrectCount] = useState(0);
  const [secondsElapsed, setSecondsElapsed] = useState(0);
  const [history, setHistory] = useState<{
    question: Question;
    selectedOption: number;
    isCorrect: boolean;
  }[]>([]);

  // Timer da rodada
  useEffect(() => {
    const timer = setInterval(() => {
      setSecondsElapsed((prev) => prev + 1);
    }, 1000);
    return () => clearInterval(timer);
  }, []);

  const currentQ = questions[currentIndex];
  const isLastQuestion = currentIndex === questions.length - 1;

  const handleSelectOption = (index: number) => {
    if (isAnswered) return;

    setSelectedOption(index);
    setIsAnswered(true);

    const isCorrect = index === currentQ.correctIndex;

    if (isCorrect) {
      sound.playCorrect();
      const streakBonus = Math.min(streak * 10, 50);
      const points = 100 + streakBonus;
      setScore((prev) => prev + points);
      setCorrectCount((prev) => prev + 1);
      const newStreak = streak + 1;
      setStreak(newStreak);
      if (newStreak > maxStreak) setMaxStreak(newStreak);
    } else {
      sound.playWrong();
      setStreak(0);
    }

    setHistory((prev) => [
      ...prev,
      {
        question: currentQ,
        selectedOption: index,
        isCorrect,
      },
    ]);
  };

  const handleNextQuestion = () => {
    sound.playClick();
    if (isLastQuestion) {
      // Finalizou as 20 questões
      sound.playVictory();
      onCompleteQuiz({
        score,
        correctAnswers: correctCount,
        totalQuestions: questions.length,
        timeSpentSeconds: secondsElapsed,
        history,
      });
    } else {
      setCurrentIndex((prev) => prev + 1);
      setSelectedOption(null);
      setIsAnswered(false);
    }
  };

  // Suporte a atalhos de teclado (1, 2, 3, 4 e Enter)
  useEffect(() => {
    const handleKeyDown = (e: KeyboardEvent) => {
      if (!isAnswered) {
        if (['1', '2', '3', '4'].includes(e.key)) {
          const idx = parseInt(e.key, 10) - 1;
          handleSelectOption(idx);
        }
      } else {
        if (e.key === 'Enter' || e.key === ' ') {
          e.preventDefault();
          handleNextQuestion();
        }
      }
    };
    window.addEventListener('keydown', handleKeyDown);
    return () => window.removeEventListener('keydown', handleKeyDown);
  }, [isAnswered, isLastQuestion, score, correctCount, history]);

  // Formatação de tempo
  const formatTimer = (totalSecs: number) => {
    const mins = Math.floor(totalSecs / 60);
    const secs = totalSecs % 60;
    return `${mins}:${secs.toString().padStart(2, '0')}`;
  };

  const letters = ['A', 'B', 'C', 'D'];

  return (
    <div className="max-w-3xl mx-auto px-4 py-6 sm:py-8">
      {/* Barra superior de status do Quiz */}
      <div className="bg-amber-950/60 backdrop-blur-md border border-amber-800/40 rounded-2xl p-4 sm:p-5 shadow-lg mb-6 space-y-3">
        <div className="flex flex-wrap items-center justify-between gap-3 text-xs sm:text-sm">
          {/* Jogador & Dificuldade */}
          <div className="flex items-center gap-2">
            <span className="text-xl">{playerAvatar}</span>
            <span className="font-semibold text-amber-100 max-w-[130px] sm:max-w-xs truncate">
              {playerName}
            </span>
            <span className="px-2 py-0.5 rounded-full bg-amber-500/20 text-amber-300 font-medium text-[11px] uppercase tracking-wide border border-amber-500/30">
              {difficulty}
            </span>
          </div>

          {/* Placar parcial, combo e relógio */}
          <div className="flex items-center gap-3 sm:gap-4 font-mono">
            <div className="flex items-center gap-1 text-amber-300" title="Tempo da partida">
              <Clock className="w-3.5 h-3.5 text-amber-400" />
              <span>{formatTimer(secondsElapsed)}</span>
            </div>

            {streak >= 2 && (
              <div className="flex items-center gap-1 text-orange-400 font-bold animate-pulse" title="Sequência de acertos">
                <Flame className="w-4 h-4 text-orange-400" />
                <span>{streak}x</span>
              </div>
            )}

            <div className="flex items-center gap-1 px-2.5 py-1 rounded-lg bg-amber-900/60 border border-amber-700/50 text-amber-200 font-bold" title="Pontos acumulados">
              <Award className="w-4 h-4 text-amber-400" />
              <span>{score} pts</span>
            </div>
          </div>
        </div>

        {/* Barra de Progresso das 20 questões */}
        <div className="space-y-1.5">
          <div className="flex items-center justify-between text-xs text-amber-300/80">
            <span>
              Questão <strong className="text-amber-100 text-sm">{currentIndex + 1}</strong> de <strong>{questions.length}</strong>
            </span>
            <span>
              Acertos: <strong className="text-emerald-400">{correctCount}</strong> / {currentIndex + (isAnswered ? 1 : 0)}
            </span>
          </div>
          
          {/* Linha com 20 segmentos */}
          <div className="grid grid-cols-20 gap-1 h-2 rounded-full overflow-hidden bg-amber-950/80 p-0.5 border border-amber-800/40">
            {questions.map((_, idx) => {
              const histItem = history[idx];
              let bg = 'bg-amber-900/40';
              if (idx === currentIndex) {
                bg = isAnswered 
                  ? histItem?.isCorrect ? 'bg-emerald-400' : 'bg-red-400'
                  : 'bg-amber-400 animate-pulse';
              } else if (idx < currentIndex) {
                bg = histItem?.isCorrect ? 'bg-emerald-500' : 'bg-red-500';
              }
              return (
                <div 
                  key={idx} 
                  className={`h-full rounded-sm transition-all duration-300 ${bg}`} 
                  title={`Questão ${idx + 1}`}
                />
              );
            })}
          </div>
        </div>
      </div>

      {/* Card da Questão */}
      <div className="bg-amber-950/40 backdrop-blur-md border border-amber-800/40 rounded-2xl p-6 sm:p-8 shadow-2xl relative overflow-hidden space-y-6">
        
        {/* Marcadores de Seção Bíblica e Livro */}
        <div className="flex flex-wrap items-center justify-between gap-2 border-b border-amber-800/30 pb-3">
          <div className="flex items-center gap-2 text-xs font-medium text-amber-300/90">
            <span className="px-2 py-0.5 rounded bg-amber-900/70 border border-amber-700/50 text-amber-200">
              {currentQ.testament === 'VT' ? 'Antigo Testamento' : 'Novo Testamento'}
            </span>
            <span className="text-amber-500">•</span>
            <span className="text-amber-300">{currentQ.section}</span>
            <span className="text-amber-500">•</span>
            <span className="font-semibold text-amber-100">{currentQ.book}</span>
          </div>

          <div className="text-[11px] font-mono text-amber-400/60 uppercase">
            ID #{currentQ.id}
          </div>
        </div>

        {/* Texto da Questão */}
        <div className="py-2">
          <h2 className="text-lg sm:text-xl lg:text-2xl font-serif font-bold text-amber-50 leading-relaxed tracking-wide">
            {currentQ.question}
          </h2>
        </div>

        {/* 4 Opções Prováveis de Resposta */}
        <div className="space-y-3">
          {currentQ.options.map((option, idx) => {
            const isSelected = selectedOption === idx;
            const isCorrectAnswer = idx === currentQ.correctIndex;
            
            // Estado visual da opção após responder:
            let buttonStyle = 'bg-amber-900/20 border-amber-800/50 hover:bg-amber-900/40 hover:border-amber-600/60 text-amber-100';
            let badgeStyle = 'bg-amber-900/60 border-amber-700/60 text-amber-300';
            let iconElement = null;

            if (isAnswered) {
              if (isCorrectAnswer) {
                // Sempre destaca a correta em verde com check
                buttonStyle = 'bg-emerald-950/60 border-emerald-500 text-emerald-100 ring-2 ring-emerald-500/50 shadow-lg shadow-emerald-950/50';
                badgeStyle = 'bg-emerald-600 text-white border-emerald-400';
                iconElement = <CheckCircle2 className="w-5 h-5 text-emerald-400 shrink-0" />;
              } else if (isSelected && !isCorrectAnswer) {
                // Se o jogador errou, destaca a escolha em vermelho com X
                buttonStyle = 'bg-red-950/60 border-red-500 text-red-200 ring-2 ring-red-500/50';
                badgeStyle = 'bg-red-600 text-white border-red-400';
                iconElement = <XCircle className="w-5 h-5 text-red-400 shrink-0" />;
              } else {
                // Outras opções incorretas não selecionadas
                buttonStyle = 'bg-amber-950/20 border-amber-900/30 text-amber-300/40 opacity-40';
                badgeStyle = 'bg-amber-950/50 border-amber-900/30 text-amber-500/40';
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
                  <span className={`w-8 h-8 rounded-lg border flex items-center justify-center font-bold text-xs shrink-0 ${badgeStyle}`}>
                    {letters[idx]}
                  </span>
                  <span className="font-medium leading-snug">
                    {option}
                  </span>
                </div>

                <div className="flex items-center gap-2">
                  {isAnswered && isCorrectAnswer && (
                    <span className="hidden sm:inline-flex text-xs font-bold text-emerald-400 uppercase tracking-wider px-2 py-0.5 rounded bg-emerald-900/50 border border-emerald-500/30">
                      Correta
                    </span>
                  )}
                  {isAnswered && isSelected && !isCorrectAnswer && (
                    <span className="hidden sm:inline-flex text-xs font-bold text-red-400 uppercase tracking-wider px-2 py-0.5 rounded bg-red-900/50 border border-red-500/30">
                      Sua Escolha
                    </span>
                  )}
                  {iconElement}
                </div>
              </button>
            );
          })}
        </div>

        {/* FEEDBACK IMEDIATO: Explicativo versículo a versículo após responder */}
        {isAnswered && (
          <div className="pt-2 animate-fadeIn space-y-4">
            
            {/* Aviso de Correção */}
            {selectedOption === currentQ.correctIndex ? (
              <div className="p-3.5 rounded-xl bg-emerald-950/40 border border-emerald-500/40 text-emerald-200 flex items-center gap-3 text-sm">
                <CheckCircle2 className="w-5 h-5 text-emerald-400 shrink-0" />
                <div>
                  <span className="font-bold text-emerald-300">Resposta Correta! </span>
                  <span>Você acertou em cheio e ganhou 100 pontos{streak > 1 ? ` + bônus de combo!` : '.'}</span>
                </div>
              </div>
            ) : (
              <div className="p-3.5 rounded-xl bg-red-950/40 border border-red-500/40 text-red-200 flex items-center gap-3 text-sm">
                <XCircle className="w-5 h-5 text-red-400 shrink-0" />
                <div>
                  <span className="font-bold text-red-300">Resposta Incorreta. </span>
                  <span>
                    A resposta correta era: <strong className="text-emerald-300 underline">{currentQ.options[currentQ.correctIndex]}</strong> (Opção {letters[currentQ.correctIndex]}).
                  </span>
                </div>
              </div>
            )}

            {/* Referência e Comentário Bíblico */}
            <div className="p-4 sm:p-5 rounded-xl bg-amber-900/30 border border-amber-700/40 text-amber-200 space-y-2">
              <div className="flex items-center gap-2 text-xs font-bold text-amber-300 uppercase tracking-wider">
                <BookOpen className="w-4 h-4 text-amber-400" />
                <span>Referência Bíblica: {currentQ.reference}</span>
              </div>
              <p className="text-sm text-amber-100/90 leading-relaxed font-serif italic">
                "{currentQ.explanation}"
              </p>
            </div>

            {/* Botão de Próxima Questão ou Finalizar */}
            <div className="pt-2 flex justify-end">
              <button
                type="button"
                onClick={handleNextQuestion}
                className="w-full sm:w-auto px-8 py-3.5 rounded-xl font-bold text-base text-amber-950 bg-gradient-to-r from-amber-400 via-amber-300 to-amber-500 hover:from-amber-300 hover:to-amber-400 shadow-xl shadow-amber-950/40 border border-amber-200 flex items-center justify-center gap-2.5 transition-all transform active:scale-[0.98] cursor-pointer"
              >
                <span>{isLastQuestion ? 'Ver Resultado Final' : 'Próxima Questão'}</span>
                <ArrowRight className="w-5 h-5 text-amber-950" />
              </button>
            </div>
          </div>
        )}

      </div>
    </div>
  );
};
