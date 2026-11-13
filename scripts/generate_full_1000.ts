import fs from 'fs';
import path from 'path';

interface QuestionItem {
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

type RawDef = {
  q: string;
  c: string; // correct
  w: [string, string, string]; // 3 wrong
  d: 'facil' | 'medio' | 'dificil';
  b: string;
  t: 'VT' | 'NT';
  s: 'Pentateuco' | 'Históricos' | 'Poéticos e Sabedoria' | 'Profetas' | 'Evangelhos' | 'Atos e Cartas' | 'Apocalipse';
  r: string;
  e: string;
};

// We will write the comprehensive generator with arrays of raw definitions
console.log("Compiling complete 1000 question generator...");
