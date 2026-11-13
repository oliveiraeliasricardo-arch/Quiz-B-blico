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

interface RawQ {
  q: string;
  c: string;
  w: [string, string, string];
  diff: 'facil' | 'medio' | 'dificil';
  book: string;
  testament: 'VT' | 'NT';
  section: 'Pentateuco' | 'Históricos' | 'Poéticos e Sabedoria' | 'Profetas' | 'Evangelhos' | 'Atos e Cartas' | 'Apocalipse';
  ref: string;
  exp: string;
}

const rawList: RawQ[] = [];

function q(
  q: string,
  c: string,
  w1: string,
  w2: string,
  w3: string,
  diff: 'facil' | 'medio' | 'dificil',
  book: string,
  testament: 'VT' | 'NT',
  section: 'Pentateuco' | 'Históricos' | 'Poéticos e Sabedoria' | 'Profetas' | 'Evangelhos' | 'Atos e Cartas' | 'Apocalipse',
  ref: string,
  exp: string
) {
  rawList.push({
    q,
    c,
    w: [w1, w2, w3],
    diff,
    book,
    testament,
    section,
    ref,
    exp
  });
}

console.log("Setting up 1000 Bible Questions Builder...");
