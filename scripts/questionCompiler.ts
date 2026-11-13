import fs from 'fs';
import path from 'path';

// Master Question interface
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

export interface QuestionDef {
  q: string;
  c: string; // correct
  w: [string, string, string]; // 3 plausible distractors
  d: 'facil' | 'medio' | 'dificil';
  b: string;
  t: 'VT' | 'NT';
  s: 'Pentateuco' | 'Históricos' | 'Poéticos e Sabedoria' | 'Profetas' | 'Evangelhos' | 'Atos e Cartas' | 'Apocalipse';
  r: string;
  e: string;
}

export function compileQuestions(defs: QuestionDef[]): Question[] {
  return defs.map((def, idx) => {
    const id = idx + 1;
    // Perfectly rotate answer placement across 0, 1, 2, 3
    const correctIndex = (idx % 4) as 0 | 1 | 2 | 3;
    const options: [string, string, string, string] = ['', '', '', ''];
    options[correctIndex] = def.c;

    let wIdx = 0;
    for (let i = 0; i < 4; i++) {
      if (i !== correctIndex) {
        options[i] = def.w[wIdx++];
      }
    }

    return {
      id,
      question: def.q,
      options,
      correctIndex,
      difficulty: def.d,
      book: def.b,
      testament: def.t,
      section: def.s,
      reference: def.r,
      explanation: def.e
    };
  });
}
