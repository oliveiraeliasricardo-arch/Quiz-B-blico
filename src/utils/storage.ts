import { PlayerScore, Difficulty } from '../types/quiz';

const LEADERBOARD_KEY = 'biblia_quiz_leaderboard_v1';
const CURRENT_PLAYER_KEY = 'biblia_quiz_current_player_v1';

export const AVATARS = [
  { id: 'peregrino', label: 'Peregrino', emoji: '📜' },
  { id: 'discipulo', label: 'Discípulo', emoji: '🕊️' },
  { id: 'levita', label: 'Levita', emoji: '🎺' },
  { id: 'profeta', label: 'Profeta', emoji: '🕯️' },
  { id: 'guerreiro', label: 'Valente da Fé', emoji: '🛡️' },
  { id: 'sabio', label: 'Sábio', emoji: '👑' },
  { id: 'pastor', label: 'Bom Pastor', emoji: '🌿' },
  { id: 'estrela', label: 'Estrela da Manhã', emoji: '⭐' },
];

export interface SavedPlayer {
  name: string;
  avatar: string;
}

export function getLeaderboard(): PlayerScore[] {
  try {
    const raw = localStorage.getItem(LEADERBOARD_KEY);
    if (!raw) {
      return [];
    }
    const parsed = JSON.parse(raw) as PlayerScore[];
    // Remove automaticamente registros fictícios de demonstração ('seed-*') caso existam
    const realScores = parsed.filter((s) => !String(s.id || '').startsWith('seed-'));
    if (realScores.length !== parsed.length) {
      localStorage.setItem(LEADERBOARD_KEY, JSON.stringify(realScores));
    }
    return sortLeaderboard(realScores);
  } catch {
    return [];
  }
}

export function savePlayerScore(score: PlayerScore): PlayerScore[] {
  try {
    const current = getLeaderboard();
    const updated = [score, ...current];
    const sorted = sortLeaderboard(updated);
    // Guarda os melhores 100
    const trimmed = sorted.slice(0, 100);
    localStorage.setItem(LEADERBOARD_KEY, JSON.stringify(trimmed));
    return trimmed;
  } catch {
    return [score];
  }
}

function sortLeaderboard(scores: PlayerScore[]): PlayerScore[] {
  return [...scores].sort((a, b) => {
    // 1º Maior pontuação
    if (b.score !== a.score) {
      return b.score - a.score;
    }
    // 2º Maior precisão de acertos
    if (b.accuracy !== a.accuracy) {
      return b.accuracy - a.accuracy;
    }
    // 3º Menor tempo gasto
    return a.timeSpentSeconds - b.timeSpentSeconds;
  });
}

export function resetLeaderboard(): PlayerScore[] {
  try {
    localStorage.setItem(LEADERBOARD_KEY, JSON.stringify([]));
  } catch {}
  return [];
}

export function getCurrentPlayer(): SavedPlayer {
  try {
    const raw = localStorage.getItem(CURRENT_PLAYER_KEY);
    if (raw) {
      return JSON.parse(raw);
    }
  } catch {}
  return {
    name: '',
    avatar: '📜',
  };
}

export function saveCurrentPlayer(player: SavedPlayer) {
  try {
    localStorage.setItem(CURRENT_PLAYER_KEY, JSON.stringify(player));
  } catch {}
}

export function formatTime(seconds: number): string {
  const mins = Math.floor(seconds / 60);
  const secs = seconds % 60;
  return `${mins}:${secs.toString().padStart(2, '0')}`;
}
