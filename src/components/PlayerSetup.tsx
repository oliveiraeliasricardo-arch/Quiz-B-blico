import React, { useState } from 'react';
import { Difficulty } from '../types/quiz';
import { AVATARS, SavedPlayer } from '../utils/storage';
import { sound } from '../utils/sound';
import { Sparkles, Award, ArrowRight, Swords } from 'lucide-react';
import { getDatabaseStats } from '../data/questions';

interface PlayerSetupProps {
  initialPlayer: SavedPlayer;
  onStartQuiz: (playerName: string, avatar: string, difficulty: Difficulty | 'misto') => void;
  onOpenLeaderboard: () => void;
  onOpenDuel: () => void;
}

export const PlayerSetup: React.FC<PlayerSetupProps> = ({
  initialPlayer,
  onStartQuiz,
  onOpenLeaderboard,
  onOpenDuel,
}) => {
  const [name, setName] = useState(initialPlayer.name || '');
  const [selectedAvatar, setSelectedAvatar] = useState(initialPlayer.avatar || '📜');
  const [selectedDifficulty, setSelectedDifficulty] = useState<Difficulty | 'misto'>('medio');
  const [nameError, setNameError] = useState('');

  const stats = getDatabaseStats();

  const handleStart = (e: React.FormEvent) => {
    e.preventDefault();
    const cleanName = name.trim();
    if (!cleanName) {
      setNameError('Por favor, informe seu nome para registrar sua pontuação no placar.');
      sound.playWrong();
      return;
    }
    setNameError('');
    sound.playClick();
    onStartQuiz(cleanName, selectedAvatar, selectedDifficulty);
  };

  const difficultyOptions = [
    {
      id: 'facil' as const,
      label: 'Fácil',
      badge: 'Iniciante',
      icon: '🌿',
      color: 'border-emerald-500/40 bg-emerald-950/20 text-emerald-200',
      activeColor: 'ring-2 ring-emerald-500 bg-emerald-900/40 border-emerald-500 text-emerald-100',
      count: stats.facil,
      desc: 'Histórias essenciais, personagens centrais e acontecimentos bíblicos célebres.',
    },
    {
      id: 'medio' as const,
      label: 'Médio',
      badge: 'Recomendado',
      icon: '📜',
      color: 'border-amber-500/40 bg-amber-950/20 text-amber-200',
      activeColor: 'ring-2 ring-amber-500 bg-amber-900/40 border-amber-500 text-amber-100',
      count: stats.medio,
      desc: 'Detalhes de passagens, ensinamentos apostólicos, profecias e versículos conhecidos.',
    },
    {
      id: 'dificil' as const,
      label: 'Difícil',
      badge: 'Teológico',
      icon: '🔥',
      color: 'border-red-500/40 bg-red-950/20 text-red-200',
      activeColor: 'ring-2 ring-red-500 bg-red-900/40 border-red-500 text-red-100',
      count: stats.dificil,
      desc: 'Genealogias, cidades antigas, detalhes minuciosos e profunda teologia bíblica.',
    },
    {
      id: 'misto' as const,
      label: 'Misto',
      badge: 'Desafio Total',
      icon: '👑',
      color: 'border-purple-500/40 bg-purple-950/20 text-purple-200',
      activeColor: 'ring-2 ring-purple-500 bg-purple-900/40 border-purple-500 text-purple-100',
      count: stats.total,
      desc: 'Sorteio aleatório abrangendo os 3 níveis entre todas as 1.000 questões da Bíblia.',
    },
  ];

  return (
    <div className="max-w-3xl mx-auto px-4 py-8">
      {/* Banner de Boas-Vindas */}
      <div className="text-center mb-8">
        <div className="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-amber-500/10 border border-amber-500/20 text-amber-300 text-xs font-medium mb-3">
          <Sparkles className="w-3.5 h-3.5 text-amber-400" />
          <span>Banco Oficial com 1.000 Questões Bíblicas</span>
        </div>
        <h1 className="text-3xl sm:text-4xl lg:text-5xl font-serif font-extrabold text-amber-100 tracking-tight mb-3">
          Quiz da Bíblia Sagrada
        </h1>
        <p className="text-amber-200/80 text-sm sm:text-base max-w-xl mx-auto leading-relaxed">
          Teste seus conhecimentos sagrados do livro de <strong>Gênesis ao Apocalipse</strong>. 
          Cada rodada contém <strong>20 questões</strong> sorteadas, com gabarito imediato e explicações versículo a versículo.
        </p>
      </div>

      {/* Formulário Principal */}
      <form onSubmit={handleStart} className="bg-amber-950/40 backdrop-blur-md border border-amber-800/40 rounded-2xl p-6 sm:p-8 shadow-2xl shadow-amber-950/50 space-y-8">
        
        {/* Seção 1: Identificação do Jogador */}
        <div className="space-y-4">
          <div className="flex items-center justify-between">
            <label htmlFor="playerName" className="text-sm font-semibold text-amber-200 flex items-center gap-2">
              <span className="w-5 h-5 rounded-full bg-amber-500/20 text-amber-300 flex items-center justify-center text-xs font-bold">1</span>
              Nome do Jogador
            </label>
            <span className="text-xs text-amber-400/60">Aparecerá no placar com posições</span>
          </div>

          <div className="relative">
            <input
              id="playerName"
              type="text"
              value={name}
              onChange={(e) => {
                setName(e.target.value);
                if (nameError) setNameError('');
              }}
              placeholder="Ex: Pedro, Maria, Discípulo João..."
              maxLength={32}
              className={`w-full px-4 py-3.5 rounded-xl bg-amber-900/30 border text-amber-100 placeholder-amber-400/40 text-base focus:outline-none focus:ring-2 transition-all ${
                nameError
                  ? 'border-red-500/80 focus:ring-red-500'
                  : 'border-amber-700/60 focus:border-amber-500 focus:ring-amber-500/30'
              }`}
            />
            {nameError && (
              <p className="mt-1.5 text-xs text-red-400 font-medium">
                {nameError}
              </p>
            )}
          </div>

          {/* Escolha do Avatar / Título Bíblico */}
          <div>
            <label className="text-xs font-medium text-amber-300/80 mb-2 block">
              Escolha seu emblema ou título:
            </label>
            <div className="grid grid-cols-4 sm:grid-cols-8 gap-2">
              {AVATARS.map((av) => {
                const isSelected = selectedAvatar === av.emoji;
                return (
                  <button
                    key={av.id}
                    type="button"
                    onClick={() => {
                      sound.playClick();
                      setSelectedAvatar(av.emoji);
                    }}
                    title={av.label}
                    className={`flex flex-col items-center justify-center py-2.5 px-1 rounded-xl border text-xl transition-all ${
                      isSelected
                        ? 'bg-amber-600/30 border-amber-400 scale-105 shadow-md shadow-amber-900/50 ring-1 ring-amber-400'
                        : 'bg-amber-900/20 border-amber-800/40 hover:bg-amber-900/40 hover:border-amber-700/60 opacity-80 hover:opacity-100'
                    }`}
                  >
                    <span>{av.emoji}</span>
                    <span className="text-[10px] text-amber-300/80 mt-1 truncate max-w-full">
                      {av.label}
                    </span>
                  </button>
                );
              })}
            </div>
          </div>
        </div>

        {/* Seção 2: Escolha da Dificuldade */}
        <div className="space-y-4">
          <div className="flex items-center justify-between">
            <label className="text-sm font-semibold text-amber-200 flex items-center gap-2">
              <span className="w-5 h-5 rounded-full bg-amber-500/20 text-amber-300 flex items-center justify-center text-xs font-bold">2</span>
              Nível de Dificuldade
            </label>
            <span className="text-xs text-amber-400/60">3 níveis oficiais + modo misto</span>
          </div>

          <div className="grid grid-cols-1 sm:grid-cols-2 gap-3">
            {difficultyOptions.map((opt) => {
              const isSelected = selectedDifficulty === opt.id;
              return (
                <div
                  key={opt.id}
                  onClick={() => {
                    sound.playClick();
                    setSelectedDifficulty(opt.id);
                  }}
                  className={`p-4 rounded-xl border cursor-pointer transition-all ${
                    isSelected ? opt.activeColor : `${opt.color} hover:border-amber-600/50 opacity-85 hover:opacity-100`
                  }`}
                >
                  <div className="flex items-center justify-between mb-1.5">
                    <div className="flex items-center gap-2">
                      <span className="text-lg">{opt.icon}</span>
                      <span className="font-bold text-base">{opt.label}</span>
                    </div>
                    <span className="text-[11px] font-semibold px-2 py-0.5 rounded-full bg-black/30 border border-white/10">
                      {opt.badge}
                    </span>
                  </div>
                  <p className="text-xs text-amber-200/70 mb-2 leading-relaxed">
                    {opt.desc}
                  </p>
                  <div className="flex items-center justify-between text-[11px] text-amber-300/60 pt-2 border-t border-white/5">
                    <span>Acervo disponível:</span>
                    <span className="font-semibold text-amber-200">{opt.count} questões</span>
                  </div>
                </div>
              );
            })}
          </div>
        </div>

        {/* Botão de Ação Primária */}
        <div className="flex flex-col sm:flex-row gap-3 pt-2">
          <button
            type="submit"
            className="flex-1 py-4 px-6 rounded-xl font-bold text-base text-amber-950 bg-gradient-to-r from-amber-400 via-amber-300 to-amber-500 hover:from-amber-300 hover:to-amber-400 shadow-xl shadow-amber-900/40 border border-amber-200 flex items-center justify-center gap-2.5 transition-all transform active:scale-[0.98] cursor-pointer"
          >
            <span>Iniciar Quiz (20 Questões)</span>
            <ArrowRight className="w-5 h-5 text-amber-950" />
          </button>

          <button
            type="button"
            onClick={() => {
              sound.playClick();
              onOpenDuel();
            }}
            className="py-4 px-5 rounded-xl font-bold text-sm text-amber-100 bg-gradient-to-r from-amber-700/80 to-amber-800/80 hover:from-amber-600 hover:to-amber-700 border border-amber-500/50 flex items-center justify-center gap-2 transition-all active:scale-[0.98] cursor-pointer shadow-lg"
            title="Jogar simultaneamente contra outro jogador nas mesmas 20 questões"
          >
            <Swords className="w-4 h-4 text-amber-300" />
            <span>Duelo (2 Jogadores)</span>
          </button>

          <button
            type="button"
            onClick={() => {
              sound.playClick();
              onOpenLeaderboard();
            }}
            className="py-4 px-5 rounded-xl font-semibold text-sm text-amber-200 bg-amber-900/40 hover:bg-amber-900/70 border border-amber-700/50 flex items-center justify-center gap-2 transition-all active:scale-[0.98] cursor-pointer"
          >
            <Award className="w-4 h-4 text-amber-400" />
            <span>Ver Placar</span>
          </button>
        </div>

      </form>

      {/* Estatísticas resumidas do banco */}
      <div className="mt-8 grid grid-cols-2 sm:grid-cols-4 gap-3 text-center">
        <div className="p-3 rounded-xl bg-amber-950/20 border border-amber-800/30">
          <div className="text-xl font-bold text-amber-200">{stats.total}</div>
          <div className="text-[11px] text-amber-400/60 uppercase tracking-wider font-semibold">Total de Questões</div>
        </div>
        <div className="p-3 rounded-xl bg-amber-950/20 border border-amber-800/30">
          <div className="text-xl font-bold text-amber-200">{stats.vt}</div>
          <div className="text-[11px] text-amber-400/60 uppercase tracking-wider font-semibold">Antigo Testamento</div>
        </div>
        <div className="p-3 rounded-xl bg-amber-950/20 border border-amber-800/30">
          <div className="text-xl font-bold text-amber-200">{stats.nt}</div>
          <div className="text-[11px] text-amber-400/60 uppercase tracking-wider font-semibold">Novo Testamento</div>
        </div>
        <div className="p-3 rounded-xl bg-amber-950/20 border border-amber-800/30">
          <div className="text-xl font-bold text-amber-200">20 / Rodada</div>
          <div className="text-[11px] text-amber-400/60 uppercase tracking-wider font-semibold">Formato do Jogo</div>
        </div>
      </div>
    </div>
  );
};
