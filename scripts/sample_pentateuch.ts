import fs from 'fs';
import path from 'path';

// Definition of RawQuestion
export interface RawQ {
  q: string;
  opts: [string, string, string, string];
  ans: 0 | 1 | 2 | 3;
  diff: 'facil' | 'medio' | 'dificil';
  book: string;
  testament: 'VT' | 'NT';
  section: 'Pentateuco' | 'Históricos' | 'Poéticos e Sabedoria' | 'Profetas' | 'Evangelhos' | 'Atos e Cartas' | 'Apocalipse';
  ref: string;
  exp: string;
}

export const pentateuchQuestions: RawQ[] = [
  // Gênesis
  {
    q: "No princípio, o que Deus criou segundo Gênesis 1:1?",
    opts: ["Os céus e a terra", "Apenas a luz e o sol", "O mar e as estrelas", "Os anjos e o homem"],
    ans: 0,
    diff: "facil",
    book: "Gênesis",
    testament: "VT",
    section: "Pentateuco",
    ref: "Gênesis 1:1",
    exp: "Gênesis 1:1 declara: 'No princípio, criou Deus os céus e a terra'."
  },
  {
    q: "Qual foi a primeira coisa criada no primeiro dia da criação?",
    opts: ["O sol", "A luz", "As plantas", "Os animais"],
    ans: 1,
    diff: "facil",
    book: "Gênesis",
    testament: "VT",
    section: "Pentateuco",
    ref: "Gênesis 1:3",
    exp: "Deus disse: 'Haja luz', e houve luz no primeiro dia."
  },
  {
    q: "Em qual dia da criação o homem e os animais terrestres foram criados?",
    opts: ["Quarto dia", "Quinto dia", "Sexto dia", "Sétimo dia"],
    ans: 2,
    diff: "facil",
    book: "Gênesis",
    testament: "VT",
    section: "Pentateuco",
    ref: "Gênesis 1:26-31",
    exp: "Deus criou os animais da terra e o homem no sexto dia da criação."
  },
  {
    q: "Qual foi o rio que não fazia parte dos rios do jardim do Éden?",
    opts: ["Pisom", "Giom", "Eufrates", "Jordão"],
    ans: 3,
    diff: "medio",
    book: "Gênesis",
    testament: "VT",
    section: "Pentateuco",
    ref: "Gênesis 2:10-14",
    exp: "Os quatro rios do Éden eram Pisom, Giom, Tigre (Hidequel) e Eufrates. O Jordão não é mencionado no Éden."
  },
  {
    q: "Qual era a profissão de Abel, segundo Gênesis?",
    opts: ["Pastor de ovelhas", "Lavrador da terra", "Ferreiro", "Pescador"],
    ans: 0,
    diff: "facil",
    book: "Gênesis",
    testament: "VT",
    section: "Pentateuco",
    ref: "Gênesis 4:2",
    exp: "Abel foi pastor de ovelhas, e Caim foi lavrador da terra."
  },
  {
    q: "Quem foi o homem que andou com Deus e não viu a morte, pois Deus o tomou para Si?",
    opts: ["Matusalém", "Enoque", "Noé", "Lameque"],
    ans: 1,
    diff: "facil",
    book: "Gênesis",
    testament: "VT",
    section: "Pentateuco",
    ref: "Gênesis 5:24",
    exp: "Enoque andou com Deus e já não foi encontrado, porque Deus o levou."
  },
  {
    q: "Quem é registrada como a pessoa mais velha na Bíblia, vivendo 969 anos?",
    opts: ["Adão", "Noé", "Matusalém", "Sem"],
    ans: 2,
    diff: "facil",
    book: "Gênesis",
    testament: "VT",
    section: "Pentateuco",
    ref: "Gênesis 5:27",
    exp: "Matusalém viveu 969 anos antes de falecer."
  },
  {
    q: "Quais eram os nomes dos três filhos de Noé que entraram na arca?",
    opts: ["Sem, Cam e Jafé", "Caim, Abel e Sete", "Abraão, Naor e Harã", "Esaú, Jacó e José"],
    ans: 0,
    diff: "facil",
    book: "Gênesis",
    testament: "VT",
    section: "Pentateuco",
    ref: "Gênesis 6:10",
    exp: "Noé gerou três filhos: Sem, Cam e Jafé."
  },
  {
    q: "Qual pássaro Noé soltou primeiro da arca para ver se as águas haviam diminuído?",
    opts: ["Uma pomba", "Um corvo", "Uma andorinha", "Uma águia"],
    ans: 1,
    diff: "medio",
    book: "Gênesis",
    testament: "VT",
    section: "Pentateuco",
    ref: "Gênesis 8:7",
    exp: "Noé soltou primeiro um corvo, que ficou indo e voltando até que as águas secaram."
  },
  {
    q: "Qual objeto a pomba trouxe no bico ao retornar para a arca pela segunda vez?",
    opts: ["Uma folha nova de oliveira", "Um galho de cedro", "Uma semente de trigo", "Uma flor silvestre"],
    ans: 0,
    diff: "facil",
    book: "Gênesis",
    testament: "VT",
    section: "Pentateuco",
    ref: "Gênesis 8:11",
    exp: "A pomba voltou à tarde trazendo uma folha de oliveira recém-colhida no bico."
  },
  {
    q: "Qual foi o sinal da aliança que Deus colocou nas nuvens para nunca mais destruir a terra por dilúvio?",
    opts: ["Uma coluna de fogo", "O arco-íris", "Uma nuvem dourada", "Uma estrela cadente"],
    ans: 1,
    diff: "facil",
    book: "Gênesis",
    testament: "VT",
    section: "Pentateuco",
    ref: "Gênesis 9:13",
    exp: "Deus disse: 'Porei nas nuvens o meu arco; ele será um sinal de aliança entre mim e a terra'."
  },
  {
    q: "Em qual cidade os homens tentaram construir uma torre cujo cume tocasse o céu?",
    opts: ["Ur dos Caldeus", "Sodoma", "Babel", "Nínive"],
    ans: 2,
    diff: "facil",
    book: "Gênesis",
    testament: "VT",
    section: "Pentateuco",
    ref: "Gênesis 11:4-9",
    exp: "A torre foi edificada em Babel, onde o Senhor confundiu a linguagem de toda a terra."
  },
  {
    q: "De qual terra Deus chamou Abrão quando lhe disse: 'Sai da tua terra e da tua parentela'?",
    opts: ["Ur dos Caldeus", "Cairo", "Damasco", "Babilônia"],
    ans: 0,
    diff: "facil",
    book: "Gênesis",
    testament: "VT",
    section: "Pentateuco",
    ref: "Gênesis 11:31; 12:1",
    exp: "Abrão partiu de Ur dos Caldeus para Canaã, habitando temporariamente em Harã."
  },
  {
    q: "Quem era o sobrinho de Abraão que viajou com ele e escolheu as campinas de Sodoma?",
    opts: ["Ló", "Labão", "Eliezer", "Ismael"],
    ans: 0,
    diff: "facil",
    book: "Gênesis",
    testament: "VT",
    section: "Pentateuco",
    ref: "Gênesis 13:11",
    exp: "Ló escolheu a planície do Jordão e armou as suas tendas até Sodoma."
  },
  {
    q: "Quem foi o rei de Salém e sacerdote do Deus Altíssimo a quem Abraão deu o dízimo?",
    opts: ["Abimeleque", "Melquisedeque", "Jeter", "Potífera"],
    ans: 1,
    diff: "medio",
    book: "Gênesis",
    testament: "VT",
    section: "Pentateuco",
    ref: "Gênesis 14:18-20",
    exp: "Melquisedeque, rei de Salém e sacerdote do Deus Altíssimo, abençoou Abraão."
  },
  {
    q: "Qual era o nome da serva egípcia de Sara que deu à luz Ismael?",
    opts: ["Quetura", "Hagar", "Zilpa", "Bila"],
    ans: 1,
    diff: "facil",
    book: "Gênesis",
    testament: "VT",
    section: "Pentateuco",
    ref: "Gênesis 16:1-3",
    exp: "Hagar era serva egípcia de Sara e mãe de Ismael."
  },
  {
    q: "Quantos anos tinha Abraão quando seu filho Isaque nasceu?",
    opts: ["75 anos", "86 anos", "99 anos", "100 anos"],
    ans: 3,
    diff: "medio",
    book: "Gênesis",
    testament: "VT",
    section: "Pentateuco",
    ref: "Gênesis 21:5",
    exp: "Abraão tinha cem anos de idade quando lhe nasceu Isaque, seu filho."
  },
  {
    q: "Em qual monte Abraão levou Isaque para ser sacrificado antes de Deus providenciar o carneiro?",
    opts: ["Monte Sinai", "Monte Moriá", "Monte Carmelo", "Monte Nebo"],
    ans: 1,
    diff: "medio",
    book: "Gênesis",
    testament: "VT",
    section: "Pentateuco",
    ref: "Gênesis 22:2",
    exp: "Deus orientou Abraão a ir à terra de Moriá e oferecer Isaque como holocausto."
  },
  {
    q: "Quem foi a esposa escolhida para Isaque junto ao poço em Padã-Arã?",
    opts: ["Raquel", "Lia", "Rebeca", "Zípora"],
    ans: 2,
    diff: "facil",
    book: "Gênesis",
    testament: "VT",
    section: "Pentateuco",
    ref: "Gênesis 24:15-67",
    exp: "Rebeca, filha de Betuel, foi trazida pelo servo de Abraão para ser esposa de Isaque."
  },
  {
    q: "Por qual alimento Esaú vendeu o seu direito de primogenitura para Jacó?",
    opts: ["Um prato de lentilhas vermelhas", "Três pães de cevada", "Um cordeiro assado", "Uma taça de vinho e figos"],
    ans: 0,
    diff: "facil",
    book: "Gênesis",
    testament: "VT",
    section: "Pentateuco",
    ref: "Gênesis 25:34",
    exp: "Jacó deu a Esaú pão e o guisado de lentilhas, e este desprezou seu direito de primogenitura."
  },
  {
    q: "Em que lugar Jacó teve a visão de uma escada que tocava o céu e anjos subindo e descendo?",
    opts: ["Betel", "Hebrom", "Siquém", "Peniel"],
    ans: 0,
    diff: "facil",
    book: "Gênesis",
    testament: "VT",
    section: "Pentateuco",
    ref: "Gênesis 28:19",
    exp: "Jacó chamou aquele lugar Betel (Casa de Deus); anteriormente a cidade se chamava Luz."
  },
  {
    q: "Quantos anos no total Jacó trabalhou para Labão a fim de se casar com Raquel?",
    opts: ["7 anos", "14 anos", "20 anos", "21 anos"],
    ans: 1,
    diff: "medio",
    book: "Gênesis",
    testament: "VT",
    section: "Pentateuco",
    ref: "Gênesis 29:18-30",
    exp: "Jacó serviu 7 anos por Raquel, recebeu Lia com engano, e serviu mais 7 anos por Raquel, totalizando 14 anos pelas esposas."
  },
  {
    q: "Em que lugar Jacó lutou com um anjo até o romper do dia e teve seu nome mudado para Israel?",
    opts: ["Maanaim", "Peniel", "Betel", "Berseba"],
    ans: 1,
    diff: "medio",
    book: "Gênesis",
    testament: "VT",
    section: "Pentateuco",
    ref: "Gênesis 32:30",
    exp: "Jacó chamou o lugar de Peniel, dizendo: 'Vi a Deus face a face, e a minha vida foi salva'."
  },
  {
    q: "Qual era o filho mais jovem de Jacó, nascido na viagem perto de Belém?",
    opts: ["José", "Benjamim", "Dã", "Gade"],
    ans: 1,
    diff: "facil",
    book: "Gênesis",
    testament: "VT",
    section: "Pentateuco",
    ref: "Gênesis 35:18",
    exp: "Raquel morreu ao dar à luz Benjamim, o décimo segundo e mais jovem filho de Jacó."
  },
  {
    q: "Qual presente especial Jacó deu a José que despertou o ciúme de seus irmãos?",
    opts: ["Um anel de ouro", "Uma túnica talar de mangas compridas e colorida", "Um cajado de pastor de prata", "Uma sandália real"],
    ans: 1,
    diff: "facil",
    book: "Gênesis",
    testament: "VT",
    section: "Pentateuco",
    ref: "Gênesis 37:3",
    exp: "Israel amava José mais do que a todos os seus filhos e fez-lhe uma túnica de várias cores."
  },
  {
    q: "Por quantas moedas de prata os irmãos de José o venderam aos mercadores ismaelitas?",
    opts: ["10 moedas", "20 moedas", "30 moedas", "50 moedas"],
    ans: 1,
    diff: "medio",
    book: "Gênesis",
    testament: "VT",
    section: "Pentateuco",
    ref: "Gênesis 37:28",
    exp: "Os irmãos de José o venderam por vinte siclos de prata aos ismaelitas."
  },
  {
    q: "Qual oficial de Faraó comprou José como escravo no Egito?",
    opts: ["Potifar", "Ficol", "Asenate", "Janes"],
    ans: 0,
    diff: "facil",
    book: "Gênesis",
    testament: "VT",
    section: "Pentateuco",
    ref: "Gênesis 39:1",
    exp: "Potifar, oficial de Faraó e capitão da guarda, comprou José dos ismaelitas."
  },
  {
    q: "Na prisão, quais dois funcionários de Faraó tiveram sonhos interpretados por José?",
    opts: ["O padeiro-chefe e o copeiro-chefe", "O tesoureiro e o escriba", "O general e o mago", "O cozinheiro e o médico"],
    ans: 0,
    diff: "facil",
    book: "Gênesis",
    testament: "VT",
    section: "Pentateuco",
    ref: "Gênesis 40:1-5",
    exp: "O copeiro-chefe e o padeiro-chefe do rei do Egito tiveram sonhos interpretados por José."
  },
  {
    q: "Quantos anos de fartura e quantos anos de fome foram profetizados nos sonhos de Faraó?",
    opts: ["3 anos de fartura e 3 de fome", "7 anos de fartura e 7 de fome", "10 anos de fartura e 10 de fome", "12 anos de fartura e 12 de fome"],
    ans: 1,
    diff: "facil",
    book: "Gênesis",
    testament: "VT",
    section: "Pentateuco",
    ref: "Gênesis 41:29-30",
    exp: "As sete vacas gordas e espigas cheias representavam 7 anos de grande fartura seguidos de 7 anos de fome."
  },
  {
    q: "Qual era o nome egípcio que Faraó deu a José ao nomeá-lo governador do Egito?",
    opts: ["Zafenate-Panéia", "Potífera", "Tutancâmon", "Ramsés"],
    ans: 0,
    diff: "dificil",
    book: "Gênesis",
    testament: "VT",
    section: "Pentateuco",
    ref: "Gênesis 41:45",
    exp: "Faraó chamou a José pelo nome de Zafenate-Panéia e deu-lhe por mulher a Asenate."
  },
  {
    q: "Quais eram os dois filhos de José que nasceram no Egito e foram abençoados por Jacó?",
    opts: ["Manassés e Efraim", "Gade e Aser", "Dan e Naftali", "Rúben e Simeão"],
    ans: 0,
    diff: "facil",
    book: "Gênesis",
    testament: "VT",
    section: "Pentateuco",
    ref: "Gênesis 41:51-52; 48:1",
    exp: "José chamou o primogênito de Manassés e o segundo de Efraim."
  },
  {
    q: "Em qual região do Egito a família de Jacó foi autorizada a habitar?",
    opts: ["Tebas", "Gósen", "Alexandria", "Mênfis"],
    ans: 1,
    diff: "medio",
    book: "Gênesis",
    testament: "VT",
    section: "Pentateuco",
    ref: "Gênesis 47:6",
    exp: "Faraó disse a José para fazer seus pais e irmãos habitarem no melhor da terra, na terra de Gósen."
  }
];

console.log("Loaded preliminary questions sample:", pentateuchQuestions.length);
