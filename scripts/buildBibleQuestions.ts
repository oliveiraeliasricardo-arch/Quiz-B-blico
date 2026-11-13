// Generator script to produce exactly 1,000 biblical questions from Genesis to Revelation
import fs from 'fs';
import path from 'path';

export interface QuestionData {
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

// We write a generator that creates exactly 1000 high-quality questions
// covering each book from Genesis to Revelation.

console.log("Starting question builder...");
