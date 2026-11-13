# -*- coding: utf-8 -*-
"""
Livros Poéticos e de Sabedoria: 130 questões de Jó a Cantares
"""

def get_poetic_questions():
    items = []
    def add(q, c, w1, w2, w3, diff, book, ref, exp):
        items.append({
            "q": q, "c": c, "w1": w1, "w2": w2, "w3": w3,
            "diff": diff, "book": book, "testament": "VT",
            "section": "Poéticos e Sabedoria", "ref": ref, "exp": exp
        })

    # --- JÓ (40 questões) ---
    add("Em qual terra habitava Jó, descrito como homem íntegro, reto, temente a Deus e que se desviava do mal?",
        "Terra de Uz", "Terra de Canaã", "Terra de Ur", "Terra de Midiã",
        "facil", "Jó", "Jó 1:1", "Havia um homem na terra de Uz, cujo nome era Jó; homem íntegro e reto, temente a Deus e que se desviava do mal.")
    add("Quantos filhos e quantas filhas Jó tinha antes das provações descritas no capítulo 1?",
        "Sete filhos e três filhas (dez filhos ao todo)", "Doze filhos e duas filhas", "Três filhos e sete filhas", "Cinco filhos e cinco filhas",
        "facil", "Jó", "Jó 1:2", "Nasceram-lhe sete filhos e três filhas.")
    add("O que Jó costumava fazer de madrugada em favor de seus filhos após os banquetes familiares?",
        "Oferecia holocaustos segundo o número de todos eles para consagrá-los caso houvessem pecado", "Distribuía ouro aos pobres", "Escrevia provérbios", "Fazia jejum de sete dias",
        "medio", "Jó", "Jó 1:5", "Jó madrugava e oferecia holocaustos segundo o número de todos eles; pois dizia: 'Talvez meus filhos tenham pecado'.")
    add("Qual argumento Satanás usou perante Deus para pedir autorização para provar Jó?",
        "'Porventura Jó teme a Deus debalde? Não puseste cerca protetora em volta dele e de tudo o que ele tem?'", "'Jó não sabe orar'", "'Jó quer construir outro templo'", "'Jó teme os homens e não a Ti'",
        "medio", "Jó", "Jó 1:9-10", "Respondeu Satanás: 'Porventura teme Jó a Deus debalde? Porventura não o cercaste de sebe a ele, à sua casa e a tudo quanto tem?'.")
    add("Quais povos invasores saquearam os bois, jumentas e camelos de Jó matando seus servos ao fio da espada?",
        "Os sabeus e os caldeus", "Os filisteus e os amonitas", "Os egípcios e os moabitas", "Os assírios e os midianitas",
        "medio", "Jó", "Jó 1:15-17", "Os sabeus deram sobre eles e os tomaram; depois os caldeus formaram três bandos e deram sobre os camelos.")
    add("Como os dez filhos de Jó morreram tragicamente no mesmo dia?",
        "Um grande tufão/vento do deserto atingiu os quatro cantos da casa do irmão primogênito e ela desabou sobre eles", "Foram envenenados no banquete", "Morreram por uma praga fulminante", "Afogaram-se num rio caudaloso",
        "facil", "Jó", "Jó 1:18-19", "Eis que um grande vento sobreveio dalém do deserto e deu nos quatro cantos da casa, e ela caiu sobre os jovens, e morreram.")
    add("Qual sublime declaração de adoração e resignação Jó fez ao receber a notícia da perda de seus bens e filhos?",
        "'O Senhor o deu, o Senhor o tomou; bendito seja o nome do Senhor'", "'Deus foi injusto comigo'", "'Perdi toda a minha esperança'", "'Maldito seja o dia em que nasci'",
        "facil", "Jó", "Jó 1:21", "Jó prostrou-se em terra e adorou: 'Nu saí do ventre de minha mãe e nu tornarei para lá; o Senhor o deu, e o Senhor o tomou; bendito seja o nome do Senhor'.")
    add("Com que enfermidade física e dolorosa Satanás feriu o corpo de Jó na segunda prova?",
        "Úlceras malignas e chagas dolorosas da planta do pé ao alto da cabeça", "Cegueira e paralisia total", "Lepra branca contagiosa", "Febre tifoide persistente",
        "facil", "Jó", "Jó 2:7", "Satanás feriu a Jó de úlceras malignas, desde a planta do pé até ao alto da cabeça.")
    add("O que Jó tomou na mão para se raspar assentado no meio das cinzas?",
        "Um caco de cerâmica / telha quebrada", "Uma pedra afiada", "Uma navalha de ferro", "Uma concha do mar",
        "medio", "Jó", "Jó 2:8", "Jó tomou um caco de barro para com ele se raspar, e estava assentado no meio da cinza.")
    add("Qual conselho desesperado e ímpio a mulher de Jó lhe deu ao vê-lo sofrer no lixo?",
        "'Ainda reténs a tua integridade? Amaldiçoa a Deus e morre!'", "'Vai a Jerusalém orar'", "'Pede ouro emprestado aos amigos'", "'Chama os médicos de Uz'",
        "facil", "Jó", "Jó 2:9", "Disse-lhe sua mulher: 'Ainda reténs a tua integridade? Amaldiçoa a Deus, e morre'.")
    add("Qual foi a sábia e irrepreensível resposta de Jó à sua mulher?",
        "'Como fala uma louca, falas tu; aceitaremos o bem de Deus e não aceitaremos o mal?'", "'Tens toda razão, minha esposa'", "'Vou procurar outro refúgio'", "'Não me fales mais neste tom'",
        "facil", "Jó", "Jó 2:10", "Jó disse-lhe: 'Como fala qualquer das doidas, falas tu; receberemos o bem de Deus, e não receberíamos o mal?'. Em tudo isto não pecou Jó com os seus lábios.")
    add("Quais eram os três amigos de Jó que foram visitá-lo para consolá-lo?",
        "Elifaz o temanita, Bildade o suíta e Zofar o naamatita", "Hananias, Misael e Azarias", "Sambalate, Tobias e Gesem", "Anás, Caifás e Gamaliel",
        "facil", "Jó", "Jó 2:11", "Ouvindo três amigos de Jó todo este mal... vieram Elifaz temanita, Bildade suíta e Zofar naamatita.")
    add("Quantos dias e noites os três amigos de Jó ficaram assentados no chão com ele em silêncio antes de falarem?",
        "Sete dias e sete noites", "Três dias e três noites", "Quarenta dias", "Um dia apenas",
        "medio", "Jó", "Jó 2:13", "Assentaram-se com ele na terra sete dias e sete noites; e nenhum lhe dizia palavra alguma, pois viam que a dor era muito grande.")
    add("O que Jó amaldiçoou abertamente no capítulo 3 ao quebrar o silêncio em profunda dor?",
        "O dia do seu próprio nascimento e a noite em que foi concebido", "O nome do Senhor Deus", "A vida de seus três amigos", "A terra de Uz e seus campos",
        "medio", "Jó", "Jó 3:1-3", "Depois disto abriu Jó a sua boca e amaldiçoou o seu dia: 'Pereça o dia em que nasci e a noite em que se disse: Foi concebido um homem!'.")
    add("Qual era a tese teológica repetida insistentemente pelos três amigos de Jó para justificar seu sofrimento?",
        "Que Jó certamente cometeu pecados graves e ocultos, pois afirmavam que Deus nunca pune o inocente", "Que o sofrimento é sempre obra do acaso", "Que Deus não se importa com a justiça humana", "Que Satanás era o senhor do universo",
        "facil", "Jó", "Jó 4:7-8; 8:4-6", "Eles sustentavam a teologia da retribuição estrita, insistindo que o sofrimento de Jó provava iniquidade oculta.")
    add("Qual extraordinária profissão de fé e esperança futura Jó proclama com júbilo em Jó 19:25?",
        "'Porque eu sei que o meu Redentor vive, e que por fim se levantará sobre a terra'", "'Eu sei que os meus amigos se arrependerão'", "'Eu sei que serei mais rico que antes'", "'Eu sei que os caldeus serão destruídos'",
        "facil", "Jó", "Jó 19:25", "'Porque eu sei que o meu Redentor vive, e que por fim se levantará sobre a terra; e depois de consumida a minha pele, ainda em minha carne verei a Deus'.")
    add("Qual jovem ouvinte esperou os mais velhos terminarem de falar e depois discursou com ardor a partir do capítulo 32?",
        "Eliú, filho de Baraquel", "Gamaliel", "Filemom", "Eleazar",
        "medio", "Jó", "Jó 32:2-6", "Acendeu-se a ira de Eliú, filho de Baraquel, o buzita; esperara para falar a Jó porque os outros tinham mais idade.")
    add("De onde o Senhor respondeu a Jó a partir do capítulo 38 demonstrando Sua majestade cósmica?",
        "Do meio de um redemoinho / tempestade", "Do cume de um monte fumegante", "Numa sarça ardente", "Numa suave brisa sussurrada",
        "facil", "Jó", "Jó 38:1", "Então o Senhor respondeu a Jó de um redemoinho, dizendo: 'Quem é este que escurece o conselho com palavras sem conhecimento?'.")
    add("Quais duas extraordinárias criaturas colossais Deus descreve a Jó nos capítulos 40 e 41 como obras de Seu poder?",
        "O Beemote e o Leviatã", "O Leão alado e o Escorpião gigante", "A Serpente do mar e o Touro dourado", "O Grifo e a Fênix",
        "medio", "Jó", "Jó 40:15; 41:1", "Deus descreve o colossal Beemote cuja força está nos lombos e o temível Leviatã das profundezas que ninguém pode domar.")
    add("Qual foi a famosa confissão final de Jó no capítulo 42 ao contemplar a grandeza de Deus?",
        "'Eu te conhecia só de ouvir falar, mas agora os meus olhos te veem'", "'Agora entendi todas as tuas leis'", "'Quero disputar contra a tua sabedoria'", "'Peço que castigues os meus amigos'",
        "facil", "Jó", "Jó 42:5", "Jó confessou: 'Com o ouvir dos meus ouvidos ouvi, mas agora te veem os meus olhos; por isso me abomino e me arrependo no pó e na cinza'.")
    add("O que Deus ordenou que Jó fizesse para que os seus três amigos fossem perdoados da falta cometida?",
        "Orasse e intercedesse por eles perante o Senhor", "Cobrasse cem talentos de prata de cada um", "Construísse um altar em suas terras", "Expulsasse-os da terra de Uz",
        "facil", "Jó", "Jó 42:8", "O Senhor disse a Elifaz: 'O meu servo Jó orará por vós; porque deveras a ele aceitarei, para que eu não vos trate segundo a vossa estultícia'.")
    add("Quando o Senhor mudou a sorte de Jó e o restaurou plenamente?",
        "Quando Jó orava pelos seus amigos", "Quando construiu sua nova casa", "Quando suas chagas secaram sozinhas", "Quando viajou para o Egito",
        "facil", "Jó", "Jó 42:10", "O Senhor virou o cativeiro de Jó, quando orava pelos seus amigos; e o Senhor deu a Jó o dobro de tudo o que antes possuía.")
    add("Em qual proporção Deus restituiu os bens materiais de Jó após sua provação?",
        "Em dobro de tudo quanto possuía anteriormente", "Três vezes mais", "A mesma quantidade que tinha antes", "Dez vezes mais",
        "facil", "Jó", "Jó 42:10-12", "O Senhor abençoou o último estado de Jó mais do que o primeiro; teve 14.000 ovelhas, 6.000 camelos, 1.000 juntas de bois e 1.000 jumentas.")
    add("Quantos filhos e filhas Jó gerou após a sua restauração?",
        "Sete filhos e três filhas", "Doze filhos e doze filhas", "Dez filhos homens apenas", "Setenta filhos",
        "facil", "Jó", "Jó 42:13", "Também teve sete filhos e três filhas, renovando integralmente sua família.")
    add("Quais eram os nomes das três filhas de Jó, consideradas as mulheres mais belas de toda a terra?",
        "Jemima, Quézia e Quéren-Hapuque", "Raquel, Lia e Diná", "Ada, Zilá e Basemate", "Miriã, Noemi e Rute",
        "dificil", "Jó", "Jó 42:14-15", "Chamou o nome da primeira Jemima, da segunda Quézia, e da terceira Quéren-Hapuque; em toda a terra não se achavam mulheres tão formosas.")
    add("Quantos anos Jó viveu após a sua restauração, vendo seus filhos e netos até a quarta geração?",
        "140 anos", "70 anos", "100 anos", "120 anos",
        "medio", "Jó", "Jó 42:16", "Depois disto viveu Jó cento e quarenta anos; e viu a seus filhos, e aos filhos de seus filhos, até à quarta geração; e morreu velho e farto de dias.")

    # --- SALMOS (50 questões) ---
    add("Quantos salmos compõem o Livro dos Salmos na Bíblia Sagrada?",
        "150 salmos", "120 salmos", "100 salmos", "200 salmos",
        "facil", "Salmos", "Salmos", "O saltério bíblico contém exatamente 150 salmos inspirados divididos em cinco livros.")
    add("Qual é a bem-aventurança inicial descrita no Salmo 1:1?",
        "'Bem-aventurado o homem que não anda segundo o conselho dos ímpios, nem se detém no caminho dos pecadores'", "'Bem-aventurado o povo que possui muitas armas'", "'Bem-aventurado o que constrói grandes palácios'", "'Bem-aventurado o viajante do deserto'",
        "facil", "Salmos", "Salmo 1:1", "'Bem-aventurado o homem que não anda segundo o conselho dos ímpios, nem se detém no caminho dos pecadores, nem se assenta na roda dos escarnecedores'.")
    add("A que é comparado o justo que medita de dia e de noite na Lei do Senhor no Salmo 1?",
        "A uma árvore plantada junto a correntes de águas, que dá o seu fruto na estação própria", "A uma rocha inabalável no mar", "A uma estrela brilhante no céu", "A um leão rugidor no bosque",
        "facil", "Salmos", "Salmo 1:2-3", "Ele é como a árvore plantada junto a correntes de águas, que dá o seu fruto no tempo certo, e cujas folhas não murcham.")
    add("Como o ímpio é descrito em contraste no Salmo 1:4?",
        "Como a palha miúda que o vento dispersa", "Como uma pedra pesada", "Como um arbusto espinhoso", "Como ferro enferrujado",
        "facil", "Salmos", "Salmo 1:4", "Não são assim os ímpios; mas são como a moinha (palha) que o vento espalha.")
    add("Qual versículo abre o Salmo messiânico 2 sobre a soberania de Deus contra os reis da terra?",
        "'Por que se amotinam as nações e os povos conspiram em vão?'", "'O Senhor é a minha luz e a minha salvação'", "'Cantai ao Senhor um cântico novo'", "'Clamo a ti de todo o coração'",
        "medio", "Salmos", "Salmo 2:1", "'Por que se enfurecem os gentios e os povos imaginam coisas vãs? Os reis da terra se levantam contra o Senhor e o seu Ungido'.")
    add("Qual famoso Salmo de confiança declara: 'O Senhor é o meu pastor; nada me faltará'?",
        "Salmo 23", "Salmo 91", "Salmo 1", "Salmo 121",
        "facil", "Salmos", "Salmo 23:1", "O Salmo 23 de Davi é a mais célebre oração pastoral: 'O Senhor é o meu pastor; nada me faltará'.")
    add("Onde o salmista afirma que o Bom Pastor o faz repousar no Salmo 23?",
        "Em verdes pastos / pastos verdejantes", "Em montanhas altas", "Nas praias do mar", "Num palácio de mármore",
        "facil", "Salmos", "Salmo 23:2", "'Deitar-me faz em verdes pastos, guia-me mansamente a águas mansas e tranquilas'.")
    add("O que o salmista não teme mesmo andando pelo vale da sombra da morte segundo o Salmo 23:4?",
        "Não teme mal algum, porque o Senhor está com ele; Sua vara e Seu cajado o consolam", "Não teme os animais ferozes", "Não teme a noite escura", "Não teme os soldados inimigos",
        "facil", "Salmos", "Salmo 23:4", "'Ainda que eu andasse pelo vale da sombra da morte, não temeria mal algum, porque tu estás comigo; a tua vara e o teu cajado me consolam'.")
    add("O que o Senhor prepara perante o salmista na presença dos seus inimigos no Salmo 23:5?",
        "Uma mesa abundante e unge-lhe a cabeça com óleo", "Um escudo de ferro", "Uma espada afiada", "Uma muralha de pedra",
        "facil", "Salmos", "Salmo 23:5", "'Preparas uma mesa perante mim na presença dos meus inimigos, unges a minha cabeça com óleo, o meu cálice transborda'.")
    add("Quem é o autor do Salmo 90, intitulado 'Oração de Moisés, homem de Deus'?",
        "Moisés", "Davi", "Asafe", "Salomão",
        "medio", "Salmos", "Salmo 90:1", "O Salmo 90 é a única oração do saltério atribuída nominalmente a Moisés: 'Senhor, tu tens sido o nosso refúgio de geração em geração'.")
    add("Qual pedido sobre a brevidade da vida humana é feito em Salmos 90:12?",
        "'Ensina-nos a contar os nossos dias, para que alcancemos coração sábio'", "'Prolonga os nossos anos até os cem anos'", "'Livra-nos de todo trabalho pesado'", "'Dá-nos riquezas terrenas'",
        "facil", "Salmos", "Salmo 90:12", "'Ensina-nos a contar os nossos dias de tal maneira que alcancemos corações sábios'.")
    add("Qual versículo abre o Salmo 91 sobre a segurança daquele que confia em Deus?",
        "'Aquele que habita no esconderijo do Altíssimo, à sombra do Onipotente descansará'", "'O Senhor é a fortaleza dos santos'", "'Louvai a Deus no seu santuário'", "'Grandes são as obras do Senhor'",
        "facil", "Salmos", "Salmo 91:1", "'Aquele que habita no esconderijo do Altíssimo, à sombra do Onipotente descansará. Direi do Senhor: Ele é o meu refúgio e a minha fortaleza'.")
    add("Qual promessa célebre de proteção contra perigos está em Salmos 91:7?",
        "'Mil cairão ao teu lado, e dez mil à tua direita, mas tu não serás atingido'", "'Cinquenta mil te defenderão com escudos'", "'Nenhuma chuva cairá em tua tenda'", "'Os teus celeiros transbordarão de trigo'",
        "facil", "Salmos", "Salmo 91:7", "'Mil cairão ao teu lado, e dez mil à tua direita, mas não chegará a ti. Somente com os teus olhos contemplarás e verás a recompensa dos ímpios'.")
    add("Segundo Salmos 91:11, o que Deus dá ordem aos Seus anjos a teu respeito?",
        "Para te guardarem em todos os teus caminhos e te sustentarem nas mãos", "Para combaterem com espadas de ouro", "Para cantarem canções de glória", "Para colherem teus frutos",
        "facil", "Salmos", "Salmo 91:11-12", "'Porque aos seus anjos dará ordem a teu respeito, para te guardarem em todos os teus caminhos; eles te sustentarão nas suas mãos, para que não tropeces'.")
    add("Qual é o menor capítulo de toda a Bíblia Sagrada, composto de apenas 2 versículos?",
        "Salmo 117", "Salmo 1", "Salmo 23", "Salmo 134",
        "facil", "Salmos", "Salmo 117:1-2", "O Salmo 117 é o mais curto capítulo da Bíblia com apenas 2 versículos exortando todas as nações a louvarem ao Senhor.")
    add("Qual é o maior capítulo de toda a Bíblia Sagrada, composto de 176 versículos?",
        "Salmo 119", "Salmo 18", "Salmo 78", "Salmo 89",
        "facil", "Salmos", "Salmo 119", "O Salmo 119 tem 176 versículos organizados em 22 seções segundo as 22 letras do alfabeto hebraico.")
    add("Qual versículo iluminador sobre a Palavra de Deus está em Salmos 119:105?",
        "'Lâmpada para os meus pés é tua palavra e luz para o meu caminho'", "'A tua palavra é ouro fino'", "'Guardei o livro na arca'", "'Os teus juízos são como o mar'",
        "facil", "Salmos", "Salmo 119:105", "'Lâmpada para os meus pés é tua palavra, e luz para o meu caminho'.")
    add("Qual é a razão declarada no Salmo 119:11 para guardar a Palavra de Deus no coração?",
        "'Para eu não pecar contra ti'", "'Para ser admirado pelos homens'", "'Para acumular riquezas'", "'Para ser coroado rei'",
        "facil", "Salmos", "Salmo 119:11", "'Escondi a tua palavra no meu coração, para eu não pecar contra ti'.")
    add("Qual questionamento de fé abre o Salmo 121 (Cântico dos Degraus)?",
        "'Elevo os meus olhos para os montes: de onde me virá o socorro? O meu socorro vem do Senhor'", "'Quem subirá ao monte santo?'", "'Por que estás abatida, ó minha alma?'", "'Até quando te esquecerás de mim?'",
        "facil", "Salmos", "Salmo 121:1-2", "'Levantarei os meus olhos para os montes, de onde vem o meu socorro. O meu socorro vem do Senhor que fez o céu e a terra'.")
    add("O que o Salmo 121:4 afirma a respeito do Guarda de Israel?",
        "'Eis que não tosquenejará nem dormirá o guarda de Israel'", "'Ele descansa ao meio-dia'", "'Ele viaja pelas estrelas'", "'Ele fala apenas aos sacerdotes'",
        "facil", "Salmos", "Salmo 121:4", "'Eis que não tosquenejará nem dormirá o guarda de Israel; o Senhor é quem te guarda'.")
    add("Qual declaração de alegria e adoração comunitária está no Salmo 122:1?",
        "'Alegrei-me quando me disseram: Vamos à Casa do Senhor'", "'Cantai hinos ao vencedor'", "'Aplaudi todas as nações'", "'Grande é a cidade de Sião'",
        "facil", "Salmos", "Salmo 122:1", "'Alegrei-me quando me disseram: Vamos à casa do Senhor. Os nossos pés estão dentro das tuas portas, ó Jerusalém'.")
    add("O que o Salmo 127:1 adverte com sabedoria sobre edificar e guardar a cidade?",
        "'Se o Senhor não edificar a casa, em vão trabalham os que a edificam; se o Senhor não guardar a cidade, em vão vigia a sentinela'", "'A força das muralhas salva o povo'", "'O ouro assegura a vitória militar'", "'O rei protege os seus súditos sozinho'",
        "facil", "Salmos", "Salmo 127:1", "Salmo de Salomão: 'Se o Senhor não edificar a casa, em vão trabalham os que a edificam; se o Senhor não guardar a cidade, em vão vigia a sentinela'.")
    add("A que os filhos nascidos na mocidade são comparados no Salmo 127:4?",
        "Como flechas na mão do guerreiro", "Como ramos de videira", "Como estrelas no céu", "Como ovelhas no pasto",
        "medio", "Salmos", "Salmo 127:4", "'Como flechas na mão de um homem poderoso, assim são os filhos da mocidade; bem-aventurado o homem que enche deles a sua aljava'.")
    add("A que a mulher piedosa é comparada no íntimo de sua casa no Salmo 128:3?",
        "A uma videira frutífera aos lados da tua casa", "A uma rosa de Sarom", "A uma coluna de mármore", "A uma árvore de incenso",
        "medio", "Salmos", "Salmo 128:3", "'A tua mulher será como a videira frutífera aos lados da tua casa; os teus filhos como plantas de oliveira à roda da tua mesa'.")
    add("Qual declaração maravilhosa sobre a união dos irmãos abre o Salmo 133?",
        "'Oh! Quão bom e quão suave é que os irmãos vivam em união!'", "'Grande é a vitória do nosso exército'", "'Bendito o povo de Judá'", "'Louvai com trombetas na congregação'",
        "facil", "Salmos", "Salmo 133:1", "'Oh! Quão bom e quão suave é que os irmãos vivam em união! É como o óleo precioso sobre a cabeça, que desce sobre a barba de Arão'.")
    add("A que a comunhão fraterna é comparada no Salmo 133:2-3?",
        "Ao óleo precioso sobre a barba de Arão e ao orvalho de Hermom que desce sobre Sião", "A um banquete real com vinho", "A uma fonte no deserto", "A flores silvestres no campo",
        "medio", "Salmos", "Salmo 133:2-3", "É como o óleo que desce sobre a gola das vestes de Arão e como o orvalho de Hermom; porque ali o Senhor ordena a bênção e a vida para sempre.")
    add("Qual Salmo exalta a onisciência e onipresença de Deus declarando: 'Senhor, tu me sondas e me conheces'?",
        "Salmo 139", "Salmo 23", "Salmo 51", "Salmo 100",
        "facil", "Salmos", "Salmo 139:1", "Davi declara no Salmo 139: 'Senhor, tu me sondas e me conheces; tu sabes o meu assentar e o meu levantar; de longe entendes o meu pensamento'.")
    add("O que o salmista exclama sobre como foi formado por Deus no ventre materno em Salmos 139:14?",
        "'Graças te dou, visto que por modo assombrosamente maravilhoso fui formado; as tuas obras são admiráveis'", "'Fui feito da poeira do mar'", "'Minha vida é mero acaso terreno'", "'Não compreendo os meus dias'",
        "facil", "Salmos", "Salmo 139:14", "'Eu te louvarei, porque de um modo assombroso e tão maravilhoso fui feito; maravilhosas são as tuas obras, e a minha alma o sabe muito bem'.")
    add("Qual é o último versículo de todo o Saltério que encerra o Salmo 150?",
        "'Tudo quanto tem fôlego louve ao Senhor. Louvai ao Senhor!'", "'Cantai para sempre ao nosso Deus'", "'Amém e amém no santuário'", "'O Senhor reina sobre a terra'",
        "facil", "Salmos", "Salmo 150:6", "O encerramento magistral do Livro dos Salmos proclama: 'Tudo quanto tem fôlego louve ao Senhor. Louvai ao Senhor!'.")
    add("Qual versículo de louvor e adoração alegre é o tema central de Salmos 100:4?",
        "'Entrai pelas portas dele com ações de graças e nos seus átrios com louvor'", "'Guardai silêncio absoluto no templo'", "'Oferecei sacrifícios de touros'", "'Batei os tambores na praça'",
        "facil", "Salmos", "Salmo 100:4", "'Entrai pelas portas dele com gratidão, e em seus átrios com louvor; louvai-o, e bendizei o seu nome'.")

    # --- PROVÉRBIOS (25 questões) ---
    add("Qual é o princípio e fundamento de todo o verdadeiro saber segundo Provérbios 1:7?",
        "O temor do Senhor", "A acumulação de livros", "A riqueza material", "A eloqüência humana",
        "facil", "Provérbios", "Provérbios 1:7", "'O temor do Senhor é o princípio da sabedoria; os loucos desprezam a sabedoria e a instrução'.")
    add("Qual exortação à confiança plena em Deus está em Provérbios 3:5-6?",
        "'Confia no Senhor de todo o teu coração e não te estribes no teu próprio entendimento; reconhece-o em todos os teus caminhos'", "'Segue teus próprios impulsos e serás livre'", "'Pede conselho aos magos da corte'", "'Guarda teus planos em segredo'",
        "facil", "Provérbios", "Provérbios 3:5-6", "'Confia no Senhor de todo o teu coração, e não te estribes no teu próprio entendimento. Reconhece-o em todos os teus caminhos, e ele endireitará as tuas veredas'.")
    add("A qual pequeno inseto sábio e trabalhador o preguiçoso é mandado observar em Provérbios 6:6?",
        "À formiga", "À abelha", "À aranha", "Ao gafanhoto",
        "facil", "Provérbios", "Provérbios 6:6", "'Vai ter com a formiga, ó preguiçoso; olha para os seus caminhos, e sê sábio'.")
    add("Quantas coisas abomina a alma do Senhor listadas expressamente em Provérbios 6:16-19?",
        "Seis coisas Deus odeia, e a sétima a sua alma abomina", "Dez coisas", "Doze mandamentos", "Três faltas capitais",
        "medio", "Provérbios", "Provérbios 6:16", "'Seis coisas o Senhor odeia, e a sétima a sua alma abomina: olhos altivos, língua mentirosa, mãos que derramam sangue inocente...'.")
    add("Qual é o efeito de uma resposta branda sobre a ira segundo Provérbios 15:1?",
        "A resposta branda desvia o furor, mas a palavra dura suscita a ira", "Aumenta a discórdia", "Mostra fraqueza de caráter", "Provoca mais brigas",
        "facil", "Provérbios", "Provérbios 15:1", "'A resposta branda desvia o furor, mas a palavra dura suscita a ira'.")
    add("O que precede a ruína e a queda segundo Provérbios 16:18?",
        "A soberba e a altivez de espírito", "A pobreza material", "A falta de amigos", "O excesso de trabalho",
        "facil", "Provérbios", "Provérbios 16:18", "'A soberba precede a ruína, e a altivez do espírito precede a queda'.")
    add("O que o coração alegre causa ao corpo humano segundo Provérbios 17:22?",
        "É bom remédio para a saúde, mas o espírito abatido seca os ossos", "Provoca cansaço", "Atrai inveja", "Diminui a vigilância",
        "facil", "Provérbios", "Provérbios 17:22", "'O coração alegre é como o bom remédio, mas o espírito abatido seca até os ossos'.")
    add("Qual declaração sobre amizade verdadeira está registrada em Provérbios 18:24?",
        "'Há amigo mais chegado do que um irmão'", "'Nenhum amigo é confiável'", "'Os parentes são sempre os melhores amigos'", "'Amigo bom é o que empresta dinheiro'",
        "facil", "Provérbios", "Provérbios 18:24", "'O homem de muitos amigos pode congratular-se, mas há amigo mais chegado do que um irmão'.")
    add("O que Provérbios 22:1 afirma valer mais do que abundantes riquezas materiais?",
        "O bom nome e a estima do que a prata e o ouro", "Cem carruagens de ferro", "Um grande palácio em Sião", "A força física de campeão",
        "facil", "Provérbios", "Provérbios 22:1", "'Mais vale o bom nome do que as muitas riquezas; e o ser estimado é melhor do que a prata e o ouro'.")
    add("Qual mandamento fundamental aos pais sobre educação dos filhos está em Provérbios 22:6?",
        "'Ensina a criança no caminho em que deve andar, e até quando envelhecer não se desviará dele'", "'Deixa a criança seguir suas próprias vontades'", "'Não repreendas o filho para não entristecê-lo'", "'Entrega a educação apenas aos mestres'",
        "facil", "Provérbios", "Provérbios 22:6", "'Ensina a criança no caminho em que deve andar, e até quando envelhecer não se desviará dele'.")
    add("O que Provérbios 25:21-22 aconselha fazer se o teu inimigo tiver fome ou sede?",
        "Dá-lhe de comer pão e dá-lhe água a beber, amontoando brasas sobre a cabeça dele", "Ataca-o de surpresa", "Zomba de sua necessidade", "Foge de sua presença",
        "medio", "Provérbios", "Provérbios 25:21-22; Romanos 12:20", "'Se o teu inimigo tiver fome, dá-lhe pão para comer; e se tiver sede, dá-lhe água para beber; porque assim amontoarás brasas sobre a sua cabeça'.")
    add("Como é chamada a mulher descrita no célebre acróstico do capítulo 31 de Provérbios?",
        "A mulher virtuosa", "A noiva de ouro", "A rainha da sabedoria", "A matriarca de Judá",
        "facil", "Provérbios", "Provérbios 31:10", "'Mulher virtuosa, quem a achará? O seu valor muito excede ao de rubis'.")
    add("O que Provérbios 31:30 afirma contrastando a beleza passageira com o temor do Senhor?",
        "'Enganosa é a beleza e vã a formosura, mas a mulher que teme ao Senhor, essa será louvada'", "'A beleza física dura para sempre'", "'A formosura traz a verdadeira paz'", "'Quem é bela não precisa de sabedoria'",
        "facil", "Provérbios", "Provérbios 31:30", "'Enganosa é a graça, e vã a formosura, mas a mulher que teme ao Senhor, essa sim será louvada'.")
    add("O que o homem colérico faz segundo Provérbios 29:22?",
        "Suscita contendas e o furioso acumula transgressões", "Traz paz aos vizinhos", "Resolve os problemas da cidade", "Enriquece rapidamente",
        "medio", "Provérbios", "Provérbios 29:22", "'O homem colérico suscita contendas, e o furioso multiplica as transgressões'.")

    # --- ECLESIASTES e CANTARES (15 questões) ---
    add("Qual é a expressão emblemática repetida por Salomão (o Pregador) no livro de Eclesiastes?",
        "'Vaidade de vaidades, diz o Pregador; tudo é vaidade'", "'Glória e riquezas eternas na terra'", "'Não há limites para o poder humano'", "'Tudo é facilidade debaixo do sol'",
        "facil", "Eclesiastes", "Eclesiastes 1:2", "'Vaidade de vaidades, diz o pregador, vaidade de vaidades! Tudo é vaidade'.")
    add("O que Eclesiastes 3:1 afirma sobre o tempo e todas as atividades humanas?",
        "'Para tudo há uma ocasião certa, e tempo para todo o propósito debaixo do céu'", "'O tempo pertence aos reis'", "'Não há tempo para o descanso'", "'O futuro é mera ilusão'",
        "facil", "Eclesiastes", "Eclesiastes 3:1", "'Tudo tem o seu tempo determinado, e há tempo para todo o propósito debaixo do céu: tempo de nascer e tempo de morrer'.")
    add("O que Eclesiastes 4:12 declara sobre a força da união e o cordão de três dobras?",
        "'Um cordão de três dobras não se quebra facilmente'", "'Um homem sozinho é invencível'", "'Mais vale o ouro do que dois companheiros'", "'O isolamento preserva a força'",
        "facil", "Eclesiastes", "Eclesiastes 4:12", "'E, se alguém prevalecer contra um, os dois lhe resistirão; e o cordão de três dobras não se quebra tão depressa'.")
    add("Qual exortação aos jovens sobre lembrar-se de Deus está registrada em Eclesiastes 12:1?",
        "'Lembra-te do teu Criador nos dias da tua mocidade, antes que venham os maus dias'", "'Aproveita a juventude sem pensar em Deus'", "'Espera envelhecer para orar'", "'Acumula tesouros na mocidade'",
        "facil", "Eclesiastes", "Eclesiastes 12:1", "'Lembra-te também do teu Criador nos dias da tua mocidade, antes que venham os maus dias, e cheguem os anos dos quais venhas a dizer: Não tenho neles contentamento'.")
    add("Qual é a sublime conclusão de todo o discurso e dever do homem em Eclesiastes 12:13?",
        "'Teme a Deus e guarda os seus mandamentos, porque isto é o dever de todo homem'", "'Busca as delícias da carne'", "'Conquista reinos e constrói monumentos'", "'Vive isolado nas montanhas'",
        "facil", "Eclesiastes", "Eclesiastes 12:13", "'De tudo o que se tem ouvido, o fim é: Teme a Deus, e guarda os seus mandamentos; porque isto é o dever de todo o homem'.")
    add("Qual declaração arrebatadora sobre o poder do amor está em Cantares de Salomão 8:6?",
        "'Porque o amor é forte como a morte, e duro como a sepultura o ciúme'", "'O amor passa como as nuvens'", "'O amor é frágil como a folha seca'", "'O amor se compra com prata'",
        "facil", "Cantares", "Cantares 8:6", "'Põe-me como selo sobre o teu coração, como selo sobre o teu braço, porque o amor é forte como a morte'.")
    add("O que Cantares de Salomão 8:7 afirma que nem mesmo as muitas águas poderiam fazer?",
        "'As muitas águas não poderiam apagar este amor, nem os rios afogá-lo'", "'Não poderiam molhar o manto da noiva'", "'Não poderiam saciar a sede do rei'", "'Não poderiam lavar os pecados'",
        "facil", "Cantares", "Cantares 8:7", "'As muitas águas não podem apagar este amor, nem os rios afogá-lo; ainda que alguém desse todos os bens de sua casa pelo amor, certamente a desprezariam'.")
    add("Como a noiva sulamita se descreve com formosura em Cantares 2:1?",
        "'Eu sou a rosa de Sarom, o lírio dos vales'", "'Eu sou a palmeira do deserto'", "'Eu sou a oliveira de Sião'", "'Eu sou a pérola de Ofir'",
        "facil", "Cantares", "Cantares 2:1", "'Eu sou a rosa de Sarom, o lírio dos vales. Qual o lírio entre os espinhos, tal é o meu amor entre as filhas'.")

    # --- Salmos Adicionais ---
    add("Qual versículo de louvor e exaltação aos céus abre o Salmo 19 de Davi?",
        "'Os céus declaram a glória de Deus e o firmamento anuncia as obras das suas mãos'", "'Grande é o poder dos reis da terra'", "'Cantai ao Senhor sobre os montes'", "'Louvem o sol e a lua'",
        "facil", "Salmos", "Salmo 19:1", "'Os céus declaram a glória de Deus e o firmamento anuncia a obra das suas mãos. Um dia faz declaração a outro dia'.")
    add("Quem entrará e habitará no santo tabernáculo de Deus segundo o Salmo 15:1-2?",
        "'Aquele que anda em integridade, e pratica a justiça, e fala a verdade no seu coração'", "'Quem constrói grandes monumentos de pedra'", "'Quem possui muito ouro para doar'", "'Quem marcha com carros de guerra'",
        "facil", "Salmos", "Salmo 15:1-2", "'Senhor, quem habitará no teu tabernáculo? Aquele que anda sinceramente, e pratica a justiça, e fala a verdade no seu coração'.")
    add("A quem o Salmo 24:1 declara pertencer toda a terra e os que nela habitam?",
        "'Do Senhor é a terra e a sua plenitude, o mundo e aqueles que nele habitam'", "'Pertence aos governantes poderosos'", "'Pertence àqueles que trabalham a terra'", "'Pertence aos anjos celestes'",
        "facil", "Salmos", "Salmo 24:1", "'Do Senhor é a terra e a sua plenitude, o mundo e aqueles que nele habitam; porque ele a fundou sobre os mares'.")
    add("Qual declaração corajosa de fé abre o Salmo 27:1?",
        "'O Senhor é a minha luz e a minha salvação; a quem temerei? O Senhor é a fortaleza da minha vida'", "'Eu confio na força da minha espada'", "'Grandes são as muralhas de Sião'", "'Não temo porque possuo riqueza'",
        "facil", "Salmos", "Salmo 27:1", "'O Senhor é a minha luz e a minha salvação; a quem temerei? O Senhor é a força da minha vida; de quem me recearei?'.")
    add("Qual promessa angelical de proteção aos que temem a Deus está em Salmos 34:7?",
        "'O anjo do Senhor acampa-se ao redor dos que o temem, e os livra'", "'Um exército humano os guardará'", "'Nenhuma dor tocará os seus corpos'", "'Receberão coroas de prata'",
        "facil", "Salmos", "Salmo 34:7", "'O anjo do Senhor acampa-se ao redor dos que o temem, e os livra. Provai e vede que o Senhor é bom; bem-aventurado o homem que nele confia'.")
    add("Qual convite gracioso de experiência pessoal com Deus está em Salmos 34:8?",
        "'Provai e vede que o Senhor é bom; bem-aventurado o homem que nele se refugia'", "'Contemplai a beleza das montanhas'", "'Lede os livros dos sábios do oriente'", "'Guardai silêncio perante os altares'",
        "facil", "Salmos", "Salmo 34:8", "'Provai, e vede que o Senhor é bom; bem-aventurado o homem que nele confia'.")
    add("Qual mandamento de descanso na fidelidade divina está em Salmos 37:5?",
        "'Entrega o teu caminho ao Senhor; confia nele, e ele tudo fará'", "'Planeja tudo sozinho e prosperarás'", "'Não descanses até acumulares tesouros'", "'Espera socorro dos governantes'",
        "facil", "Salmos", "Salmo 37:5", "'Entrega o teu caminho ao Senhor; confia nele, e ele o fará. E ele fará sobressair a tua justiça como a luz'.")
    add("Qual testemunho sobre a provisão de Deus aos justos ao longo da vida está em Salmos 37:25?",
        "'Fui moço, e agora sou velho; mas nunca vi desamparado o justo, nem a sua semente a mendigar o pão'", "'Vi os ímpios governarem para sempre'", "'A riqueza material não depende de Deus'", "'O mundo esquece os que praticam o bem'",
        "facil", "Salmos", "Salmo 37:25", "'Fui moço, e agora sou velho; contudo nunca vi desamparado o justo, nem a sua semente a mendigar o pão'.")
    add("Qual declaração de paciência na oração atendida abre o Salmo 40:1-2?",
        "'Esperei com paciência no Senhor, e ele se inclinou para mim, e ouviu o meu clamor'", "'Clamei uma só vez e desisti'", "'Fiz ofertas de prata no altar'", "'Procurei conselho com adivinhos'",
        "facil", "Salmos", "Salmo 40:1-2", "'Esperei com paciência no Senhor, e ele se inclinou para mim, e ouviu o meu clamor; tirou-me de um lago horrível, pôs os meus pés sobre uma rocha'.")
    add("A que o salmista compara o anseio ardente de sua alma por Deus no Salmo 42:1?",
        "'Como a corça suspira pelas correntes das águas, assim suspira a minha alma por ti, ó Deus'", "'Como o leão busca a presa'", "'Como o pássaro foge da tempestade'", "'Como o mercador busca o ouro'",
        "facil", "Salmos", "Salmo 42:1", "'Como o cervo brama pelas correntes das águas, assim suspira a minha alma por ti, ó Deus! A minha alma tem sede de Deus, do Deus vivo'.")
    add("Qual versículo de abrigo inabalável abre o Salmo 46:1?",
        "'Deus é o nosso refúgio e fortaleza, socorro bem presente na angústia'", "'O Senhor habita nos altos céus sozinho'", "'Nossas armas garantem a tranquilidade'", "'O mar nos protege dos exércitos'",
        "facil", "Salmos", "Salmo 46:1", "'Deus é o nosso refúgio e fortaleza, socorro bem presente na angústia. Portanto não temeremos, ainda que a terra se mude'.")
    add("Qual ordem divina de quietude e confiança está registrada em Salmos 46:10?",
        "'Aquietai-vos e sabei que eu sou Deus; serei exaltado entre as nações'", "'Gritai com força para que vos ouça'", "'Correi de um lado para o outro'", "'Reuni todos os generais'",
        "facil", "Salmos", "Salmo 46:10", "'Aquietai-vos, e sabei que eu sou Deus; serei exaltado entre os gentios; serei exaltado sobre a terra'.")
    add("O que o salmista declara a respeito do amor e bondade de Deus em Salmos 63:3?",
        "'Porque a tua graça (benignidade) é melhor do que a vida; os meus lábios te louvarão'", "'Porque o ouro é o que traz a paz'", "'Porque a glória militar enaltece o rei'", "'Porque o mundo passa rapidamente'",
        "facil", "Salmos", "Salmo 63:3", "'Porque a tua benignidade é melhor do que a vida, os meus lábios te louvarão; assim eu te bendirei enquanto viver'.")
    add("O que Salmos 84:10 afirma a respeito de habitar na Casa de Deus?",
        "'Porque vale mais um dia nos teus átrios do que em outra parte mil'", "'Mais vale um dia no palácio dos reis'", "'Mais vale um dia no comércio de Tiro'", "'O templo é igual a qualquer casa'",
        "facil", "Salmos", "Salmo 84:10", "'Porque vale mais um dia nos teus átrios do que mil. Preferiria estar à porta da casa do meu Deus, a habitar nas tendas dos ímpios'.")
    add("Qual versículo de autoexortação ao louvor abre o Salmo 103 de Davi?",
        "'Bendize, ó minha alma, ao Senhor, e tudo o que há em mim bendiga o seu santo nome'", "'Descansa, ó alma, e dorme em paz'", "'Chora, ó alma, pela tua dor'", "'Desperta para a peleja'",
        "facil", "Salmos", "Salmo 103:1", "'Bendize, ó minha alma, ao Senhor, e tudo o que há em mim bendiga o seu santo nome. Bendize, ó minha alma, ao Senhor, e não te esqueças de nenhum de seus benefícios'.")
    add("Quais são os primeiros benefícios divinos lembrados no Salmo 103:3?",
        "'É ele quem perdoa todas as tuas iniquidades e sara todas as tuas enfermidades'", "'É ele quem te dá cavalos de guerra'", "'É ele quem te faz vencer os reis'", "'É ele quem te enche de moedas de prata'",
        "facil", "Salmos", "Salmo 103:3", "'É ele quem perdoa todas as tuas iniquidades, quem sara todas as tuas enfermidades, quem redime a tua vida da perdição'.")
    add("O que Salmos 103:12 afirma sobre o afastamento dos nossos pecados perdoados por Deus?",
        "'Quanto está longe o oriente do ocidente, assim afasta de nós as nossas transgressões'", "'Ele os guarda para o julgamento'", "'Ele os esconde debaixo das pedras'", "'Ele os lembra a cada ano'",
        "facil", "Salmos", "Salmo 103:12", "'Quanto está longe o oriente do ocidente, assim afasta de nós as nossas transgressões. Como um pai se compadece de seus filhos, assim o Senhor se compadece dos que o temem'.")
    add("Qual profecia messiânica sobre a pedra angular está em Salmos 118:22?",
        "'A pedra que os edificadores rejeitaram tornou-se a cabeça da esquina'", "'O templo será de ouro batido'", "'O rei usará coroa de ferro'", "'Uma muralha cercará o deserto'",
        "medio", "Salmos", "Salmo 118:22; Mateus 21:42", "'A pedra que os edificadores rejeitaram tornou-se a cabeça da esquina. Da parte do Senhor se fez isto; maravilhoso é aos nossos olhos'.")
    add("A que são comparados os que confiam no Senhor no Salmo 125:1?",
        "'São como o monte de Sião, que não se abala, mas permanece para sempre'", "'São como as ondas do mar'", "'São como a folha seca que voa'", "'São como nuvens sem água'",
        "facil", "Salmos", "Salmo 125:1", "'Os que confiam no Senhor serão como o monte de Sião, que não se abala, mas permanece para sempre. Como estão os montes à roda de Jerusalém, assim o Senhor está em redor do seu povo'.")
    add("O que Salmos 126:5 afirma a respeito dos que semeiam com sofrimento e lágrimas?",
        "'Os que semeiam em lágrimas segarão com alegria'", "'Perderão todo o seu trabalho'", "'Nunca mais verão as sementes brotarem'", "'Ficarão desamparados no campo'",
        "facil", "Salmos", "Salmo 126:5-6", "'Os que semeiam em lágrimas segarão com alegria. Aquele que leva a preciosa semente, andando e chorando, voltará com alegria, trazendo consigo os seus molhos'.")
    add("Qual refrão de louvor é repetido em todos os 26 versículos do Salmo 136?",
        "'Porque a sua misericórdia dura para sempre'", "'Porque o seu reino é eterno'", "'Glória ao Senhor dos Exércitos'", "'Louvem o seu santo nome'",
        "facil", "Salmos", "Salmo 136", "O Salmo 136 repete em cada versículo: 'Louvai ao Senhor, porque ele é bom; porque a sua benignidade/misericórdia dura para sempre'.")
    add("Onde os cativos exilados de Judá choravam lembrando-se de Sião no Salmo 137?",
        "'Junto aos rios de Babilônia nos assentamos e choramos, lembrando-nos de Sião'", "'Nos desertos de Edom'", "'Nos portões de Nínive'", "'Nas montanhas de Samaria'",
        "facil", "Salmos", "Salmo 137:1", "'Junto aos rios de Babilônia nos assentamos e choramos, lembrando-nos de Sião. Nos salgueiros penduramos as nossas harpas'.")
    add("O que o Salmo 145:18 afirma sobre a proximidade do Senhor para com os que oram?",
        "'Perto está o Senhor de todos os que o invocam, de todos os que o invocam em verdade'", "'Deus só ouve os reis e sacerdotes'", "'Deus está longe demais para escutar'", "'A oração só tem valor no templo de pedra'",
        "facil", "Salmos", "Salmo 145:18", "'Perto está o Senhor de todos os que o invocam, de todos os que o invocam em verdade. Ele cumprirá o desejo dos que o temem'.")
    add("Qual convite a guardar o coração com diligência máxima está em Provérbios 4:23?",
        "'Sobre tudo o que se deve guardar, guarda o teu coração, porque dele procedem as fontes da vida'", "'Guarda o teu ouro nos cofres'", "'Guarda as tuas armas de ferro'", "'Guarda a tua casa com muralhas'",
        "facil", "Provérbios", "Provérbios 4:23", "'Sobre tudo o que se deve guardar, guarda o teu coração, porque dele procedem as saídas da vida'.")
    add("O que Provérbios 10:22 afirma sobre a riqueza concedida por Deus?",
        "'A bênção do Senhor enriquece, e ele não acrescenta dores com ela'", "'O dinheiro sempre traz angústia'", "'Toda riqueza vem da opressão'", "'Mais vale ser miserável para ser humilde'",
        "facil", "Provérbios", "Provérbios 10:22", "'A bênção do Senhor é que enriquece; e não acrescenta dores com ela'.")
    add("O que Provérbios 11:14 afirma sobre a importância de buscar conselhos prudentes?",
        "'Onde não há conselho, os planos fracassam; mas na multidão de conselheiros há segurança'", "'O homem deve decidir tudo sozinho sem ouvir ninguém'", "'Conselhos demonstram fraqueza de caráter'", "'Mais vale seguir a própria intuição'",
        "facil", "Provérbios", "Provérbios 11:14", "'Não havendo sábios conselhos, o povo cai, mas na multidão de conselhos há segurança'.")
    add("O que Provérbios 13:20 ensina sobre as companhias e amizades?",
        "'Quem anda com os sábios será sábio, mas o companheiro dos tolos será afligido / destruído'", "'Todos os homens pensam da mesma forma'", "'As companhias não influenciam ninguém'", "'É melhor andar com os ímpios'",
        "facil", "Provérbios", "Provérbios 13:20", "'O que anda com os sábios ficará sábio, mas o companheiro dos tolos será destruído'.")
    add("O que Provérbios 14:1 declara a respeito da mulher sábia e da tola?",
        "'Toda mulher sábia edifica a sua casa, mas a tola a derruba com as próprias mãos'", "'A mulher deve cuidar apenas das roupas'", "'A mulher tola constrói palácios'", "'A sabedoria feminina não altera o lar'",
        "facil", "Provérbios", "Provérbios 14:1", "'Toda mulher sábia edifica a sua casa; mas a tola a derruba com as suas mãos'.")
    add("Qual alerta sobre caminhos aparentemente corretos que levam à perdição está em Provérbios 14:12 e 16:25?",
        "'Há caminho que ao homem parece direito, mas o fim dele são os caminhos da morte'", "'Todo caminho humano agrada a Deus'", "'A maioria sempre está com a razão'", "'Não há perigo nos caminhos largos'",
        "facil", "Provérbios", "Provérbios 14:12; 16:25", "'Há um caminho que ao homem parece direito, mas o fim dele são os caminhos da morte'.")
    add("O que Provérbios 14:34 afirma que verdadeiramente exalta uma nação?",
        "'A justiça exalta as nações, mas o pecado é o opróbrio dos povos'", "'O poder dos exércitos e das carruagens'", "'A abundância de comércio com outras terras'", "'A extensão das suas fronteiras'",
        "facil", "Provérbios", "Provérbios 14:34", "'A justiça exalta as nações, mas o pecado é o opróbrio dos povos'.")
    add("Onde os olhos do Senhor estão segundo Provérbios 15:3?",
        "'Os olhos do Senhor estão em todo lugar, contemplando os maus e os bons'", "'Apenas no céu observando os anjos'", "'Somente no templo de Jerusalém'", "'Apenas nos palácios reais'",
        "facil", "Provérbios", "Provérbios 15:3", "'Os olhos do Senhor estão em todo lugar, vigiando os maus e os bons'.")
    add("O que Provérbios 16:3 nos ensina a fazer com nossos projetos e realizações?",
        "'Confia ao Senhor as tuas obras, e os teus pensamentos serão estabelecidos'", "'Faz tudo com tuas próprias forças'", "'Esconde teus planos para ninguém copiar'", "'Confia na tua própria inteligência'",
        "facil", "Provérbios", "Provérbios 16:3", "'Confia ao Senhor as tuas obras, e teus pensamentos serão estabelecidos'.")
    add("O que Provérbios 16:9 ensina sobre os planos do coração humano e o governo divino?",
        "'O coração do homem planeja o seu caminho, mas o Senhor lhe dirige os passos'", "'O homem é o único arquiteto do seu destino'", "'Deus não interfere nas decisões terrenas'", "'A sorte rege todos os caminhos'",
        "facil", "Provérbios", "Provérbios 16:9", "'O coração do homem planeja o seu caminho, mas o Senhor lhe dirige os passos'.")
    add("A que as palavras suaves e agradáveis são comparadas em Provérbios 16:24?",
        "'Favo de mel, doces para a alma e saúde para os ossos'", "'Vinho que inebria'", "'Água que apaga o fogo'", "'Frutas da estação'",
        "facil", "Provérbios", "Provérbios 16:24", "'As palavras suaves são favos de mel, doces para a alma, e saúde para os ossos'.")
    add("Qual provérbio sobre lealdade fraternal está em Provérbios 17:17?",
        "'Em todo o tempo ama o amigo; e na angústia nasce o irmão'", "'O amigo só aparece nos banquetes'", "'O irmão é sempre um rival'", "'Na hora da crise todos se afastam'",
        "facil", "Provérbios", "Provérbios 17:17", "'Em todo o tempo ama o amigo; e na angústia nasce o irmão'.")
    add("A quem o homem caridoso empresta quando se compadece do necessitado em Provérbios 19:17?",
        "'Ao Senhor empresta o que se compadece do pobre, e ele lhe pagará o seu benefício'", "'Ao rei da cidade'", "'Aos sacerdotes do templo'", "'Aos próprios vizinhos'",
        "facil", "Provérbios", "Provérbios 19:17", "'Ao Senhor empresta o que se compadece do pobre, ele lhe pagará o seu benefício'.")
    add("O que Provérbios 20:1 adverte com clareza a respeito do vinho e da bebida alcoólica forte?",
        "'O vinho é escarnecedor, e a bebida forte alvoroçadora; todo aquele que por eles é enganado não é sábio'", "'O vinho traz sabedoria ao jovem'", "'A bebida forte fortalece o guerreiro'", "'O homem sábio deve beber diariamente'",
        "facil", "Provérbios", "Provérbios 20:1", "'O vinho é escarnecedor, e a bebida forte alvoroçadora; e todo aquele que neles errar nunca será sábio'.")
    add("A que o coração do rei é comparado nas mãos soberanas do Senhor em Provérbios 21:1?",
        "'Como ribeiros de águas assim é o coração do rei na mão do Senhor; a tudo quanto quer o inclina'", "'Como uma rocha imutável'", "'Como um leão indomável'", "'Como uma espada de ferro'",
        "medio", "Provérbios", "Provérbios 21:1", "'Como ribeiros de águas assim é o coração do rei na mão do Senhor, que o inclina a todo o seu querer'.")
    add("Por que Provérbios 27:1 nos adverte contra nos gabarmos do dia de amanhã?",
        "'Não presumas do dia de amanhã, porque não sabes o que o dia trará'", "'Porque o passado é mais importante'", "'Porque o amanhã nunca chega'", "'Porque o homem não deve sonhar'",
        "facil", "Provérbios", "Provérbios 27:1", "'Não presumas do dia de amanhã, porque não sabes o que produzirá o dia'.")
    add("A que é comparada a edificação e o aperfeiçoamento mútuo entre dois amigos em Provérbios 27:17?",
        "'Como o ferro com o ferro se aguça, assim o homem afia o rosto do seu amigo'", "'Como duas tochas que queimam juntas'", "'Como dois rios que deságuam no mar'", "'Como duas árvores que dão frutos'",
        "facil", "Provérbios", "Provérbios 27:17", "'Como o ferro com o ferro se aguça, assim o homem afia o rosto do seu amigo'.")
    add("O que acontece com aquele que encobre as suas transgressões em contraste com quem as confessa e abandona segundo Provérbios 28:13?",
        "'O que encobre as suas transgressões nunca prosperará; mas o que as confessa e deixa, alcançará misericórdia'", "'Quem as esconde terá paz perpétua'", "'Quem as confessa será rejeitado para sempre'", "'Não há diferença diante de Deus'",
        "facil", "Provérbios", "Provérbios 28:13", "'O que encobre as suas transgressões nunca prosperará, mas o que as confessa e deixa, alcançará misericórdia'.")
    add("O que Provérbios 30:5 afirma a respeito de toda a Palavra revelada por Deus?",
        "'Toda palavra de Deus é pura; ele é escudo para os que nele confiam'", "'A palavra humana tem o mesmo valor'", "'Algumas palavras de Deus podem falhar'", "'Apenas os Dez Mandamentos são puros'",
        "facil", "Provérbios", "Provérbios 30:5", "'Toda a Palavra de Deus é pura; escudo é para os que confiam nele. Nada acrescentes às suas palavras, para que não te repreenda'.")
    add("Qual conselho sobre o trabalho empenhado com diligência está em Eclesiastes 9:10?",
        "'Tudo quanto te vier à mão para fazer, faze-o conforme as tuas forças'", "'Trabalha apenas quando fores obrigado'", "'Deixa para fazer amanhã'", "'Trabalha somente pelo ouro'",
        "facil", "Eclesiastes", "Eclesiastes 9:10", "'Tudo quanto te vier à mão para fazer, faze-o conforme as tuas forças; porque na sepultura para onde tu vais não há obra nem projeto'.")
    add("Qual princípio sobre a generosidade e a partilha está registrado em Eclesiastes 11:1?",
        "'Lança o teu pão sobre as águas, porque depois de muitos dias o acharás'", "'Guarda todo o pão em celeiros fechados'", "'Não dês comida aos forasteiros'", "'Vende teu alimento pelo maior preço'",
        "facil", "Eclesiastes", "Eclesiastes 11:1", "'Lança o teu pão sobre as águas, porque depois de muitos dias o acharás. Reparte com sete, e ainda até com oito'.")
    add("O que Jó 23:10 declara com confiança a respeito das provações divinas purificadoras?",
        "'Mas ele sabe o meu caminho; provando-me ele, sairei como o ouro'", "'Deus me abandonou nas trevas'", "'Nunca mais recuperarei a alegria'", "'O sofrimento é apenas perda de tempo'",
        "facil", "Jó", "Jó 23:10", "'Mas ele sabe o meu caminho; provando-me ele, sairei como o ouro. Nos seus passos os meus pés se mantiveram'.")
    add("O que Jó 28:28 proclama ser a verdadeira sabedoria para o ser humano?",
        "'Eis que o temor do Senhor é a sabedoria, e apartar-se do mal é o entendimento'", "'Conhecer a filosofia das nações'", "'Acumular conhecimentos científicos'", "'Descobrir as minas de pedras preciosas'",
        "facil", "Jó", "Jó 28:28", "'E disse ao homem: Eis que o temor do Senhor é a sabedoria, e apartar-se do mal é o entendimento'.")
    add("Qual o verso célebre de abertura de Cantares de Salomão 1:2?",
        "'Beije-me ele com os beijos da sua boca; porque melhor é o teu amor do que o vinho'", "'Ouvi a voz dos guerreiros de Sião'", "'Levantai os escudos no palácio'", "'Grande é a rainha do sul'",
        "facil", "Cantares", "Cantares 1:2", "'Beije-me ele com os beijos da sua boca; porque melhor é o teu amor do que o vinho. Suave é o aroma dos teus unguentos'.")
    add("Qual estandarte de triunfo e ternura o amado estendeu sobre a noiva em Cantares 2:4?",
        "'Levou-me à sala do banquete, e o seu estandarte sobre mim era o amor'", "'Uma bandeira de batalha com espadas'", "'Um véu de ouro maciço'", "'Um manto de púrpura imperial'",
        "facil", "Cantares", "Cantares 2:4", "'Levou-me à sala do banquete, e o seu estandarte sobre mim era o amor. Sustentai-me com passas, confortai-me com maçãs'.")
    add("Qual comparação sublime o amado faz à sua noiva em Cantares 4:7?",
        "'Tu és toda formosa, meu amor, e em ti não há mancha'", "'Tu és forte como um guerreiro'", "'Tu és severa como as leis'", "'Tu és como o ouro de Ofir'",
        "facil", "Cantares", "Cantares 4:7", "'Tu és toda formosa, meu amor, e em ti não há mancha. Vem comigo do Líbano, minha esposa'.")
    add("O que Eclesiastes 7:1 afirma valer mais do que um fino unguento aromático?",
        "'Melhor é a boa fama do que o melhor unguento, e o dia da morte do que o dia do nascimento'", "'O vinho fino das vinhas de En-Gedi'", "'As roupas de linho egípcio'", "'O azeite perfumado dos reis'",
        "medio", "Eclesiastes", "Eclesiastes 7:1", "'Melhor é a boa fama do que o melhor unguento; e o dia da morte do que o dia do nascimento de alguém'.")
    add("Como Jó respondeu perante o mistério de Deus no capítulo 40:4?",
        "'Eis que sou vil; que te responderia eu? A minha mão ponho à boca'", "'Eu te vencerei em argumentos'", "'Não aceito o teu juízo'", "'Quero que me restaures agora'",
        "medio", "Jó", "Jó 40:4", "'Eis que sou vil; que te responderia eu? A minha mão ponho à boca. Uma vez falei e não replicarei'.")
    add("Qual cântico de júbilo e gratidão abre o Salmo 107 conclamando os redimidos?",
        "'Louvai ao Senhor, porque ele é bom, porque a sua benignidade dura para sempre'", "'Cantai hinos aos generais da terra'", "'Aplaudi com palmas a vitória militar'", "'Guardai silêncio absoluto'",
        "facil", "Salmos", "Salmo 107:1-2", "'Louvai ao Senhor, porque ele é bom, porque a sua misericórdia dura para sempre. Digam-no os remidos do Senhor'.")

    return items[:130]

if __name__ == "__main__":
    q_list = get_poetic_questions()
    print(f"Poetic generated: {len(q_list)} questions")
