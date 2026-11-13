# -*- coding: utf-8 -*-
"""
Pentateuco: 160 questões de Gênesis a Deuteronômio
"""

def get_pentateuch_questions():
    items = []
    def add(q, c, w1, w2, w3, diff, book, ref, exp):
        items.append({
            "q": q, "c": c, "w1": w1, "w2": w2, "w3": w3,
            "diff": diff, "book": book, "testament": "VT",
            "section": "Pentateuco", "ref": ref, "exp": exp
        })

    # --- GÊNESIS (70 questões) ---
    add("Qual foi a primeira coisa criada no primeiro dia da criação segundo Gênesis 1?",
        "A luz", "O sol e a lua", "A terra firme", "As estrelas",
        "facil", "Gênesis", "Gênesis 1:3", "Deus disse: 'Haja luz', e houve luz no primeiro dia.")
    add("Em qual dia da criação foram estabelecidos o sol, a lua e as estrelas?",
        "Quarto dia", "Primeiro dia", "Terceiro dia", "Sexto dia",
        "medio", "Gênesis", "Gênesis 1:14-19", "No quarto dia Deus fez os luminares celestes para governarem o dia e a noite.")
    add("Em qual dia da criação os peixes e as aves foram criados?",
        "Quinto dia", "Quarto dia", "Terceiro dia", "Sexto dia",
        "medio", "Gênesis", "Gênesis 1:20-23", "No quinto dia Deus criou os seres marinhos e as aves do céu.")
    add("Em qual dia da criação foram criados o homem e os animais terrestres?",
        "Sexto dia", "Quinto dia", "Sétimo dia", "Quarto dia",
        "facil", "Gênesis", "Gênesis 1:26-31", "Deus fez os animais terrestres e criou o homem à Sua imagem no sexto dia.")
    add("O que Deus fez no sétimo dia após findar Sua criação?",
        "Descansou e o santificou", "Criou os anjos", "Edificou um tabernáculo", "Separou as nações",
        "facil", "Gênesis", "Gênesis 2:2-3", "Havendo Deus terminado no sétimo dia a sua obra, descansou e o santificou.")
    add("De que matéria o Senhor Deus formou o primeiro homem, Adão?",
        "Do pó da terra", "Da argila sagrada", "Da rocha bruta", "Da água do mar",
        "facil", "Gênesis", "Gênesis 2:7", "O Senhor Deus formou o homem do pó da terra e soprou-lhe nas narinas o fôlego da vida.")
    add("De qual parte do corpo de Adão Deus formou a mulher?",
        "De uma de suas costelas", "Do seu ombro", "Do seu coração", "Da sua mão",
        "facil", "Gênesis", "Gênesis 2:21-22", "Deus fez cair pesado sono sobre o homem e da costela dele formou a mulher.")
    add("Qual rio NÃO saía do jardim do Éden segundo Gênesis 2?",
        "Rio Jordão", "Rio Pisom", "Rio Giom", "Rio Eufrates",
        "medio", "Gênesis", "Gênesis 2:10-14", "Os quatro rios eram Pisom, Giom, Tigre e Eufrates. O Jordão não pertencia ao Éden.")
    add("Qual árvore no Éden tinha seu fruto proibido sob pena de morte?",
        "A árvore do conhecimento do bem e do mal", "A árvore da vida", "A videira dourada", "A figueira de prata",
        "facil", "Gênesis", "Gênesis 2:17", "'Da árvore do conhecimento do bem e do mal, dela não comerás, porque no dia em que dela comeres morrerás'.")
    add("Qual animal foi usado pelo tentador para enganar Eva?",
        "A serpente", "O leão", "O escorpião", "O dragão alado",
        "facil", "Gênesis", "Gênesis 3:1", "A serpente era mais astuta que todos os animais selvagens que o Senhor Deus tinha feito.")
    add("O que Adão e Eva costuraram para cobrir a sua nudez após pecarem?",
        "Folhas de figueira", "Peles de carneiro", "Fibras de linho", "Folhas de oliveira",
        "facil", "Gênesis", "Gênesis 3:7", "Coseram folhas de figueira e fizeram aventais para cobrir sua nudez.")
    add("Com o que Deus vestiu Adão e Eva antes de expulsá-los do jardim?",
        "Túnicas de peles de animais", "Mantos de linho alvo", "Vestes de lã pura", "Tecidos de algodão",
        "medio", "Gênesis", "Gênesis 3:21", "Fez o Senhor Deus túnicas de peles para Adão e sua mulher, e os vestiu.")
    add("Quem guardava o caminho da árvore da vida a oriente do Éden?",
        "Querubins com uma espada flamejante", "Serafins com escudos", "Arcanjos com lanças", "Uma coluna de fogo",
        "medio", "Gênesis", "Gênesis 3:24", "Deus pôs querubins a oriente e uma espada inflamada que se revolvia para guardar o caminho.")
    add("Qual era a ocupação de Caim e de Abel?",
        "Caim era lavrador da terra e Abel, pastor de ovelhas", "Caim era pastor e Abel, lavrador", "Abel era ferreiro e Caim, caçador", "Ambos cuidavam de vinhas",
        "facil", "Gênesis", "Gênesis 4:2", "Abel foi pastor de ovelhas, e Caim foi lavrador da terra.")
    add("Por que Caim matou seu irmão Abel?",
        "Porque Deus se agradou da oferta de Abel e não da sua", "Por disputa de rebanhos", "Por ciúme de terras férteis", "Por causa da herança paterna",
        "facil", "Gênesis", "Gênesis 4:4-5", "Atentou o Senhor para Abel e sua oferta, mas para Caim e sua oferta não atentou.")
    add("Para qual terra Caim partiu após cometer o homicídio?",
        "Terra de Node", "Terra de Canaã", "Terra de Havilá", "Terra de Ur",
        "dificil", "Gênesis", "Gênesis 4:16", "Saiu Caim de diante do Senhor e habitou na terra de Node, ao oriente do Éden.")
    add("Quem foi o terceiro filho nominal de Adão e Eva, nascido após a morte de Abel?",
        "Sete", "Enos", "Matusalém", "Jarede",
        "facil", "Gênesis", "Gênesis 4:25", "Eva deu à luz um filho e lhe chamou Sete, dizendo: 'Deus me deu outro filho em lugar de Abel'.")
    add("Quem andou com Deus e não viu a morte, pois Deus o tomou para Si?",
        "Enoque", "Noé", "Matusalém", "Lameque",
        "facil", "Gênesis", "Gênesis 5:24", "Enoque andou com Deus e já não foi encontrado, porque Deus o levou.")
    add("Quantos anos viveu Matusalém, a pessoa mais idosa mencionada na Bíblia?",
        "969 anos", "930 anos", "950 anos", "895 anos",
        "facil", "Gênesis", "Gênesis 5:27", "Foram todos os dias de Matusalém 969 anos; e morreu.")
    add("Quais eram os três filhos de Noé que entraram na arca?",
        "Sem, Cam e Jafé", "Caim, Abel e Sete", "Abraão, Naor e Harã", "Esaú, Jacó e José",
        "facil", "Gênesis", "Gênesis 6:10", "Noé gerou três filhos: Sem, Cam e Jafé.")
    add("De qual madeira Deus ordenou que Noé construísse a arca?",
        "Madeira de gôfer (cipreste)", "Cedro do Líbano", "Madeira de acácia", "Carvalho de Basã",
        "medio", "Gênesis", "Gênesis 6:14", "Deus disse: 'Faze para ti uma arca da madeira de gôfer'.")
    add("Quantas pessoas foram salvas na arca de Noé durante o dilúvio?",
        "8 pessoas", "6 pessoas", "10 pessoas", "12 pessoas",
        "facil", "Gênesis", "Gênesis 7:13; 1 Pedro 3:20", "Salvaram-se 8 pessoas: Noé, seus três filhos e suas respectivas esposas.")
    add("Quantos dias e noites choveu ininterruptamente no dilúvio?",
        "40 dias e 40 noites", "7 dias e 7 noites", "150 dias", "120 dias",
        "facil", "Gênesis", "Gênesis 7:12", "Caiu chuva sobre a terra quarenta dias e quarenta noites.")
    add("Onde a arca de Noé repousou após as águas do dilúvio minguarem?",
        "Nos montes de Ararate", "No monte Sinai", "No monte Carmelo", "No monte Nebo",
        "facil", "Gênesis", "Gênesis 8:4", "A arca repousou sobre os montes de Ararate no sétimo mês.")
    add("Qual foi a primeira ave que Noé soltou da arca?",
        "Um corvo", "Uma pomba", "Uma andorinha", "Uma águia",
        "medio", "Gênesis", "Gênesis 8:7", "Noé soltou um corvo, que saía, indo e voltando até secarem as águas.")
    add("O que a pomba trouxe no bico na segunda vez que Noé a soltou?",
        "Uma folha fresca de oliveira", "Um ramo de videira", "Uma espiga de trigo", "Uma pedra seca",
        "facil", "Gênesis", "Gênesis 8:11", "A pomba voltou à tarde trazendo no bico uma folha de oliveira recém-colhida.")
    add("Qual foi o sinal colocado por Deus nas nuvens como aliança do dilúvio?",
        "O arco-íris", "Uma coluna de fogo", "Uma estrela cadente", "Um cometa dourado",
        "facil", "Gênesis", "Gênesis 9:13", "Deus pôs o arco nas nuvens como sinal da perpétua aliança de paz.")
    add("Quem era o caçador vigoroso na terra e fundador de Babel?",
        "Ninrode", "Canaã", "Mizraim", "Quir",
        "medio", "Gênesis", "Gênesis 10:8-10", "Ninrode começou a ser poderoso na terra; o princípio do seu reino foi Babel.")
    add("Por que Deus confundiu a língua dos homens em Babel?",
        "Para conter a soberba e dispersá-los pela terra", "Porque adoravam o fogo", "Porque se recusaram a plantar", "Porque faziam armas de bronze",
        "facil", "Gênesis", "Gênesis 11:7-8", "Deus desceu e confundiu a linguagem deles para impedir sua presunção e espalhá-los.")
    add("De qual cidade Deus chamou Abrão com a ordem: 'Sai da tua terra'?",
        "Ur dos Caldeus", "Babilônia", "Damasco", "Nínive",
        "facil", "Gênesis", "Gênesis 11:31; 12:1", "Abrão habitava em Ur dos Caldeus e dali partiu rumo a Canaã.")
    add("Quantos anos tinha Abrão quando partiu de Harã obedecendo ao Senhor?",
        "75 anos", "50 anos", "80 anos", "100 anos",
        "medio", "Gênesis", "Gênesis 12:4", "Tinha Abrão setenta e cinco anos quando saiu de Harã.")
    add("Quem era o sobrinho de Abrão que viajou com ele e depois habitou perto de Sodoma?",
        "Ló", "Labão", "Eliezer", "Naor",
        "facil", "Gênesis", "Gênesis 13:11-12", "Ló escolheu para si toda a planície do Jordão e armou suas tendas até Sodoma.")
    add("Quem era o rei de Salém e sacerdote do Deus Altíssimo que serviu pão e vinho a Abraão?",
        "Melquisedeque", "Abimeleque", "Potifar", "Ficol",
        "facil", "Gênesis", "Gênesis 14:18", "Melquisedeque, rei de Salém e sacerdote do Deus Altíssimo, trouxe pão e vinho e o abençoou.")
    add("O que Abraão entregou a Melquisedeque de tudo o que havia recuperado?",
        "O dízimo (a décima parte)", "A metade", "Dois terços", "Uma oferta de ouro puro",
        "facil", "Gênesis", "Gênesis 14:20", "E Abrão deu-lhe o dízimo de tudo.")
    add("Qual era a nacionalidade e nome da serva de Sara que deu à luz Ismael?",
        "Hagar, egípcia", "Zilpa, cananeia", "Bila, siríaca", "Quetura, moabita",
        "facil", "Gênesis", "Gênesis 16:1-3", "Sarai tinha uma serva egípcia chamada Hagar, que gerou Ismael.")
    add("Com quantos anos Abraão foi circuncidado ao ratificar a aliança?",
        "99 anos", "75 anos", "85 anos", "100 anos",
        "medio", "Gênesis", "Gênesis 17:24", "Abraão tinha noventa e nove anos de idade quando foi circuncidado.")
    add("Qual é o significado do nome Isaque?",
        "'Ele ri' ou 'riso'", "'Filho amado'", "'Príncipe de Deus'", "'O consolador'",
        "medio", "Gênesis", "Gênesis 17:19; 21:6", "O nome Isaque deriva do hebraico para riso, por causa da incredulidade e júbilo de Sara.")
    add("Por quantos justos Deus prometeu poupar a cidade de Sodoma no diálogo com Abraão?",
        "10 justos", "50 justos", "20 justos", "5 justos",
        "medio", "Gênesis", "Gênesis 18:32", "Disse o Senhor: 'Não a destruirei por amor dos dez'.")
    add("Em que a esposa de Ló se converteu ao olhar para trás durante a destruição de Sodoma?",
        "Numa estátua de sal", "Num pilar de cinzas", "Num bloco de granito", "Num monte de enxofre",
        "facil", "Gênesis", "Gênesis 19:26", "A mulher de Ló olhou para trás e converteu-se numa estátua de sal.")
    add("Qual era a idade de Abraão quando seu filho Isaque nasceu?",
        "100 anos", "80 anos", "90 anos", "120 anos",
        "facil", "Gênesis", "Gênesis 21:5", "Abraão tinha cem anos de idade quando lhe nasceu Isaque, seu filho.")
    add("Em qual monte Abraão foi provado para oferecer Isaque em sacrifício?",
        "Monte Moriá", "Monte Sinai", "Monte Nebo", "Monte Carmelo",
        "medio", "Gênesis", "Gênesis 22:2", "Deus disse: 'Vai-te à terra de Moriá e oferece-o ali em holocausto'.")
    add("O que Deus proveu preso no matagal para ser sacrificado em lugar de Isaque?",
        "Um carneiro preso pelos chifres", "Um novilho manso", "Uma pomba alva", "Um cordeiro sem mancha",
        "facil", "Gênesis", "Gênesis 22:13", "Abraão viu um carneiro preso no matagal pelos chifres e o ofereceu em holocausto.")
    add("Qual nome Abraão deu ao monte Moriá em comemoração ao livramento de Deus?",
        "Jeová-Jiré (O Senhor Proverá)", "El-Shaddai", "Jeová-Nissi", "Ebenézer",
        "facil", "Gênesis", "Gênesis 22:14", "Chamou Abraão o nome daquele lugar O Senhor Proverá (Jeová-Jiré).")
    add("Onde Abraão comprou uma cova para sepultar sua falecida esposa Sara?",
        "Na cova de Macpela, em Hebrom", "No vale de Cedrom", "Em Betel", "Na colina de Siquém",
        "medio", "Gênesis", "Gênesis 23:19", "Abraão sepultou Sara na cova do campo de Macpela, defronte de Manre (Hebrom).")
    add("Quem era o servo mais antigo de Abraão que buscou esposa para Isaque?",
        "Eliezer de Damasco", "Ziba", "Geazi", "Urias",
        "medio", "Gênesis", "Gênesis 15:2; 24:2", "Eliezer de Damasco era o servo responsável por toda a casa de Abraão.")
    add("Qual donzela ofereceu água ao servo de Abraão e saciou a sede de seus camelos?",
        "Rebeca", "Raquel", "Lia", "Zípora",
        "facil", "Gênesis", "Gênesis 24:15-19", "Rebeca desceu à fonte, encheu seu cântaro e deu de beber também a todos os camelos.")
    add("Quem foi a segunda esposa de Abraão após a morte de Sara, mãe de vários filhos?",
        "Quetura", "Hagar", "Zilpa", "Bila",
        "dificil", "Gênesis", "Gênesis 25:1-2", "Abraão tomou outra mulher, cujo nome era Quetura.")
    add("Quais filhos gêmeos nasceram de Isaque e Rebeca?",
        "Esaú e Jacó", "Efraim e Manassés", "Fares e Zara", "José e Benjamim",
        "facil", "Gênesis", "Gênesis 25:24-26", "Nasceram gêmeos: o primeiro ruivo e peludo (Esaú) e o segundo segurando o calcanhar (Jacó).")
    add("Por que refeição Esaú vendeu a Jacó seu direito de primogenitura?",
        "Um prato de guisado de lentilhas vermelhas", "Carne assada de cordeiro", "Pão e taça de vinho doce", "Peixe com figos",
        "facil", "Gênesis", "Gênesis 25:34", "Jacó deu a Esaú pão e o guisado de lentilhas, e este desprezou sua primogenitura.")
    add("Como Jacó enganou seu idoso pai Isaque para receber a bênção patriarcal?",
        "Cobriu as mãos e o pescoço com peles de cabrito e vestiu as roupas de Esaú", "Imitou a voz do irmão no escuro", "Disse que Esaú havia morrido no campo", "Ofereceu-lhe um cálice de vinho embriagador",
        "medio", "Gênesis", "Gênesis 27:15-16", "Rebeca cobriu as mãos e a lisura do pescoço de Jacó com peles de cabritos para simular a pelugem de Esaú.")
    add("O que Jacó viu em sonho no lugar que denominou Betel?",
        "Uma escada apoiada na terra cujo cume tocava os céus e anjos subindo e descendo", "Um carro de fogo puxado por cavalos", "Doze estrelas cadentes", "Um grande trono de marfim",
        "facil", "Gênesis", "Gênesis 28:12", "Jacó sonhou com uma escada cujo cume tocava o céu e os anjos de Deus subiam e desciam por ela.")
    add("Quantos anos no total Jacó trabalhou para Labão pelas filhas Lia e Raquel?",
        "14 anos (7 anos por cada uma)", "7 anos", "20 anos", "10 anos",
        "medio", "Gênesis", "Gênesis 29:18-30", "Jacó trabalhou 7 anos por Raquel, recebeu Lia enganado, e serviu mais 7 anos por Raquel.")
    add("Quem foi o filho primogênito de Jacó com Lia?",
        "Rúben", "Simeão", "Levi", "Judá",
        "facil", "Gênesis", "Gênesis 29:32", "Concebeu Lia e deu à luz um filho e lhe chamou Rúben.")
    add("Qual filho de Jacó recebeu a promessa de que o cetro não se arredaria de sua linhagem?",
        "Judá", "Rúben", "José", "Levi",
        "facil", "Gênesis", "Gênesis 49:10", "'O cetro não se arredará de Judá, nem o bastão de entre seus pés, até que venha Siló'.")
    add("Quem era a única filha nominal de Jacó descrita em Gênesis?",
        "Diná", "Miriã", "Tamar", "Acsa",
        "medio", "Gênesis", "Gênesis 30:21", "Depois disto deu à luz uma filha, e chamou-lhe Diná.")
    add("O que Raquel furtou de seu pai Labão ao fugirem para Canaã?",
        "Os ídolos domésticos (terafins)", "As joias da família", "Os títulos de terra", "As vestes sagradas",
        "medio", "Gênesis", "Gênesis 31:19", "Raquel furtou os terafins que pertenciam a seu pai Labão.")
    add("Onde Jacó lutou com o Anjo do Senhor até o despontar da aurora?",
        "No vau do ribeiro de Jaboque (Peniel)", "No monte Horebe", "No monte Carmelo", "No deserto de Parã",
        "facil", "Gênesis", "Gênesis 32:22-30", "Ficou Jacó só; e lutava com ele um homem até ao romper do dia no ribeiro de Jaboque.")
    add("Qual novo nome Jacó recebeu após prevalecer na luta espiritual em Peniel?",
        "Israel", "Betel", "Judá", "Melquisedeque",
        "facil", "Gênesis", "Gênesis 32:28", "'Não se chamará mais o teu nome Jacó, mas Israel; pois lutaste com Deus e com os homens e prevaleceste'.")
    add("Qual foi a sequela física que Jacó levou da luta com o Anjo?",
        "Passou a mancar da juntura da coxa", "Ficou cego do olho direito", "Perdeu o movimento do braço", "Ficou mudo temporariamente",
        "medio", "Gênesis", "Gênesis 32:25-31", "O anjo tocou a articulação da coxa de Jacó, que se deslocou, fazendo-o manquejar.")
    add("Qual presente Jacó deu a José que despertou ciúme de seus irmãos?",
        "Uma túnica talar de mangas compridas e várias cores", "Um arco de caça dourado", "Um anel de prata", "Um cajado de cedro",
        "facil", "Gênesis", "Gênesis 37:3", "Israel amava José mais do que a todos os seus filhos e fez-lhe uma túnica de várias cores.")
    add("Por quanto os irmãos venderam José aos mercadores ismaelitas?",
        "20 siclos de prata", "30 siclos de prata", "50 siclos de prata", "10 siclos de ouro",
        "medio", "Gênesis", "Gênesis 37:28", "Tiraram José da cova e o venderam por vinte moedas de prata aos ismaelitas.")
    add("Quem comprou José no Egito e o colocou sobre sua casa?",
        "Potifar, capitão da guarda de Faraó", "Potífera, sacerdote de Om", "Ficol, capitão do exército", "Janes, mago do palácio",
        "facil", "Gênesis", "Gênesis 39:1", "Potifar, oficial de Faraó e capitão da guarda, comprou-o dos ismaelitas.")
    add("O que José deixou nas mãos da mulher de Potifar ao fugir da tentação moral?",
        "Sua capa/veste", "Seu anel de selar", "Suas sandálias", "Seu cajado",
        "facil", "Gênesis", "Gênesis 39:12", "Ela o pegou pela capa... mas ele, deixando a capa na mão dela, fugiu para fora.")
    add("Qual dos servos de Faraó na prisão foi enforcado após três dias, segundo o sonho?",
        "O padeiro-chefe", "O copeiro-chefe", "O tesoureiro real", "O cozinheiro do rei",
        "medio", "Gênesis", "Gênesis 40:19-22", "Como José interpretara, ao terceiro dia Faraó mandou enforcar o padeiro-chefe.")
    add("O que significavam as sete vacas magras que devoravam as sete gordas no sonho de Faraó?",
        "Sete anos de fome extrema após sete anos de grande fartura", "Sete exércitos inimigos que atacariam o Nilo", "Sete enchentes destrutivas", "Sete reis iníquos",
        "facil", "Gênesis", "Gênesis 41:29-30", "José explicou que viriam 7 anos de grande fartura seguidos por 7 anos de fome severa.")
    add("Qual era a idade de José ao ser nomeado governador do Egito?",
        "30 anos", "20 anos", "40 anos", "25 anos",
        "medio", "Gênesis", "Gênesis 41:46", "Era José da idade de trinta anos quando se apresentou perante Faraó, rei do Egito.")
    add("Quais eram os dois filhos de José abençoados pelo avô Jacó?",
        "Manassés e Efraim", "Nadabe e Abiú", "Gérson e Eliezer", "Fares e Zara",
        "facil", "Gênesis", "Gênesis 41:51-52; 48:1", "José chamou ao primogênito Manassés e ao segundo Efraim.")
    add("Qual região do Egito foi concedida aos familiares de Jacó para habitarem com rebanhos?",
        "A terra de Gósen", "A cidade de Tebas", "O delta de Mênfis", "A planície de Alexandria",
        "facil", "Gênesis", "Gênesis 47:6", "Faraó disse: 'No melhor da terra faze habitar teu pai e teus irmãos; habitem na terra de Gósen'.")
    add("Qual juramento José exigiu de seus irmãos com respeito aos seus ossos?",
        "Que levassem seus ossos quando Deus visitasse o povo para tirá-los do Egito", "Que construíssem uma pirâmide no deserto", "Que os queimassem no altar de Betel", "Que fossem jogados no mar Vermelho",
        "medio", "Gênesis", "Gênesis 50:24-25", "José fez os filhos de Israel jurarem: 'Deus certamente vos visitará, e fareis transportar os meus ossos daqui'.")

    # --- ÊXODO (45 questões) ---
    add("Qual ordem mortal o Faraó deu às parteiras sobre os bebês hebreus?",
        "Que matassem todo recém-nascido do sexo masculino", "Que escravizassem as meninas", "Que levassem os bebês para o templo de Rá", "Que expulsassem as mães",
        "facil", "Êxodo", "Êxodo 1:16", "Disse Faraó às parteiras: 'Se for filho, matai-o; mas se for filha, viva'.")
    add("Quem vigiou o cesto do menino Moisés à beira do rio Nilo?",
        "Sua irmã Miriã", "Sua mãe Joquebede", "Zípora", "Sifrá",
        "facil", "Êxodo", "Êxodo 2:4", "Sua irmã postou-se de longe, para ver o que haveria de acontecer com ele.")
    add("Quem recolheu o cesto de Moisés no Nilo e o adotou como filho?",
        "A filha de Faraó", "A rainha egípcia", "A serva de Potifar", "Uma sacerdotisa do Nilo",
        "facil", "Êxodo", "Êxodo 2:5-10", "A filha de Faraó desceu para banhar-se no rio, viu o cesto, compadeceu-se da criança e o adotou.")
    add("Por que Moisés teve de fugir do Egito para a terra de Midiã?",
        "Porque matou um egípcio que feria um hebreu e o caso chegou aos ouvidos de Faraó", "Porque recusou adorar os deuses egípcios", "Porque liderou um motim de escravos", "Porque roubou ouro do tesouro",
        "facil", "Êxodo", "Êxodo 2:11-15", "Moisés feriu o feitor egípcio; sabendo que Faraó o procurava para matar, fugiu para Midiã.")
    add("Como Deus se manifestou a Moisés no monte Horebe quando o vocacionou?",
        "Numa chama de fogo do meio de uma sarça que não se consumia", "Num trovão estrondoso em céu limpo", "Numa suave brisa da tarde", "Numa chuva torrencial de granizo",
        "facil", "Êxodo", "Êxodo 3:2", "Apareceu-lhe o anjo do Senhor numa chama de fogo do meio de uma sarça que ardia sem ser consumida.")
    add("Qual o Nome eterno revelado por Deus a Moisés ao enviá-lo ao povo?",
        "'EU SOU O QUE SOU' (Yahweh)", "'O Deus dos Deuses'", "'O Criador dos Astros'", "'O Santo Guerreiro'",
        "facil", "Êxodo", "Êxodo 3:14", "Disse Deus a Moisés: 'EU SOU O QUE SOU'. E disse: 'Assim dirás aos filhos de Israel: EU SOU me enviou a vós'.")
    add("Quem foi designado por Deus para ser a voz e porta-voz de Moisés perante Faraó?",
        "Arão, seu irmão", "Josué", "Hur", "Calebe",
        "facil", "Êxodo", "Êxodo 4:14", "Deus disse que Arão o levita falava muito bem e seria a boca de Moisés.")
    add("Qual foi o primeiro milagre em que a vara de Arão se transformou perante Faraó?",
        "A vara transformou-se numa serpente que engoliu as varas dos magos", "Transformou-se numa espada dourada", "Brotou flores instantâneas", "Queimou em chamas azuis",
        "medio", "Êxodo", "Êxodo 7:10-12", "Arão lançou a sua vara diante de Faraó e ela se tornou em serpente; e a vara de Arão tragou as varas dos magos.")
    add("Qual foi a primeira praga com a qual Deus feriu as águas do Egito?",
        "Transformação das águas em sangue", "A invasão de rãs", "A infestação de piolhos", "A praga de moscas",
        "facil", "Êxodo", "Êxodo 7:20", "Arão feriu as águas do Nilo e todas as águas do rio se converteram em sangue.")
    add("Qual foi a segunda praga do Egito que invadiu as casas e os fornos de Faraó?",
        "A praga de rãs", "A praga de mosquitos", "A praga de úlceras", "A praga de gafanhotos",
        "facil", "Êxodo", "Êxodo 8:2-3", "As rãs subiram e cobriram a terra do Egito, entrando nas casas e câmaras de dormir.")
    add("Em qual praga os magos do Egito confessaram: 'Isto é o dedo de Deus'?",
        "Na terceira praga: piolhos/mosquitos do pó da terra", "Na praga das rãs", "Na praga do sangue", "Na praga das úlceras",
        "dificil", "Êxodo", "Êxodo 8:18-19", "Os magos tentaram com seus encantamentos produzir piolhos, mas não puderam, e disseram: 'Isto é o dedo de Deus'.")
    add("Qual foi a nona praga do Egito que durou três dias inteiros?",
        "Trevas densas e escuridão que se podia apalpar", "Chuva de pedras de fogo", "Gafanhotos devastadores", "Peste nos rebanhos",
        "facil", "Êxodo", "Êxodo 10:21-22", "Houve trevas espessas em toda a terra do Egito por três dias; ninguém viu o outro.")
    add("Qual foi a décima e decisiva praga enviada sobre o Egito?",
        "A morte de todos os primogênitos", "A destruição das colheitas por fogo", "A morte de todos os cavalos", "A cegueira dos sacerdotes",
        "facil", "Êxodo", "Êxodo 12:29", "À meia-noite o Senhor feriu todos os primogênitos na terra do Egito, desde o de Faraó até o do cativo.")
    add("Onde os israelitas deveriam passar o sangue do cordeiro da Páscoa?",
        "Nos dois umbrais e na verga superior da porta das casas", "Nas vestes de toda a família", "Nos altares do pátio", "Nas janelas das casas",
        "facil", "Êxodo", "Êxodo 12:7", "Tomarão do sangue e o porão em ambos os umbrais e na verga da porta das casas em que o comerem.")
    add("O que o anjo do Senhor fazia ao ver o sangue nas portas durante a noite da Páscoa?",
        "Passava por cima da casa sem ferir seus moradores", "Entrava para benzer os filhos", "Deixava uma bênção de ouro", "Acendia uma tocha protetora",
        "facil", "Êxodo", "Êxodo 12:13", "'Vendo eu o sangue, passarei por cima de vós, e não haverá entre vós praga para vos destruir'.")
    add("Como Deus conduzia os israelitas de dia e de noite pelo deserto?",
        "Numa coluna de nuvem de dia e numa coluna de fogo de noite", "Por estrelas guias e corvos alados", "Por três tochas acesas", "Por uma fumaça aromática de mirra",
        "facil", "Êxodo", "Êxodo 13:21", "O Senhor ia adiante deles de dia numa coluna de nuvem e de noite numa coluna de fogo.")
    add("Qual mar se dividiu para a passagem de Israel a pé enxuto?",
        "Mar Vermelho", "Mar Morto", "Mar da Galileia", "Mar Mediterrâneo",
        "facil", "Êxodo", "Êxodo 14:21-22", "Moisés estendeu a mão sobre o mar, e o mar se retirou; e os filhos de Israel entraram a pé enxuto.")
    add("O que aconteceu ao exército e carros de guerra de Faraó no Mar Vermelho?",
        "As águas voltaram e afogaram todo o exército egípcio", "Eles recuaram em pânico", "Ficaram presos na areia da praia", "Foram feridos por raios",
        "facil", "Êxodo", "Êxodo 14:28", "As águas, voltando, cobriram os carros e os cavaleiros de todo o exército de Faraó; não ficou nem sequer um.")
    add("O que Moisés fez para adoçar as águas amargas de Mara?",
        "Lançou uma árvore indicada pelo Senhor nas águas", "Bateu na água com sua vara de pastor", "Derramou azeite de unção", "Orou durante três dias",
        "medio", "Êxodo", "Êxodo 15:25", "Moisés clamou ao Senhor, e o Senhor mostrou-lhe uma árvore; ele a lançou nas águas, e as águas tornaram-se doces.")
    add("Qual alimento milagroso caía como orvalho toda manhã para alimentar Israel no deserto?",
        "O maná", "Trigo silvestre pronto", "Frutas colhidas por anjos", "Bolos de mel prontos",
        "facil", "Êxodo", "Êxodo 16:14-15", "Evaporando-se o orvalho, havia sobre o deserto uma coisa miúda e redonda: o maná.")
    add("O que acontecia se guardassem o maná de um dia para o outro nos dias úteis comuns?",
        "Criava bichos e cheirava mal", "Tornava-se ouro em pó", "Secava como areia", "Queimava como brasa",
        "medio", "Êxodo", "Êxodo 16:20", "Alguns guardaram para a manhã seguinte; e deu bichos e cheirava mal.")
    add("O que saía da rocha em Horebe quando Moisés a feriu com a vara por ordem de Deus?",
        "Água abundante para o povo beber", "Azeite de oliva", "Fogo consumidor", "Vinho doce",
        "facil", "Êxodo", "Êxodo 17:6", "'Ferirás a rocha, e dela sairão águas, e o povo beberá'. Assim fez Moisés perante os anciãos.")
    add("Quem sustentou os braços de Moisés no monte até o pôr do sol para derrotar Amaleque?",
        "Arão e Hur", "Josué e Calebe", "Eleazar e Finéias", "Gérson e Coate",
        "facil", "Êxodo", "Êxodo 17:12", "Arão e Hur sustentaram as mãos de Moisés, um de um lado e o outro do outro, até ao pôr do sol.")
    add("Qual sogro de Moisés aconselhou a instituição de líderes de mil, cem, cinquenta e dez para julgar as causas?",
        "Jetro (Reuel)", "Melquisedeque", "Balaão", "Labão",
        "medio", "Êxodo", "Êxodo 18:17-22", "Jetro disse a Moisés: 'Não é bom o que fazes... escolhe homens capazes para julgarem o povo com você'.")
    add("Em qual monte Deus desceu em fogo e fumaça para entregar a Sua santa Lei?",
        "Monte Sinai", "Monte Carmelo", "Monte Tabor", "Monte das Oliveiras",
        "facil", "Êxodo", "Êxodo 19:18-20", "Todo o monte Sinai fumegava, porque o Senhor descera sobre ele em fogo.")
    add("Qual é o primeiro dos Dez Mandamentos entregues em Êxodo 20?",
        "'Não terás outros deuses diante de mim'", "'Não farás para ti imagem de escultura'", "'Não matarás'", "'Honra teu pai e tua mãe'",
        "facil", "Êxodo", "Êxodo 20:3", "O primeiro mandamento é: 'Não terás outros deuses diante de mim'.")
    add("Qual mandamento do Decálogo proíbe expressamente a fabricação de imagens e ídolos para culto?",
        "O segundo mandamento", "O primeiro mandamento", "O terceiro mandamento", "O quarto mandamento",
        "medio", "Êxodo", "Êxodo 20:4-5", "'Não farás para ti imagem de escultura... não te curvarás a elas nem as servirás'.")
    add("Qual mandamento adverte contra tomar o Nome de Deus em vão?",
        "O terceiro mandamento", "O segundo mandamento", "O quinto mandamento", "O sétimo mandamento",
        "medio", "Êxodo", "Êxodo 20:7", "'Não tomarás o nome do Senhor teu Deus em vão; porque o Senhor não terá por inocente o que tomar o seu nome em vão'.")
    add("Qual é o único mandamento dos Dez com uma promessa explícita de longa vida na terra?",
        "Honra a teu pai e a tua mãe", "Lembra-te do sábado", "Não furtarás", "Não cobiçarás",
        "facil", "Êxodo", "Êxodo 20:12", "'Honra a teu pai e a tua mãe, para que se prolonguem os teus dias na terra que o Senhor teu Deus te dá'.")
    add("Que ídolo foi fundido por Arão e adorado pelo povo enquanto Moisés estava no cume do monte?",
        "Um bezerro de ouro", "Um cordeiro de prata", "Um falcão alado", "Uma serpente de bronze",
        "facil", "Êxodo", "Êxodo 32:4", "Arão forjou um bezerro de fundição, e o povo disse: 'Estes são os teus deuses, ó Israel'.")
    add("O que Moisés fez com as primeiras tábuas da Lei ao contemplar a idolatria do povo?",
        "Arremessou-as e quebrou-as ao pé do monte", "Escondeu-as numa caverna", "Lançou-as no fogo", "Entregou-as aos levitas",
        "facil", "Êxodo", "Êxodo 32:19", "Acendeu-se o furor de Moisés, e arremessou as tábuas das suas mãos e quebrou-as ao pé do monte.")
    add("O que Moisés fez com o bezerro de ouro idólatra?",
        "Queimou-o no fogo, moeu-o até virar pó, espalhou-o sobre a água e deu de beber aos israelitas", "Enterrou-o na areia do deserto", "Fundiu-o para fazer lanças", "Devolveu aos egípcios",
        "medio", "Êxodo", "Êxodo 32:20", "Tomou o bezerro que tinham feito, queimou-o no fogo, moeu-o até reduzi-lo a pó, e o deu de beber ao povo.")
    add("Qual tribo se reuniu ao lado de Moisés ao seu chamado: 'Quem é do Senhor venha a mim'?",
        "A tribo de Levi", "A tribo de Judá", "A tribo de Benjamim", "A tribo de Efraim",
        "medio", "Êxodo", "Êxodo 32:26", "Postou-se Moisés à entrada do arraial e disse: 'Quem é do Senhor venha a mim'. E juntaram-se a ele todos os filhos de Levi.")
    add("Quais dois homens foram cheios do Espírito de Deus com talento artístico para construir o Tabernáculo?",
        "Bezalel e Aoliabe", "Hur e Eleazar", "Nadabe e Abiú", "Itamar e Corá",
        "medio", "Êxodo", "Êxodo 31:1-6", "O Senhor chamou Bezalel da tribo de Judá e Aoliabe da tribo de Dã para liderarem toda a arte do santuário.")
    add("O que ficava dentro do Santo dos Santos do Tabernáculo?",
        "A Arca da Aliança coberta pelo Propiciatório com os querubins", "O Candelabro de sete braços", "A Mesa dos pães da proposição", "O Altar de incenso",
        "facil", "Êxodo", "Êxodo 26:33-34", "O véu separava o Santo Lugar do Santo dos Santos; ali repousava a Arca do Testemunho com o propiciatório.")
    add("De que madeira era feita a estrutura da Arca da Aliança, recoberta de ouro puro?",
        "Madeira de acácia (cetim)", "Cedro do Líbano", "Madeira de cipreste", "Carvalho de Basã",
        "medio", "Êxodo", "Êxodo 25:10-11", "Farão uma arca de madeira de acácia; de ouro puro a cobrirás por dentro e por fora.")
    add("Quantos braços e lâmpadas tinha o Candelabro de ouro puro (Menorá) no Tabernáculo?",
        "7 lâmpadas (uma haste central e 6 braços)", "12 lâmpadas", "10 lâmpadas", "3 lâmpadas",
        "facil", "Êxodo", "Êxodo 25:31-37", "O candelabro de ouro batido tinha uma haste e seis braços laterais, totalizando sete lâmpadas.")
    add("Quantas pedras preciosas havia no Peitoral do Juízo usado pelo Sumo Sacerdote?",
        "12 pedras (uma para cada tribo de Israel)", "7 pedras", "10 pedras", "24 pedras",
        "medio", "Êxodo", "Êxodo 28:17-21", "O peitoral continha quatro fileiras de três pedras preciosas gravadas com os nomes das doze tribos.")
    add("Quais eram os dois objetos sagrados colocados no peitoral para consultar a vontade de Deus?",
        "O Urim e o Tumim", "O éfode e o cinto", "A mitra e a lâmina de ouro", "Duas pérolas brancas",
        "medio", "Êxodo", "Êxodo 28:30", "Também porás no peitoral do juízo o Urim e o Tumim, para que estejam sobre o coração de Arão.")
    add("O que estava gravado na lâmina de ouro puro afixada na fronte da mitra de Arão?",
        "'SANTIDADE AO SENHOR'", "'DEUS É O NOSSO REI'", "'A LEI DE ISRAEL'", "'JUSTIÇA E PAZ'",
        "dificil", "Êxodo", "Êxodo 28:36", "Farás uma lâmina de ouro puro e nela gravarás à maneira de gravuras de sinetes: SANTIDADE AO SENHOR.")
    add("O que desceu sobre o Tabernáculo quando ele foi inaugurado no deserto?",
        "A nuvem de glória e a presença do Senhor encheu o santuário", "Uma chuva de ouro celestial", "Um coro de vozes angelicais visíveis", "Uma coluna de água límpida",
        "facil", "Êxodo", "Êxodo 40:34-35", "A nuvem cobriu a tenda da congregação, e a glória do Senhor encheu o tabernáculo.")

    # --- LEVÍTICO (15 questões) ---
    add("Qual é o tema teológico e imperativo central de Levítico repetido pelo Senhor?",
        "'Sede santos, porque eu, o Senhor vosso Deus, sou santo'", "'Sede ricos e poderosos entre as nações'", "'Edificai muralhas fortes nas cidades'", "'Marchai com carros de ferro'",
        "facil", "Levítico", "Levítico 19:2; 20:7", "'Santos sereis, porque eu, o Senhor vosso Deus, sou santo'.")
    add("Quem foi o primeiro Sumo Sacerdote de Israel formalmente consagrado?",
        "Arão", "Moisés", "Eleazar", "Finéias",
        "facil", "Levítico", "Levítico 8:12", "Moisés derramou o óleo da unção sobre a cabeça de Arão e ungiu-o, para santificá-lo.")
    add("Quais filhos de Arão morreram fulminados por fogo por oferecerem fogo estranho diante de Deus?",
        "Nadabe e Abiú", "Eleazar e Itamar", "Hofni e Finéias", "Corá e Datã",
        "medio", "Levítico", "Levítico 10:1-2", "Nadabe e Abiú trouxeram fogo estranho perante o Senhor; saiu fogo de diante do Senhor e os devorou.")
    add("Qual dia anual era instituído para a expiação solene dos pecados de todo o povo?",
        "O Dia da Expiação (Yom Kippur)", "A Festa de Pentecostes", "A Festa dos Tabernáculos", "A Festa de Purim",
        "medio", "Levítico", "Levítico 16:29-34", "No décimo dia do sétimo mês comemorava-se o solene Yom Kippur para expiação nacional.")
    add("Qual animal era enviado ao deserto carregando simbolicamente as culpas de Israel no Yom Kippur?",
        "O bode emissário (Azazel)", "Um cordeiro macho de um ano", "Um bezerro vermelho", "Uma novilha sem jugo",
        "medio", "Levítico", "Levítico 16:21-22", "Arão punha as mãos sobre a cabeça do bode vivo e confessava sobre ele as iniquidades; e o bode ia ao deserto.")
    add("Por que a Lei de Levítico proibia terminantemente a ingestão de sangue animal?",
        "Porque a vida da carne está no sangue, que foi dado para expiação no altar", "Porque era costume dos cananeus", "Porque apodrecia rapidamente no calor", "Porque atraía insetos nocivos",
        "medio", "Levítico", "Levítico 17:11", "'Porque a vida da carne está no sangue; eu vo-lo dei sobre o altar para fazer expiação por vossas almas'.")
    add("Qual mandamento sobre amor fraternal está expresso em Levítico 19:18?",
        "'Amarás o teu próximo como a ti mesmo'", "'Não emprestarás a juros a nenhum irmão'", "'Guardarás as ofertas nos celeiros'", "'Não andarás com povos estrangeiros'",
        "facil", "Levítico", "Levítico 19:18", "Levítico 19:18 proclama: 'Não te vingarás nem guardarás ira... mas amarás o teu próximo como a ti mesmo'.")
    add("De quantos em quantos anos era celebrado o Ano do Jubileu com proclamação de liberdade e cancelamento de dívidas?",
        "A cada 50 anos", "A cada 7 anos", "A cada 40 anos", "A cada 70 anos",
        "medio", "Levítico", "Levítico 25:10", "Santificareis o quinquagésimo ano e apregoareis liberdade na terra a todos os seus moradores: ano de jubileu vos será.")
    add("Qual festa bíblica era celebrada habitando em cabanas de ramos por sete dias para lembrar a jornada no deserto?",
        "Festa dos Tabernáculos (Sucot)", "Festa da Páscoa (Pêssach)", "Festa do Pentecostes (Shavuot)", "Festa das Trombetas (Rosh Hashaná)",
        "facil", "Levítico", "Levítico 23:42-43", "Sete dias habitareis em cabanas, para que saibam as vossas gerações que fiz habitar os filhos de Israel em cabanas.")
    add("Quais animais aquáticos eram considerados puros para alimentação segundo Levítico 11?",
        "Os que possuem barbatanas e escamas nas águas", "Todos os peixes de rio", "Os mariscos e crustáceos", "Apenas as enguias e polvos",
        "medio", "Levítico", "Levítico 11:9", "De todos os animais que há nas águas comereis os que têm barbatanas e escamas.")
    add("O fogo sobre o altar dos holocaustos podia apagar-se durante a noite?",
        "Não, devia arder continuamente sem jamais apagar-se", "Sim, podia ser reacendido a cada aurora", "Apenas no dia de sábado", "Somente durante chuvas fortes",
        "dificil", "Levítico", "Levítico 6:13", "'O fogo arderá continuamente sobre o altar; não se apagará'.")
    add("O que o sacerdote colocava na ponta da orelha direita, no polegar da mão direita e no polegar do pé direito na consagração?",
        "O sangue do carneiro da consagração e o óleo da unção", "Pó de ouro sagrado", "Água purificada da bacia", "Vinho aromático",
        "dificil", "Levítico", "Levítico 8:23-24", "Moisés pôs do sangue sobre a ponta da orelha direita de Arão, sobre o polegar de sua mão direita e do pé direito.")
    add("Como era chamada a oferta pacífica voluntária de gratidão em Levítico?",
        "Sacrifício de ação de graças / ofertas pacíficas", "Holocausto pelo pecado", "Oferta de ciúmes", "Voto de nazireado",
        "medio", "Levítico", "Levítico 7:11-12", "Se for oferecido por ação de graças, trará com o sacrifício de louvor bolos ázimos amassados com azeite.")
    add("Qual animal era sacrificado para a purificação da lepra curada junto com uma ave solta no campo aberto?",
        "Duas aves vivas e limpas, pau de cedro, carmesim e hissopo", "Dois bodes brancos", "Dois novilhos gordos", "Duas ovelhas sem mancha",
        "dificil", "Levítico", "Levítico 14:4-7", "O sacerdote ordenará que se tomem duas aves vivas e limpas, pau de cedro, carmesim e hissopo para purificação.")
    add("Qual festa solene ocorria cinquenta dias após a Páscoa, celebrando as primícias da colheita de trigo?",
        "Festa de Pentecostes (Semanas / Shavuot)", "Festa das Trombetas", "Festa dos Tabernáculos", "Festa de Purim",
        "medio", "Levítico", "Levítico 23:15-16", "Contareis cinquenta dias até ao dia seguinte ao sétimo sábado; então oferecereis nova oferta de cereais.")

    # --- NÚMEROS (20 questões) ---
    add("Qual célebre bênção sacerdotal Deus ordenou a Arão e seus filhos para abençoar o povo em Nm 6?",
        "'O Senhor te abençoe e te guarde; o Senhor faça resplandecer o seu rosto sobre ti'", "'Reine o Senhor com poder sobre teus inimigos'", "'Sejam abundantes tuas colheitas de trigo e cevada'", "'Que tuas tendas se multipliquem nas montanhas'",
        "facil", "Números", "Números 6:24-26", "'O Senhor te abençoe e te guarde; o Senhor faça resplandecer o seu rosto sobre ti e tenha misericórdia de ti; o Senhor sobre ti levante o seu rosto e te dê a paz'.")
    add("Quantos espias foram enviados de Cades-Barneia para reconhecer a terra prometida?",
        "12 espias (um líder de cada tribo)", "2 espias", "70 anciãos", "10 guerreiros",
        "facil", "Números", "Números 13:1-16", "Moisés enviou 12 homens, cada um príncipe de sua tribo de Israel.")
    add("Quais dois espias trouxeram relatório de fé e coragem para conquistar Canaã?",
        "Josué e Calebe", "Samua e Safate", "Gadi e Amiel", "Arão e Hur",
        "facil", "Números", "Números 14:6-9", "Josué, filho de Num, e Calebe, filho de Jofoné, rasgaram as vestes e encorajaram o povo.")
    add("Quantos anos a congregação teve de peregrinar no deserto por causa da incredulidade?",
        "40 anos (um ano para cada dia espiado)", "7 anos", "70 anos", "12 anos",
        "facil", "Números", "Números 14:34", "Pelo número dos quarenta dias em que espiastes esta terra, cada dia por um ano, levareis as vossas iniquidades quarenta anos.")
    add("Quem liderou a conspiração contra Moisés e Arão e foi tragado pela terra?",
        "Corá, Datã e Abirão", "Balaque e Balaão", "Seom e Ogue", "Zinri e Cosbi",
        "medio", "Números", "Números 16:31-33", "A terra abriu a sua boca e engoliu Corá, Datã e Abirão com suas famílias e bens.")
    add("Qual vara seca brotou botões, floresceu e deu amêndoas para confirmar o sacerdócio?",
        "A vara de Arão", "A vara de Moisés", "A vara de Josué", "A vara de Hur",
        "medio", "Números", "Números 17:8", "A vara de Arão, pela casa de Levi, brotou, produziu flores e amêndoas maduras.")
    add("Qual erro Moisés cometeu nas águas de Meribá que lhe custou a entrada em Canaã?",
        "Feriu a rocha duas vezes com a vara em ira em vez de apenas falar a ela", "Recusou-se a orar diante do povo", "Fugiu do acampamento com medo", "Amaldiçoou a congregação",
        "medio", "Números", "Números 20:8-12", "Deus mandou falar à rocha; Moisés feriu-a duas vezes com a vara exaltando-se arrogantemente e não santificou a Deus.")
    add("Onde Arão faleceu e suas vestes sacerdotais foram passadas para seu filho Eleazar?",
        "No monte Hor", "No monte Sinai", "No monte Nebo", "No monte Horebe",
        "dificil", "Números", "Números 20:25-28", "Moisés despiu a Arão de suas vestes e as vestiu em seu filho Eleazar; e Arão morreu ali no cume do monte Hor.")
    add("O que Deus mandou Moisés erguer numa haste para curar as picadas de serpentes abrasadoras?",
        "Uma serpente de bronze", "Um querubim dourado", "Um candelabro de prata", "Uma tocha de incenso",
        "facil", "Números", "Números 21:8-9", "Moisés fez uma serpente de bronze e a pôs sobre uma haste; e quem olhava para a serpente de bronze vivia.")
    add("Qual rei de Moabe contratou o profeta Balaão para amaldiçoar Israel?",
        "Balaque", "Seom", "Ogue", "Agague",
        "facil", "Números", "Números 22:2-6", "Balaque, filho de Zipor, rei dos moabitas, enviou mensageiros a Balaão para amaldiçoar Israel.")
    add("O que aconteceu com a jumenta de Balaão a caminho de Moabe?",
        "Viu o anjo do Senhor armado e falou repreendendo o profeta", "Caiu morta subitamente", "Fugiu veloz para o deserto", "Transformou-se num corcel",
        "facil", "Números", "Números 22:28-30", "O Senhor abriu a boca da jumenta, e ela disse a Balaão: 'Que te fiz eu, que me espancaste estas três vezes?'.")
    add("O que saía da boca de Balaão toda vez que tentava amaldiçoar o povo de Israel?",
        "Bênçãos inspiradas pelo Espírito de Deus", "Fogo e enxofre", "Maldições terríveis", "Palavras mudas sem som",
        "facil", "Números", "Números 23:11-12; 24:10", "Balaão disse a Balaque: 'Eis que recebi ordem de abençoar; Deus abençoou, e eu não o posso revogar'.")
    add("Qual jovem sacerdote teve zelo fervoroso e traspassou os pecadores em Sitim, cessando a praga?",
        "Finéias, neto de Arão", "Eleazar", "Itamar", "Calebe",
        "dificil", "Números", "Números 25:7-13", "Finéias tomou uma lança e feriu a Zinri e Cosbi; assim cessou a praga entre os israelitas.")
    add("Quais filhas reivindicaram e receberam o direito de herança das terras de seu falecido pai?",
        "As filhas de Zelofeade", "As filhas de Labão", "As filhas de Jetro", "As filhas de Ló",
        "dificil", "Números", "Números 27:1-7", "As filhas de Zelofeade falaram o que era justo, e o Senhor ordenou que recebessem herança entre os irmãos de seu pai.")
    add("Quem foi consagrado publicamente perante o sacerdote Eleazar como sucessor de Moisés?",
        "Josué, filho de Num", "Calebe", "Finéias", "Hur",
        "facil", "Números", "Números 27:18-23", "O Senhor disse a Moisés: 'Toma a Josué, homem em quem há o Espírito, e impõe sobre ele a tua mão'.")
    add("Quais duas tribos e meia pediram para se estabelecer nas terras conquistadas a leste do Jordão?",
        "Rúben, Gade e meia tribo de Manassés", "Judá, Simeão e Benjamim", "Efraim, Dã e Aser", "Zebulom, Issacar e Naftali",
        "medio", "Números", "Números 32:1-5", "Os filhos de Rúben e os filhos de Gade tinham gado em grande quantidade e pediram as terras de Gileade.")
    add("Quantas cidades no total foram designadas para os levitas habitarem com seus campos?",
        "48 cidades", "12 cidades", "24 cidades", "70 cidades",
        "dificil", "Números", "Números 35:7", "Todas as cidades que dareis aos levitas serão quarenta e oito cidades, juntamente com os seus campos.")
    add("Quantas dessas cidades dos levitas eram Cidades de Refúgio para o homicida involuntário?",
        "6 cidades", "3 cidades", "12 cidades", "4 cidades",
        "medio", "Números", "Números 35:6-13", "Das cidades que dareis aos levitas, seis serão cidades de refúgio para que nelas se acolha o homicida involuntário.")
    add("O que o voto de Nazireu em Números 6 exigia expressamente?",
        "Não beber vinho ou suco de uva, não passar navalha no cabelo e não tocar em cadáver", "Não comer carne bovina e vestir saco de crina", "Ficar em jejum completo quarenta dias", "Viver isolado numa caverna",
        "medio", "Números", "Números 6:1-8", "O nazireu abstinha-se de vinho e uvas, não cortava o cabelo e não se contaminava com nenhum morto.")
    add("Qual gigante rei de Basã dormia num leito de ferro de nove côvados de comprimento?",
        "Ogue", "Seom", "Golias", "Arba",
        "dificil", "Números", "Números 21:33-35; Deuteronômio 3:11", "Ogue, rei de Basã, governava cidades fortificadas e sua cama de ferro media nove côvados.")

    # --- DEUTERONÔMIO (10 questões) ---
    add("Qual é o Shemá, mandamento central e declaração de fé de Israel em Dt 6:4-5?",
        "'Ouve, Israel, o Senhor nosso Deus é o único Senhor; amarás o Senhor teu Deus de todo o teu coração'", "'Guarda as ofertas nos celeiros do santuário'", "'Não terás amizade com os reis das nações'", "'Constrói altares de pedras lavradas'",
        "facil", "Deuteronômio", "Deuteronômio 6:4-5", "'Ouve, Israel, o Senhor nosso Deus é o único Senhor. Amarás, pois, o Senhor teu Deus de todo o teu coração, de toda a tua alma e de todas as tuas forças'.")
    add("Quais dois montes serviram para proclamar bênçãos e maldições da aliança?",
        "Monte Gerizim (bênçãos) e Monte Ebal (maldições)", "Monte Sinai e Monte Carmelo", "Monte Sião e Monte Hermom", "Monte Tabor e Monte Nebo",
        "dificil", "Deuteronômio", "Deuteronômio 27:12-13", "Seis tribos postaram-se no monte Gerizim para abençoar e outras seis no monte Ebal para pronunciar as maldições.")
    add("Qual promessa profética messiânica é registrada em Deuteronômio 18:15?",
        "'O Senhor teu Deus te suscitará um profeta do meio de ti, de teus irmãos, semelhante a mim; a ele ouvirás'", "'Um anjo descerá para governar os reis da terra'", "'Canaã será dividida por doze generais'", "'O templo será construído em ouro puro'",
        "medio", "Deuteronômio", "Deuteronômio 18:15; Atos 3:22", "Moisés profetizou o envio de um Profeta semelhante a ele (cumprido em Cristo Jesus).")
    add("Em qual monte Moisés subiu para contemplar a Terra Prometida antes de sua morte?",
        "Monte Nebo (cume de Pisga)", "Monte Sinai", "Monte Carmelo", "Monte Horebe",
        "facil", "Deuteronômio", "Deuteronômio 34:1", "Moisés subiu ao monte Nebo, ao cume de Pisga, defronte de Jericó, e o Senhor mostrou-lhe toda a terra.")
    add("Qual era a idade de Moisés ao falecer, conservando visão e vigor?",
        "120 anos", "100 anos", "80 anos", "140 anos",
        "facil", "Deuteronômio", "Deuteronômio 34:7", "Tinha Moisés 120 anos quando morreu; não se lhe escureceram os olhos, nem se lhe abateu o vigor natural.")
    add("Quem sepultou Moisés na terra de Moabe, de modo que ninguém sabe o paradeiro de sua cova?",
        "O próprio Senhor Deus", "Josué e Calebe", "Eleazar e os levitas", "Os anciãos do povo",
        "medio", "Deuteronômio", "Deuteronômio 34:6", "E o Senhor o sepultou num vale, defronte de Bete-Peor; e ninguém soube até hoje o lugar da sua sepultura.")
    add("O que Deus ordenou que os futuros reis de Israel fizessem para si para não se desviarem da Lei?",
        "Escrever para si um rolo com uma cópia desta Lei e lê-la todos os dias da sua vida", "Acumular grandes manadas de cavalos do Egito", "Casar com muitas princesas estrangeiras", "Guardar tesouros de ouro maciço",
        "medio", "Deuteronômio", "Deuteronômio 17:18-19", "O rei escreverá para si uma cópia desta lei num livro e a lerá todos os dias da sua vida para aprender a temer ao Senhor.")
    add("Onde as duas tábuas de pedra da Lei foram guardadas por Moisés?",
        "Dentro da Arca da Aliança", "No peitoral do sumo sacerdote", "Sobre o altar de incenso", "Numa gruta do monte Sinai",
        "facil", "Deuteronômio", "Deuteronômio 10:5", "Moisés colocou as tábuas na arca que havia feito, e ali ficaram como o Senhor ordenara.")
    add("Como era decidida a aplicação de penalidade capital segundo Deuteronômio 19:15?",
        "Pela boca de duas ou três testemunhas confirmadas", "Pelo depoimento de uma única pessoa", "Por sorteio com dados de osso", "Pela decisão do rei sem audiência",
        "medio", "Deuteronômio", "Deuteronômio 19:15", "Pelo depoimento de duas ou três testemunhas se estabelecerá o fato.")
    add("Quantos dias os médicos egípcios gastaram para embalsamar o corpo de Jacó segundo Gênesis 50?",
        "40 dias", "7 dias", "10 dias", "70 dias",
        "dificil", "Gênesis", "Gênesis 50:3", "Gastaram-se nisto quarenta dias, porque assim se cumprem os dias do embalsamamento.")
    add("Quais eram os nomes dos dois filhos nascidos de Moisés e Zípora em Midiã?",
        "Gérson e Eliezer", "Nadabe e Abiú", "Manassés e Efraim", "Eleazar e Itamar",
        "medio", "Êxodo", "Êxodo 18:3-4", "O nome de um era Gérson ('fui peregrino em terra alheia') e o do outro Eliezer ('o Deus de meu pai foi minha ajuda').")
    add("De acordo com Levítico 25, com que frequência a terra agrícola deveria ter um ano de descanso sabático?",
        "A cada 7 anos", "A cada 50 anos", "A cada 10 anos", "A cada 3 anos",
        "facil", "Levítico", "Levítico 25:3-4", "Seis anos semearás o teu campo, mas ao sétimo ano haverá sábado de descanso para a terra.")
    add("O que foi guardado diante do testemunho junto com as tábuas da lei e o vaso de maná como memorial?",
        "A vara de Arão que floresceu", "A espada de Faraó", "O cajado de Jetro", "Uma pedra do monte Horebe",
        "medio", "Números", "Números 17:10; Hebreus 9:4", "Disse o Senhor a Moisés: 'Torna a pôr a vara de Arão perante o testemunho, para que se guarde por sinal para os rebeldes'.")
    add("Quantos dias os filhos de Israel choraram a morte de Moisés nas campinas de Moabe?",
        "30 dias", "7 dias", "40 dias", "14 dias",
        "medio", "Deuteronômio", "Deuteronômio 34:8", "Os filhos de Israel choraram a Moisés trinta dias nas campinas de Moabe.")
    add("Qual cidade cananeia foi consagrada à destruição e chamada Horma após a vitória de Israel em Nm 21?",
        "Horma", "Jericó", "Ai", "Hazor",
        "dificil", "Números", "Números 21:1-3", "Israel fez um voto ao Senhor e destruiu totalmente os cananeus e suas cidades, chamando aquele lugar Horma.")

    return items

if __name__ == "__main__":
    q_list = get_pentateuch_questions()
    print(f"Pentateuch generated: {len(q_list)} questions")
