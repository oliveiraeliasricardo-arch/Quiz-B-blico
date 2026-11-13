import React, { useState } from 'react';
import { BookOpen, Trophy, Volume2, VolumeX } from 'lucide-react';
import { sound } from '../utils/sound';
import { SavedPlayer } from '../utils/storage';

interface NavbarProps {
  player: SavedPlayer;
  onOpenLeaderboard: () => void;
  onNewGame: () => void;
  isInGame: boolean;
}

export const Navbar: React.FC<NavbarProps> = ({
  player,
  onOpenLeaderboard,
  onNewGame,
  isInGame,
}) => {
  const [muted, setMuted] = useState(sound.getMuted());
  const [confirmRestart, setConfirmRestart] = useState(false);

  const handleToggleSound = () => {
    const isNowMuted = sound.toggleMute();
    setMuted(isNowMuted);
    if (!isNowMuted) {
      sound.playClick();
    }
  };

  return (
    <header className="sticky top-0 z-40 bg-amber-950/90 backdrop-blur-md border-b border-amber-800/40 text-amber-50 shadow-lg">
      <div className="max-w-6xl mx-auto px-4 h-16 flex items-center justify-between">
        {/* Logo / Brand */}
        <div 
          onClick={onNewGame}
          className="flex items-center gap-3 cursor-pointer group transition-transform active:scale-95"
        >
          <div className="w-10 h-10 rounded-xl bg-gradient-to-br from-amber-500 to-amber-700 flex items-center justify-center shadow-md shadow-amber-900/30 border border-amber-300/30 group-hover:scale-105 transition-all">
            <BookOpen className="w-5 h-5 text-amber-100" />
          </div>
          <div>
            <div className="flex items-center gap-2">
              <span className="font-serif text-lg font-bold tracking-wide text-amber-100 group-hover:text-amber-200 transition-colors">
                Quiz Bíblico
              </span>
              <span className="text-[10px] uppercase font-bold tracking-widest px-1.5 py-0.5 rounded bg-amber-500/20 text-amber-300 border border-amber-500/30">
                1.000 Questões
              </span>
            </div>
            <p className="text-[11px] text-amber-300/70 hidden sm:block">
              Do Gênesis ao Apocalipse • Bíblia Sagrada
            </p>
          </div>
        </div>

        {/* Action Controls */}
        <div className="flex items-center gap-2 sm:gap-3">
          {/* Player chip */}
          {player.name && (
            <div className="hidden md:flex items-center gap-1.5 px-3 py-1.5 rounded-full bg-amber-900/60 border border-amber-700/50 text-xs text-amber-200">
              <span>{player.avatar}</span>
              <span className="font-medium max-w-[120px] truncate">{player.name}</span>
            </div>
          )}

          {/* Placar com posições */}
          <button
            onClick={() => {
              sound.playClick();
              onOpenLeaderboard();
            }}
            className="flex items-center gap-1.5 px-2.5 sm:px-3 py-1.5 rounded-lg text-xs font-semibold text-amber-100 bg-gradient-to-r from-amber-600 to-amber-700 hover:from-amber-500 hover:to-amber-600 shadow-sm border border-amber-400/30 transition-all active:scale-95"
            title="Ver posições e placar dos jogadores"
          >
            <Trophy className="w-4 h-4 text-amber-200" />
            <span>Placar</span>
          </button>

          {/* Toggle de Som */}
          <button
            onClick={handleToggleSound}
            aria-label={muted ? 'Ativar som' : 'Desativar som'}
            className="w-9 h-9 rounded-lg flex items-center justify-center text-amber-300 hover:text-amber-100 bg-amber-900/40 hover:bg-amber-900/70 border border-amber-700/40 transition-colors"
            title={muted ? 'Ativar áudio' : 'Desativar áudio'}
          >
            {muted ? <VolumeX className="w-4 h-4 text-amber-400/60" /> : <Volume2 className="w-4 h-4 text-amber-300" />}
          </button>

          {/* Botão Novo Jogo se estiver em andamento */}
          {isInGame && (
            <button
              onClick={() => {
                sound.playClick();
                if (!confirmRestart) {
                  setConfirmRestart(true);
                  setTimeout(() => setConfirmRestart(false), 3500);
                  return;
                }
                setConfirmRestart(false);
                onNewGame();
              }}
              className={`text-xs px-2.5 py-1.5 rounded-lg transition-colors ${
                confirmRestart
                  ? 'bg-red-600/80 text-white font-bold'
                  : 'text-amber-300/80 hover:text-amber-200 underline decoration-amber-700 underline-offset-4'
              }`}
            >
              {confirmRestart ? 'Confirmar?' : 'Reiniciar'}
            </button>
          )}
        </div>
      </div>
    </header>
  );
};
