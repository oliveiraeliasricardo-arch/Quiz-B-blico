import rawQuestions from './questionsData.json';
import { Question, Difficulty, BibleSection } from '../types/quiz';

export const allQuestions: Question[] = rawQuestions as Question[];
export const totalQuestionsCount = allQuestions.length;

/**
 * Embaralha um array usando Fisher-Yates
 */
function shuffleArray<T>(array: T[]): T[] {
  const arr = [...array];
  for (let i = arr.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [arr[i], arr[j]] = [arr[j], arr[i]];
  }
  return arr;
}

/**
 * Seleciona exatamente `count` (padrão 20) questões aleatórias
 * filtradas pelo nível de dificuldade escolhido ('facil', 'medio', 'dificil' ou 'misto').
 */
export function getQuestionsForRound(
  difficulty: Difficulty | 'misto',
  count: number = 20
): Question[] {
  let pool: Question[];

  if (difficulty === 'misto') {
    pool = [...allQuestions];
  } else {
    pool = allQuestions.filter(q => q.difficulty === difficulty);
  }

  // Se o pool for menor que o count (improvável já que cada dificuldade tem > 300), usa todas
  if (pool.length <= count) {
    return shuffleArray(pool);
  }

  const shuffled = shuffleArray(pool);
  return shuffled.slice(0, count);
}

/**
 * Retorna estatísticas gerais do banco de dados bíblico
 */
export function getDatabaseStats() {
  const facilCount = allQuestions.filter(q => q.difficulty === 'facil').length;
  const medioCount = allQuestions.filter(q => q.difficulty === 'medio').length;
  const dificilCount = allQuestions.filter(q => q.difficulty === 'dificil').length;
  const vtCount = allQuestions.filter(q => q.testament === 'VT').length;
  const ntCount = allQuestions.filter(q => q.testament === 'NT').length;

  return {
    total: allQuestions.length,
    facil: facilCount,
    medio: medioCount,
    dificil: dificilCount,
    vt: vtCount,
    nt: ntCount,
  };
}

const questionsByIdMap = new Map<number, Question>(
  allQuestions.map((q) => [q.id, q])
);

/**
 * Reconstrói exatamente as mesmas questões na ordem especificada pelos IDs (usado no Modo Duelo).
 */
export function getQuestionsByIds(ids: number[]): Question[] {
  const result: Question[] = [];
  for (const id of ids) {
    const found = questionsByIdMap.get(id);
    if (found) {
      result.push(found);
    }
  }
  return result;
}

