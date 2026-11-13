import React, { useEffect, useState } from 'react';
import confetti from 'canvas-confetti';
import {
  Difficulty,
  DuelParticipant,
  DuelSlot,
  Question,
} from '../types/quiz';
import { formatResponseMs } from '../utils/duelService';
import { DuelHistoryItem } from './DuelQuizScreen';
import { sound } from '../utils/sound';
import {
  Award,
  BookOpen,
  CheckCircle2,
  Clock,
  Crown,
  RotateCcw,
  Share2,
  Swords,
  Target,
  Timer,
  XCircle,
  Zap,
} from 'lucide-react';

interface DuelResultsScreenProps {
  roomCode: string;
  mySlot: DuelSlot;
  difficulty: Difficulty | 'misto';
  questions: Question[];
  host: DuelParticipant;
  guest: DuelParticipant;
  myHistory: DuelHistoryItem[];
  onNewDuel: () => void;
  onReturnHome: () => void;
}

export const DuelResultsScreen: React.FC<DuelResultsScreenProps> = ({
  roomCode,
  mySlot,
  difficulty,
  questions,
  host,
  guest,
  myHistory,
  onNewDuel,
  onReturnHome,
}) => {
  const [filter, setFilter] = useState<'all' | 'diff' | 'bothCorrect'>('all');
  const [copied, setCopied] = useState(false);

  const me = mySlot === 'host' ? host : guest;
  const opponent = mySlot === 'host' ? guest : host;

  const myAccuracy = Math.round((me.correctAnswers / 20) * 100);
  const oppAccuracy = Math.round((opponent.correctAnswers / 20) * 100);

  // Critério do Duelo: 1º Precisão (acertos), 2º Menor Tempo Total de Resposta, 3º Pontuação
  let winnerSlot: DuelSlot | 'tie' = 'tie';
  let winReason = 'Empate absoluto em precisão, tempo e pontuação!';

  if (host.correctAnswers !== guest.correctAnswers) {
    winnerSlot = host.correctAnswers > guest.correctAnswers ? 'host' : 'guest';
    const winAcc = Math.round(
      ((winnerSlot === 'host' ? host.correctAnswers : guest.correctAnswers) / 20) * 100
    );
    const loseAcc = Math.round(
      ((winnerSlot === 'host' ? guest.correctAnswers : host.correctAnswers) / 20) * 100
    );
    winReason = `Venceu por maior precisão (${winAcc}% contra ${loseAcc}% de acertos).`;
  } else if (host.totalTimeMs !== guest.totalTimeMs) {
    winnerSlot = host.totalTimeMs < guest.totalTimeMs ? 'host' : 'guest';
    const fastTime = formatResponseMs(
      winnerSlot === 'host' ? host.totalTimeMs : guest.totalTimeMs
    );
    const slowTime = formatResponseMs(
      winnerSlot === 'host' ? guest.totalTimeMs : host.totalTimeMs
    );
    winReason = `Empate em precisão (${myAccuracy}%) — venceu pelo menor tempo de resposta (${fastTime} vs ${slowTime})!`;
  } else if (host.score !== guest.score) {
    winnerSlot = host.score > guest.score ? 'host' : 'guest';
    winReason = 'Empate em precisão e tempo — desempate por pontos de sequência!';
  }

  const iWon = winnerSlot === mySlot;
  const isTie = winnerSlot === 'tie';
  const winnerPlayer =
    winnerSlot === 'host' ? host : winnerSlot === 'guest' ? guest : null;

  const fasterSlot: DuelSlot | 'tie' =
    me.totalTimeMs < opponent.totalTimeMs
      ? mySlot
      : opponent.totalTimeMs < me.totalTimeMs
      ? opponent.slot
      : 'tie';
  const moreAccurateSlot: DuelSlot | 'tie' =
    me.correctAnswers > opponent.correctAnswers
      ? mySlot
      : opponent.correctAnswers > me.correctAnswers
      ? opponent.slot
      : 'tie';

  useEffect(() => {
    if (iWon || isTie) {
      try {
        confetti({
          particleCount: 90,
          spread: 75,
          origin: { y: 0.6 },
          colors: ['#f59e0b', '#fbbf24', '#10b981', '#ffffff'],
        });
      } catch {}
    }
  }, [iWon, isTie]);

  const handleShareDuel = () => {
    sound.playClick();
    const hostAcc = Math.round((host.correctAnswers / 20) * 100);
    const guestAcc = Math.round((guest.correctAnswers / 20) * 100);
    const headline = winnerPlayer
      ? `🏆 Vencedor: ${winnerPlayer.playerName}`
      : '🤝 Empate!';
    const text = `⚔️ Duelo Bíblico (20 Questões - ${difficulty.toUpperCase()})
${headline}
${host.playerAvatar} ${host.playerName}: ${host.correctAnswers}/20 (${hostAcc}%) • Tempo: ${formatResponseMs(host.totalTimeMs)} (média ${formatResponseMs(host.avgResponseMs)})
${guest.playerAvatar} ${guest.playerName}: ${guest.correctAnswers}/20 (${guestAcc}%) • Tempo: ${formatResponseMs(guest.totalTimeMs)} (média ${formatResponseMs(guest.avgResponseMs)})`;

    if (navigator.clipboard) {
      navigator.clipboard.writeText(text);
      setCopied(true);
      setTimeout(() => setCopied(false), 2500);
    }
  };

  const renderPlayerCard = (p: DuelParticipant, isMe: boolean) => {
    const acc = Math.round((p.correctAnswers / 20) * 100);
    const isWinner = winnerSlot === p.slot;
    const isFaster = fasterSlot === p.slot;
    const isMoreAccurate = moreAccurateSlot === p.slot;

    return (
      <div
        className={`p-5 rounded-2xl border transition-all space-y-4 text-left ${
          isWinner
            ? 'bg-gradient-to-b from-amber-900/50 to-amber-950/70 border-amber-400 ring-2 ring-amber-400/40 shadow-xl'
            : 'bg-amber-950/40 border-amber-800/50'
        }`}
      >
        <div className="flex items-center justify-between gap-2">
          <div className="flex items-center gap-3 min-w-0">
            <div className="w-12 h-12 rounded-2xl bg-amber-900/50 border border-amber-700/50 flex items-center justify-center text-2xl shrink-0">
              {p.playerAvatar}
            </div>
            <div className="min-w-0">
              <div className="flex items-center gap-1.5">
                <span className="font-bold text-base sm:text-lg text-amber-100 truncate">
                  {p.playerName}
                </span>
                {isMe && (
                  <span className="text-[10px] px-1.5 py-0.5 rounded bg-amber-500/20 text-amber-300 border border-amber-400/30 font-bold">
                    Você
                  </span>
                )}
              </div>
              <div className="text-xs text-amber-300/70">
                {p.slot === 'host' ? 'Jogador 1' : 'Jogador 2'}
              </div>
            </div>
          </div>

          {isWinner && (
            <div className="inline-flex items-center gap-1 px-2.5 py-1 rounded-full bg-amber-400 text-amber-950 text-xs font-black shadow">
              <Crown className="w-3.5 h-3.5" />
              <span>Vencedor</span>
            </div>
          )}
        </div>

        <div className="grid grid-cols-2 gap-2.5">
          <div className="p-3 rounded-xl bg-amber-900/30 border border-amber-800/40">
            <div className="flex items-center justify-between text-[11px] text-amber-300/75 mb-1">
              <span className="flex items-center gap-1">
                <Target className="w-3.5 h-3.5 text-emerald-400" />
                Precisão
              </span>
              {isMoreAccurate && (
                <span className="text-[9px] px-1.5 py-0.2 rounded bg-emerald-500/20 text-emerald-300 font-bold">
                  +Preciso
                </span>
              )}
            </div>
            <div className="text-xl font-mono font-bold text-emerald-300">
              {acc}%{' '}
              <span className="text-xs text-amber-300/70 font-normal">
                ({p.correctAnswers}/20)
              </span>
            </div>
          </div>

          <div className="p-3 rounded-xl bg-amber-900/30 border border-amber-800/40">
            <div className="flex items-center justify-between text-[11px] text-amber-300/75 mb-1">
              <span className="flex items-center gap-1">
                <Clock className="w-3.5 h-3.5 text-amber-400" />
                Tempo Total
              </span>
              {isFaster && (
                <span className="text-[9px] px-1.5 py-0.2 rounded bg-sky-500/20 text-sky-300 font-bold">
                  +Rápido
                </span>
              )}
            </div>
            <div className="text-xl font-mono font-bold text-amber-100">
              {formatResponseMs(p.totalTimeMs)}
            </div>
          </div>

          <div className="p-3 rounded-xl bg-amber-900/30 border border-amber-800/40">
            <div className="flex items-center gap-1 text-[11px] text-amber-300/75 mb-1">
              <Timer className="w-3.5 h-3.5 text-amber-400" />
              <span>Média / Questão</span>
            </div>
            <div className="text-lg font-mono font-bold text-amber-200">
              {formatResponseMs(p.avgResponseMs)}
            </div>
          </div>

          <div className="p-3 rounded-xl bg-amber-900/30 border border-amber-800/40">
            <div className="flex items-center gap-1 text-[11px] text-amber-300/75 mb-1">
              <Award className="w-3.5 h-3.5 text-amber-400" />
              <span>Pontuação</span>
            </div>
            <div className="text-lg font-mono font-bold text-amber-200">
              {p.score} pts
            </div>
          </div>
        </div>
      </div>
    );
  };

  const rows = questions.map((q, idx) => {
    const myCorrect = me.answersCorrect[idx] ?? false;
    const oppCorrect = opponent.answersCorrect[idx] ?? false;
    const myTimeMs = me.answerTimesMs[idx] ?? 0;
    const oppTimeMs = opponent.answerTimesMs[idx] ?? 0;
    const mySelection = myHistory[idx]?.selectedOption;
    return { q, idx, myCorrect, oppCorrect, myTimeMs, oppTimeMs, mySelection };
  });

  const filteredRows = rows.filter((r) => {
    if (filter === 'diff') return r.myCorrect !== r.oppCorrect;
    if (filter === 'bothCorrect') return r.myCorrect && r.oppCorrect;
    return true;
  });

  const timeDiffMs = Math.abs(me.totalTimeMs - opponent.totalTimeMs);
  const accuracyDiff = Math.abs(myAccuracy - oppAccuracy);

  return (
    <div className="max-w-4xl mx-auto px-4 py-8 space-y-8">
      {/* Banner Principal do Resultado do Duelo */}
      <div className="bg-gradient-to-b from-amber-950/85 to-amber-950/50 backdrop-blur-md border border-amber-700/60 rounded-3xl p-6 sm:p-8 shadow-2xl text-center space-y-6">
        <div className="inline-flex items-center gap-2 px-4 py-1.5 rounded-full bg-amber-500/20 border border-amber-400/40 text-amber-200 text-xs font-bold uppercase tracking-wider">
          <Swords className="w-4 h-4 text-amber-400" />
          <span>Comparativo Final • Sala {roomCode}</span>
        </div>

        <div className="space-y-2">
          <h1 className="text-2xl sm:text-4xl font-serif font-black text-amber-100">
            {isTie
              ? 'Empate Perfeito no Duelo!'
              : iWon
              ? `Vitória de ${me.playerName}!`
              : `Vitória de ${opponent.playerName}!`}
          </h1>
          <p className="text-sm sm:text-base text-amber-200/85 max-w-xl mx-auto">
            {winReason}
          </p>
        </div>

        {/* Cards Lado a Lado */}
        <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
          {renderPlayerCard(me, true)}
          {renderPlayerCard(opponent, false)}
        </div>

        {/* Resumo Comparativo Rápido */}
        <div className="grid grid-cols-1 sm:grid-cols-2 gap-3 text-xs text-left">
          <div className="p-3.5 rounded-xl bg-amber-900/25 border border-amber-800/40 flex items-center gap-3">
            <Target className="w-5 h-5 text-emerald-400 shrink-0" />
            <div>
              <div className="font-bold text-amber-100">Comparação de Precisão</div>
              <div className="text-amber-200/80">
                {accuracyDiff === 0
                  ? `Ambos alcançaram exatamente ${myAccuracy}% de precisão (${me.correctAnswers}/20).`
                  : `${
                      myAccuracy > oppAccuracy ? me.playerName : opponent.playerName
                    } foi ${accuracyDiff}% mais preciso(a) (${Math.max(
                      me.correctAnswers,
                      opponent.correctAnswers
                    )}/20 vs ${Math.min(
                      me.correctAnswers,
                      opponent.correctAnswers
                    )}/20).`}
              </div>
            </div>
          </div>

          <div className="p-3.5 rounded-xl bg-amber-900/25 border border-amber-800/40 flex items-center gap-3">
            <Zap className="w-5 h-5 text-sky-400 shrink-0" />
            <div>
              <div className="font-bold text-amber-100">Comparação de Velocidade</div>
              <div className="text-amber-200/80">
                {timeDiffMs === 0
                  ? 'Tempo de resposta total exatamente igual!'
                  : `${
                      me.totalTimeMs < opponent.totalTimeMs
                        ? me.playerName
                        : opponent.playerName
                    } respondeu ${formatResponseMs(
                      timeDiffMs
                    )} mais rápido no total das 20 questões.`}
              </div>
            </div>
          </div>
        </div>

        {/* Botões de Ação */}
        <div className="flex flex-wrap items-center justify-center gap-3 pt-2">
          <button
            type="button"
            onClick={() => {
              sound.playClick();
              onNewDuel();
            }}
            className="px-6 py-3.5 rounded-xl font-bold text-sm text-amber-950 bg-gradient-to-r from-amber-400 to-amber-500 hover:from-amber-300 hover:to-amber-400 shadow-lg border border-amber-200 flex items-center gap-2 cursor-pointer transition-all"
          >
            <Swords className="w-4 h-4" />
            <span>Novo Duelo (Novas 20 Questões)</span>
          </button>

          <button
            type="button"
            onClick={handleShareDuel}
            className="px-5 py-3.5 rounded-xl font-semibold text-sm text-amber-200 bg-amber-900/50 hover:bg-amber-900/80 border border-amber-700/50 flex items-center gap-2 cursor-pointer transition-all"
          >
            <Share2 className="w-4 h-4" />
            <span>{copied ? 'Resultado Copiado!' : 'Compartilhar Comparativo'}</span>
          </button>

          <button
            type="button"
            onClick={() => {
              sound.playClick();
              onReturnHome();
            }}
            className="px-4 py-3.5 rounded-xl font-semibold text-sm text-amber-300 hover:text-white bg-amber-950/60 hover:bg-amber-900/40 border border-amber-800/40 flex items-center gap-1.5 cursor-pointer transition-all"
          >
            <RotateCcw className="w-4 h-4" />
            <span>Início</span>
          </button>
        </div>
      </div>

      {/* Comparação Questão por Questão */}
      <div className="space-y-4">
        <div className="flex flex-wrap items-center justify-between gap-3">
          <div>
            <h2 className="text-xl font-serif font-bold text-amber-100 flex items-center gap-2">
              <BookOpen className="w-5 h-5 text-amber-400" />
              <span>Comparativo Questão por Questão (20 Questões)</span>
            </h2>
            <p className="text-xs text-amber-300/70">
              Veja quem acertou e quem foi mais rápido em cada uma das 20 perguntas idênticas
            </p>
          </div>

          <div className="flex items-center gap-1.5 p-1 rounded-xl bg-amber-950/60 border border-amber-800/40 text-xs">
            <button
              type="button"
              onClick={() => setFilter('all')}
              className={`px-3 py-1 rounded-lg font-medium cursor-pointer transition-all ${
                filter === 'all'
                  ? 'bg-amber-600 text-white'
                  : 'text-amber-300/70 hover:text-amber-200'
              }`}
            >
              Todas (20)
            </button>
            <button
              type="button"
              onClick={() => setFilter('diff')}
              className={`px-3 py-1 rounded-lg font-medium cursor-pointer transition-all ${
                filter === 'diff'
                  ? 'bg-amber-600 text-white'
                  : 'text-amber-300/70 hover:text-amber-200'
              }`}
            >
              Divergências
            </button>
            <button
              type="button"
              onClick={() => setFilter('bothCorrect')}
              className={`px-3 py-1 rounded-lg font-medium cursor-pointer transition-all ${
                filter === 'bothCorrect'
                  ? 'bg-emerald-600 text-white'
                  : 'text-emerald-400/70 hover:text-emerald-300'
              }`}
            >
              Ambos Acertaram
            </button>
          </div>
        </div>

        <div className="space-y-3">
          {filteredRows.map(({ q, idx, myCorrect, oppCorrect, myTimeMs, oppTimeMs }) => {
            const fasterHere =
              myTimeMs < oppTimeMs
                ? me.playerName
                : oppTimeMs < myTimeMs
                ? opponent.playerName
                : 'Empate';

            return (
              <div
                key={q.id}
                className="p-4 sm:p-5 rounded-2xl bg-amber-950/30 border border-amber-800/40 space-y-3"
              >
                <div className="flex flex-wrap items-center justify-between gap-2 text-xs">
                  <div className="flex items-center gap-2">
                    <span className="font-mono font-bold text-amber-400">
                      Q#{idx + 1}
                    </span>
                    <span className="text-amber-200 font-semibold">{q.book}</span>
                    <span className="text-amber-500">•</span>
                    <span className="text-amber-300/75">{q.reference}</span>
                  </div>
                  <span className="text-[11px] text-sky-300/90 font-medium">
                    Mais rápido: <strong>{fasterHere}</strong>
                  </span>
                </div>

                <h3 className="text-sm sm:text-base font-serif font-bold text-amber-100">
                  {q.question}
                </h3>

                <div className="grid grid-cols-1 sm:grid-cols-2 gap-2.5 text-xs">
                  <div
                    className={`p-3 rounded-xl border flex items-center justify-between ${
                      myCorrect
                        ? 'bg-emerald-950/35 border-emerald-600/40 text-emerald-200'
                        : 'bg-red-950/35 border-red-600/40 text-red-200'
                    }`}
                  >
                    <div className="flex items-center gap-2 min-w-0">
                      {myCorrect ? (
                        <CheckCircle2 className="w-4 h-4 text-emerald-400 shrink-0" />
                      ) : (
                        <XCircle className="w-4 h-4 text-red-400 shrink-0" />
                      )}
                      <span className="font-semibold truncate">
                        {me.playerAvatar} {me.playerName}
                      </span>
                    </div>
                    <span className="font-mono font-bold shrink-0">
                      {formatResponseMs(myTimeMs)}
                    </span>
                  </div>

                  <div
                    className={`p-3 rounded-xl border flex items-center justify-between ${
                      oppCorrect
                        ? 'bg-emerald-950/35 border-emerald-600/40 text-emerald-200'
                        : 'bg-red-950/35 border-red-600/40 text-red-200'
                    }`}
                  >
                    <div className="flex items-center gap-2 min-w-0">
                      {oppCorrect ? (
                        <CheckCircle2 className="w-4 h-4 text-emerald-400 shrink-0" />
                      ) : (
                        <XCircle className="w-4 h-4 text-red-400 shrink-0" />
                      )}
                      <span className="font-semibold truncate">
                        {opponent.playerAvatar} {opponent.playerName}
                      </span>
                    </div>
                    <span className="font-mono font-bold shrink-0">
                      {formatResponseMs(oppTimeMs)}
                    </span>
                  </div>
                </div>

                <div className="text-xs text-amber-200/80 bg-amber-900/20 p-2.5 rounded-lg border border-amber-800/30">
                  <strong className="text-emerald-300">Resposta correta:</strong>{' '}
                  {q.options[q.correctIndex]}
                </div>
              </div>
            );
          })}
        </div>
      </div>
    </div>
  );
};
