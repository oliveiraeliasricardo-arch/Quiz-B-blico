import fs from 'fs';
import path from 'path';

interface QuestionRaw {
  q: string;
  opts: [string, string, string, string];
  ans: 0 | 1 | 2 | 3;
  diff: 'facil' | 'medio' | 'dificil';
  book: string;
  testament: 'VT' | 'NT';
  section: string;
  ref: string;
  exp: string;
}

// We will construct verified biblical question sets covering Genesis to Revelation
// grouped by thematic sections, ensuring each question has 4 plausible biblical options,
// an exact correct index, verified book/ref, and an informative explanation.

console.log("Preparing question generator...");
