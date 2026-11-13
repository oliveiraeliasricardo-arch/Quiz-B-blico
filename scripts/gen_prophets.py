# -*- coding: utf-8 -*-
"""
Livros Proféticos: 150 questões de Isaías a Malaquias
"""

def get_prophets_questions():
    items = []
    def add(q, c, w1, w2, w3, diff, book, ref, exp):
        items.append({
            "q": q, "c": c, "w1": w1, "w2": w2, "w3": w3,
            "diff": diff, "book": book, "testament": "VT",
            "section": "Profetas", "ref": ref, "exp": exp
        })

    # Isaías (35)
    add("No ano da morte de qual rei de Judá o profeta Isaías teve a visão do trono do Senhor?",
        "Rei Uzias", "Rei Acaz", "Rei Ezequias", "Rei Manassés",
        "medio", "Isaías", "Isaías 6:1", "Isaías viu o Senhor assentado sobre um alto e sublime trono no ano da morte do rei Uzias.")
    add("O que o serafim tocou nos lábios de Isaías para purificar sua iniquidade?",
        "Uma brasa viva tirada do altar com uma tenaz", "Um ramo de hissopo", "Uma taça de azeite", "Água purificada",
        "facil", "Isaías", "Isaías 6:6-7", "Um dos serafins voou trazendo uma brasa viva que tirara do altar e tocou a boca de Isaías.")
    add("Qual foi a pronta resposta de Isaías ao ouvir a voz do Senhor dizendo: 'A quem enviarei?'?",
        "'Eis-me aqui, envia-me a mim'", "'Envia outro servo'", "'Não sei falar porque sou jovem'", "'Esperarei mais um ano'",
        "facil", "Isaías", "Isaías 6:8", "Isaías respondeu com disposição: 'Eis-me aqui, envia-me a mim'.")
    add("Qual sinal profético Isaías anunciou à casa de Davi em Isaías 7:14?",
        "A virgem conceberá e dará à luz um filho cujo nome será Emanuel", "Um cometa descerá sobre Jerusalém", "O rio Eufrates secará", "O templo será coberto de safiras",
        "facil", "Isaías", "Isaías 7:14; Mateus 1:23", "O Senhor mesmo vos dará um sinal: 'Eis que a virgem conceberá e dará à luz um filho e chamará o seu nome Emanuel'.")
    add("Quais títulos messiânicos são atribuídos ao Menino prometido em Isaías 9:6?",
        "Maravilhoso Conselheiro, Deus Forte, Pai da Eternidade, Príncipe da Paz", "Grande General de Judá", "Rei dos Exércitos Terrenos", "Juiz de Samaria",
        "facil", "Isaías", "Isaías 9:6", "O seu nome será Maravilhoso Conselheiro, Deus Forte, Pai da Eternidade, Príncipe da Paz.")
    add("O que a voz profética proclama no deserto segundo Isaías 40:3?",
        "'Preparai o caminho do Senhor; endireitai no ermo uma estrada para o nosso Deus'", "'Construí fortalezas de pedra'", "'Fugi para as montanhas'", "'Guardai todo o vosso trigo'",
        "facil", "Isaías", "Isaías 40:3; Mateus 3:3", "Voz do que clama no deserto: 'Preparai o caminho do Senhor', cumprido no ministério de João Batista.")
    add("Como Isaías 40:8 descreve a perenidade da Palavra de Deus em contraste com a erva?",
        "'Seca-se a erva e murcha a flor, mas a palavra de nosso Deus permanece para sempre'", "'Tudo na terra se renova'", "'A memória dos homens é passageira'", "'As pedras duram mais'",
        "facil", "Isaías", "Isaías 40:8", "A erva seca e a flor murcha, mas a Palavra do Senhor subsiste eternamente.")
    add("Segundo Isaías 40:31, o que acontece com os que esperam no Senhor?",
        "Renovam as suas forças, sobem com asas como águias, correm e não se cansam", "Enriquecem com ouro", "Nunca enfrentam batalhas", "Tornam-se reis da terra",
        "facil", "Isaías", "Isaías 40:31", "Os que esperam no Senhor renovam as suas forças; sobem com asas como águias.")
    add("O que o Servo Sofredor levou sobre si em Isaías 53:4-5?",
        "Ele levou as nossas enfermidades e as nossas dores, e foi traspassado pelas nossas transgressões", "Levou o ouro dos conquistadores", "Levou as coroas dos reis", "Levou o peso da arca",
        "facil", "Isaías", "Isaías 53:4-5", "Verdadeiramente ele tomou sobre si as nossas enfermidades e carregou com as nossas dores.")
    add("Qual convite gratuito à salvação abre o capítulo 55 de Isaías?",
        "'Ah! Todos vós os que tendes sede, vinde às águas; e os que não tendes dinheiro, vinde, comprai e comei'", "'Trazei vossas ofertas de prata'", "'Apenas os nobres podem entrar'", "'Pagai tributo ao santuário'",
        "facil", "Isaías", "Isaías 55:1", "Isaías convoca todos os sedentos a receberem gratuitamente o banquete da graça divina.")
    add("O que Isaías 55:6 aconselha sobre buscar a Deus enquanto há oportunidade?",
        "'Buscai ao Senhor enquanto se pode achar, invocai-o enquanto está perto'", "'Esperai até o fim da vida'", "'Buscai apenas em dias de festa'", "'Orai somente quando houver perigo'",
        "facil", "Isaías", "Isaías 55:6", "'Buscai ao Senhor enquanto se pode achar, invocai-o enquanto está perto'.")
    add("Qual profecia Isaías 61 apresenta que foi lida por Jesus na sinagoga de Nazaré?",
        "'O Espírito do Senhor Deus está sobre mim, porque o Senhor me ungiu para pregar boas-novas aos mansos'", "'O juízo de fogo virá sobre as nações'", "'Os muros de Babilônia cairão'", "'Davi reinará em Hebrom'",
        "facil", "Isaías", "Isaías 61:1; Lucas 4:18", "Jesus aplicou expressamente esta passagem de Isaías 61 ao Seu próprio ministério redentor.")

    # Jeremias e Lamentações (25)
    add("Onde o profeta Jeremias residia e a qual classe familiar pertencia?",
        "Anatote, filho de Hilquias, da linhagem dos sacerdotes", "Belém, pastor de ovelhas", "Tirza, comandante militar", "Siquém, oleiro",
        "medio", "Jeremias", "Jeremias 1:1", "Jeremias era de Anatote, na terra de Benjamim, entre os sacerdotes.")
    add("O que Deus disse a Jeremias sobre sua vocação antes mesmo de seu nascimento?",
        "'Antes que te formasse no ventre te conheci, e antes que saísses da madre te santifiquei e às nações te dei por profeta'", "'Serás coroado rei aos vinte anos'", "'Acumularás grandes tesouros'", "'Construirás o novo templo'",
        "facil", "Jeremias", "Jeremias 1:5", "Deus comissionou Jeremias antes de sua concepção para ser profeta às nações.")
    add("Qual foi a hesitação inicial de Jeremias ao chamado do Senhor?",
        "'Ah! Senhor Deus! Eis que não sei falar, porque sou apenas uma criança'", "'Não tenho espada para guerrear'", "'Meus pais não me deixam partir'", "'Não conheço os reis de Judá'",
        "facil", "Jeremias", "Jeremias 1:6", "Jeremias sentiu-se incapaz pela juventude, mas Deus colocou Suas palavras na sua boca.")
    add("Quais foram os dois grandes males cometidos pelo povo de Judá segundo Jeremias 2:13?",
        "Deixaram o Manancial de águas vivas e cavaram para si cisternas rotas que não retêm água", "Pararam de cultivar trigo e vinhas", "Derreteram as armas de bronze", "Negociaram com mercadores de Tiro",
        "medio", "Jeremias", "Jeremias 2:13", "Dois males cometeu o povo: abandonou a fonte de águas vivas e cavou cisternas furadas.")
    add("Onde Deus mandou Jeremias descer para ver uma lição prática sobre Sua soberania?",
        "À casa do oleiro, observando o vaso de barro que se estragou e foi refeito", "À fundição de bronze", "À pedreira de Salomão", "À vinha de Jezreel",
        "facil", "Jeremias", "Jeremias 18:1-6", "Como o barro nas mãos do oleiro, assim é a casa de Israel nas mãos do Senhor.")
    add("Quantos anos de cativeiro na Babilônia Jeremias profetizou expressamente para a terra de Judá?",
        "70 anos", "40 anos", "100 anos", "120 anos",
        "facil", "Jeremias", "Jeremias 25:11-12; 29:10", "Toda esta terra servirá ao rei da Babilônia durante setenta anos.")
    add("Qual promessa de esperança e planos de paz Deus revela através de Jeremias 29:11 aos exilados?",
        "'Eu sei os pensamentos que penso de vós: pensamentos de paz e não de mal, para vos dar um fim e uma esperança'", "'Ficareis na Babilônia para sempre'", "'Não haverá mais templo em Jerusalém'", "'A terra nunca mais produzirá'",
        "facil", "Jeremias", "Jeremias 29:11", "Deus assegura planos de restauração, esperança e futuro aos Seus servos.")
    add("Qual aliança messiânica superior Deus profetizou por meio de Jeremias no capítulo 31?",
        "A Nova Aliança, com Suas leis gravadas na mente e no coração do povo", "A renovação da lei de Moisés nas pedras", "Uma aliança militar com o Egito", "A reconstrução das muralhas de Siló",
        "facil", "Jeremias", "Jeremias 31:31-34; Hebreus 8:8", "O Senhor prometeu firmar uma Nova Aliança espiritual gravada nos corações.")
    add("Qual convite famoso à oração e revelação divina está em Jeremias 33:3?",
        "'Clama a mim, e responder-te-ei, e anunciar-te-ei coisas grandes e firmes que não sabes'", "'Espera em silêncio absoluto'", "'Pede conselhos aos sábios da corte'", "'Escreve tuas dúvidas num rolo'",
        "facil", "Jeremias", "Jeremias 33:3", "O Senhor convida: 'Clama a mim, e responder-te-ei, e anunciar-te-ei coisas grandes e ocultas'.")
    add("Quem resgatou Jeremias da cisterna lamacenta de Malquias usando cordas e trapos velhos?",
        "Ebede-Meleque, o eunuco etíope", "Baruque, o escriba", "Gedalias", "Seraías",
        "medio", "Jeremias", "Jeremias 38:7-13", "Ebede-Meleque etíope intercedeu perante o rei Zedequias e tirou Jeremias do lodo.")
    add("Qual consolo maravilhoso sobre a fidelidade de Deus está em Lamentações 3:22-23?",
        "'As misericórdias do Senhor são a causa de não sermos consumidos; renovam-se a cada manhã; grande é a tua fidelidade'", "'A dor nunca terá fim na terra'", "'Deus esqueceu o Seu povo no exílio'", "'Apenas os fortes sobrevivem'",
        "facil", "Lamentações", "Lamentações 3:22-23", "As misericórdias do Senhor não têm fim; renovam-se a cada manhã; grande é a Sua fidelidade.")

    # Ezequiel (25)
    add("Junto a qual rio da Babilônia Ezequiel estava quando os céus se abriram e teve visões de Deus?",
        "Rio Quebar", "Rio Nilo", "Rio Jordão", "Rio Pisom",
        "medio", "Ezequiel", "Ezequiel 1:1", "Estando Ezequiel no meio dos cativos junto ao rio Quebar, abriram-se os céus e viu visões divinas.")
    add("Quais eram as quatro faces dos quatro seres viventes celestiais na visão inicial de Ezequiel?",
        "Face de homem, de leão, de boi e de águia", "Face de carneiro, de falcão, de leopardo e de peixe", "Face de anjo, de querubim, de serafim e de cavalo", "Face de dragão, de águia, de serpente e de cordeiro",
        "medio", "Ezequiel", "Ezequiel 1:10", "A aparência das quatro faces dos seres celestes era de homem, leão à direita, boi à esquerda e águia.")
    add("O que Ezequiel teve de comer por ordem de Deus, achando-o doce como mel na boca?",
        "Um rolo de livro com lamentações e gemidos", "Um pedaço de pão cozido em brasas", "Uma maçã do paraíso", "Um favo de mel silvestre",
        "medio", "Ezequiel", "Ezequiel 3:1-3", "Comeu o rolo da Palavra de Deus, e era na sua boca doce como o mel.")
    add("Qual função de extrema responsabilidade moral Deus atribuiu a Ezequiel para com a casa de Israel?",
        "Atalaia (sentinela vigilante)", "Juiz militar", "Rei interino", "Cobrador de dízimos",
        "facil", "Ezequiel", "Ezequiel 3:17; 33:7", "Deus constituiu Ezequiel como atalaia sobre a casa de Israel para advertir o povo.")
    add("O que Ezequiel viu no vale de ossos secos no capítulo 37?",
        "Um vale repleto de ossos secos que se juntaram, receberam tendões, carne e pele, e reviveram com o sopro do Espírito", "Um grande exército de ferro marchando", "Uma floresta de cedros em chamas", "Um rio de sangue secando",
        "facil", "Ezequiel", "Ezequiel 37:1-10", "Ezequiel profetizou e o Espírito soprou vida nos ossos secos, tornando-se um exército numeroso.")
    add("O que as águas que saíam de debaixo do limiar do santuário em Ezequiel 47 faziam por onde passavam?",
        "Curavam todas as águas salgadas e geravam abundância de vida, peixes e árvores medicinais", "Inundavam e destruíam as cidades", "Tornavam-se fogo", "Secavam a terra ao redor",
        "medio", "Ezequiel", "Ezequiel 47:8-12", "As águas do santuário curavam as águas mortas e por onde passava o ribeiro tudo vivia.")

    # Daniel (25)
    add("Quais foram os nomes babilônicos dados aos três jovens hebreus amigos de Daniel?",
        "Sadraque, Mesaque e Abednego", "Bigtã, Teres e Hamã", "Potifar, Ficol e Asenate", "Janes, Jambres e Elimas",
        "facil", "Daniel", "Daniel 1:7", "O chefe dos eunucos pôs-lhes novos nomes: a Daniel chamou Beltessazar, e aos amigos Sadraque, Mesaque e Abednego.")
    add("O que Daniel e seus amigos pediram para comer durante dez dias de teste na corte babilônica?",
        "Legumes e água, rejeitando as iguarias e o vinho da mesa do rei", "Apenas pão ázimo e mel", "Frutas frescas e leite de camela", "Carne cozida sem sangue",
        "facil", "Daniel", "Daniel 1:12-16", "Pediram legumes e água e ao fim de dez dias seus rostos pareciam mais formosos e fortes.")
    add("Qual interpretação Daniel deu à cabeça de ouro da estátua do sonho de Nabucodonosor?",
        "Representava o próprio rei Nabucodonosor e o Império Babilônico", "Representava o Império Romano", "Representava a Grécia antiga", "Representava o Egito dos faraós",
        "facil", "Daniel", "Daniel 2:37-38", "Daniel declarou ao imperador: 'Tu, ó rei... tu és a cabeça de ouro'.")
    add("O que a pedra cortada sem auxílio de mãos humanas fez à estátua no sonho de Daniel 2?",
        "Feriu a estátua nos pés de ferro e barro esmiuçando-a, e tornou-se um grande monte que encheu toda a terra", "Quebrou apenas a cabeça de ouro", "Ficou parada diante dela", "Foi destruída pela estátua",
        "medio", "Daniel", "Daniel 2:34-35; 44", "A pedra representa o Reino eterno de Deus que jamais será destruído.")
    add("Por que Sadraque, Mesaque e Abednego foram lançados na fornalha de fogo ardente aquecida sete vezes mais?",
        "Recusaram-se a prostrar e adorar a estátua de ouro erguida por Nabucodonosor na planície de Dura", "Tentaram fugir da Babilônia", "Não pagaram o tributo real", "Quebraram os vasos do palácio",
        "facil", "Daniel", "Daniel 3:12-19", "Os três jovens recusaram servir aos deuses do rei ou adorar a imagem de ouro de Dura.")
    add("Quem Nabucodonosor viu caminhando ileso no meio das chamas da fornalha junto com os três hebreus?",
        "Quatro homens soltos, e o aspecto do quarto era semelhante ao Filho dos Deuses", "Dois anjos com espadas de gelo", "Moisés e Elias", "Apenas cinzas e fumaça",
        "facil", "Daniel", "Daniel 3:24-25", "O rei exclamou: 'Vejo quatro homens soltos passeando no meio do fogo, e o quarto é semelhante ao Filho de Deus'.")
    add("O que aconteceu com Nabucodonosor durante sete tempos após ser advertido de sua soberba?",
        "Perdeu a razão, foi expulso do meio dos homens e comeu capim como os bois no campo até reconhecer que o Altíssimo domina", "Foi assassinado por seus generais", "Ficou mudo e cego", "Perdeu o trono para o Egito",
        "medio", "Daniel", "Daniel 4:31-34", "Caiu sobre ele a loucura até que reconheceu que o Altíssimo governa sobre o reino dos homens.")
    add("O que dedos de mão humana escreveram na parede do palácio de Belsazar durante o banquete profano?",
        "'MENE, MENE, TEQUEL, PARSIM'", "'GLÓRIA A BABILÔNIA'", "'PAZ AO IMPÉRIO DOS CALDEUS'", "'OURO E PRATA A BELSAZAR'",
        "facil", "Daniel", "Daniel 5:5; 25", "Surgiram dedos de mão humana e escreveram defronte do candelabro: 'Mene, Mene, Tequel, Parsim'.")
    add("Qual o significado revelado por Daniel para a palavra TEQUEL na inscrição da parede?",
        "'Pesado foste na balança, e achado em falta'", "'Teu reino será multiplicado'", "'Teus exércitos vencerão a Pérsia'", "'Edificarás novos templos'",
        "facil", "Daniel", "Daniel 5:27", "Tequel: 'Pesado foste na balança e achado em falta'. Naquela mesma noite Belsazar foi morto.")
    add("Por que Daniel foi lançado na cova dos leões pelo rei Dario?",
        "Continuou orando três vezes ao dia a Deus de janelas abertas para Jerusalém, desobedecendo ao decreto real", "Foi acusado de roubar o tesouro persa", "Recusou liderar o exército", "Criticou a lei dos medos e persas",
        "facil", "Daniel", "Daniel 6:10-16", "Daniel orava três vezes ao dia dando graças ao seu Deus; e os príncipes o acusaram perante o rei.")
    add("Como Daniel saiu ileso da cova dos leões famintos na manhã seguinte?",
        "Deus enviou o Seu anjo que fechou a boca dos leões para que não lhe fizessem dano algum", "Os leões haviam sido alimentados", "Daniel usou uma tocha de fogo", "Daniel dormiu numa árvore interna",
        "facil", "Daniel", "Daniel 6:22", "Daniel respondeu ao rei: 'O meu Deus enviou o seu anjo e fechou a boca dos leões, e não me fizeram dano'.")

    # Os 12 Profetas Menores (40)
    add("O que Deus ordenou ao profeta Oseias para ilustrar a infidelidade espiritual de Israel para com o Senhor?",
        "Casar-se com uma mulher de prostituições chamada Gômer", "Jejuar quarenta dias na praça", "Vestir-se de panos de saco rotos", "Viver como eremita no deserto",
        "facil", "Oseias", "Oseias 1:2", "Disse o Senhor a Oseias: 'Vai, toma uma mulher de prostituições e filhos de prostituição; porque a terra se prostituiu'." )
    add("Qual denúncia célebre sobre a destruição pela ignorância espiritual está em Oseias 4:6?",
        "'O meu povo foi destruído, porque lhe faltou o conhecimento'", "'O meu povo perece por falta de espadas'", "'Israel caiu pela seca dos campos'", "'As nações têm mais ouro'",
        "facil", "Oseias", "Oseias 4:6", "'O meu povo foi destruído, porque lhe faltou o conhecimento; porque tu rejeitaste o conhecimento, também eu te rejeitarei'.")
    add("Qual praga natural devastadora o profeta Joel usou como alerta e prenúncio do Dia do Senhor?",
        "A praga de quatro espécies de gafanhotos destruidores", "Uma peste de ratos", "Uma inundação do Nilo", "Uma tempestade de granizo",
        "medio", "Joel", "Joel 1:4", "O que ficou da lagarta o comeu o gafanhoto, o que ficou do gafanhoto o comeu a locusta.")
    add("Qual promessa messiânica sobre a efusão do Espírito está em Joel 2:28, citada por Pedro no Pentecostes?",
        "'Derramarei o meu Espírito sobre toda a carne; vossos filhos e vossas filhas profetizarão'", "'Cairá chuva de ouro nos altares'", "'Todos os israelitas serão reis'", "'Os inimigos serão expulsos'",
        "facil", "Joel", "Joel 2:28; Atos 2:17", "Profecia do derramamento do Espírito Santo sobre toda a humanidade cumprida no dia de Pentecostes.")
    add("Qual profissão simples o profeta Amós exercia em Tecoa antes de ser enviado a profetizar em Israel?",
        "Boiadeiro e colhedor de sicômoros / figos bravos", "Sacerdote levítico em Siló", "Pescador no mar da Galileia", "Escriba real em Samaria",
        "medio", "Amós", "Amós 7:14", "Amós respondeu: 'Não sou profeta nem filho de profeta, mas boieiro e cultivador de sicômoros'.")
    add("Qual apelo por retidão moral e justiça social Amós proclamou em Amós 5:24?",
        "'Corra o juízo como as águas, e a justiça como um ribeiro perene'", "'Aumentai o número dos sacrifícios'", "'Construí santuários de mármore'", "'Guardai todo o ouro colhido'",
        "facil", "Amós", "Amós 5:24", "'Antes corra o juízo como as águas, e a justiça como o ribeiro perene'.")
    add("Qual é o menor livro de todo o Velho Testamento com apenas um capítulo contendo 21 versículos?",
        "Obadias", "Naum", "Habacuque", "Ageu",
        "facil", "Obadias", "Obadias 1", "O livro de Obadias possui um único capítulo de 21 versículos anunciando o juízo sobre Edom.")
    add("Para qual cidade Jonas tentou fugir num navio a fim de desobedecer à ordem de pregar em Nínive?",
        "Társis", "Damasco", "Babilônia", "Alexandria",
        "facil", "Jonas", "Jonas 1:3", "Jonas levantou-se para fugir da presença do Senhor para Társis, descendo a Jope onde achou um navio.")
    add("O que Jonas fazia no porão do navio enquanto a terrível tempestade açoitava a embarcação?",
        "Dormia profundamente um sono pesado", "Orava com lágrimas", "Ajudava a lançar a carga ao mar", "Remava com vigor",
        "facil", "Jonas", "Jonas 1:5", "Jonas havia descido para o porão do navio e, tendo-se deitado, dormia um profundo sono.")
    add("Quantos dias e quantas noites Jonas permaneceu no ventre do grande peixe orando ao Senhor?",
        "Três dias e três noites", "Sete dias e sete noites", "Quarenta dias", "Um dia apenas",
        "facil", "Jonas", "Jonas 1:17; Mateus 12:40", "Jonas esteve no ventre do peixe três dias e três noites, sinal apontado por Jesus sobre Sua ressurreição.")
    add("Qual cidade foi profetizada pelo profeta Miqueias como o humilde local do nascimento do Messias de Israel?",
        "Belém de Efrata", "Jerusalém", "Nazaré", "Cafarnaum",
        "facil", "Miqueias", "Miqueias 5:2; Mateus 2:6", "'E tu, Belém-Efrata, posto que pequena entre os milhares de Judá, de ti me sairá o que governará em Israel'.")
    add("O que o Senhor requer do homem segundo Miqueias 6:8?",
        "Que pratique a justiça, ame a misericórdia e ande humildemente com o seu Deus", "Que ofereça milhares de carneiros", "Que doe toda a sua riqueza aos sacerdotes", "Que viva em isolamento",
        "facil", "Miqueias", "Miqueias 6:8", "O que o Senhor pede de ti senão que pratiques a justiça, ames a bondade e andes humildemente com o teu Deus?")
    add("Qual declaração fundamental de fé inspirou o apóstolo Paulo e os reformadores em Habacuque 2:4?",
        "'O justo viverá pela sua fé'", "'O homem sábio acumula ouro'", "'A força da espada trará vitória'", "'Todos os caminhos são iguais'",
        "facil", "Habacuque", "Habacuque 2:4; Romanos 1:17", "A célebre verdade evangélica 'O justo viverá pela fé' está proclamada em Habacuque 2:4.")
    add("Qual sublime oração de júbilo e confiança incondicional Habacuque faz no final de seu livro?",
        "'Ainda que a figueira não floresça, nem haja fruto na vide... todavia eu me alegrarei no Senhor'", "'Peço riquezas e palácios'", "'Foge de mim a esperança'", "'Desejo a morte dos caldeus'",
        "facil", "Habacuque", "Habacuque 3:17-18", "'Ainda que a figueira não floresça... todavia eu me alegrarei no Senhor; exultarei no Deus da minha salvação'.")
    add("O que o profeta Ageu confrontou com firmeza ao povo que retornou do cativeiro?",
        "Cuidavam de suas próprias casas com forro requintado enquanto a Casa do Senhor permanecia em ruínas", "Não guerreavam contra a Pérsia", "Não queriam plantar oliveiras", "Fugiram para o Egito",
        "medio", "Ageu", "Ageu 1:4", "Disse o Senhor por Ageu: 'É tempo de habitardes em vossas casas forradas, enquanto esta casa jaz deserta?'.")
    add("Qual promessa sobre a glória futura do Templo está registrada em Ageu 2:9?",
        "'A glória desta última casa será maior do que a da primeira, e neste lugar darei a paz'", "'O novo templo terá mais ouro'", "'As muralhas serão invencíveis'", "'Não haverá mais necessidade de sacerdotes'",
        "facil", "Ageu", "Ageu 2:9", "'A glória desta última casa será maior do que a da primeira, diz o Senhor dos Exércitos, e neste lugar darei a paz'.")
    add("Qual profecia messiânica sobre a entrada humilde do Rei em Jerusalém está em Zacarias 9:9?",
        "'Eis que o teu rei virá a ti, justo e salvador, humilde e montado sobre um jumentinho'", "'O rei virá num carro de ouro puxado por quatro leões'", "'O rei virá com exércitos da Pérsia'", "'O rei descerá em nuvens de fogo'",
        "facil", "Zacarias", "Zacarias 9:9; Mateus 21:5", "'Alegra-te muito, filha de Sião... eis que o teu Rei virá a ti, manso e assentado sobre um jumento'.")
    add("Qual valor profético foi estipulado como salário desprezível pelo Bom Pastor em Zacarias 11:12-13?",
        "Trinta moedas de prata (preço de um escravo arremessado para o oleiro)", "Cem talentos de ouro", "Cinquenta barras de ferro", "Dez moedas de cobre",
        "medio", "Zacarias", "Zacarias 11:12-13; Mateus 26:15", "Pesaram por meu salário trinta moedas de prata, lançadas ao oleiro na casa do Senhor (traição de Judas).")
    add("Qual pergunta retórica célebre sobre fidelidade financeira está em Malaquias 3:8-10?",
        "'Roubará o homem a Deus? Todavia vós me roubais nos dízimos e nas ofertas alçadas'", "'Por que não comprais cavalos no Egito?'", "'Quem edificará outro altar?'", "'Por que os sacerdotes não jejuam?'",
        "facil", "Malaquias", "Malaquias 3:8-10", "'Roubará o homem a Deus? Trazei todos os dízimos à casa do tesouro, para que haja mantimento na minha casa'.")
    add("Qual título messiânico glorioso é atribuído a Cristo no último capítulo de Malaquias?",
        "O Sol da Justiça, trazendo cura nas suas asas", "A Estrela de Ouro", "A Tocha de Judá", "O Leão do Deserto",
        "facil", "Malaquias", "Malaquias 4:2", "'Mas para vós que temeis o meu nome nascerá o Sol da Justiça, trazendo cura sob as suas asas'.")

    # --- Isaías Adicionais ---
    add("Qual convite gracioso de perdão completo está em Isaías 1:18?",
        "'Vinde e arrazoemos: ainda que os vossos pecados sejam como a escarlata, eles se tornarão brancos como a neve'", "'Fazei ofertas de cem bezerros'", "'Queimai incenso de mirra'", "'Constrói muralhas mais altas'",
        "facil", "Isaías", "Isaías 1:18", "'Vinde então, e argui-me, diz o Senhor: ainda que os vossos pecados sejam como a escarlata, eles se tornarão brancos como a neve'.")
    add("O que as nações farão com suas armas no Reino da paz segundo Isaías 2:4?",
        "Converterão as suas espadas em relhas de arados e as suas lanças em foices", "Construirão mais lanças", "Guardarão o ferro em cofres", "Fundirão armas de prata",
        "facil", "Isaías", "Isaías 2:4", "'E converterão as suas espadas em enxadas e as suas lanças em foices; não levantará espada nação contra nação'.")
    add("A qual descendência davídica Isaías 11:1 compara o surgimento do Messias?",
        "Um broto que sairá do tronco de Jessé, e um renovo que brotará de suas raízes", "A uma palmeira do Nilo", "A um cedro de Tiro", "A um carvalho de Basã",
        "medio", "Isaías", "Isaías 11:1", "'Porque brotará um rebento do tronco de Jessé, e das suas raízes um renovo frutificará'.")
    add("Como a reconciliação e a paz da criação são descritas em Isaías 11:6?",
        "O lobo habitará com o cordeiro, e o leopardo com o cabrito se deitará", "Os leões devorarão as serpentes", "Os animais fugirão para o mar", "A terra será habitada só por aves",
        "facil", "Isaías", "Isaías 11:6", "'Morará o lobo com o cordeiro, e o leopardo com o cabrito se deitará... e um menino pequeno os guiará'.")
    add("Qual promessa de paz mental constante está em Isaías 26:3?",
        "'Tu conservarás em paz aquele cuja mente está firme em ti; porque ele confia em ti'", "'A paz vem das muitas riquezas'", "'A mente humana alcança paz sozinha'", "'A paz depende dos governantes'",
        "facil", "Isaías", "Isaías 26:3", "'Tu conservarás em paz aquele cuja mente está firme em ti; porque ele confia em ti. Confiai no Senhor perpetuamente'.")
    add("Qual consolo maravilhoso de coragem contra o medo está em Isaías 41:10?",
        "'Não temas, porque eu sou contigo; não te assombres, porque eu sou o teu Deus; eu te fortaleço e te ajudo'", "'Confia no teu próprio braço'", "'Pede ajuda aos soldados vizinhos'", "'Foge enquanto há tempo'",
        "facil", "Isaías", "Isaías 41:10", "'Não temas, porque eu sou contigo; não te assombres, porque eu sou o teu Deus; eu te fortaleço, e te ajudo, e te sustento'.")
    add("Qual promessa de companhia nas tribulações está em Isaías 43:2?",
        "'Quando passares pelas águas estarei contigo, e quando pelos rios, eles não te submergirão; quando passares pelo fogo, não te queimarás'", "'Nenhum perigo chegará perto de ti'", "'Os anjos te levarão para as nuvens'", "'Não terás nenhuma dificuldade na terra'",
        "facil", "Isaías", "Isaías 43:2", "'Quando passares pelas águas estarei contigo... quando passares pelo fogo, não te queimarás, nem a chama arderá em ti'.")
    add("Qual imperador persa foi chamado profeticamente por Deus pelo nome mais de um século antes em Isaías 45:1?",
        "Ciro", "Dario", "Artaxerxes", "Xerxes",
        "medio", "Isaías", "Isaías 45:1", "Deus chamou por nome a Ciro, seu ungido, séculos antes de seu nascimento para libertar os cativos judeus.")
    add("O que Isaías 49:15 afirma comparando o amor de Deus com o amor materno mais profundo?",
        "'Pode uma mulher esquecer-se de seu filho de peito? Ainda que ela se esquecesse, eu, todavia, não me esquecerei de ti'", "'O amor humano é perfeito'", "'As mães nunca falham'", "'Deus ama apenas os sábios'",
        "facil", "Isaías", "Isaías 49:15", "'Porventura pode uma mulher esquecer-se tanto de seu filho... mas ainda que esta se esquecesse dele, contudo eu não me esquecerei de ti'.")
    add("O que Isaías 52:7 declara a respeito daqueles que proclamam o Evangelho de paz?",
        "'Quão formosos sobre os montes são os pés do que anuncia boas-novas, que faz ouvir a paz!'", "'Eles receberão muitas coroas de ouro'", "'Marcharão com trombetas de prata'", "'Serão recebidos em todos os palácios'",
        "facil", "Isaías", "Isaías 52:7; Romanos 10:15", "'Quão formosos sobre os montes são os pés do que anuncia as boas-novas, que faz ouvir a paz, que anuncia o bem!'.")
    add("Qual garantia de proteção divina contra perseguições está em Isaías 54:17?",
        "'Toda a ferramenta preparada contra ti não prosperará; e toda a língua que se levantar contra ti em juízo tu a condenarás'", "'Nunca serás criticado'", "'Todos os homens te aplaudirão'", "'Não haverá batalhas em teus dias'",
        "facil", "Isaías", "Isaías 54:17", "'Toda a ferramenta preparada contra ti não prosperará... esta é a herança dos servos do Senhor'.")
    add("Qual é o verdadeiro jejum que agrada a Deus segundo Isaías 58:6-7?",
        "Soltar as ligaduras da impiedade, desatar as cordas do jugo, repartir o pão com o faminto e recolher os pobres desabrigados", "Apenas abster-se de carne e vinho", "Ficar em silêncio numa caverna", "Vestir roupas cinzentas",
        "facil", "Isaías", "Isaías 58:6-7", "'Porventura não é este o jejum que escolhi: que soltes as ligaduras da impiedade... que repartas o teu pão com o faminto?'.")
    add("Qual promessa escatológica de renovação de todas as coisas Deus anuncia em Isaías 65:17?",
        "'Pois eis que crio novos céus e nova terra; e não haverá lembrança das coisas passadas'", "'O mundo antigo permanecerá o mesmo'", "'A terra será destruída para sempre sem restauração'", "'As cidades antigas serão reformadas'",
        "facil", "Isaías", "Isaías 65:17; Apocalipse 21:1", "'Pois eis que eu crio novos céus e nova terra; e não haverá mais lembrança das coisas passadas'.")

    # --- Jeremias Adicionais ---
    add("Quais duas visões inaugurais Jeremias teve ao ser vocacionado no capítulo 1?",
        "Uma vara de amendoeira e uma panela fervendo cuja face olhava do norte", "Um leão com asas e um carneiro", "Um templo de ouro e uma espada", "Duas oliveiras e um castiçal",
        "medio", "Jeremias", "Jeremias 1:11-13", "Deus mostrou a Jeremias a vara de amendoeira ('Eu velo sobre a minha palavra') e a panela fervendo voltada do norte.")
    add("Em que o homem verdadeiramente sábio deve se gloriar segundo Jeremias 9:23-24?",
        "Em entender e conhecer a Deus, sabendo que Ele é o Senhor que faz misericórdia, juízo e justiça na terra", "Na sua força física e destreza bélica", "Na quantidade de prata e ouro que acumulou", "Nos títulos e cargos do palácio",
        "facil", "Jeremias", "Jeremias 9:23-24", "'Mas o que se gloriar, glorie-se nisto: em me entender e me conhecer, que eu sou o Senhor, que faço benignidade, juízo e justiça'.")
    add("A que é comparado o homem que confia no homem e faz da carne mortal o seu braço em Jeremias 17:5-6?",
        "À tamargueira solitária no deserto, que não vê quando vem o bem", "A uma oliveira fértil", "A um carvalho frondoso", "A uma videira cheia de frutos",
        "medio", "Jeremias", "Jeremias 17:5-6", "'Maldito o homem que confia no homem... porque será como a tamargueira no deserto, e não verá quando vem o bem'.")
    add("A que é comparado o homem que confia no Senhor no mesmo texto de Jeremias 17:7-8?",
        "À árvore plantada junto às águas, que estende as raízes para o ribeiro e não receia o calor nem cessa de dar fruto", "A uma montanha de areia", "A uma flor efêmera", "A uma rocha sem vegetação",
        "facil", "Jeremias", "Jeremias 17:7-8", "'Bendito o homem que confia no Senhor... será como a árvore plantada junto às águas, que estende as suas raízes para o ribeiro'.")
    add("Como Jeremias descreveu a Palavra de Deus em seu coração quando pensou em calar-se em Jeremias 20:9?",
        "Como um fogo ardente encerrado nos seus ossos, de modo que não pôde conter-se", "Como um fardo de pedra pesada", "Como uma brisa fresca passageira", "Como água que evaporou",
        "facil", "Jeremias", "Jeremias 20:9", "'Havia em meu coração um como fogo ardente, encerrado nos meus ossos; e fiquei cansado de conter o fogo e não pude mais'.")
    add("Qual título messiânico profético é anunciado para o Renovo de justiça em Jeremias 23:6?",
        "O SENHOR, JUSTIÇA NOSSA (Yahweh Tsidkenu)", "O Santo de Salém", "O Leão dos Caldeus", "O Príncipe do Templo",
        "medio", "Jeremias", "Jeremias 23:5-6", "'E este será o seu nome, com o qual o chamarão: O SENHOR, JUSTIÇA NOSSA'.")
    add("O que o ímpio rei Jeoaquim fez com o rolo das profecias de Jeremias lido por Jeudi em Jeremias 36?",
        "Cortou-o com um canivete de escrivão e lançou os pedaços no braseiro aceso até consumir-se todo o rolo", "Guardou-o no arquivo real", "Pediu perdão a Deus em cinzas", "Mandou selar o livro com ouro",
        "medio", "Jeremias", "Jeremias 36:23", "Havendo Jeudi lido três ou quatro folhas, o rei cortou-o com um canivete de escrivão e lançou-o no fogo que estava no braseiro.")
    add("O que aconteceu ao rei Zedequias após o cerco e queda final de Jerusalém em Jeremias 52?",
        "Seus olhos foram vazados em Ribla após ver seus filhos serem mortos, e foi levado preso em cadeias de bronze à Babilônia", "Fugiu disfarçado para o Egito", "Faleceu lutando com espada nas muralhas", "Foi coroado vice-rei na Pérsia",
        "medio", "Jeremias", "Jeremias 52:10-11", "O rei da Babilônia degolou os filhos de Zedequias perante os seus olhos; depois vazou os olhos de Zedequias e o atou com cadeias.")

    # --- Ezequiel Adicionais ---
    add("O que a partida da Glória do Senhor do templo de Jerusalém significou nas visões de Ezequiel 10 e 11?",
        "O abandono da presença divina por causa das graves idolatrias secretas praticadas no santuário", "Uma visita aos povos gentios", "Uma tempestade de areia passageira", "A aprovação das ofertas dos sacerdotes",
        "medio", "Ezequiel", "Ezequiel 10:18-19; 11:23", "A glória do Senhor subiu do meio da cidade e pôs-se sobre o monte que está ao oriente da cidade.")
    add("Qual princípio de responsabilidade moral individual Deus ensina no capítulo 18 de Ezequiel?",
        "'A alma que pecar, essa morrerá; o filho não levará a iniquidade do pai nem o pai a iniquidade do filho'", "'O pecado de uma pessoa condena todas as gerações sem perdão'", "'Os filhos pagam eternamente pelos crimes dos pais'", "'A justiça humana salva toda a família'",
        "facil", "Ezequiel", "Ezequiel 18:20", "'A alma que pecar, essa morrerá; o filho não levará a maldade do pai, nem o pai levará a maldade do filho'.")
    add("Qual promessa de regeneração interior e novo coração Deus faz em Ezequiel 36:26?",
        "'Dar-vos-ei um coração novo e porei dentro de vós um espírito novo; tirarei o coração de pedra e vos darei um coração de carne'", "'Dar-vos-ei armas invencíveis'", "'Multiplicarei o vosso ouro'", "'Tornar-vos-ei reis sobre todas as nações'",
        "facil", "Ezequiel", "Ezequiel 36:26", "'Dar-vos-ei coração novo, e porei dentro de vós espírito novo; e tirarei da vossa carne o coração de pedra e vos darei um coração de carne'.")
    add("Como os falsos pastores de Israel são repreendidos por Deus no capítulo 34 de Ezequiel?",
        "Apascentavam a si mesmos em vez de apascentarem o rebanho, não fortalecendo a fraca nem curando a doente", "Oravam demais no templo", "Não cobravam dízimos suficientes", "Não construíram currais de pedra",
        "medio", "Ezequiel", "Ezequiel 34:2-4", "'Ai dos pastores de Israel que se apascentam a si mesmos! Não apascentarão os pastores as ovelhas?'.")
    add("Qual nome da nova cidade celestial restaurada é revelado no último versículo do livro de Ezequiel?",
        "O SENHOR ESTÁ ALI (Yahweh Shamah)", "Jerusalém de Ouro", "Monte Santo de Judá", "A Fortaleza Inabalável",
        "dificil", "Ezequiel", "Ezequiel 48:35", "O nome da cidade desde aquele dia será: O SENHOR ESTÁ ALI (Yahweh Shamah).")

    # --- Daniel Adicionais ---
    add("Quais quatro animais simbólicos representavam os grandes impérios mundiais na visão de Daniel 7?",
        "Um leão com asas de águia, um urso com três costelas na boca, um leopardo com quatro asas e quatro cabeças, e um animal terrível e espantoso com dentes de ferro e dez chifres", "Quatro cavalos de cores distintas", "Um touro, um carneiro, um bode e uma serpente", "Quatro águias reais",
        "medio", "Daniel", "Daniel 7:3-7", "Quatro grandes animais subiam do mar representando Babilônia, Média-Pérsia, Grécia e Roma.")
    add("Quem Daniel viu assentado no trono celestial com vestes brancas como a neve e trono em chamas de fogo em Daniel 7:9?",
        "O Ancião de Dias", "O rei Salomão", "O arcanjo Miguel", "Moisés glorificado",
        "medio", "Daniel", "Daniel 7:9", "Olhei até que foram postos uns tronos, e o Ancião de Dias se assentou; a sua veste era branca como a neve.")
    add("Quem veio nas nuvens do céu até o Ancião de Dias para receber domínio, glória e reino eterno em Daniel 7:13-14?",
        "Um semelhante ao Filho do Homem", "Um guerreiro persa", "O arcanjo Gabriel", "Um querubim alado",
        "facil", "Daniel", "Daniel 7:13-14; Mateus 26:64", "Eis que vinha nas nuvens do céu um como o Filho do Homem, e foi-lhe dado o domínio perpétuo que não passará.")
    add("Qual arcanjo apareceu a Daniel em resposta às suas orações revelando a profecia das Setenta Semanas?",
        "O anjo Gabriel", "O anjo Rafael", "O anjo Uriel", "O anjo Melquisedeque",
        "facil", "Daniel", "Daniel 9:21-24", "O varão Gabriel veio voando rapidamente e tocou-me à hora do sacrifício da tarde para dar entendimento.")
    add("Qual príncipe celestial de primeira grandeza guerreou contra o príncipe do reino da Pérsia em Daniel 10?",
        "Miguel", "Gabriel", "Lúcifer", "Aoliabe",
        "medio", "Daniel", "Daniel 10:13; 21", "Eis que Miguel, um dos primeiros príncipes, veio para ajudar-me; e eu fiquei ali com os reis da Pérsia.")
    add("Qual profecia gloriosa sobre a ressurreição dos mortos encerra o livro de Daniel no capítulo 12:2-3?",
        "'Muitos dos que dormem no pó da terra ressuscitarão, uns para a vida eterna e outros para vergonha e desprezo eterno; os sábios resplandecerão como o firmamento'", "'Todos permanecerão adormecidos no pó'", "'Apenas os reis ressuscitarão'", "'A morte é o fim de tudo'",
        "facil", "Daniel", "Daniel 12:2-3", "'Muitos dos que dormem no pó da terra ressuscitarão... e os que forem sábios resplandecerão como o fulgor do firmamento'.")

    # --- Profetas Menores Adicionais ---
    add("Qual convite ao retorno e à cura espiritual está em Oseias 6:1-3?",
        "'Vinde e tornemos ao Senhor; conheçamos e prossigamos em conhecer ao Senhor: como a alva, a sua vinda é certa'", "'Construí santuários de mármore'", "'Oferecei sacrifícios de bois'", "'Fugi para as montanhas de Gileade'",
        "facil", "Oseias", "Oseias 6:1-3", "'Conheçamos, e prossigamos em conhecer ao Senhor; a sua saída, como a alva, é certa; e ele a nós virá como a chuva'.")
    add("Qual palavra de amor paternal de Deus por Israel é lembrada em Oseias 11:1, citada no retorno do menino Jesus do Egito?",
        "'Quando Israel era menino, eu o amei; e do Egito chamei o meu filho'", "'Israel foi sempre obediente'", "'Os reis do Egito eram meus amigos'", "'Nunca castiguei o meu povo'",
        "facil", "Oseias", "Oseias 11:1; Mateus 2:15", "Profecia cumprida na infância de Jesus quando retornou do refúgio no Egito para Nazaré.")
    add("Qual exortação ao arrependimento sincero do íntimo está em Joel 2:13?",
        "'Rasgai o vosso coração, e não as vossas vestes, e convertei-vos ao Senhor vosso Deus'", "'Rasgai as vossas capas nos cantos das ruas'", "'Chorai apenas perante os sacerdotes'", "'Fazei promessas de ouro'",
        "facil", "Joel", "Joel 2:13", "'E rasgai o vosso coração, e não as vossas vestes, e convertei-vos ao Senhor vosso Deus; porque ele é misericordioso e compassivo'.")
    add("O que Amós 3:7 ensina a respeito das revelações de Deus aos Seus profetas?",
        "'Certamente o Senhor Deus não fará coisa alguma, sem ter revelado o seu segredo aos seus servos, os profetas'", "'Deus age sem aviso algum'", "'O futuro é oculto até para os anjos'", "'Os profetas adivinham por sorteio'",
        "facil", "Amós", "Amós 3:7", "'Certamente o Senhor Deus não fará coisa alguma, sem ter revelado o seu segredo aos seus servos, os profetas'.")
    add("Qual tipo terrível de fome sobreviria à terra profetizado em Amós 8:11?",
        "Não fome de pão nem sede de água, mas de ouvir as palavras do Senhor", "Seca total de todos os poços", "Morte de todos os rebanhos", "Perda das colheitas de trigo",
        "facil", "Amós", "Amós 8:11", "'Eis que vêm dias em que enviarei fome sobre a terra; não fome de pão, nem sede de água, mas de ouvir as palavras do Senhor'.")
    add("O que Deus fez crescer e depois secar por um verme para ensinar compaixão a Jonas em Nínive?",
        "Uma aboboreira (planta de sombra)", "Uma oliveira frondosa", "Uma figueira de Judá", "Uma videira doce",
        "facil", "Jonas", "Jonas 4:6-7", "Deus fez nascer uma aboboreira para cobrir a cabeça de Jonas; no dia seguinte enviou um bicho que feriu a aboboreira e ela secou.")
    add("Quantas pessoas que não sabiam discernir entre a mão direita e a mão esquerda habitavam na grande Nínive segundo Jonas 4:11?",
        "Mais de cento e vinte mil pessoas (além de muitos animais)", "Dez mil habitantes", "Cinquenta mil pessoas", "Um milhão de almas",
        "medio", "Jonas", "Jonas 4:11", "Deus disse: 'Não hei de eu ter compaixão da grande cidade de Nínive, em que há mais de cento e vinte mil pessoas?'.")
    add("Qual versículo de louvor ao perdão inigualável de Deus encerra o livro de Miqueias no capítulo 7:18-19?",
        "'Quem, ó Deus, é semelhante a ti, que perdoas a iniquidade? Lançarás todos os nossos pecados nas profundezas do mar'", "'O Senhor destruirá todas as nações'", "'Os nossos erros nunca serão apagados'", "'A justiça humana é suficiente'",
        "facil", "Miqueias", "Miqueias 7:18-19", "'Tornará a ter compaixão de nós; pisará aos pés as nossas iniquidades e lançará todos os nossos pecados nas profundezas do mar'.")
    add("Como o profeta Naum descreve a bondade e proteção do Senhor no capítulo 1:7?",
        "'O Senhor é bom, uma fortaleza no dia da angústia, e conhece os que confiam nele'", "'Deus é inacessível aos homens'", "'A força das armas traz segurança'", "'Os exércitos assírios são invencíveis'",
        "facil", "Naum", "Naum 1:7", "'O Senhor é bom, ele serve de fortaleza no dia da angústia, e conhece os que confiam nele'.")
    add("Qual cântico alegre de Deus sobre o Seu povo remanescente está em Sofonias 3:17?",
        "'O Senhor teu Deus está no meio de ti, poderoso para salvar; ele se deleitará em ti com júbilo; renovar-te-á no seu amor'", "'Deus se afasta dos pecadores'", "'O julgamento de fogo não perdoa'", "'Os montes tremerão para sempre'",
        "facil", "Sofonias", "Sofonias 3:17", "'O Senhor teu Deus está no meio de ti, poderoso para salvar; ele se deleitará em ti com alegria; renovar-te-á no seu amor'.")
    add("A quem pertencia toda a prata e o ouro segundo a palavra do Senhor em Ageu 2:8?",
        "'Minha é a prata, e meu é o ouro, diz o Senhor dos Exércitos'", "'Pertence ao rei da Pérsia'", "'Pertence aos mercadores de Tiro'", "'Pertence aos governadores das cidades'",
        "facil", "Ageu", "Ageu 2:8", "'Minha é a prata, e meu é o ouro, disse o Senhor dos Exércitos'.")
    add("Qual resposta célebre o Senhor deu a Zorobabel em Zacarias 4:6 sobre a realização das obras divinas?",
        "'Não por força nem por violência, mas pelo meu Espírito, diz o Senhor dos Exércitos'", "'Pela quantidade de ouro acumulado'", "'Pelo poder das carruagens de ferro'", "'Pela astúcia dos generais'",
        "facil", "Zacarias", "Zacarias 4:6", "'Não por força nem por violência, mas sim pelo meu Espírito, diz o Senhor dos Exércitos'.")
    add("O que Zacarias 12:10 profetizou com respeito ao arrependimento de Israel ao contemplar o Messias crucificado?",
        "'Olharão para aquele a quem traspassaram, e prantearão por ele como quem pranteia pelo filho unigênito'", "'Festejarão a vitória com danças'", "'Não reconhecerão o Ungido'", "'Construirão outro templo'",
        "medio", "Zacarias", "Zacarias 12:10; João 19:37", "'E olharão para mim, a quem traspassaram; e prantearão sobre ele, como quem pranteia pelo filho unigênito'.")
    add("O que haverá aberto para a casa de Davi em Zacarias 13:1 para purificação do pecado e da impureza?",
        "Uma fonte aberta para remover o pecado e a impureza", "Um rio de ouro líquido", "Um poço de água salgada", "Uma fogueira de sacrifícios",
        "medio", "Zacarias", "Zacarias 13:1", "'Naquele dia haverá uma fonte aberta para a casa de Davi e para os habitantes de Jerusalém, para purificação do pecado e da imundícia'.")
    add("Qual grande promessa messiânica sobre o reinado universal de Deus está em Zacarias 14:9?",
        "'O Senhor será Rei sobre toda a terra; naquele dia um só será o Senhor, e um só será o seu nome'", "'Haverá doze reis dividindo a terra'", "'Os impérios nunca se curvarão'", "'Jerusalém será esquecida'",
        "facil", "Zacarias", "Zacarias 14:9", "'E o Senhor será rei sobre toda a terra; naquele dia um será o Senhor, e um será o seu nome'.")
    add("Qual promessa encerra o Antigo Testamento em Malaquias 4:5-6 sobre o envio do precursor espiritual?",
        "'Eis que eu vos enviarei o profeta Elias antes que venha o grande e terrível Dia do Senhor; e ele converterá o coração dos pais aos filhos'", "'Enviarei um general armado com espada de ouro'", "'O sol escurecerá para sempre sem esperança'", "'Moisés descerá no monte Sinai'",
        "facil", "Malaquias", "Malaquias 4:5-6; Lucas 1:17", "A profecia de Elias precursor cumpriu-se no ministério de João Batista no espírito e poder de Elias.")

    # --- Mais Profetas para completar 150 ---
    add("Qual parábola da vinha estéril Isaías canta no capítulo 5 a respeito de Israel?",
        "Esperava uvas boas, mas a vinha produziu uvas bravas (injustiça e opressão)", "A vinha foi devorada por gafanhotos", "A vinha produziu vinho de ouro", "A vinha foi roubada por mercadores",
        "medio", "Isaías", "Isaías 5:1-4", "O Senhor plantou uma vinha seleta e esperava que desse uvas boas, mas deu uvas bravas.")
    add("Qual cidade fenícia opulenta teve sua queda profetizada com lamento em Isaías 23?",
        "Tiro", "Damasco", "Babilônia", "Nínive",
        "medio", "Isaías", "Isaías 23:1", "Oráculo contra Tiro: 'Uivai, navios de Társis, porque ela está desolada'.")
    add("Qual profecia sobre a destruição da morte para sempre está em Isaías 25:8?",
        "'Tragará a morte para sempre, e assim enxugará o Senhor Deus as lágrimas de todos os rostos'", "'A morte reinará eternamente'", "'Não haverá ressurreição'", "'Os homens viverão apenas cem anos'",
        "facil", "Isaías", "Isaías 25:8; 1 Coríntios 15:54", "'Tragará a morte na vitória; e o Senhor Deus enxugará as lágrimas de todos os rostos'.")
    add("O que Isaías 30:15 ensina sobre o verdadeiro descanso e salvação?",
        "'Na tranquilidade e na confiança estaria a vossa força'", "'Na pressa das carruagens'", "'Nos pactos com o Egito'", "'No acúmulo de prata'",
        "facil", "Isaías", "Isaías 30:15", "'Em vos converterdes e em sossegardes está a vossa salvação; na tranquilidade e na confiança a vossa força'.")
    add("Como Isaías 35:1 descreve a alegria da restauração no deserto?",
        "'O deserto e o lugar solitário se alegrarão, e o ermo exultará e florescerá como a rosa'", "'O deserto será coberto de pedras'", "'As águas do mar invadirão a terra'", "'A terra ficará desolada'",
        "facil", "Isaías", "Isaías 35:1", "'O deserto e a terra sedenta se regozijarão; e o ermo exultará e florescerá como a rosa'.")
    add("Qual profeta consolou o rei Ezequias contra as ameaças de Senaqueribe garantindo o livramento de Jerusalém?",
        "Isaías", "Jeremias", "Miqueias", "Oseias",
        "facil", "Isaías", "Isaías 37:5-7", "Isaías enviou a dizer a Ezequias que não temesse as palavras blasfemas dos servos do rei da Assíria.")
    add("Quantos anos de vida foram acrescentados a Ezequias quando orou a Deus e Isaías profetizou sua cura?",
        "15 anos", "7 anos", "10 anos", "20 anos",
        "facil", "Isaías", "Isaías 38:5", "Disse o Senhor a Ezequias: 'Ouvi a tua oração e vi as tuas lágrimas; eis que acrescentarei aos teus dias quinze anos'.")
    add("Qual sinal no relógio de sol de Acaz confirmou a promessa da cura de Ezequias?",
        "A sombra do sol retrocedeu dez graus nos degraus", "O sol ficou imóvel dois dias", "Houve um eclipse total de três horas", "A lua surgiu ao meio-dia",
        "medio", "Isaías", "Isaías 38:8", "Eis que farei voltar dez graus atrás a sombra dos graus que já declinou no relógio de sol de Acaz.")
    add("Qual remédio natural à base de frutas Isaías mandou aplicar sobre a úlcera de Ezequias para sarar?",
        "Uma pasta de figos prensados", "Azeite de mirra pura", "Vinho aromático", "Mel com sal",
        "medio", "Isaías", "Isaías 38:21", "Dissera Isaías: 'Tomem uma pasta de figos e a ponham como emplastro sobre a chaga; e sarará'.")
    add("O que Jeremias comprou enquanto estava preso no pátio da guarda durante o cerco de Jerusalém para demonstrar fé no retorno?",
        "Um campo em Anatote de seu primo Hanamel por dezessete siclos de prata", "Uma carruagem de bronze", "Uma vinha em Hebrom", "Um rebanho de ovelhas",
        "medio", "Jeremias", "Jeremias 32:7-9", "Jeremias comprou o campo como sinal profético de que ainda se comprariam casas, campos e vinhas na terra.")
    add("Qual escriba fiel registrou as palavras ditadas por Jeremias e o auxiliou fielmente?",
        "Baruque, filho de Nerias", "Esdras", "Seraías", "Gedalias",
        "facil", "Jeremias", "Jeremias 36:4", "Jeremias chamou a Baruque, filho de Nerias; e escreveu Baruque no rolo de um livro todas as palavras do Senhor.")
    add("Qual governador de Judá nomeado pelos babilônios após a queda de Jerusalém foi assassinado por Ismael?",
        "Gedalias", "Zedequias", "Jeoaquim", "Pecá",
        "medio", "Jeremias", "Jeremias 40:7; 41:2", "Gedalias fora posto por governador da terra; mas Ismael se levantou com dez homens e o feriu à espada.")
    add("Para qual país os líderes rebeldes judeus fugiram à força levando Jeremias contra a expressa ordem divina?",
        "Egito (Tafnes)", "Assíria", "Moabe", "Roma",
        "medio", "Jeremias", "Jeremias 43:5-7", "Não obedeceram à voz do Senhor e foram para a terra do Egito, e chegaram a Tafnes.")
    add("Qual grande profecia contra a soberba babilônica ocupa os capítulos 50 e 51 de Jeremias?",
        "A queda inevitável de Babilônia perante as nações do norte", "A vitória eterna dos caldeus", "A construção do templo de Bel", "A expansão de Nínive",
        "facil", "Jeremias", "Jeremias 50:1-2", "'Anunciai entre as nações... Babilônia está tomada, Bel está confundido, Merodaque está despedaçado'.")
    add("O que Seraías fez com o rolo de profecias de Jeremias após lê-lo junto ao rio Eufrates?",
        "Atou-lhe uma pedra e lançou-o no meio do rio Eufrates dizendo: 'Assim se afundará Babilônia e não se levantará'", "Queimou-o no palácio", "Enterrou-o na areia", "Levou-o de volta a Jerusalém",
        "medio", "Jeremias", "Jeremias 51:63-64", "Quando acabares de ler este livro, atar-lhe-ás uma pedra e o lançarás no meio do Eufrates, como símbolo da queda da Babilônia.")
    add("Qual sacerdote e profeta teve visões de querubins com quatro asas e rodas que se moviam com o espírito?",
        "Ezequiel", "Jeremias", "Isaías", "Ageu",
        "facil", "Ezequiel", "Ezequiel 10:9-12", "Ezequiel contemplou as rodas e os querubins cuja glória e mobilidade refletiam a presença do Deus vivo.")
    add("O que representavam as duas varas unidas numa só mão profetizadas em Ezequiel 37:16-19?",
        "A unificação futura das tribos de Judá e de José (Israel) sob um só Rei e Pastor", "A aliança entre Roma e Pérsia", "Duas armas de guerra", "Dois sacerdócios rivais",
        "medio", "Ezequiel", "Ezequiel 37:19-24", "Deus fará de Judá e Efraim uma só nação sobre os montes de Israel, com um só Pastor e Rei.")
    add("Contra qual príncipe de Tiro Ezequiel profetiza denunciando seu orgulho de querer ser como Deus em Ez 28?",
        "O príncipe e rei de Tiro, comparado à queda de um querubim ungido da guarda", "O faraó do Egito", "O rei de Moabe", "O general da Síria",
        "medio", "Ezequiel", "Ezequiel 28:2; 12-14", "Diz o Senhor ao príncipe de Tiro: 'Visto que o teu coração se elevou e disseste: Eu sou um deus... serás derribado'.")
    add("Em qual visão Ezequiel viu uma cana de medir de seis côvados e a planta do novo santuário de Deus?",
        "Ezequiel capítulo 40", "Ezequiel capítulo 1", "Ezequiel capítulo 12", "Ezequiel capítulo 20",
        "dificil", "Ezequiel", "Ezequiel 40:3-5", "Um homem cujo aspecto era como de bronze tinha um cordel de linho e uma cana de medir para medir o futuro templo.")
    add("Por que Daniel recusou comer as carnes e vinhos da mesa de Nabucodonosor?",
        "Para não se contaminar com alimentos consagrados aos ídolos e proibidos pela Lei", "Porque era vegetariano por gosto pessoal", "Porque desconfiava de veneno", "Porque estava em greve de fome",
        "facil", "Daniel", "Daniel 1:8", "Daniel propôs no seu coração não se contaminar com a porção das iguarias do rei, nem com o vinho que ele bebia.")
    add("Quantas vezes ao dia Daniel se ajoelhava em seu quarto em oração voltado para Jerusalém?",
        "Três vezes ao dia", "Sete vezes ao dia", "Uma vez ao dia", "Cinco vezes ao dia",
        "facil", "Daniel", "Daniel 6:10", "Três vezes ao dia se punha de joelhos, e orava, e dava graças diante do seu Deus, como também antes costumava fazer.")
    add("Quem governava a Babilônia quando ocorreu a misteriosa escrita na parede 'Mene, Mene, Tequel, Parsim'?",
        "Belsazar", "Nabucodonosor", "Ciro", "Dario",
        "facil", "Daniel", "Daniel 5:1", "O rei Belsazar deu um grande banquete a mil dos seus grandes, usando os vasos de ouro do templo de Jerusalém.")
    add("Qual profeta dos doze menores profetizou o julgamento e a destruição definitiva da cidade de Nínive com poemas bélicos vívidos?",
        "Naum", "Jonas", "Ageu", "Malaquias",
        "medio", "Naum", "Naum 1:1; 3:1-7", "O livro de Naum profetiza a ruína da sanguinária Nínive, capital do Império Assírio.")
    add("Qual foi a perplexidade inicial do profeta Habacuque perante Deus no capítulo 1?",
        "Por que Deus usaria os caldeus (babilônios), um povo ainda mais ímpio e cruel, para castigar os pecados de Judá?", "Por que a chuva não caía nos campos", "Por que não havia mais sacerdotes", "Por que o templo era pequeno",
        "medio", "Habacuque", "Habacuque 1:12-13", "Habacuque indaga: 'Tu és tão puro de olhos que não podes ver o mal... por que te calas quando o ímpio devora o que é mais justo do que ele?'.")
    add("Sobre qual torre de vigia o profeta Habacuque se postou para ouvir o que Deus lhe diria?",
        "Sobre a fortaleza / torre de sentinela", "Sobre o monte Sinai", "Sobre os muros de Samaria", "Junto ao mar da Galileia",
        "facil", "Habacuque", "Habacuque 2:1", "'Pôr-me-ei na minha torre de vigia e colocar-me-ei sobre a fortaleza, e vigiarei para ver o que ele me dirá'.")
    add("O que o profeta Sofonias enfatiza com veemência em sua mensagem profética?",
        "A iminência e o terror do 'Grande Dia do Senhor' contra toda a idolatria", "A vitória militar do Egito", "A restauração imediata de Tiro", "A coroação de novos reis",
        "medio", "Sofonias", "Sofonias 1:14-15", "'O grande dia do Senhor está perto, está perto e se apressa muito... dia de indignação é aquele dia'.")
    add("Qual líder civil governava Judá na época em que Ageu e Zacarias profetizaram reconstruir o templo?",
        "Zorobabel, filho de Sealtiel", "Neemias", "Esdras", "Mardoqueu",
        "facil", "Ageu", "Ageu 1:1", "Veio a palavra do Senhor por intermédio do profeta Ageu a Zorobabel, governador de Judá, e a Josué, o sumo sacerdote.")
    add("Qual visão de quatro cavalos patrulhando a terra Zacarias teve entre as murteiras no capítulo 1?",
        "Um cavalo vermelho, e atrás dele cavalos vermelhos, baios e brancos que patrulhavam a terra em paz", "Quatro cavalos alados de ouro", "Dois cavalos de ferro e dois de bronze", "Cavalos que devoravam montanhas",
        "medio", "Zacarias", "Zacarias 1:8-11", "Um homem montado num cavalo vermelho entre as murteiras liderava os patrulheiros celestes da terra.")
    add("Quem estava em pé à direita de Josué, o sumo sacerdote, para se lhe opor na visão de Zacarias 3?",
        "Satanás para acusá-lo diante do Anjo do Senhor", "O rei da Pérsia", "Um soldado de Samaria", "Um falso profeta",
        "medio", "Zacarias", "Zacarias 3:1", "Ele me mostrou o sumo sacerdote Josué, e Satanás estava à sua mão direita para se lhe opor; mas o Senhor o repreendeu.")
    add("O que o Anjo do Senhor mandou fazer com as vestes de Josué em Zacarias 3:4-5?",
        "Tirar as suas vestes sujas, vesti-lo de trajes festivos limpos e pôr-lhe uma mitra limpa sobre a cabeça", "Rasgar suas roupas de sacerdote", "Cobri-lo de cinzas", "Descalçar seus sapatos",
        "facil", "Zacarias", "Zacarias 3:4-5", "'Tirai-lhe estas vestes sujas... eis que fiz passar de ti a tua iniquidade e te vestirei de trajes nobres e porás uma mitra limpa'.")
    add("O que Zacarias profetizou sobre os falsos profetas em Zacarias 13:4?",
        "Terão vergonha das suas visões e não mais vestirão manto de pelos para enganar", "Serão coroados reis", "Construirão seus próprios altares", "Fugirão para a Babilônia",
        "dificil", "Zacarias", "Zacarias 13:4", "Naquele dia os profetas se envergonharão cada um de sua visão quando profetizarem, e não vestirão mais manto de pelos.")
    add("Onde os pés do Senhor pousarão na batalha final profetizada em Zacarias 14:4?",
        "Sobre o Monte das Oliveiras, que se fenderá pelo meio", "Sobre o monte Sinai", "Sobre o monte Carmelo", "Nas margens do rio Jordão",
        "medio", "Zacarias", "Zacarias 14:4", "'Naquele dia estarão os seus pés sobre o monte das Oliveiras, que está defronte de Jerusalém para o oriente; e o monte se fenderá pelo meio'.")
    add("O que Malaquias 1:11 profetiza sobre a adoração mundial ao Nome do Senhor entre as nações gentias?",
        "'Desde o nascente do sol até ao poente é grande o meu nome entre as nações, e em todo lugar se oferecerá incenso puro'", "'Apenas em Jerusalém se adorará ao Senhor'", "'Nenhum gentio conhecerá a Deus'", "'O templo de Sião será o único santuário'",
        "facil", "Malaquias", "Malaquias 1:11", "'Porque desde o nascente do sol até ao poente é grande entre as nações o meu nome; e em todo o lugar se oferecerá ao meu nome incenso e uma oferta pura'.")
    add("Qual repreensão severa Malaquias fez aos sacerdotes sobre os animais oferecidos em sacrifício no capítulo 1?",
        "Ofereciam animais cegos, coxos e enfermos sobre o altar que nem sequer o governador aceitaria", "Não ofereciam vinho suficiente", "Cobravam taxas muito baixas", "Não limpavam o altar de incenso",
        "medio", "Malaquias", "Malaquias 1:8", "'Quando ofereceis animal cego para o sacrifício, isso não é mau? E quando ofereceis o coxo ou enfermo, isso não é mau? Apresenta-o ao teu governador'.")
    add("O que Deus abomina expressamente em Malaquias 2:16 a respeito da união conjugal?",
        "O repúdio / divórcio injusto que cobre de violência as vestes", "O trabalho da mulher no campo", "O casamento com levitas", "A educação dos filhos na lei",
        "medio", "Malaquias", "Malaquias 2:16", "'Pois o Senhor, o Deus de Israel, diz que odeia o repúdio (divórcio)... guardai-vos pois em vosso espírito e não sejais desleais'.")
    add("Qual promessa de bênção abundante Deus faz aos que trazem todos os dízimos em Malaquias 3:10?",
        "'Abrirei as janelas do céu e derramarei sobre vós bênção tal que dela vos advenha a maior abastança'", "'Enviarei carruagens de prata'", "'Não precisareis mais plantar'", "'Vossos inimigos vos pagarão tributos'",
        "facil", "Malaquias", "Malaquias 3:10", "'Trazei todos os dízimos à casa do tesouro... e provai-me nisto, diz o Senhor, se eu não vos abrir as janelas do céu'.")
    add("Quem Deus promete repreender por amor dos dizimistas fiéis em Malaquias 3:11?",
        "O devorador (as pragas que destroem o fruto da terra)", "Os governadores injustos", "Os mercadores estrangeiros", "Os ladrões de gado",
        "facil", "Malaquias", "Malaquias 3:11", "'E por causa de vós repreenderei o devorador, e ele não destruirá os frutos da vossa terra; nem a vossa vide no campo lançará o seu fruto antes do tempo'.")
    add("O que foi escrito perante o Senhor para aqueles que temem o Seu Nome em Malaquias 3:16?",
        "Um Memorial / Livro de Memórias", "Um decreto de guerra", "Uma tábua de julgamento", "Um testamento de ouro",
        "facil", "Malaquias", "Malaquias 3:16", "'O Senhor atentou e ouviu; e um memorial foi escrito diante dele, para os que temeram o Senhor, e para os que lembraram do seu nome'.")
    add("O que acontecerá no Dia do Senhor aos que praticam a soberba segundo Malaquias 4:1?",
        "Serão como restolho consumido pelo fogo, sem lhes deixar nem raiz nem ramo", "Fugirão para as ilhas do mar", "Serão exilados em Roma", "Ficarão ocultos nas grutas",
        "medio", "Malaquias", "Malaquias 4:1", "'Pois eis que aquele dia vem ardendo como fornalha; todos os soberbos e todos os que cometem impiedade serão como palha; e o dia que vem os abrasará'.")
    add("Qual livro da Lei de Moisés o povo é mandado lembrar no encerramento de Malaquias no capítulo 4:4?",
        "A Lei de Moisés com seus estatutos e juízos dados em Horebe", "O livro das guerras do Senhor", "Os provérbios de Salomão", "As crônicas dos reis de Judá",
        "facil", "Malaquias", "Malaquias 4:4", "'Lembrai-vos da lei de Moisés, meu servo, a qual lhe mandei em Horebe para todo o Israel, a saber, estatutos e juízos'.")
    add("Qual é o livro profético que contém a visão da glória de Deus deixando o templo?",
        "Ezequiel", "Isaías", "Jeremias", "Daniel",
        "facil", "Ezequiel", "Ezequiel 10:18", "O profeta Ezequiel registrou com detalhes a visão da partida da glória do Senhor dos querubins do templo.")
    add("Qual profeta viu os anjos celestiais com tenazes tirando uma brasa do altar?",
        "Isaías", "Daniel", "Ezequiel", "Zacarias",
        "facil", "Isaías", "Isaías 6:6", "Isaías contemplou os serafins diante do trono de Deus tirando a brasa viva do altar.")

    return items[:150]

if __name__ == "__main__":
    q_list = get_prophets_questions()
    print(f"Prophets generated: {len(q_list)} questions")
