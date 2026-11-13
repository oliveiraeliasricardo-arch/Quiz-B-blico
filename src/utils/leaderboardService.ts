import {
  collection,
  doc,
  getDocs,
  limit,
  onSnapshot,
  query,
  serverTimestamp,
  setDoc,
  Timestamp,
  where,
  writeBatch,
} from 'firebase/firestore';
import { db, handleFirestoreError, OperationType } from '../firebase';
import { Difficulty, PlayerScore } from '../types/quiz';
import { getLeaderboard as getLocalLeaderboard, savePlayerScore as saveLocalPlayerScore, resetLeaderboard as resetLocalLeaderboard } from './storage';

const SCORES_COLLECTION = 'scores';

export function sortScores(scores: PlayerScore[]): PlayerScore[] {
  return [...scores].sort((a, b) => {
    if (b.score !== a.score) return b.score - a.score;
    if (b.accuracy !== a.accuracy) return b.accuracy - a.accuracy;
    return a.timeSpentSeconds - b.timeSpentSeconds;
  });
}

function docToPlayerScore(id: string, data: Record<string, unknown>): PlayerScore {
  let isoDate = new Date().toISOString();
  const createdAt = data.createdAt;
  if (createdAt instanceof Timestamp) {
    isoDate = createdAt.toDate().toISOString();
  } else if (typeof createdAt === 'string') {
    isoDate = createdAt;
  }

  return {
    id,
    playerName: typeof data.playerName === 'string' ? data.playerName : 'Jogador',
    playerAvatar: typeof data.playerAvatar === 'string' ? data.playerAvatar : '📜',
    score: typeof data.score === 'number' ? data.score : 0,
    correctAnswers: typeof data.correctAnswers === 'number' ? data.correctAnswers : 0,
    totalQuestions: typeof data.totalQuestions === 'number' ? data.totalQuestions : 20,
    accuracy: typeof data.accuracy === 'number' ? data.accuracy : 0,
    difficulty: (data.difficulty as Difficulty | 'misto') || 'medio',
    timeSpentSeconds: typeof data.timeSpentSeconds === 'number' ? data.timeSpentSeconds : 0,
    date: isoDate,
  };
}

/**
 * Inscreve-se em tempo real no placar online compartilhado no Firestore.
 */
export function subscribeToOnlineLeaderboard(
  onUpdate: (scores: PlayerScore[]) => void,
  onError?: (err: Error) => void
): () => void {
  const q = query(
    collection(db, SCORES_COLLECTION),
    where('isPublic', '==', true),
    limit(100)
  );

  const unsubscribe = onSnapshot(
    q,
    (snapshot) => {
      const onlineScores: PlayerScore[] = snapshot.docs.map((d) =>
        docToPlayerScore(d.id, d.data() as Record<string, unknown>)
      );
      const sorted = sortScores(onlineScores);
      try {
        localStorage.setItem('biblia_quiz_leaderboard_v1', JSON.stringify(sorted.slice(0, 100)));
      } catch {}
      onUpdate(sorted);
    },
    (error) => {
      if (onError) {
        onError(error);
      }
      try {
        handleFirestoreError(error, OperationType.GET, SCORES_COLLECTION);
      } catch (wrapped) {
        console.error(wrapped);
      }
    }
  );

  return unsubscribe;
}

/**
 * Salva a pontuação do jogador no Placar Online (Firestore) e no cache local.
 */
export async function saveOnlineScore(entry: Omit<PlayerScore, 'id' | 'date'>): Promise<PlayerScore> {
  const randomSuffix = Math.random().toString(36).replace(/[^a-z0-9]/gi, '').slice(0, 8) || 'quiz';
  const safeId = `score_${Date.now()}_${randomSuffix}`;

  const cleanName = entry.playerName.trim().slice(0, 32) || 'Discípulo';
  const cleanAvatar = entry.playerAvatar.trim().slice(0, 16) || '📜';
  const safeScore = Math.min(3000, Math.max(0, Math.round(entry.score)));
  const safeCorrect = Math.min(20, Math.max(0, Math.round(entry.correctAnswers)));
  const safeTotal = 20;
  const safeAccuracy = Math.min(100, Math.max(0, Math.round((safeCorrect / safeTotal) * 100)));
  const validDiffs: Array<Difficulty | 'misto'> = ['facil', 'medio', 'dificil', 'misto'];
  const safeDifficulty = validDiffs.includes(entry.difficulty) ? entry.difficulty : 'medio';
  const safeTime = Math.min(86400, Math.max(0, Math.round(entry.timeSpentSeconds)));

  const localRecord: PlayerScore = {
    id: safeId,
    playerName: cleanName,
    playerAvatar: cleanAvatar,
    score: safeScore,
    correctAnswers: safeCorrect,
    totalQuestions: safeTotal,
    accuracy: safeAccuracy,
    difficulty: safeDifficulty,
    timeSpentSeconds: safeTime,
    date: new Date().toISOString(),
  };

  // Salva cópia local imediata
  saveLocalPlayerScore(localRecord);

  // Salva na nuvem (Firestore) para todos os jogadores verem
  const payload = {
    playerName: cleanName,
    playerAvatar: cleanAvatar,
    score: safeScore,
    correctAnswers: safeCorrect,
    totalQuestions: safeTotal,
    accuracy: safeAccuracy,
    difficulty: safeDifficulty,
    timeSpentSeconds: safeTime,
    isPublic: true,
    createdAt: serverTimestamp(),
  };

  try {
    await setDoc(doc(db, SCORES_COLLECTION, safeId), payload);
  } catch (error) {
    handleFirestoreError(error, OperationType.CREATE, `${SCORES_COLLECTION}/${safeId}`);
  }

  return localRecord;
}

/**
 * Remove todas as pontuações do placar online (somente Administrador autenticado).
 */
export async function clearAllOnlineScores(): Promise<void> {
  const q = query(collection(db, SCORES_COLLECTION), where('isPublic', '==', true));
  try {
    const snapshot = await getDocs(q);
    if (!snapshot.empty) {
      const batch = writeBatch(db);
      snapshot.docs.forEach((docSnap) => {
        batch.delete(docSnap.ref);
      });
      await batch.commit();
    }
    resetLocalLeaderboard();
  } catch (error) {
    handleFirestoreError(error, OperationType.DELETE, SCORES_COLLECTION);
  }
}

export function getInitialCachedLeaderboard(): PlayerScore[] {
  return getLocalLeaderboard();
}
