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

export interface RawQItem {
  q: string;
  c: string; // correct answer
  w: [string, string, string]; // 3 wrong answers
  diff: 'facil' | 'medio' | 'dificil';
  book: string;
  testament: 'VT' | 'NT';
  section: 'Pentateuco' | 'Históricos' | 'Poéticos e Sabedoria' | 'Profetas' | 'Evangelhos' | 'Atos e Cartas' | 'Apocalipse';
  ref: string;
  exp: string;
}

export function makeQ(
  id: number,
  raw: RawQItem
): Question {
  // Rotate correct answer position evenly across 0, 1, 2, 3 based on id
  const targetPos = (id % 4) as 0 | 1 | 2 | 3;
  const opts: [string, string, string, string] = ['', '', '', ''];
  opts[targetPos] = raw.c;
  
  let wIndex = 0;
  for (let i = 0; i < 4; i++) {
    if (i !== targetPos) {
      opts[i] = raw.w[wIndex++];
    }
  }

  return {
    id,
    question: raw.q,
    options: opts,
    correctIndex: targetPos,
    difficulty: raw.diff,
    book: raw.book,
    testament: raw.testament,
    section: raw.section,
    reference: raw.ref,
    explanation: raw.exp
  };
}
