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

export interface RawItem {
  q: string;
  c: string; // correct
  w1: string; // wrong
  w2: string;
  w3: string;
  diff: 'facil' | 'medio' | 'dificil';
  book: string;
  testament: 'VT' | 'NT';
  section: 'Pentateuco' | 'Históricos' | 'Poéticos e Sabedoria' | 'Profetas' | 'Evangelhos' | 'Atos e Cartas' | 'Apocalipse';
  ref: string;
  exp: string;
}

// We will export a function to compile raw items into final Questions with deterministic rotating answer index
export function buildQuestions(items: RawItem[]): Question[] {
  return items.map((item, index) => {
    const id = index + 1;
    const correctIndex = (index % 4) as 0 | 1 | 2 | 3;
    const options: [string, string, string, string] = ['', '', '', ''];
    options[correctIndex] = item.c;

    const wrongs = [item.w1, item.w2, item.w3];
    let wIdx = 0;
    for (let i = 0; i < 4; i++) {
      if (i !== correctIndex) {
        options[i] = wrongs[wIdx++];
      }
    }

    return {
      id,
      question: item.q,
      options,
      correctIndex,
      difficulty: item.diff,
      book: item.book,
      testament: item.testament,
      section: item.section,
      reference: item.ref,
      explanation: item.exp
    };
  });
}
