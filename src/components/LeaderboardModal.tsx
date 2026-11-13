import React, { useState, useEffect } from 'react';
import { onAuthStateChanged, User } from 'firebase/auth';
import { PlayerScore, Difficulty } from '../types/quiz';
import { sound } from '../utils/sound';
import { formatTime } from '../utils/storage';
import { clearAllOnlineScores } from '../utils/leaderboardService';
import { auth, ADMIN_EMAIL, signInWithGoogle, signOutFirebase } from '../firebase';
import { 
  Trophy, 
  X, 
  RotateCcw,
  Sparkles,
  Globe,
  ShieldCheck,
  LogOut
} from 'lucide-react';

interface LeaderboardModalProps {
  isOpen: boolean;
  onClose: () => void;
  scores: PlayerScore[];
  currentPlayerName: string;
  onScoresReset: (newScores: PlayerScore[]) => void;
}

export const LeaderboardModal: React.FC<LeaderboardModalProps> = ({
  isOpen,
  onClose,
  scores,
  currentPlayerName,
  onScoresReset,
}) => {
  const [filterDiff, setFilterDiff] = useState<'all' | Difficulty | 'misto'>('all');
  const [confirmReset, setConfirmReset] = useState(false);
  const [isClearing, setIsClearing] = useState(false);
  const [currentUser, setCurrentUser] = useState<User | null>(auth.currentUser);
  const [authError, setAuthError] = useState('');

  useEffect(() => {
    const unsub = onAuthStateChanged(auth, (user) => {
      setCurrentUser(user);
      setAuthError('');
    });
    return () => unsub();
  }, []);

  if (!isOpen) return null;

  const isAdmin =
    !!currentUser &&
    currentUser.email === ADMIN_EMAIL &&
    currentUser.emailVerified === true;

  const filteredScores = scores.filter((s) => {
    if (filterDiff === 'all') return true;
    return s.difficulty === filterDiff;
  });

  const handleAdminLogin = async () => {
    sound.playClick();
    setAuthError('');
    try {
      const res = await signInWithGoogle();
      if (res.user.email !== ADMIN_EMAIL) {
        setAuthError('Apenas o administrador do aplicativo pode limpar o placar online.');
      }
    } catch {
      setAuthError('Não foi possível entrar com a conta Google.');
    }
  };

  const handleReset = async () => {
    sound.playClick();
    if (!confirmReset) {
      setConfirmReset(true);
      setTimeout(() => setConfirmReset(false), 4000);
      return;
    }

    setIsClearing(true);
    setAuthError('');
    try {
      await clearAllOnlineScores();
      onScoresReset([]);
      setConfirmReset(false);
    } catch {
      setAuthError('Erro ao limpar o placar online. Verifique sua conexão.');
    } finally {
      setIsClearing(false);
    }
  };

  const getRankBadge = (pos: number) => {
    if (pos === 1) {
      return (
        <div className="w-8 h-8 rounded-full bg-gradient-to-br from-yellow-300 via-amber-400 to-amber-600 flex items-center justify-center text-amber-950 font-black text-sm shadow-md shadow-amber-500/30 border border-yellow-200">
          🥇
        </div>
      );
    }
    if (pos === 2) {
      return (
        <div className="w-8 h-8 rounded-full bg-gradient-to-br from-slate-200 via-slate-300 to-slate-400 flex items-center justify-center text-slate-900 font-black text-sm shadow-md shadow-slate-400/30 border border-slate-100">
          🥈
        </div>
      );
    }
    if (pos === 3) {
      return (
        <div className="w-8 h-8 rounded-full bg-gradient-to-br from-amber-600 via-amber-700 to-amber-800 flex items-center justify-center text-amber-100 font-black text-sm shadow-md shadow-amber-800/30 border border-amber-500">
          🥉
        </div>
      );
    }
    return (
      <div className="w-8 h-8 rounded-full bg-amber-900/40 border border-amber-700/50 flex items-center justify-center text-amber-300 font-bold text-xs">
        {pos}º
      </div>
    );
  };

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center p-3 sm:p-4 bg-black/80 backdrop-blur-sm animate-fadeIn">
      <div className="bg-amber-950 border border-amber-800/60 w-full max-w-3xl rounded-3xl shadow-2xl overflow-hidden flex flex-col max-h-[90vh]">
        
        {/* Cabeçalho do Placar */}
        <div className="p-5 sm:p-6 border-b border-amber-800/50 flex items-center justify-between bg-amber-900/30">
          <div className="flex items-center gap-3">
            <div className="w-10 h-10 rounded-xl bg-gradient-to-br from-amber-500 to-amber-700 flex items-center justify-center shadow-lg border border-amber-300/30">
              <Trophy className="w-5 h-5 text-amber-100" />
            </div>
            <div>
              <div className="flex items-center gap-2">
                <h2 className="text-xl sm:text-2xl font-serif font-bold text-amber-100 tracking-wide">
                  Placar Online com Posições
                </h2>
                <span className="inline-flex items-center gap-1 text-[10px] font-bold uppercase tracking-wider px-2 py-0.5 rounded-full bg-emerald-500/20 text-emerald-300 border border-emerald-500/30">
                  <Globe className="w-3 h-3" />
                  Global
                </span>
              </div>
              <p className="text-xs text-amber-300/70">
                Ranking compartilhado em tempo real entre todos os jogadores
              </p>
            </div>
          </div>

          <button
            onClick={() => {
              sound.playClick();
              onClose();
            }}
            className="w-9 h-9 rounded-xl flex items-center justify-center text-amber-400 hover:text-white bg-amber-900/40 hover:bg-amber-900/80 border border-amber-700/50 transition-colors"
          >
            <X className="w-5 h-5" />
          </button>
        </div>

        {/* Filtros de Dificuldade */}
        <div className="p-3 sm:px-6 sm:py-3 bg-amber-950/70 border-b border-amber-800/40 flex flex-wrap items-center justify-between gap-2 text-xs">
          <div className="flex items-center gap-1.5 overflow-x-auto py-1">
            <span className="text-amber-400/70 font-semibold mr-1">Filtrar:</span>
            {[
              { id: 'all', label: 'Geral' },
              { id: 'facil', label: 'Fácil' },
              { id: 'medio', label: 'Médio' },
              { id: 'dificil', label: 'Difícil' },
              { id: 'misto', label: 'Misto' },
            ].map((f) => (
              <button
                key={f.id}
                onClick={() => {
                  sound.playClick();
                  setFilterDiff(f.id as typeof filterDiff);
                }}
                className={`px-3 py-1.5 rounded-lg font-semibold transition-all ${
                  filterDiff === f.id
                    ? 'bg-amber-500 text-amber-950 shadow-md font-bold'
                    : 'bg-amber-900/30 text-amber-200/80 hover:bg-amber-900/60 hover:text-white border border-amber-800/30'
                }`}
              >
                {f.label}
              </button>
            ))}
          </div>

          {/* Controles de Administrador para limpar o placar online */}
          {scores.length > 0 && (
            <div className="flex items-center gap-2">
              {isAdmin ? (
                <>
                  <button
                    onClick={handleReset}
                    disabled={isClearing}
                    className={`text-[11px] flex items-center gap-1 transition-colors px-2.5 py-1 rounded-md ${
                      confirmReset
                        ? 'bg-red-600/80 text-white font-bold'
                        : 'text-amber-300 hover:text-white bg-amber-900/40 border border-amber-700/40'
                    }`}
                    title="Limpar todas as pontuações online"
                  >
                    <RotateCcw className="w-3 h-3" />
                    <span>
                      {isClearing
                        ? 'Limpando...'
                        : confirmReset
                        ? 'Confirmar limpeza?'
                        : 'Limpar placar online'}
                    </span>
                  </button>
                  <button
                    onClick={() => signOutFirebase()}
                    className="text-[11px] text-amber-400/60 hover:text-amber-200 flex items-center gap-1"
                    title="Sair do modo administrador"
                  >
                    <LogOut className="w-3 h-3" />
                  </button>
                </>
              ) : (
                <button
                  onClick={handleAdminLogin}
                  className="text-[11px] text-amber-400/50 hover:text-amber-300 flex items-center gap-1 transition-colors"
                  title="Acesso do administrador para gerenciar o placar"
                >
                  <ShieldCheck className="w-3.5 h-3.5" />
                  <span>Admin</span>
                </button>
              )}
            </div>
          )}
        </div>

        {authError && (
          <div className="mx-4 sm:mx-6 mt-3 p-2.5 rounded-xl bg-red-950/60 border border-red-500/40 text-red-200 text-xs">
            {authError}
          </div>
        )}

        {/* Lista de Classificação com Posições */}
        <div className="overflow-y-auto p-4 sm:p-6 space-y-2.5 flex-1">
          {filteredScores.length === 0 ? (
            <div className="text-center py-12 text-amber-300/60 text-sm">
              {scores.length === 0
                ? 'Nenhum jogador registrado no placar online ainda. Complete uma rodada de 20 questões para estrear o ranking!'
                : 'Nenhuma pontuação registrada para este nível de dificuldade ainda.'}
            </div>
          ) : (
            filteredScores.map((scoreItem, index) => {
              const position = index + 1;
              const isCurrent =
                currentPlayerName &&
                scoreItem.playerName.toLowerCase() === currentPlayerName.toLowerCase();

              const formattedDate = new Date(scoreItem.date).toLocaleDateString('pt-BR', {
                day: '2-digit',
                month: '2-digit',
              });

              return (
                <div
                  key={scoreItem.id || index}
                  className={`p-3 sm:p-4 rounded-2xl border flex items-center justify-between gap-3 transition-all ${
                    isCurrent
                      ? 'bg-amber-900/40 border-amber-400 ring-1 ring-amber-400/40 shadow-md'
                      : position <= 3
                      ? 'bg-amber-950/40 border-amber-700/60 hover:border-amber-500/60'
                      : 'bg-amber-950/20 border-amber-900/40 hover:border-amber-800/60'
                  }`}
                >
                  {/* Posição e Jogador */}
                  <div className="flex items-center gap-3 min-w-0">
                    <div className="shrink-0">{getRankBadge(position)}</div>
                    
                    <div className="min-w-0">
                      <div className="flex items-center gap-2">
                        <span className="text-base">{scoreItem.playerAvatar}</span>
                        <span className="font-bold text-sm sm:text-base text-amber-100 truncate">
                          {scoreItem.playerName}
                        </span>
                        {isCurrent && (
                          <span className="text-[10px] px-1.5 py-0.2 rounded bg-amber-500/20 text-amber-300 font-bold border border-amber-400/30">
                            Você
                          </span>
                        )}
                      </div>

                      <div className="flex items-center gap-2 text-[11px] text-amber-300/70 mt-0.5">
                        <span className="capitalize font-medium text-amber-400">
                          {scoreItem.difficulty}
                        </span>
                        <span>•</span>
                        <span>{scoreItem.correctAnswers}/{scoreItem.totalQuestions} acertos ({scoreItem.accuracy}%)</span>
                        <span className="hidden sm:inline">•</span>
                        <span className="hidden sm:inline">{formatTime(scoreItem.timeSpentSeconds)}</span>
                      </div>
                    </div>
                  </div>

                  {/* Pontuação e Data */}
                  <div className="text-right shrink-0">
                    <div className="text-base sm:text-lg font-bold font-mono text-amber-300">
                      {scoreItem.score} pts
                    </div>
                    <div className="text-[10px] text-amber-400/50">
                      {formattedDate}
                    </div>
                  </div>
                </div>
              );
            })
          )}
        </div>

        {/* Rodapé com Dica */}
        <div className="p-4 border-t border-amber-800/50 bg-amber-900/20 flex items-center justify-between text-xs text-amber-300/80">
          <div className="flex items-center gap-2">
            <Sparkles className="w-4 h-4 text-amber-400" />
            <span>Todos os jogadores com o link veem este placar em tempo real!</span>
          </div>
          <button
            onClick={() => {
              sound.playClick();
              onClose();
            }}
            className="px-4 py-2 rounded-xl bg-amber-600 hover:bg-amber-500 text-amber-950 font-bold text-xs transition-colors cursor-pointer"
          >
            Fechar
          </button>
        </div>

      </div>
    </div>
  );
};
