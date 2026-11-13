# -*- coding: utf-8 -*-
"""
Gerador de 60 questões bíblicas de Apocalipse (Revelação).
Livro: Apocalipse capítulos 1 a 22.
"""

def get_revelation_questions():
    items = []

    def add(q, c, w1, w2, w3, diff, ref, exp):
        items.append({
            "q": q,
            "c": c,
            "w1": w1,
            "w2": w2,
            "w3": w3,
            "diff": diff,
            "book": "Apocalipse",
            "testament": "NT",
            "section": "Apocalipse",
            "ref": ref,
            "exp": exp
        })

    # --- CAPÍTULO 1 ---
    add("Em qual ilha o apóstolo João se achava no exílio quando recebeu a revelação do Apocalipse?",
        "Ilha de Patmos", "Ilha de Chipre", "Ilha de Creta", "Ilha de Malta",
        "facil", "Apocalipse 1:9", "João estava na ilha chamada Patmos por causa da palavra de Deus e do testemunho de Jesus.")
    add("Em qual dia da semana João declara que foi arrebatado em espírito em Apocalipse 1:10?",
        "No dia do Senhor (domingo)", "No dia do sábado solene", "No primeiro dia do ano civil", "No dia da lua nova",
        "facil", "Apocalipse 1:10", "João foi arrebatado em espírito no Dia do Senhor e ouviu uma voz como de trombeta.")
    add("Como Jesus glorificado Se identifica na abertura solene do Apocalipse em Apocalipse 1:8?",
        "'Eu sou o Alfa e o Ômega, o princípio e o fim, o que é, o que era e o que há de vir, o Todo-Poderoso'",
        "'Eu sou o mestre de Nazaré'",
        "'Eu sou um anjo enviado do trono'",
        "'Eu sou o rei militar dos séculos'",
        "facil", "Apocalipse 1:8", "Cristo revela Sua soberania absoluta e eternidade como a primeira e última letra do alfabeto grego.")
    add("Como eram os olhos e os pés do Filho do Homem na visão triunfante de Apocalipse 1:14-15?",
        "Olhos como chama de fogo e pés semelhantes a latão reluzente",
        "Olhos vendados e pés descalços feridos",
        "Olhos azuis serenos e pés de ouro puro",
        "Olhos brilhando em trevas e pés de ferro escuro",
        "facil", "Apocalipse 1:14-15", "Os olhos de fogo simbolizam a onisciência perscrutadora e os pés de latão o juízo irrepreensível.")
    add("O que o Cristo glorificado segurava em Sua mão direita na visão de Apocalipse 1:16?",
        "Sete estrelas", "Sete taças de ouro", "Uma espada de ferro", "Um cetro de marfim",
        "facil", "Apocalipse 1:16", "As sete estrelas representam os mensageiros (anjos/pastores) das sete igrejas.")
    add("O que saía da boca do Filho do Homem na visão joanina de Apocalipse 1:16?",
        "Uma afiada espada de dois gumes", "Um rio de águas cristalinas", "Uma labareda de enxofre", "Uma harpa celestial",
        "facil", "Apocalipse 1:16", "A espada afiada de dois gumes simboliza a autoridade soberana e o poder julgador da Palavra de Deus.")
    add("O que representam os sete candeeiros (castiçais) de ouro segundo a explicação de Jesus em Apocalipse 1:20?",
        "As sete igrejas da Ásia Menor", "Os sete planetas do céu", "Os sete dias da criação", "Os sete reis de Roma",
        "facil", "Apocalipse 1:20", "Os candeeiros de ouro representam as igrejas, chamadas a resplandecer a luz de Cristo nas trevas.")

    # --- CAPÍTULOS 2 E 3 (AS SETE IGREJAS) ---
    add("Qual elogio e qual repreensão a igreja de Éfeso recebeu em Apocalipse 2:2-4?",
        "Elogiada pelo trabalho e perseverança, mas repreendida por ter abandonado o seu primeiro amor",
        "Elogiada pela caridade, mas repreendida por praticar feitiçaria",
        "Elogiada pela riqueza material, mas repreendida pela preguiça",
        "Elogiada pela música litúrgica, mas repreendida pela discórdia",
        "facil", "Apocalipse 2:2-4", "Jesus ordenou a Éfeso: 'Lembra-te, pois, de onde caíste, e arrepende-te, e pratica as primeiras obras'.")
    add("Qual promessa solene Cristo fez à igreja perseguida de Esmirna em Apocalipse 2:10?",
        "'Sê fiel até à morte, e dar-te-ei a coroa da vida'",
        "'Eu te livrarei de qualquer dor na terra'",
        "'Far-te-ei reinar sobre o imperador romano'",
        "'Receberás montanhas de ouro da Ásia'",
        "facil", "Apocalipse 2:10", "A igreja de Esmirna enfrentava prisão e tribulação, mas recebeu a promessa da coroa da vida eterna.")
    add("O que Jesus reprovou na igreja de Pérgamo em Apocalipse 2:14-15?",
        "A tolerância com os que sustentavam a doutrina de Balaão e dos nicolaítas",
        "A falta de dízimos e ofertas",
        "O esquecimento do templo judaico",
        "A desobediência às autoridades imperiais",
        "medio", "Apocalipse 2:14-15", "Pérgamo tolerava falsos ensinos que induziam os crentes à idolatria e imoralidade.")
    add("Qual profetisa perversa e imoral a igreja de Tiatira tolerava segundo Apocalipse 2:20?",
        "Jezabel", "Atalia", "Herodias", "Safira",
        "medio", "Apocalipse 2:20", "Cristo reprovou Tiatira por permitir que a mulher Jezabel enganasse os servos de Deus.")
    add("Qual era o trágico estado espiritual da igreja de Sardes descrito em Apocalipse 3:1?",
        "Tinha nome de que vivia, mas estava morta",
        "Era muito pobre financeiramente",
        "Estava sendo destruída por guerras externas",
        "Era perseguida dia e noite por leões",
        "facil", "Apocalipse 3:1", "Sardes desfrutava de boa reputação exterior, mas espiritualmente estava morta diante de Deus.")
    add("Qual oportunidade sem precedentes Cristo colocou diante da fiel igreja de Filadélfia em Apocalipse 3:8?",
        "Uma porta aberta diante dela que ninguém pode fechar",
        "A posse de todas as minas da Lídia",
        "Um exército de dez mil soldados",
        "O domínio político sobre Éfeso",
        "facil", "Apocalipse 3:8", "Filadélfia guardou a palavra com pouca força e Cristo lhe franqueou uma porta aberta inabalável.")
    add("Como Cristo descreveu a temperatura espiritual da igreja de Laodiceia em Apocalipse 3:15-16?",
        "Morno (nem frio nem quente), a ponto de vomitá-la de Sua boca",
        "Fervorosa como o fogo do altar",
        "Fria como as neves do monte Hermom",
        "Perfeita em todos os caminhos",
        "facil", "Apocalipse 3:15-16", "A autossuficiência e apatia de Laodiceia eram repulsivas ao Senhor.")
    add("Qual conselho gracioso Jesus dá a Laodiceia para sanar sua pobreza espiritual em Apocalipse 3:18?",
        "Comprar d'Ele ouro provado no fogo para enriquecer, vestes brancas para cobrir a vergonha e colírio para os olhos",
        "Investir em moedas cunhadas em Roma",
        "Construir mosteiros nas colinas vizinhas",
        "Contratar oradores da Grécia",
        "facil", "Apocalipse 3:18", "Cristo oferece verdadeira riqueza espiritual, justiça e discernimento salvador.")
    add("Qual célebre convite de comunhão íntima Jesus faz em Apocalipse 3:20?",
        "'Eis que estou à porta e bato; se alguém ouvir a minha voz e abrir a porta, entrarei em sua casa e cearei com ele, e ele comigo'",
        "'Eis que venho com espadas para destruir a tua casa'",
        "'Eis que fujo da terra para sempre'",
        "'Eis que exijo ofertas caras para te ouvir'",
        "facil", "Apocalipse 3:20", "Jesus bate pacientemente à porta do coração pedindo permissão para entrar em doce comunhão.")

    # --- CAPÍTULOS 4 E 5 (O TRONO E O LIVRO SELADO) ---
    add("Quantos anciãos estavam assentados ao redor do trono de Deus com vestes brancas e coroas de ouro em Apocalipse 4:4?",
        "Vinte e quatro anciãos", "Doze anciãos", "Setenta anciãos", "Cento e quarenta e quatro",
        "facil", "Apocalipse 4:4", "Os 24 anciãos representam o povo de Deus redimido de ambas as alianças ao redor do trono.")
    add("Quais eram as quatro figuras dos quatro seres viventes ao redor do trono em Apocalipse 4:7?",
        "Semelhantes a leão, novilho (bezerro), rosto de homem e águia voando",
        "Semelhantes a cavalo, lobo, falcão e serpente",
        "Semelhantes a anjo, peixe, ovelha e dragão",
        "Semelhantes a tigre, urso, leopardo e elefante",
        "facil", "Apocalipse 4:7", "Os seres viventes proclamam a santidade e majestade de Deus dia e noite sem cessar.")
    add("O que os quatro seres viventes proclamam dia e noite sem cessar diante do trono de Deus em Apocalipse 4:8?",
        "'Santo, Santo, Santo é o Senhor Deus, o Todo-Poderoso, que era, e que é, e que há de vir'",
        "'Glória aos reis da terra e aos seus generais'",
        "'Que o tempo pare para sempre'",
        "'O homem é o senhor do cosmos'",
        "facil", "Apocalipse 4:8", "O cântico incessante louva a santidade trina e a eternidade incontestável do Criador.")
    add("O que o livro que estava na mão direita dAquele assentado no trono continha em Apocalipse 5:1?",
        "Estava escrito por dentro e por fora, selado com sete selos",
        "Tinha apenas três páginas em branco",
        "Estava rasgado em pedaços",
        "Continha apenas leis em hebraico",
        "facil", "Apocalipse 5:1", "Nenhum ser criado no céu, na terra ou debaixo da terra podia abrir o livro ou olhar para ele.")
    add("Quem foi achado digno de abrir o livro e desatar os seus sete selos em Apocalipse 5:5-7?",
        "O Leão da tribo de Judá, a Raiz de Davi (o Cordeiro como havendo sido morto)",
        "O arcanjo Gabriel",
        "O profeta Moisés",
        "O rei Davi",
        "facil", "Apocalipse 5:5", "Cristo venceu pela Sua morte vicária na cruz, tornando-Se o único Digno de governar os destinos da história.")
    add("Quantos chifres e quantos olhos tinha o Cordeiro que estava no meio do trono em Apocalipse 5:6?",
        "Sete chifres e sete olhos, que são os sete Espíritos de Deus enviados por toda a terra",
        "Dois chifres e dois olhos humanos",
        "Quatro chifres de bronze e dez olhos",
        "Doze chifres de marfim e três olhos",
        "medio", "Apocalipse 5:6", "Os sete chifres simbolizam a onipotência perfeita e os sete olhos a onisciência do Espírito.")
    add("O que representam as taças de ouro cheias de incenso nas mãos dos vinte e quatro anciãos em Apocalipse 5:8?",
        "As orações dos santos", "O valor dos dízimos", "As lágrimas de arrependimento", "O sangue dos sacrifícios antigos",
        "facil", "Apocalipse 5:8", "As taças aromáticas de incenso personificam as preciosas súplicas dos santos que sobem a Deus.")

    # --- CAPÍTULO 6 (OS SETE SELOS) ---
    add("Ao ser aberto o primeiro selo, qual cavaleiro surgiu em Apocalipse 6:2?",
        "Um cavalo branco, e o seu cavaleiro tinha um arco e foi-lhe dada uma coroa, e saiu vencendo e para vencer",
        "Um cavalo vermelho com uma espada",
        "Um cavalo preto com uma balança",
        "Um cavalo amarelo com a peste",
        "facil", "Apocalipse 6:2", "O primeiro selo revela o cavalo branco, associado à conquista e ao engano no cenário mundial.")
    add("Qual poder foi dado ao cavaleiro do cavalo vermelho no segundo selo em Apocalipse 6:4?",
        "Tirar a paz da terra, para que os homens se matassem uns aos outros; e foi-lhe dada uma grande espada",
        "Curar todas as doenças",
        "Enriquecer os mercadores",
        "Destruir as florestas com fogo",
        "facil", "Apocalipse 6:4", "O cavalo vermelho simboliza a guerra devastadora e o conflito sangrento entre as nações.")
    add("O que o cavaleiro do cavalo preto segurava em sua mão no terceiro selo em Apocalipse 6:5?",
        "Uma balança na mão (simbolizando severa escassez e racionamento de alimentos)",
        "Uma tocha de fogo",
        "Um arco sem flechas",
        "Um escudo de prata",
        "facil", "Apocalipse 6:5-6", "Uma medida de trigo por um denário denota extrema carestia e fome econômica global.")
    add("Qual era o nome do cavaleiro do cavalo amarelo (ou pálido) no quarto selo em Apocalipse 6:8?",
        "A Morte, e o Inferno (Hades) o seguia de perto",
        "O Engano, seguido pela Tristeza",
        "A Peste, seguida pela Injustiça",
        "O Terror, seguido pelas Cinzas",
        "facil", "Apocalipse 6:8", "Foi-lhes dado poder sobre a quarta parte da terra para matar com espada, fome, mortandade e feras.")
    add("O que João viu debaixo do altar quando o Cordeiro abriu o quinto selo em Apocalipse 6:9?",
        "As almas dos que foram mortos por amor da palavra de Deus e do testemunho que deram",
        "As armas dos exércitos conquistadores",
        "Ouro e incenso acumulados",
        "Régios estandartes imperiais",
        "facil", "Apocalipse 6:9", "As almas dos mártires clamavam por justiça: 'Até quando, ó verdadeiro e santo Soberano?'.")
    add("O que aconteceu na terra e no céu quando o sexto selo foi aberto em Apocalipse 6:12-14?",
        "Um grande terremoto, o sol ficou negro como saco de crina, a lua como sangue e as estrelas caíram sobre a terra",
        "Uma chuva de pedras de prata e calmaria suave",
        "O mar secou completamente em um segundo",
        "O céu ficou dourado e todos os homens riram",
        "facil", "Apocalipse 6:12-14", "O sexto selo desencadeia cataclismos cósmicos anunciando o grande Dia da ira do Cordeiro.")

    # --- CAPÍTULO 7 A 9 (OS 144 MIL E AS TROMBETAS) ---
    add("Quantos servos de Deus foram selados na fronte dentre todas as tribos dos filhos de Israel em Apocalipse 7:4?",
        "144.000 (cento e quarenta e quatro mil, 12 mil de cada tribo)",
        "Setenta mil",
        "Doze mil no total",
        "Um milhão",
        "facil", "Apocalipse 7:4", "Doze mil de cada uma das doze tribos de Israel foram assinalados e protegidos por Deus.")
    add("Como a grande multidão incontável de todas as nações se apresentava diante do trono em Apocalipse 7:9?",
        "Vestidos de vestes brancas e com palmas nas mãos",
        "Com armaduras de ferro e lanças afiadas",
        "Com vestes de púrpura e diademas reais",
        "Com grilhões de bronze e cabeças baixas",
        "facil", "Apocalipse 7:9", "Uma multidão que ninguém podia contar louvava a Deus e ao Cordeiro com palmas de triunfo.")
    add("O que a voz do ancião explicou sobre as vestes brancas da grande multidão em Apocalipse 7:14?",
        "'Estes são os que vieram da grande tribulação, e lavaram as suas vestes e as branquearam no sangue do Cordeiro'",
        "'Estes são os que compraram tecidos finos em Tiro'",
        "'Estes são os filósofos de sabedoria secular'",
        "'Estes são os que nunca sofreram dor na terra'",
        "facil", "Apocalipse 7:14", "A pureza imaculada dos santos advém exclusivamente da expiação redentora no sangue de Cristo.")
    add("O que ocorreu no céu quando o Cordeiro abriu o sétimo selo em Apocalipse 8:1?",
        "Fez-se silêncio no céu quase por meia hora",
        "Houve um canto estrondoso de todos os anjos",
        "Caiu granizo de fogo sobre o mar",
        "Surgiram quatro sóis no firmamento",
        "facil", "Apocalipse 8:1", "O solene silêncio celestial de trinta minutos antecede a execução dos juízos das sete trombetas.")
    add("Qual é o nome da grande estrela ardente como uma tocha que caiu na terceira trombeta e amargou as águas em Apocalipse 8:11?",
        "Absinto", "Lúcifer", "Orion", "Sírius",
        "medio", "Apocalipse 8:11", "O nome da estrela é Absinto, e a terça parte das águas tornou-se amarga, matando muitos homens.")
    add("Qual é o nome em hebraico e em grego do anjo do abismo, rei dos gafanhotos na quinta trombeta (Apocalipse 9:11)?",
        "Abadom em hebraico e Apoliom em grego (que significa O Destruidor)",
        "Belzebu e Moloque",
        "Mamom e Baal",
        "Satanás e Belial",
        "medio", "Apocalipse 9:11", "O anjo do poço do abismo é denominado Abadom no hebraico e Apoliom no grego.")
    add("Junto a qual grande rio histórico os quatro anjos estavam atados e foram soltos na sexta trombeta em Apocalipse 9:14?",
        "Junto ao grande rio Eufrates", "Junto ao rio Jordão", "Junto ao rio Nilo", "Junto ao rio Tigre",
        "medio", "Apocalipse 9:14", "Os quatro anjos atados junto ao Eufrates foram desatados para matar a terça parte dos homens.")

    # --- CAPÍTULO 10 A 13 (AS TESTEMUNHAS E AS BESTAS) ---
    add("O que aconteceu com João quando ele comeu o livrinho entregue pelo anjo forte em Apocalipse 10:9-10?",
        "Na sua boca foi doce como mel, mas no seu ventre tornou-se amargo",
        "Foi amargo na boca e suave no estômago",
        "Causou-lhe sono profundo por três dias",
        "Transformou-se em pão de trigo puro",
        "facil", "Apocalipse 10:9-10", "A Palavra profética é deleitosa ao ser acolhida, mas amarga no anúncio de juízos solenes.")
    add("Por quanto tempo as duas testemunhas profetizarão vestidas de saco em Apocalipse 11:3?",
        "1.260 dias (mil duzentos e sessenta dias)", "Quarenta dias", "Setenta semanas", "Sete anos completos",
        "medio", "Apocalipse 11:3", "As duas oliveiras e candeeiros de Deus profetizam com autoridade sobrenatural por 1.260 dias.")
    add("O que aconteceu com as duas testemunhas após ficarem mortas na praça da grande cidade por três dias e meio em Apocalipse 11:11-12?",
        "O espírito de vida vindo de Deus entrou nelas, puseram-se em pé e subiram ao céu em uma nuvem",
        "Foram sepultadas em um túmulo lacrado de bronze",
        "Seus corpos desapareceram nas águas do mar",
        "Permaneceram na sepultura para sempre",
        "facil", "Apocalipse 11:11-12", "Deus ressuscitou miraculosamente Suas testemunhas aos olhos de todos os seus adversários.")
    add("Qual proclamação ressoou no céu ao toque da sétima trombeta em Apocalipse 11:15?",
        "'Os reinos do mundo vieram a ser de nosso Senhor e do seu Cristo, e ele reinará para todo o sempre'",
        "'A vitória pertence aos deuses do olimpo'",
        "'O homem conquistou a paz universal'",
        "'A criação será esquecida nas trevas'",
        "facil", "Apocalipse 11:15", "O clímax escatológico proclama o reinado soberano e eterno de Deus e do Seu Cristo.")
    add("Como a mulher celestial do capítulo 12 de Apocalipse estava vestida e o que tinha na cabeça?",
        "Vestida do sol, com a lua debaixo dos pés e uma coroa de doze estrelas sobre a cabeça",
        "Vestida de linho fino e tiara de marfim",
        "Vestida de escarlate com coroa de espinhos",
        "Vestida de armadura de ouro com elmo de ferro",
        "facil", "Apocalipse 12:1", "A mulher (representando o povo da promessa) deu à luz o Filho varão destinado a reger as nações.")
    add("Quem liderou os anjos na guerra no céu contra o grande dragão vermelho (Satanás) em Apocalipse 12:7-9?",
        "Miguel e os seus anjos", "Gabriel e os seus querubins", "Moisés e Elias", "Os vinte e quatro anciãos",
        "facil", "Apocalipse 12:7-9", "O arcanjo Miguel guerreou vitoriosamente, e a antiga serpente foi precipitada para a terra.")
    add("Como os santos venceram o acusador dos irmãos segundo a declaração triunfante de Apocalipse 12:11?",
        "Pelo sangue do Cordeiro e pela palavra do seu testemunho; e não amaram as suas vidas até à morte",
        "Pela força de suas espadas e cavalos",
        "Pela diplomacia perante os governantes",
        "Pela riqueza financeira acumulada",
        "facil", "Apocalipse 12:11", "A redenção na cruz e a fidelidade inegociável à verdade garantem a vitória total dos fiéis.")
    add("De onde surge a primeira besta que possui sete cabeças e dez chifres em Apocalipse 13:1?",
        "Sobe do mar", "Desce do céu como um raio", "Brota de uma montanha de fogo", "Sai de dentro do templo",
        "facil", "Apocalipse 13:1", "A besta que sobe do mar representa o império político anticristão global opressor.")
    add("Qual é o enigmático número da besta revelado em Apocalipse 13:18?",
        "666 (seiscentos e sessenta e seis)", "777", "144", "1000",
        "facil", "Apocalipse 13:18", "'Aquele que tem entendimento calcule o número da besta; porque é o número de um homem, e o seu número é seiscentos e sessenta e seis'.")

    # --- CAPÍTULO 14 A 18 (O CORDEIRO NO SIÃO E A QUEDA DE BABILÔNIA) ---
    add("O que os 144.000 tinham escrito em suas frontes sobre o monte Sião em Apocalipse 14:1?",
        "O nome do Cordeiro e o nome de Seu Pai", "O número de suas tribos", "A lei escrita em ouro", "Uma estrela de sete pontas",
        "facil", "Apocalipse 14:1", "Os santos selados exibem com júbilo o santo nome de Deus em suas frontes.")
    add("Qual é a mensagem do segundo anjo que voa pelo meio do céu em Apocalipse 14:8?",
        "'Caiu, caiu a grande Babilônia, que a todas as nações deu a beber do vinho da ira da sua prostituição'",
        "'Fazei penitência no deserto'",
        "'Edificai fortalezas nas montanhas'",
        "'Paz e prosperidade eterna aos mercadores'",
        "facil", "Apocalipse 14:8", "O colapso inevitável do corrupto sistema babilônico mundial é sumariamente anunciado.")
    add("Qual bênção aos que morrem na fé é pronunciada pelo Espírito em Apocalipse 14:13?",
        "'Bem-aventurados os mortos que desde agora morrem no Senhor... para que descansem dos seus trabalhos, e as suas obras os sigam'",
        "'Ai dos que partirem sem filhos'",
        "'A morte é o esquecimento eterno'",
        "'Os mortos nunca serão lembrados'",
        "facil", "Apocalipse 14:13", "Os mártires e crentes encontram repouso eterno nos braços acolhedores do Salvador.")
    add("Qual cântico sublime os vencedores da besta cantam junto ao mar de vidro em Apocalipse 15:3?",
        "O cântico de Moisés, servo de Deus, e o cântico do Cordeiro",
        "O cântico dos guerreiros de Israel",
        "O salmo de lamentação de Asafe",
        "O hino patriótico de Sião",
        "facil", "Apocalipse 15:3", "'Grandes e maravilhosas são as tuas obras, ó Senhor Deus Todo-Poderoso! Justos e verdadeiros são os teus caminhos'.")
    add("Em qual célebre local os reis de toda a terra são congregados para a batalha do grande dia de Deus Todo-Poderoso (Apocalipse 16:16)?",
        "Armagedom (monte de Megido)", "Monte Sinai", "Vale do Jordão", "Planalto de Bete-El",
        "facil", "Apocalipse 16:16", "Armagedom é o palco profético da congregação dos exércitos hostis antes de sua derrota final.")
    add("Como a mulher infiel que cavalga a besta é chamada em Apocalipse 17:5?",
        "Babilônia, a Grande, a Mãe das Prostituições e Abominações da Terra",
        "A rainha de Sabá",
        "A deusa Afrodite",
        "A deusa Diana de Éfeso",
        "facil", "Apocalipse 17:5", "A grande meretriz personifica a apostasia espiritual e a sedução idólatra dos impérios mundiais.")
    add("Qual ordem urgente a voz do céu proclama ao povo de Deus sobre a Babilônia em Apocalipse 18:4?",
        "'Sai dela, povo meu, para que não sejas participante dos seus pecados, e para que não incorras nas suas pragas'",
        "'Permanecei nela para fazer reformas civis'",
        "'Buscai tesouros em seus mercados'",
        "'Adorai suas estátuas de mármore'",
        "facil", "Apocalipse 18:4", "Deus convoca Seus filhos à radical separação moral da contaminação do sistema corrompido.")

    # --- CAPÍTULO 19 A 22 (AS BODAS, O MILÊNIO, A NOVA JERUSALÉM) ---
    add("Qual celebração gloriosa e alegre da Igreja com Cristo é anunciada em Apocalipse 19:7-9?",
        "As bodas do Cordeiro (o banquete nupcial de Cristo com Sua Noiva)",
        "A coroação de novos imperadores terrenos",
        "A festa dos tabernáculos no deserto",
        "O aniversário da cidade de Roma",
        "facil", "Apocalipse 19:7-9", "A Noiva (a Igreja) aprontou-se revestida de linho finíssimo, puro e resplandecente.")
    add("Qual é o nome supremo escrito no manto e na coxa do cavaleiro do cavalo branco em Apocalipse 19:16?",
        "Rei dos reis e Senhor dos senhores",
        "Príncipe dos homens",
        "Profeta de Israel",
        "Conquistador das nações",
        "facil", "Apocalipse 19:16", "Jesus Cristo retorna em triunfo absoluto com soberania indiscutível sobre todos os governantes.")
    add("Por quantos anos Satanás é aprisionado no poço do abismo para que não engane mais as nações em Apocalipse 20:1-3?",
        "1.000 anos (Milênio)", "Setenta anos", "Cento e vinte anos", "Sete anos",
        "facil", "Apocalipse 20:2-3", "Durante o reinado milenar de Cristo, Satanás permanece atado no abismo.")
    add("Qual grande evento de juízo universal perante o qual fogem a terra e o céu é descrito em Apocalipse 20:11-12?",
        "O julgamento diante do Grande Trono Branco",
        "O julgamento no Areópago de Atenas",
        "O sinédrio no monte Sião",
        "O tribunal de César em Roma",
        "facil", "Apocalipse 20:11-12", "Os mortos, grandes e pequenos, são julgados segundo as suas obras registradas nos livros.")
    add("Quem é lançado no lago de fogo e enxofre segundo a advertência final de Apocalipse 20:15?",
        "Aquele cujo nome não foi achado escrito no Livro da Vida",
        "Apenas os que foram pobres na terra",
        "Apenas os soldados das nações pagãs",
        "Ninguém, pois o lago é apenas figurativo",
        "facil", "Apocalipse 20:15", "O Livro da Vida registra os redimidos pelo Cordeiro; quem não está nele sofre a segunda morte.")
    add("O que Deus fará com o sofrimento e o choro na Nova Jerusalém segundo a comovente promessa de Apocalipse 21:4?",
        "Limpará de seus olhos toda lágrima; e não haverá mais morte, nem pranto, nem clamor, nem dor",
        "Permitirá luto parcial aos domingos",
        "Manterá as enfermidades leves para lição",
        "Deixará a morte agir uma vez ao ano",
        "facil", "Apocalipse 21:4", "No estado eterno restaurado, a morte e a dor são erradicadas definitivamente pela glória divina.")
    add("Quantas portas de pérola tem a Nova Jerusalém e quantos fundamentos têm seus muros em Apocalipse 21:12-14?",
        "Doze portas (com os nomes das 12 tribos de Israel) e doze fundamentos (com os nomes dos 12 apóstolos)",
        "Sete portas de ferro e quatro fundamentos",
        "Vinte e quatro portas de ouro e um fundamento",
        "Dez portas de mármore e setenta fundamentos",
        "facil", "Apocalipse 21:12-14", "As 12 portas e os 12 fundamentos unem a aliança de Israel e da Igreja no tabernáculo eterno.")
    add("Por que a Nova Jerusalém não necessita de sol nem de lua para que nela resplandeçam em Apocalipse 21:23?",
        "Porque a glória de Deus a ilumina, e o Cordeiro é a sua lâmpada",
        "Porque os anjos acendem tochas douradas",
        "Porque a noite é eterna e bela",
        "Porque o céu terá miríades de estrelas cadentes",
        "facil", "Apocalipse 21:23", "A radiância direta da presença do Criador e do Cordeiro fornece luz perpétua e celestial.")
    add("O que procede do trono de Deus e do Cordeiro no meio da praça da cidade celestial em Apocalipse 22:1-2?",
        "O rio puro da água da vida, claro como cristal, e a árvore da vida que produz doze frutos",
        "Um ribeiro de azeite aromático",
        "Um canal de vinho doce da Galileia",
        "Um poço selado com pedras de jade",
        "facil", "Apocalipse 22:1-2", "O rio da água da vida e a árvore da vida simbolizam a imortalidade, sustento e vigor perpétuos.")
    add("Qual é a sublime promessa de comunhão que os servos de Deus desfrutarão na eternidade em Apocalipse 22:4?",
        "'E verão o seu rosto, e nas suas frontes estará o seu nome'",
        "'Ficarão distantes observando através de um véu'",
        "'Ouvirão apenas a Sua voz sem nunca O contemplar'",
        "'Esquecerão a identidade do Criador'",
        "facil", "Apocalipse 22:4", "A visão beatífica face a face com Deus é a recompensa máxima e consumação de toda a redenção.")
    add("Qual é a promessa de retorno e a oração de resposta que encerram calorosamente a Bíblia Sagrada em Apocalipse 22:20?",
        "'Certamente, cedo venho. Amém! Ora, vem, Senhor Jesus!'",
        "'Esperai mais dez mil anos na terra'",
        "'O Senhor não mais voltará fisicamente'",
        "'Que o homem resolva seus próprios caminhos'",
        "facil", "Apocalipse 22:20", "A Bíblia sela suas profecias com a expectativa ardente do regresso iminente de Cristo: 'Maranata!'.")

    return items[:60]

if __name__ == "__main__":
    q_list = get_revelation_questions()
    print(f"Revelation generated: {len(q_list)} questions")
