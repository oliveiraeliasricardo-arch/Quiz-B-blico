import fs from 'fs';
import path from 'path';

export interface Question {
  id: number;
  question: string;
  options: [string, string, string, string];
  correctIndex: 0 | 1 | 2 | 3;
  difficulty: 'facil' | 'medio' | 'dificil';
  book: string;
  testament: 'VT' | 'NT';
  section: 'Pentateuco' | 'Históricos' | 'Poéticos e Sabedoria' | 'Profetas' | 'Evangelhos' | 'Atos e Cartas' | 'Apocalipse';
  reference: string;
  explanation: string;
}

export type RawItem = Omit<Question, 'id'>;

// Helper to shuffle options and set correctIndex
export function createQ(
  question: string,
  correct: string,
  wrong1: string,
  wrong2: string,
  wrong3: string,
  difficulty: 'facil' | 'medio' | 'dificil',
  book: string,
  testament: 'VT' | 'NT',
  section: 'Pentateuco' | 'Históricos' | 'Poéticos e Sabedoria' | 'Profetas' | 'Evangelhos' | 'Atos e Cartas' | 'Apocalipse',
  reference: string,
  explanation: string,
  preferredPos?: 0 | 1 | 2 | 3
): RawItem {
  const optionsRaw = [correct, wrong1, wrong2, wrong3];
  let targetPos: 0 | 1 | 2 | 3;
  if (preferredPos !== undefined) {
    targetPos = preferredPos;
  } else {
    // deterministic based on question length for balanced distribution
    targetPos = (question.length % 4) as 0 | 1 | 2 | 3;
  }

  const finalOpts: [string, string, string, string] = ['', '', '', ''];
  finalOpts[targetPos] = correct;
  let wrongIdx = 1;
  for (let i = 0; i < 4; i++) {
    if (i !== targetPos) {
      finalOpts[i] = optionsRaw[wrongIdx++];
    }
  }

  return {
    question,
    options: finalOpts,
    correctIndex: targetPos,
    difficulty,
    book,
    testament,
    section,
    reference,
    explanation
  };
}
