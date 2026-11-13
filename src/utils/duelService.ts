import {
  doc,
  getDoc,
  onSnapshot,
  serverTimestamp,
  Timestamp,
  updateDoc,
  writeBatch,
} from 'firebase/firestore';
import { db, handleFirestoreError, OperationType } from '../firebase';
import { getQuestionsByIds, getQuestionsForRound } from '../data/questions';
import {
  Difficulty,
  DuelParticipant,
  DuelRoom,
  DuelSlot,
  DuelStatus,
  Question,
} from '../types/quiz';

const DUELS_COLLECTION = 'duels';
const ROOM_CHARS = 'ABCDEFGHJKLMNPQRSTUVWXYZ23456789';

export function normalizeRoomCode(raw: string): string {
  return raw
    .toUpperCase()
    .replace(/[^A-Z0-9]/g, '')
    .slice(0, 6);
}

export function generateRoomCode(): string {
  let code = '';
  for (let i = 0; i < 6; i++) {
    code += ROOM_CHARS[Math.floor(Math.random() * ROOM_CHARS.length)];
  }
  return code;
}

function sanitizeName(name: string): string {
  return name.trim().slice(0, 32) || 'Discípulo';
}

function sanitizeAvatar(avatar: string): string {
  return avatar.trim().slice(0, 16) || '📜';
}

function toIsoDate(val: unknown): string | undefined {
  if (val instanceof Timestamp) {
    return val.toDate().toISOString();
  }
  if (typeof val === 'string') {
    return val;
  }
  return undefined;
}

function docToDuelRoom(id: string, data: Record<string, unknown>): DuelRoom {
  const validDiffs: Array<Difficulty | 'misto'> = ['facil', 'medio', 'dificil', 'misto'];
  const diff = validDiffs.includes(data.difficulty as Difficulty | 'misto')
    ? (data.difficulty as Difficulty | 'misto')
    : 'medio';
  const validStatuses: DuelStatus[] = ['waiting', 'playing', 'finished'];
  const status = validStatuses.includes(data.status as DuelStatus)
    ? (data.status as DuelStatus)
    : 'waiting';
  const rawIds = Array.isArray(data.questionIds)
    ? data.questionIds.filter((n): n is number => typeof n === 'number')
    : [];

  return {
    roomCode: typeof data.roomCode === 'string' ? data.roomCode : id,
    difficulty: diff,
    questionIds: rawIds,
    status,
    createdAt: toIsoDate(data.createdAt),
    startedAt: toIsoDate(data.startedAt),
  };
}

function docToParticipant(
  duelId: string,
  slot: DuelSlot,
  data: Record<string, unknown>
): DuelParticipant {
  const answerTimesMs = Array.isArray(data.answerTimesMs)
    ? data.answerTimesMs
        .filter((n): n is number => typeof n === 'number')
        .slice(0, 20)
    : [];
  const answersCorrect = Array.isArray(data.answersCorrect)
    ? data.answersCorrect
        .filter((b): b is boolean => typeof b === 'boolean')
        .slice(0, 20)
    : [];

  return {
    duelId: typeof data.duelId === 'string' ? data.duelId : duelId,
    slot: data.slot === 'guest' ? 'guest' : slot,
    playerName: typeof data.playerName === 'string' ? data.playerName : 'Jogador',
    playerAvatar: typeof data.playerAvatar === 'string' ? data.playerAvatar : '📜',
    currentQuestionIndex:
      typeof data.currentQuestionIndex === 'number' ? data.currentQuestionIndex : 0,
    answeredCount: typeof data.answeredCount === 'number' ? data.answeredCount : 0,
    correctAnswers: typeof data.correctAnswers === 'number' ? data.correctAnswers : 0,
    score: typeof data.score === 'number' ? data.score : 0,
    totalTimeMs: typeof data.totalTimeMs === 'number' ? data.totalTimeMs : 0,
    avgResponseMs: typeof data.avgResponseMs === 'number' ? data.avgResponseMs : 0,
    answerTimesMs,
    answersCorrect,
    finished: data.finished === true,
  };
}

/**
 * Cria uma nova sala de duelo com 20 questões sorteadas e registra o anfitrião.
 */
export async function createDuelRoom(
  playerName: string,
  playerAvatar: string,
  difficulty: Difficulty | 'misto'
): Promise<{ roomCode: string; questions: Question[] }> {
  const questions = getQuestionsForRound(difficulty, 20);
  const questionIds = questions.map((q) => q.id);

  let roomCode = '';
  for (let attempt = 0; attempt < 4; attempt++) {
    const candidate = generateRoomCode();
    try {
      const existingSnap = await getDoc(doc(db, DUELS_COLLECTION, candidate));
      if (!existingSnap.exists()) {
        roomCode = candidate;
        break;
      }
    } catch (error) {
      handleFirestoreError(error, OperationType.GET, `${DUELS_COLLECTION}/${candidate}`);
    }
  }

  if (!roomCode) {
    roomCode = generateRoomCode();
  }

  const cleanName = sanitizeName(playerName);
  const cleanAvatar = sanitizeAvatar(playerAvatar);

  const duelRef = doc(db, DUELS_COLLECTION, roomCode);
  const hostRef = doc(db, DUELS_COLLECTION, roomCode, 'participants', 'host');

  const batch = writeBatch(db);
  batch.set(duelRef, {
    roomCode,
    difficulty,
    questionIds,
    status: 'waiting',
    createdAt: serverTimestamp(),
  });
  batch.set(hostRef, {
    duelId: roomCode,
    slot: 'host',
    playerName: cleanName,
    playerAvatar: cleanAvatar,
    currentQuestionIndex: 0,
    answeredCount: 0,
    correctAnswers: 0,
    score: 0,
    totalTimeMs: 0,
    avgResponseMs: 0,
    answerTimesMs: [],
    answersCorrect: [],
    finished: false,
    joinedAt: serverTimestamp(),
    updatedAt: serverTimestamp(),
  });

  try {
    await batch.commit();
  } catch (error) {
    handleFirestoreError(error, OperationType.CREATE, `${DUELS_COLLECTION}/${roomCode}`);
  }

  return { roomCode, questions };
}

/**
 * Entra em uma sala de duelo existente usando o código de 6 caracteres.
 */
export async function joinDuelRoom(
  rawCode: string,
  playerName: string,
  playerAvatar: string
): Promise<{
  roomCode: string;
  difficulty: Difficulty | 'misto';
  questions: Question[];
}> {
  const roomCode = normalizeRoomCode(rawCode);
  if (roomCode.length !== 6) {
    throw new Error('Informe o código completo de 6 letras/números da sala.');
  }

  const duelRef = doc(db, DUELS_COLLECTION, roomCode);
  let duelSnap;
  try {
    duelSnap = await getDoc(duelRef);
  } catch (error) {
    handleFirestoreError(error, OperationType.GET, `${DUELS_COLLECTION}/${roomCode}`);
  }

  if (!duelSnap.exists()) {
    throw new Error('Sala de duelo não encontrada. Confira o código com seu amigo.');
  }

  const room = docToDuelRoom(duelSnap.id, duelSnap.data() as Record<string, unknown>);
  if (room.status !== 'waiting') {
    throw new Error('Este duelo já foi iniciado ou encerrado.');
  }

  const questions = getQuestionsByIds(room.questionIds);
  if (questions.length !== 20) {
    throw new Error('Não foi possível carregar as 20 questões deste duelo.');
  }

  const guestRef = doc(db, DUELS_COLLECTION, roomCode, 'participants', 'guest');
  const batch = writeBatch(db);
  batch.set(guestRef, {
    duelId: roomCode,
    slot: 'guest',
    playerName: sanitizeName(playerName),
    playerAvatar: sanitizeAvatar(playerAvatar),
    currentQuestionIndex: 0,
    answeredCount: 0,
    correctAnswers: 0,
    score: 0,
    totalTimeMs: 0,
    avgResponseMs: 0,
    answerTimesMs: [],
    answersCorrect: [],
    finished: false,
    joinedAt: serverTimestamp(),
    updatedAt: serverTimestamp(),
  });
  batch.update(duelRef, {
    status: 'playing',
    startedAt: serverTimestamp(),
  });

  try {
    await batch.commit();
  } catch (error) {
    handleFirestoreError(error, OperationType.WRITE, `${DUELS_COLLECTION}/${roomCode}`);
  }

  return {
    roomCode,
    difficulty: room.difficulty,
    questions,
  };
}

/**
 * Escuta em tempo real a sala e os dois participantes (anfitrião e convidado).
 */
export function subscribeToDuelSession(
  roomCode: string,
  callbacks: {
    onRoom: (room: DuelRoom | null) => void;
    onHost: (host: DuelParticipant | null) => void;
    onGuest: (guest: DuelParticipant | null) => void;
    onError?: (error: Error) => void;
  }
): () => void {
  const duelRef = doc(db, DUELS_COLLECTION, roomCode);
  const hostRef = doc(db, DUELS_COLLECTION, roomCode, 'participants', 'host');
  const guestRef = doc(db, DUELS_COLLECTION, roomCode, 'participants', 'guest');

  const unsubRoom = onSnapshot(
    duelRef,
    (snap) => {
      if (!snap.exists()) {
        callbacks.onRoom(null);
        return;
      }
      callbacks.onRoom(docToDuelRoom(snap.id, snap.data() as Record<string, unknown>));
    },
    (error) => {
      if (callbacks.onError) callbacks.onError(error);
      try {
        handleFirestoreError(error, OperationType.GET, `${DUELS_COLLECTION}/${roomCode}`);
      } catch (wrapped) {
        console.error(wrapped);
      }
    }
  );

  const unsubHost = onSnapshot(
    hostRef,
    (snap) => {
      if (!snap.exists()) {
        callbacks.onHost(null);
        return;
      }
      callbacks.onHost(
        docToParticipant(roomCode, 'host', snap.data() as Record<string, unknown>)
      );
    },
    (error) => {
      if (callbacks.onError) callbacks.onError(error);
      try {
        handleFirestoreError(
          error,
          OperationType.GET,
          `${DUELS_COLLECTION}/${roomCode}/participants/host`
        );
      } catch (wrapped) {
        console.error(wrapped);
      }
    }
  );

  const unsubGuest = onSnapshot(
    guestRef,
    (snap) => {
      if (!snap.exists()) {
        callbacks.onGuest(null);
        return;
      }
      callbacks.onGuest(
        docToParticipant(roomCode, 'guest', snap.data() as Record<string, unknown>)
      );
    },
    (error) => {
      if (callbacks.onError) callbacks.onError(error);
      try {
        handleFirestoreError(
          error,
          OperationType.GET,
          `${DUELS_COLLECTION}/${roomCode}/participants/guest`
        );
      } catch (wrapped) {
        console.error(wrapped);
      }
    }
  );

  return () => {
    unsubRoom();
    unsubHost();
    unsubGuest();
  };
}

/**
 * Atualiza em tempo real o progresso e tempo de resposta do jogador na sala de duelo.
 */
export async function submitDuelAnswerProgress(params: {
  roomCode: string;
  slot: DuelSlot;
  currentQuestionIndex: number;
  answeredCount: number;
  correctAnswers: number;
  score: number;
  answerTimesMs: number[];
  answersCorrect: boolean[];
  finished: boolean;
}): Promise<void> {
  const { roomCode, slot } = params;
  const clampedTimes = params.answerTimesMs
    .slice(0, 20)
    .map((t) => Math.min(3600000, Math.max(0, Math.round(t))));
  const clampedCorrects = params.answersCorrect.slice(0, 20);
  const answeredCount = Math.min(20, Math.max(0, Math.round(params.answeredCount)));
  const totalTimeMs = Math.min(
    86400000,
    Math.max(
      0,
      clampedTimes.reduce((acc, val) => acc + val, 0)
    )
  );
  const avgResponseMs =
    answeredCount > 0 ? Math.round(totalTimeMs / answeredCount) : 0;

  const participantRef = doc(db, DUELS_COLLECTION, roomCode, 'participants', slot);

  try {
    await updateDoc(participantRef, {
      currentQuestionIndex: Math.min(20, Math.max(0, Math.round(params.currentQuestionIndex))),
      answeredCount,
      correctAnswers: Math.min(20, Math.max(0, Math.round(params.correctAnswers))),
      score: Math.min(3000, Math.max(0, Math.round(params.score))),
      totalTimeMs,
      avgResponseMs,
      answerTimesMs: clampedTimes,
      answersCorrect: clampedCorrects,
      finished: Boolean(params.finished),
      updatedAt: serverTimestamp(),
    });
  } catch (error) {
    handleFirestoreError(
      error,
      OperationType.UPDATE,
      `${DUELS_COLLECTION}/${roomCode}/participants/${slot}`
    );
  }
}

/**
 * Marca a sala de duelo como encerrada quando ambos concluíram as 20 questões.
 */
export async function markDuelFinished(roomCode: string): Promise<void> {
  const duelRef = doc(db, DUELS_COLLECTION, roomCode);
  try {
    await updateDoc(duelRef, { status: 'finished' });
  } catch (error) {
    handleFirestoreError(error, OperationType.UPDATE, `${DUELS_COLLECTION}/${roomCode}`);
  }
}

export function formatResponseMs(ms: number): string {
  const safeMs = Math.max(0, ms);
  const totalSeconds = safeMs / 1000;
  if (totalSeconds < 60) {
    return `${totalSeconds.toFixed(1)}s`;
  }
  const mins = Math.floor(totalSeconds / 60);
  const secs = (totalSeconds % 60).toFixed(1).padStart(4, '0');
  return `${mins}m ${secs}s`;
}
