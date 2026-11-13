export type Difficulty = 'facil' | 'medio' | 'dificil';
export type Testament = 'VT' | 'NT';

export type BibleSection = 
  | 'Pentateuco'
  | 'Históricos'
  | 'Poéticos e Sabedoria'
  | 'Profetas'
  | 'Evangelhos'
  | 'Atos e Cartas'
  | 'Apocalipse';

export interface Question {
  id: number;
  question: string;
  options: [string, string, string, string];
  correctIndex: 0 | 1 | 2 | 3;
  difficulty: Difficulty;
  book: string;
  testament: Testament;
  section: BibleSection;
  reference: string;
  explanation: string;
}

export interface PlayerScore {
  id: string;
  playerName: string;
  playerAvatar: string;
  score: number;
  correctAnswers: number;
  totalQuestions: number;
  accuracy: number;
  difficulty: Difficulty | 'misto';
  timeSpentSeconds: number;
  date: string; // ISO string
}

export interface QuizState {
  currentQuestionIndex: number;
  selectedOption: number | null;
  isAnswered: boolean;
  score: number;
  streak: number;
  maxStreak: number;
  history: {
    question: Question;
    selectedOption: number;
    isCorrect: boolean;
    timeSpent: number;
  }[];
}

export type DuelSlot = 'host' | 'guest';
export type DuelStatus = 'waiting' | 'playing' | 'finished';

export interface DuelRoom {
  roomCode: string;
  difficulty: Difficulty | 'misto';
  questionIds: number[];
  status: DuelStatus;
  createdAt?: string;
  startedAt?: string;
}

export interface DuelParticipant {
  duelId: string;
  slot: DuelSlot;
  playerName: string;
  playerAvatar: string;
  currentQuestionIndex: number;
  answeredCount: number;
  correctAnswers: number;
  score: number;
  totalTimeMs: number;
  avgResponseMs: number;
  answerTimesMs: number[];
  answersCorrect: boolean[];
  finished: boolean;
}

