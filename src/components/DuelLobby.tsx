import React, { useEffect, useState } from 'react';
import { Difficulty, DuelParticipant, DuelRoom, DuelSlot, Question } from '../types/quiz';
import { AVATARS, SavedPlayer } from '../utils/storage';
import {
  createDuelRoom,
  joinDuelRoom,
  normalizeRoomCode,
  subscribeToDuelSession,
} from '../utils/duelService';
import { sound } from '../utils/sound';
import {
  ArrowLeft,
  Check,
  Copy,
  Link2,
  Loader2,
  Share2,
  Swords,
  Users,
  Sparkles,
} from 'lucide-react';

interface DuelLobbyProps {
  initialPlayer: SavedPlayer;
  initialInviteCode?: string;
  onUpdatePlayer: (player: SavedPlayer) => void;
  onStartDuel: (session: {
    roomCode: string;
    slot: DuelSlot;
    difficulty: Difficulty | 'misto';
    questions: Question[];
  }) => void;
  onBack: () => void;
}

export const DuelLobby: React.FC<DuelLobbyProps> = ({
  initialPlayer,
  initialInviteCode = '',
  onUpdatePlayer,
  onStartDuel,
  onBack,
}) => {
  const [tab, setTab] = useState<'create' | 'join'>(
    initialInviteCode ? 'join' : 'create'
  );
  const [name, setName] = useState(initialPlayer.name || '');
  const [avatar, setAvatar] = useState(initialPlayer.avatar || '📜');
  const [difficulty, setDifficulty] = useState<Difficulty | 'misto'>('medio');
  const [joinCode, setJoinCode] = useState(normalizeRoomCode(initialInviteCode));

  const [isLoading, setIsLoading] = useState(false);
  const [errorMsg, setErrorMsg] = useState('');

  // Sala criada pelo anfitrião aguardando o 2º jogador
  const [waitingRoomCode, setWaitingRoomCode] = useState<string | null>(null);
  const [waitingQuestions, setWaitingQuestions] = useState<Question[]>([]);
  const [roomState, setRoomState] = useState<DuelRoom | null>(null);
  const [hostInfo, setHostInfo] = useState<DuelParticipant | null>(null);
  const [guestInfo, setGuestInfo] = useState<DuelParticipant | null>(null);

  const [copiedCode, setCopiedCode] = useState(false);
  const [copiedLink, setCopiedLink] = useState(false);

  useEffect(() => {
    if (initialInviteCode) {
      setTab('join');
      setJoinCode(normalizeRoomCode(initialInviteCode));
    }
  }, [initialInviteCode]);

  useEffect(() => {
    if (!waitingRoomCode) return;

    const unsubscribe = subscribeToDuelSession(waitingRoomCode, {
      onRoom: (room) => setRoomState(room),
      onHost: (host) => setHostInfo(host),
      onGuest: (guest) => setGuestInfo(guest),
      onError: () => {
        setErrorMsg('Erro de conexão com a sala. Verifique sua internet.');
      },
    });

    return () => unsubscribe();
  }, [waitingRoomCode]);

  // Quando o segundo jogador entra, inicia automaticamente nos dois aparelhos
  useEffect(() => {
    if (
      waitingRoomCode &&
      roomState?.status === 'playing' &&
      guestInfo &&
      waitingQuestions.length === 20
    ) {
      sound.playVictory();
      onStartDuel({
        roomCode: waitingRoomCode,
        slot: 'host',
        difficulty: roomState.difficulty,
        questions: waitingQuestions,
      });
    }
  }, [waitingRoomCode, roomState, guestInfo, waitingQuestions, onStartDuel]);

  const validatePlayer = (): { cleanName: string; cleanAvatar: string } | null => {
    const cleanName = name.trim();
    if (!cleanName) {
      setErrorMsg('Informe seu nome para entrar no duelo.');
      sound.playWrong();
      return null;
    }
    const updated = { name: cleanName, avatar };
    onUpdatePlayer(updated);
    return { cleanName, cleanAvatar: avatar };
  };

  const handleCreateRoom = async (e: React.FormEvent) => {
    e.preventDefault();
    const valid = validatePlayer();
    if (!valid) return;

    sound.playClick();
    setIsLoading(true);
    setErrorMsg('');

    try {
      const { roomCode, questions } = await createDuelRoom(
        valid.cleanName,
        valid.cleanAvatar,
        difficulty
      );
      setWaitingQuestions(questions);
      setWaitingRoomCode(roomCode);
    } catch {
      setErrorMsg('Não foi possível criar a sala agora. Tente novamente.');
    } finally {
      setIsLoading(false);
    }
  };

  const handleJoinRoom = async (e: React.FormEvent) => {
    e.preventDefault();
    const valid = validatePlayer();
    if (!valid) return;

    const cleanCode = normalizeRoomCode(joinCode);
    if (cleanCode.length !== 6) {
      setErrorMsg('Digite o código completo de 6 caracteres da sala.');
      sound.playWrong();
      return;
    }

    sound.playClick();
    setIsLoading(true);
    setErrorMsg('');

    try {
      const joined = await joinDuelRoom(cleanCode, valid.cleanName, valid.cleanAvatar);
      sound.playVictory();
      onStartDuel({
        roomCode: joined.roomCode,
        slot: 'guest',
        difficulty: joined.difficulty,
        questions: joined.questions,
      });
    } catch (err) {
      sound.playWrong();
      setErrorMsg(
        err instanceof Error
          ? err.message
          : 'Não foi possível entrar na sala. Confira o código.'
      );
    } finally {
      setIsLoading(false);
    }
  };

  const inviteUrl = waitingRoomCode
    ? `${window.location.origin}/?duel=${waitingRoomCode}`
    : '';

  const copyText = (text: string, type: 'code' | 'link') => {
    sound.playClick();
    if (navigator.clipboard) {
      navigator.clipboard.writeText(text);
      if (type === 'code') {
        setCopiedCode(true);
        setTimeout(() => setCopiedCode(false), 2200);
      } else {
        setCopiedLink(true);
        setTimeout(() => setCopiedLink(false), 2200);
      }
    }
  };

  const handleShareInvite = async () => {
    sound.playClick();
    if (navigator.share) {
      try {
        await navigator.share({
          title: 'Duelo Bíblico — 20 Questões',
          text: `Te desafio para um duelo bíblico simultâneo! Use o código ${waitingRoomCode} ou acesse o link:`,
          url: inviteUrl,
        });
        return;
      } catch {
        // Fallback para copiar link se o usuário cancelar
      }
    }
    copyText(inviteUrl, 'link');
  };

  const diffLabels: Record<Difficulty | 'misto', string> = {
    facil: 'Fácil',
    medio: 'Médio',
    dificil: 'Difícil',
    misto: 'Misto',
  };

  // Tela de espera do anfitrião
  if (waitingRoomCode) {
    return (
      <div className="max-w-2xl mx-auto px-4 py-8">
        <div className="bg-amber-950/50 backdrop-blur-md border border-amber-700/50 rounded-3xl p-6 sm:p-8 shadow-2xl space-y-6">
          <div className="flex items-center justify-between">
            <button
              type="button"
              onClick={() => {
                sound.playClick();
                setWaitingRoomCode(null);
                setRoomState(null);
                setHostInfo(null);
                setGuestInfo(null);
              }}
              className="text-xs text-amber-300/80 hover:text-amber-100 flex items-center gap-1.5 cursor-pointer"
            >
              <ArrowLeft className="w-4 h-4" />
              <span>Cancelar sala</span>
            </button>

            <span className="px-2.5 py-1 rounded-full bg-amber-500/20 border border-amber-400/30 text-amber-200 text-xs font-bold uppercase">
              Nível: {diffLabels[difficulty]}
            </span>
          </div>

          <div className="text-center space-y-2">
            <div className="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-emerald-500/15 border border-emerald-500/30 text-emerald-300 text-xs font-semibold">
              <Loader2 className="w-3.5 h-3.5 animate-spin" />
              <span>Sala aberta! Aguardando o 2º jogador...</span>
            </div>
            <h2 className="text-2xl sm:text-3xl font-serif font-bold text-amber-100">
              Convide seu Desafiante
            </h2>
            <p className="text-xs sm:text-sm text-amber-200/75 max-w-md mx-auto">
              Envie o código ou o link abaixo para o outro jogador. Assim que ele entrar, as mesmas 20 questões começam simultaneamente nos dois aparelhos!
            </p>
          </div>

          {/* Código da Sala em Destaque */}
          <div className="p-5 rounded-2xl bg-amber-900/30 border border-amber-600/40 text-center space-y-3">
            <div className="text-[11px] uppercase tracking-widest text-amber-300/70 font-bold">
              Código da Sala
            </div>
            <div className="text-4xl sm:text-5xl font-mono font-black tracking-[0.25em] text-amber-200 select-all">
              {waitingRoomCode}
            </div>
            <div className="flex flex-wrap items-center justify-center gap-2 pt-1">
              <button
                type="button"
                onClick={() => copyText(waitingRoomCode, 'code')}
                className="px-4 py-2 rounded-xl bg-amber-800/60 hover:bg-amber-700/70 border border-amber-600/50 text-amber-100 text-xs font-semibold flex items-center gap-1.5 cursor-pointer transition-colors"
              >
                {copiedCode ? <Check className="w-4 h-4 text-emerald-400" /> : <Copy className="w-4 h-4" />}
                <span>{copiedCode ? 'Código Copiado!' : 'Copiar Código'}</span>
              </button>

              <button
                type="button"
                onClick={() => copyText(inviteUrl, 'link')}
                className="px-4 py-2 rounded-xl bg-amber-800/60 hover:bg-amber-700/70 border border-amber-600/50 text-amber-100 text-xs font-semibold flex items-center gap-1.5 cursor-pointer transition-colors"
              >
                {copiedLink ? <Check className="w-4 h-4 text-emerald-400" /> : <Link2 className="w-4 h-4" />}
                <span>{copiedLink ? 'Link Copiado!' : 'Copiar Link Direto'}</span>
              </button>

              <button
                type="button"
                onClick={handleShareInvite}
                className="px-4 py-2 rounded-xl bg-gradient-to-r from-amber-400 to-amber-500 hover:from-amber-300 hover:to-amber-400 text-amber-950 text-xs font-bold flex items-center gap-1.5 cursor-pointer transition-all shadow-md"
              >
                <Share2 className="w-4 h-4" />
                <span>Enviar Convite</span>
              </button>
            </div>
          </div>

          {/* Slots dos 2 Jogadores */}
          <div className="grid grid-cols-1 sm:grid-cols-2 gap-3">
            <div className="p-4 rounded-2xl bg-emerald-950/30 border border-emerald-500/40 flex items-center gap-3">
              <div className="w-11 h-11 rounded-xl bg-emerald-900/50 border border-emerald-500/40 flex items-center justify-center text-2xl">
                {hostInfo?.playerAvatar || avatar}
              </div>
              <div className="min-w-0">
                <div className="text-[10px] uppercase tracking-wider font-bold text-emerald-400">
                  Jogador 1 • Pronto
                </div>
                <div className="font-bold text-amber-100 truncate">
                  {hostInfo?.playerName || name}
                </div>
              </div>
            </div>

            <div className="p-4 rounded-2xl bg-amber-950/40 border border-dashed border-amber-700/60 flex items-center gap-3">
              <div className="w-11 h-11 rounded-xl bg-amber-900/30 border border-amber-800/50 flex items-center justify-center">
                <Users className="w-5 h-5 text-amber-400/60 animate-pulse" />
              </div>
              <div className="min-w-0">
                <div className="text-[10px] uppercase tracking-wider font-bold text-amber-400/70">
                  Jogador 2
                </div>
                <div className="text-sm text-amber-200/70">
                  Aguardando entrar na sala...
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    );
  }

  return (
    <div className="max-w-3xl mx-auto px-4 py-8">
      <div className="mb-4">
        <button
          type="button"
          onClick={() => {
            sound.playClick();
            onBack();
          }}
          className="inline-flex items-center gap-1.5 text-xs font-semibold text-amber-300 hover:text-amber-100 transition-colors cursor-pointer"
        >
          <ArrowLeft className="w-4 h-4" />
          <span>Voltar para o modo individual</span>
        </button>
      </div>

      <div className="text-center mb-6">
        <div className="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-amber-500/15 border border-amber-500/30 text-amber-300 text-xs font-semibold mb-3">
          <Swords className="w-3.5 h-3.5 text-amber-400" />
          <span>Duelo Bíblico Simultâneo • 2 Jogadores</span>
        </div>
        <h1 className="text-2xl sm:text-4xl font-serif font-extrabold text-amber-100 tracking-tight mb-2">
          Mesmas 20 Questões em Tempo Real
        </h1>
        <p className="text-amber-200/80 text-xs sm:text-sm max-w-xl mx-auto">
          Respondam às mesmas 20 perguntas simultaneamente e comparem <strong>precisão</strong> e <strong>tempo de resposta</strong> ao final da rodada.
        </p>
      </div>

      <div className="bg-amber-950/45 backdrop-blur-md border border-amber-800/50 rounded-2xl p-6 sm:p-8 shadow-2xl space-y-6">
        {/* Identificação do Jogador */}
        <div className="space-y-3">
          <label htmlFor="duelPlayerName" className="text-sm font-semibold text-amber-200 block">
            Seu Nome e Emblema
          </label>
          <input
            id="duelPlayerName"
            type="text"
            value={name}
            onChange={(e) => {
              setName(e.target.value);
              if (errorMsg) setErrorMsg('');
            }}
            placeholder="Digite seu nome..."
            maxLength={32}
            className="w-full px-4 py-3 rounded-xl bg-amber-900/30 border border-amber-700/60 text-amber-100 placeholder-amber-400/40 text-base focus:outline-none focus:ring-2 focus:border-amber-500 focus:ring-amber-500/30"
          />

          <div className="grid grid-cols-4 sm:grid-cols-8 gap-2">
            {AVATARS.map((av) => {
              const isSelected = avatar === av.emoji;
              return (
                <button
                  key={av.id}
                  type="button"
                  onClick={() => {
                    sound.playClick();
                    setAvatar(av.emoji);
                  }}
                  title={av.label}
                  className={`flex flex-col items-center justify-center py-2 px-1 rounded-xl border text-lg transition-all cursor-pointer ${
                    isSelected
                      ? 'bg-amber-600/30 border-amber-400 scale-105 ring-1 ring-amber-400'
                      : 'bg-amber-900/20 border-amber-800/40 hover:bg-amber-900/40 opacity-80 hover:opacity-100'
                  }`}
                >
                  <span>{av.emoji}</span>
                  <span className="text-[10px] text-amber-300/80 mt-0.5 truncate max-w-full">
                    {av.label}
                  </span>
                </button>
              );
            })}
          </div>
        </div>

        {/* Abas Criar Sala vs Entrar com Código */}
        <div className="grid grid-cols-2 gap-2 p-1 rounded-xl bg-amber-900/30 border border-amber-800/40">
          <button
            type="button"
            onClick={() => {
              sound.playClick();
              setTab('create');
              setErrorMsg('');
            }}
            className={`py-2.5 rounded-lg text-xs sm:text-sm font-bold transition-all cursor-pointer ${
              tab === 'create'
                ? 'bg-amber-500 text-amber-950 shadow-md'
                : 'text-amber-200/80 hover:text-white'
            }`}
          >
            Criar Sala (Convidar)
          </button>
          <button
            type="button"
            onClick={() => {
              sound.playClick();
              setTab('join');
              setErrorMsg('');
            }}
            className={`py-2.5 rounded-lg text-xs sm:text-sm font-bold transition-all cursor-pointer ${
              tab === 'join'
                ? 'bg-amber-500 text-amber-950 shadow-md'
                : 'text-amber-200/80 hover:text-white'
            }`}
          >
            Entrar com Código
          </button>
        </div>

        {errorMsg && (
          <div className="p-3 rounded-xl bg-red-950/60 border border-red-500/40 text-red-200 text-xs font-medium">
            {errorMsg}
          </div>
        )}

        {tab === 'create' ? (
          <form onSubmit={handleCreateRoom} className="space-y-4">
            <div>
              <span className="text-xs font-semibold text-amber-300/80 block mb-2">
                Escolha o nível das 20 questões do duelo:
              </span>
              <div className="grid grid-cols-2 sm:grid-cols-4 gap-2">
                {[
                  { id: 'facil' as const, label: 'Fácil', icon: '🌿' },
                  { id: 'medio' as const, label: 'Médio', icon: '📜' },
                  { id: 'dificil' as const, label: 'Difícil', icon: '🔥' },
                  { id: 'misto' as const, label: 'Misto', icon: '👑' },
                ].map((opt) => (
                  <button
                    key={opt.id}
                    type="button"
                    onClick={() => {
                      sound.playClick();
                      setDifficulty(opt.id);
                    }}
                    className={`p-3 rounded-xl border text-sm font-bold flex items-center justify-center gap-2 transition-all cursor-pointer ${
                      difficulty === opt.id
                        ? 'bg-amber-500/25 border-amber-400 text-amber-100 ring-1 ring-amber-400'
                        : 'bg-amber-900/20 border-amber-800/40 text-amber-200/75 hover:bg-amber-900/40'
                    }`}
                  >
                    <span>{opt.icon}</span>
                    <span>{opt.label}</span>
                  </button>
                ))}
              </div>
            </div>

            <button
              type="submit"
              disabled={isLoading}
              className="w-full py-4 px-6 rounded-xl font-bold text-base text-amber-950 bg-gradient-to-r from-amber-400 via-amber-300 to-amber-500 hover:from-amber-300 hover:to-amber-400 shadow-xl border border-amber-200 flex items-center justify-center gap-2 transition-all cursor-pointer disabled:opacity-60"
            >
              {isLoading ? (
                <Loader2 className="w-5 h-5 animate-spin" />
              ) : (
                <Sparkles className="w-5 h-5" />
              )}
              <span>{isLoading ? 'Criando Sala...' : 'Criar Sala e Gerar Convite'}</span>
            </button>
          </form>
        ) : (
          <form onSubmit={handleJoinRoom} className="space-y-4">
            <div>
              <label htmlFor="roomCodeInput" className="text-xs font-semibold text-amber-300/80 block mb-2">
                Código da Sala (6 caracteres):
              </label>
              <input
                id="roomCodeInput"
                type="text"
                value={joinCode}
                onChange={(e) => {
                  setJoinCode(normalizeRoomCode(e.target.value));
                  if (errorMsg) setErrorMsg('');
                }}
                placeholder="Ex: K7M9P2"
                maxLength={6}
                className="w-full px-4 py-4 rounded-xl bg-amber-900/30 border border-amber-700/60 text-amber-100 placeholder-amber-400/30 text-center text-2xl font-mono font-black tracking-[0.3em] uppercase focus:outline-none focus:ring-2 focus:border-amber-500 focus:ring-amber-500/30"
              />
            </div>

            <button
              type="submit"
              disabled={isLoading}
              className="w-full py-4 px-6 rounded-xl font-bold text-base text-amber-950 bg-gradient-to-r from-amber-400 via-amber-300 to-amber-500 hover:from-amber-300 hover:to-amber-400 shadow-xl border border-amber-200 flex items-center justify-center gap-2 transition-all cursor-pointer disabled:opacity-60"
            >
              {isLoading ? (
                <Loader2 className="w-5 h-5 animate-spin" />
              ) : (
                <Swords className="w-5 h-5" />
              )}
              <span>{isLoading ? 'Entrando no Duelo...' : 'Entrar no Duelo Agora'}</span>
            </button>
          </form>
        )}
      </div>
    </div>
  );
};
