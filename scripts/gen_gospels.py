# -*- coding: utf-8 -*-
"""
Evangelhos: 200 questões de Mateus, Marcos, Lucas e João
"""

def get_gospels_questions():
    items = []
    def add(q, c, w1, w2, w3, diff, book, ref, exp):
        items.append({
            "q": q, "c": c, "w1": w1, "w2": w2, "w3": w3,
            "diff": diff, "book": book, "testament": "NT",
            "section": "Evangelhos", "ref": ref, "exp": exp
        })

    # --- Nascimento e Infância de Jesus (30) ---
    add("Qual anjo anunciou o nascimento de João Batista a Zacarias e o de Jesus a Maria?",
        "O anjo Gabriel", "O anjo Miguel", "O anjo Rafael", "O anjo Uriel",
        "facil", "Lucas", "Lucas 1:19; 26", "Gabriel foi enviado por Deus à cidade de Nazaré a uma virgem prometida em casamento chamada Maria.")
    add("O que aconteceu ao sacerdote Zacarias por ter duvidado do anúncio do anjo de que sua esposa Isabel teria um filho na velhice?",
        "Ficou mudo sem poder falar até o nascimento do menino", "Ficou cego do olho direito", "Perdeu o movimento das mãos", "Foi exilado no deserto",
        "facil", "Lucas", "Lucas 1:20-22", "Gabriel disse: 'Ficarás mudo e não poderás falar até ao dia em que estas coisas aconteçam, porquanto não crestes'.")
    add("Em qual cidade da Judeia Jesus nasceu conforme profetizado pelas Escrituras?",
        "Belém", "Nazaré", "Jerusalém", "Cafarnaum",
        "facil", "Mateus", "Mateus 2:1; Lucas 2:4-7", "Jesus nasceu em Belém da Judeia por ocasião do recenseamento ordenado por César Augusto.")
    add("Por que Maria deitou o menino Jesus recém-nascido numa manjedoura?",
        "Porque não havia lugar para eles na estalagem", "Porque era costume judaico", "Porque estavam no campo aberto", "Porque o templo estava fechado",
        "facil", "Lucas", "Lucas 2:7", "Deu à luz o seu filho primogênito, enfaixou-o e o deitou numa manjedoura, porque não havia lugar para eles na hospedaria.")
    add("Quem foram os primeiros a receber a notícia do nascimento de Cristo através de um coro angelical?",
        "Pastores que guardavam seus rebanhos nos campos à noite", "Os sacerdotes no templo", "Os governadores romanos", "Os escribas de Jerusalém",
        "facil", "Lucas", "Lucas 2:8-14", "Anjos apareceram aos pastores no campo anunciando grande alegria para todo o povo com o cântico 'Glória a Deus nas alturas'.")
    add("Quais presentes preciosos os Magos do Oriente ofertaram ao Menino Jesus ao se prostrarem em adoração?",
        "Ouro, incenso e mirra", "Prata, trigo e azeite", "Pérolas, seda e gemas", "Túnicas reais e cetros",
        "facil", "Mateus", "Mateus 2:11", "Abrindo os seus tesouros, ofertaram-lhe dádivas: ouro (realeza), incenso (divindade) e mirra (sacrifício).")
    add("Para qual país a sagrada família fugiu à noite por ordem do anjo em sonho para escapar de Herodes?",
        "Egito", "Assíria", "Roma", "Grécia",
        "facil", "Mateus", "Mateus 2:13-14", "José levantou-se de noite, tomou o menino e sua mãe e partiu para o Egito até à morte de Herodes.")
    add("Qual terrível massacre de crianças o rei Herodes ordenou em Belém e arredores?",
        "O massacre de todos os meninos de dois anos para baixo", "A deportação de todas as famílias", "A prisão dos pais hebreus", "A queima das casas da cidade",
        "facil", "Mateus", "Mateus 2:16", "Herodes mandou matar todos os meninos de dois anos para baixo segundo o tempo averiguado com os magos.")
    add("Em qual cidade da Galileia Jesus cresceu após o retorno do Egito?",
        "Nazaré", "Betânia", "Tiberíades", "Jerusalém",
        "facil", "Lucas", "Lucas 2:39-40; 51", "Voltaram para a Galileia, à sua cidade de Nazaré; e o menino crescia e fortalecia-se em espírito.")
    add("Onde os pais encontraram Jesus aos doze anos após procurá-lo aflitos por três dias?",
        "No Templo de Jerusalém, assentado entre os mestres da Lei, ouvindo-os e interrogando-os", "Nas margens do rio Jordão", "No monte das Oliveiras", "Numa padaria em Belém",
        "facil", "Lucas", "Lucas 2:46", "Acharam-no no templo, assentado no meio dos doutores, ouvindo-os e interrogando-os; e todos se maravilhavam da sua inteligência.")

    # --- Ministério de João Batista e Batismo (15) ---
    add("Quais eram as vestes rústicas e a alimentação simples de João Batista no deserto da Judeia?",
        "Vestes de pelos de camelo com cinto de couro, alimentando-se de gafanhotos e mel silvestre", "Mantos de linho e pães de cevada", "Túnicas de lã e azeitonas", "Roupas sacerdotais e figos",
        "facil", "Mateus", "Mateus 3:4", "João usava uma veste de pelos de camelo e um cinto de couro; o seu sustento eram gafanhotos e mel silvestre.")
    add("Qual mensagem central e urgente João Batista proclamava pregando no deserto?",
        "'Arrependei-vos, porque é chegado o Reino dos Céus'", "'Vinde pagar os vossos impostos'", "'Construí novas fortalezas'", "'Guerreai contra os romanos'",
        "facil", "Mateus", "Mateus 3:2", "João Batista pregava: 'Arrependei-vos, porque é chegado o reino dos céus'.")
    add("Em qual rio João Batista batizava as multidões que confessavam seus pecados?",
        "Rio Jordão", "Rio Nilo", "Rio Eufrates", "Rio Cedrom",
        "facil", "Mateus", "Mateus 3:6", "E eram por ele batizados no rio Jordão, confessando os seus pecados.")
    add("Qual declaração profética sublime João Batista fez ao avistar Jesus aproximando-se no Jordão?",
        "'Eis o Cordeiro de Deus, que tira o pecado do mundo!'", "'Eis o novo rei de Sião!'", "'Eis o guerreiro com espada!'", "'Eis o sacerdote de Jerusalém!'",
        "facil", "João", "João 1:29", "No dia seguinte João viu a Jesus, que vinha para ele, e disse: 'Eis o Cordeiro de Deus, que tira o pecado do mundo!'.")
    add("O que aconteceu visível e audivelmente quando Jesus foi batizado e saía das águas do Jordão?",
        "Os céus se abriram, o Espírito Santo desceu em forma corpórea como pomba e a voz do Pai disse: 'Este é o meu Filho amado em quem me comprazo'", "Houve um terremoto na Galileia", "Caiu fogo do céu sobre a água", "Um arco-íris envolveu a multidão",
        "facil", "Mateus", "Mateus 3:16-17; Lucas 3:21-22", "O Espírito Santo desceu em forma de pomba e ouviu-se uma voz dos céus: 'Tu és o meu Filho amado; em ti me comprazo'.")

    # --- Tentação e Início do Ministério (15) ---
    add("Quantos dias e noites Jesus jejuou no deserto antes de ser tentado pelo diabo?",
        "40 dias e 40 noites", "7 dias e 7 noites", "3 dias e 3 noites", "12 dias",
        "facil", "Mateus", "Mateus 4:2", "E, tendo jejuado quarenta dias e quarenta noites, depois teve fome.")
    add("Qual foi a primeira resposta de Jesus à tentação de transformar pedras em pães?",
        "'Está escrito: Nem só de pão viverá o homem, mas de toda a palavra que sai da boca de Deus'", "'Não tenho fome'", "'Pedras não viram pão'", "'Prefiro pães do céu'",
        "facil", "Mateus", "Mateus 4:4; Deuteronômio 8:3", "Jesus repeliu a tentação citando Deuteronômio: 'Nem só de pão viverá o homem, mas de toda a palavra de Deus'.")
    add("Com o que Jesus repeliu todas as investidas e tentações do diabo no deserto?",
        "Com a Palavra de Deus citando as Escrituras Sagradas ('Está escrito')", "Com raios de fogo celestial", "Chamando doze legiões de anjos", "Fugindo do deserto",
        "facil", "Mateus", "Mateus 4:4; 7; 10", "Em cada investida do tentador Jesus respondeu com autoridade imutável: 'Está escrito...'.")
    add("Onde ocorreu o primeiro milagre de Jesus registrado no Evangelho de João?",
        "Nas bodas de Caná da Galileia, transformando água em vinho excelente", "Em Cafarnaum curando um leproso", "Em Jerusalém no templo", "No mar da Galileia",
        "facil", "João", "João 2:1-11", "Jesus transformou cerca de seiscentas litros de água em vinho em Caná da Galileia, manifestando a Sua glória.")
    add("Quantos apóstolos principais Jesus escolheu formalmente para acompanhá-lo e enviá-los a pregar?",
        "12 apóstolos", "7 apóstolos", "10 apóstolos", "70 apóstolos",
        "facil", "Lucas", "Lucas 6:13", "Quando amanheceu, chamou a si os seus discípulos e escolheu doze dentre eles, aos quais deu também o nome de apóstolos.")

    # --- O Sermão da Montanha (25) ---
    add("Quem Jesus declara bem-aventurados na primeira sentença das Bem-aventuranças em Mateus 5:3?",
        "Os humildes de espírito (pobres em espírito), porque deles é o Reino dos Céus", "Os ricos da terra", "Os fortes e poderosos", "Os governantes ilustres",
        "facil", "Mateus", "Mateus 5:3", "'Bem-aventurados os pobres de espírito, porque deles é o reino dos céus'.")
    add("A que Jesus compara os Seus discípulos em Mateus 5:13-14 diante do mundo?",
        "O sal da terra e a luz do mundo", "O ouro e a prata", "As águias e os leões", "As árvores frondosas",
        "facil", "Mateus", "Mateus 5:13-14", "'Vós sois o sal da terra... Vós sois a luz do mundo; não se pode esconder uma cidade edificada sobre um monte'.")
    add("Qual é a sublime instrução de Jesus sobre o amor em Mateus 5:44?",
        "'Amai a vossos inimigos, bendizei os que vos maldizem, fazei bem aos que vos odeiam e orai pelos que vos perseguem'", "'Amai apenas aos que vos amam'", "'Vingai-vos com firmeza'", "'Ignorai os vossos adversários'",
        "facil", "Mateus", "Mateus 5:44", "'Eu, porém, vos digo: Amai a vossos inimigos, bendizei os que vos maldizem, fazei bem aos que vos odeiam, e orai pelos que vos maltratam'.")
    add("Qual famosa oração modelo Jesus ensinou aos discípulos no Sermão da Montanha?",
        "A oração do Pai Nosso", "O cântico de Miriã", "A bênção de Moisés", "A oração de Davi no deserto",
        "facil", "Mateus", "Mateus 6:9-13", "'Portanto vós orareis assim: Pai nosso, que estás nos céus, santificado seja o teu nome...'.")
    add("Onde Jesus nos ensina a ajuntar tesouros imperecíveis que a traça e a ferrugem não consom?",
        "No Céu", "Em bancos de ouro", "Em propriedades rurais", "Em cofres subterrâneos",
        "facil", "Mateus", "Mateus 6:19-20", "'Não ajunteis tesouros na terra... mas ajuntai tesouros no céu, onde nem a traça nem a ferrugem consomem'.")
    add("O que Jesus disse sobre a impossibilidade de servir a dois mestres antagônicos em Mateus 6:24?",
        "'Não podeis servir a Deus e a Mamom (às riquezas)'", "'Podeis servir a dois reis ao mesmo tempo'", "'O ouro e Deus andam sempre juntos'", "'Não há perigo em amar o dinheiro'",
        "facil", "Mateus", "Mateus 6:24", "'Nenhum servo pode servir a dois senhores... Não podeis servir a Deus e a Mamom'.")
    add("A que aves e flores Jesus apontou para ensinar que não devemos andar ansiosos pelo dia de amanhã?",
        "Às aves do céu que não semeiam e aos lírios do campo que nem Salomão se vestiu como um deles", "Aos corvos e aos espinhos", "Às pombas e às palmeiras", "Aos falcões e às oliveiras",
        "facil", "Mateus", "Mateus 6:26-29", "'Olhai para as aves do céu... Olhai para os lírios do campo como crescem; nem Salomão em toda a sua glória se vestiu como um deles'.")
    add("Qual prioridade de vida deve ser buscada em primeiro lugar segundo Mateus 6:33?",
        "'Buscai primeiro o Reino de Deus e a sua justiça, e todas estas coisas vos serão acrescentadas'", "'Buscai primeiro vossa estabilidade financeira'", "'Buscai a aprovação dos amigos'", "'Buscai cargos de honra'",
        "facil", "Mateus", "Mateus 6:33", "'Mas buscai primeiro o reino de Deus, e a sua justiça, e todas estas coisas vos serão acrescentadas'.")
    add("Qual lição prática sobre a hipocrisia de julgar o próximo está em Mateus 7:3?",
        "Repara no cisco no olho do irmão sem notar a trave no próprio olho", "Compara com a pedra no sapato", "Fala sobre a nuvem sem chuva", "Cita a folha que cai",
        "facil", "Mateus", "Mateus 7:3-5", "'E por que reparas tu no cisco que está no olho do teu irmão, e não vês a trave que está no teu olho?'.")
    add("A quem Jesus compara o homem prudente que ouve Suas palavras e as pratica no final do Sermão da Montanha?",
        "A um homem prudente que edificou a sua casa sobre a rocha inabalável", "A um construtor de barcos velozes", "A um agricultor que colheu trigo", "A um guerreiro com escudo",
        "facil", "Mateus", "Mateus 7:24-25", "'Todo aquele que ouve estas minhas palavras e as pratica é semelhante ao homem prudente que edificou a sua casa sobre a rocha; desceu a chuva e ela não caiu'.")

    # --- Milagres de Jesus (35) ---
    add("Qual palavra de autoridade e fé o centurião romano em Cafarnaum disse a Jesus sobre a cura de seu servo?",
        "'Senhor, dize somente uma palavra, e o meu servo será curado'", "'Vem tocar no meu criado'", "'Aceita cem moedas de prata'", "'Traze os teus apóstolos à minha casa'",
        "facil", "Mateus", "Mateus 8:8-10", "Jesus maravilhou-se e disse: 'Em verdade vos digo que nem mesmo em Israel encontrei tamanha fé'.")
    add("O que Jesus ordenou aos ventos e ao mar bravio quando a tempestade açoitava o barco dos discípulos?",
        "'Cala-te, emudece!', e houve grande bonança", "'Espalhai as águas para longe'", "'Remai com mais força'", "'Saltemos todos ao mar'",
        "facil", "Marcos", "Marcos 4:39", "Ele, despertando, repreendeu o vento e disse ao mar: 'Cala-te, emudece'. O vento aquietou-se e houve grande bonança.")
    add("Como quatro amigos levaram um paralítico à presença de Jesus em Cafarnaum quando a casa estava cheia?",
        "Subiram ao eirado, destelharam o teto e baixaram o leito com o enfermo diante de Jesus", "Empurraram a multidão com violência", "Esperaram a noite inteira do lado de fora", "Chamaram Jesus pela janela",
        "facil", "Marcos", "Marcos 2:3-5", "Vendo Jesus a fé deles, disse ao paralítico: 'Filho, perdoados estão os teus pecados; levanta-te, toma o teu leito e vai para tua casa'.")
    add("O que a mulher que sofria de hemorragia havia doze anos fez para ser instantaneamente curada?",
        "Aproximou-se por trás no meio da multidão e tocou na orla das vestes de Jesus", "Gritou alto chamando seu nome", "Pediu aos apóstolos que intercedessem", "Ofereceu prata a Jesus",
        "facil", "Lucas", "Lucas 8:43-48", "Ela tocou a borda do seu manto e logo estancou o fluxo do seu sangue; Jesus disse: 'A tua fé te salvou; vai em paz'.")
    add("Quais palavras em aramaico Jesus disse ao ressuscitar a filha de Jairo de doze anos?",
        "'Talita cumi' (que significa: 'Menina, a ti te digo, levanta-te')", "'Efatá'", "'Maranata'", "'Eli, Eli'",
        "facil", "Marcos", "Marcos 5:41-42", "Tomando a mão da menina, disse-lhe: 'Talita cumi', e imediatamente a menina de doze anos levantou-se e andava.")
    add("Quantos pães e peixinhos estavam disponíveis na primeira multiplicação para alimentar mais de cinco mil homens?",
        "Cinco pães de cevada e dois pequenos peixes trazidos por um rapazinho", "Sete pães e três peixes", "Dez pães de trigo e cinco peixes", "Vinte pães prontos",
        "facil", "João", "João 6:9", "André disse: 'Está aqui um rapaz que tem cinco pães de cevada e dois peixinhos; mas que é isto para tantos?'.")
    add("Quantos cestos cheios de pedaços sobraram após os cinco mil comerem e se saciarem?",
        "12 cestos cheios", "7 cestos", "3 cestos", "40 cestos",
        "facil", "Mateus", "Mateus 14:20", "Comeram todos e ficaram fartos; e recolheram dos pedaços que sobraram doze cestos cheios.")
    add("O que o apóstolo Pedro fez quando viu Jesus caminhando sobre as águas no mar da Galileia?",
        "Desceu do barco e andou sobre as águas ao encontro de Jesus, até temer o vento e começar a afundar clamando: 'Senhor, salva-me!'", "Ficou com medo e escondeu-se no fundo do barco", "Atirou uma corda para Jesus", "Remou em fuga apressada",
        "facil", "Mateus", "Mateus 14:28-31", "Pedro andou sobre as águas; mas, sentindo o vento forte, teve medo e afundando clamou: 'Senhor, salva-me!'. Jesus estendeu a mão e o segurou.")
    add("Onde o cego de nascença foi instruído por Jesus a ir lavar os olhos untados de lodo para receber a visão?",
        "No tanque de Siloé (que quer dizer Enviado)", "No tanque de Betesda", "No rio Jordão", "No poço de Jacó",
        "facil", "João", "João 9:6-7", "Jesus cuspiu na terra, fez lodo com a saliva e untou os olhos do cego dizendo: 'Vai, lava-te no tanque de Siloé'. Ele foi, lavou-se e voltou vendo.")
    add("Qual declaração inesquecível o ex-cego de nascença deu aos fariseus que interrogavam o milagre?",
        "'Uma coisa sei: eu era cego e agora vejo'", "'Jesus é apenas um homem comum'", "'Não me lembro de como enxerguei'", "'Prefiro continuar calado'",
        "facil", "João", "João 9:25", "Ele respondeu: 'Se é pecador, não sei; uma coisa sei: que, havendo eu sido cego, agora vejo'.")
    add("Quantos leprosos foram curados por Jesus na Galileia e quantos voltaram para agradecer prostrados aos Seus pés?",
        "Dez foram limpos, mas apenas um (um samaritano) voltou dando glória a Deus", "Todos os dez voltaram celebrando", "Três voltaram", "Nenhum agradeceu",
        "facil", "Lucas", "Lucas 17:12-19", "Jesus perguntou: 'Não foram dez os limpos? Onde estão os nove? Não houve quem voltasse para dar glória a Deus senão este estrangeiro?'.")
    add("Quantos dias Lázaro de Betânia já estava sepultado na gruta quando Jesus ordenou que a pedra fosse retirada?",
        "Quatro dias (já cheirava mal)", "Três dias", "Sete dias", "Um dia",
        "facil", "João", "João 11:17; 39", "Disse Marta: 'Senhor, já cheira mal, porque é já de quatro dias'. Jesus disse: 'Se creres, verás a glória de Deus'.")
    add("Qual é o menor versículo da Bíblia Sagrada registrado no contexto da comoção com a morte de Lázaro?",
        "'Jesus chorou' (João 11:35)", "'Deus é amor'", "'Orai sem cessar'", "'Tende fé'",
        "facil", "João", "João 11:35", "João 11:35 registra a profunda compaixão e humanidade do Salvador em apenas duas palavras: 'Jesus chorou'.")
    add("Qual ordem com voz audível Jesus bradou diante do túmulo aberto de Lázaro ressuscitando-o?",
        "'Lázaro, vem para fora!'", "'Desperta, meu amigo'", "'Levanta-te do sono'", "'Saia deste sepulcro'",
        "facil", "João", "João 11:43-44", "Tendo dito isto, clamou com grande voz: 'Lázaro, vem para fora!'. E o que havia morrido saiu atado de pés e mãos com faixas.")
    add("Como o cego Bartimeu clamava insistentemente à beira do caminho de Jericó quando soube que Jesus passava?",
        "'Jesus, Filho de Davi, tem misericórdia de mim!'", "'Senhor, dá-me esmola de prata'", "'Profeta da Galileia, cura-me'", "'Mestre, olha para o pobre'",
        "facil", "Marcos", "Marcos 10:46-48", "Ouvindo que era Jesus de Nazaré, começou a clamar: 'Jesus, Filho de Davi, tem misericórdia de mim!'. E recuperou a vista.")

    # --- Parábolas de Jesus (35) ---
    add("Na Parábola do Semeador, quais sementes deram fruto a trinta, sessenta e cem por um?",
        "As que caíram em boa terra (corações nobres que ouvem e guardam a palavra)", "As que caíram à beira do caminho", "As que caíram entre espinhos", "As que caíram entre as pedras",
        "facil", "Mateus", "Mateus 13:8; 23", "A que foi semeada em boa terra é o que ouve e compreende a palavra, e dá fruto a cem, a sessenta e a trinta por um.")
    add("Na Parábola do Bom Samaritano, quais líderes religiosos passaram ao largo sem socorrer o homem ferido?",
        "Um sacerdote e um levita", "Dois fariseus de Jerusalém", "Dois soldados romanos", "Dois pescadores da Galileia",
        "facil", "Lucas", "Lucas 10:31-32", "Um sacerdote descia pelo mesmo caminho e, vendo-o, passou de largo; e de igual modo um levita passou de largo.")
    add("O que o bom samaritano derramou nas feridas do homem espancado antes de levá-lo à hospedaria?",
        "Azeite e vinho", "Água pura e sal", "Mel e azeite aromático", "Leite e vinagre",
        "medio", "Lucas", "Lucas 10:34", "Aproximando-se, atou-lhe as feridas, deitando nelas azeite e vinho; e pondo-o sobre a sua cavalgadura, levou-o a uma estalagem.")
    add("O que aconteceu na Parábola do Filho Pródigo quando o jovem gastou dissolutamente toda a sua herança?",
        "Veio grande fome naquela terra e ele foi cuidar de porcos desejando comer das alfarrobas", "Enriqueceu no comércio", "Tornou-se general militar", "Casou-se com uma nobre",
        "facil", "Lucas", "Lucas 15:13-16", "Havendo gasto tudo, houve naquela terra grande fome, e ele desejava encher o estômago com as alfarrobas que os porcos comiam.")
    add("O que o pai amoroso fez ao avistar o filho pródigo retornando arrependido e maltrapilho de longe?",
        "Correu ao seu encontro cheio de compaixão, abraçou-o com ternura e beijou-o", "Repreendeu-o na porta da cidade", "Mandou-o trabalhar como jornaleiro", "Fechou a cancela da fazenda",
        "facil", "Lucas", "Lucas 15:20", "Quando ainda estava longe, o pai o viu e moveu-se de íntima compaixão e, correndo, lançou-se-lhe ao pescoço e o beijou.")
    add("Quais presentes de honra e restauração o pai concedeu ao filho pródigo na festa do retorno?",
        "A melhor veste, um anel no dedo, sandálias nos pés e o novilho cevado assado para celebrar", "Apenas uma capa de pastor", "Cem moedas de prata", "Um cajado de madeira",
        "facil", "Lucas", "Lucas 15:22-23", "O pai disse: 'Trazei depressa a melhor túnica e vesti-lho, e ponde-lhe um anel na mão e sandálias nos pés; e trazei o bezerro cevado'.")
    add("O que a mulher fez na Parábola da Dracma Perdida ao perder uma de suas dez moedas de prata?",
        "Acendeu a candeia, varreu a casa com diligência até encontrá-la e alegrou-se com as amigas", "Deixou de lado sem se importar", "Comprou mais duas moedas", "Chorou sem procurar",
        "facil", "Lucas", "Lucas 15:8-9", "Acende a candeia, varre a casa e busca com diligência até a achar; e reunindo as vizinhas, diz: 'Alegrai-vos comigo!'.")
    add("Para onde o mendigo Lázaro foi levado pelos anjos ao morrer na parábola de Lucas 16?",
        "Para o seio de Abraão (paraíso de consolo)", "Para o abismo de chamas", "Para o túmulo dos reis", "Para uma ilha deserta",
        "facil", "Lucas", "Lucas 16:22", "Aconteceu que o mendigo morreu e foi levado pelos anjos para o seio de Abraão; morreu também o rico e foi sepultado.")
    add("O que o homem rico em tormentos no Hades pediu a Abraão em Lucas 16:24?",
        "Que enviasse Lázaro para molhar a ponta do dedo na água e refrescar a sua língua atormentada no fogo", "Que lhe devolvesse seus palácios", "Que apagasse todas as chamas", "Que lhe desse pão quente",
        "facil", "Lucas", "Lucas 16:24", "Clamou o rico: 'Pai Abraão, tem misericórdia de mim e envia a Lázaro para que molhe a ponta do dedo na água e me refresque a língua'.")
    add("O que o publicano humilde orava no fundo do templo na parábola de Lucas 18:13?",
        "Batia no peito dizendo: 'Ó Deus, sê propício a mim, pecador!'", "Agradecia por ser melhor que todos os homens", "Pedia para ser coroado sacerdote", "Contava suas muitas doações de ouro",
        "facil", "Lucas", "Lucas 18:13-14", "O publicano, estando em pé de longe, não ousava levantar os olhos aos céus, mas batia no peito dizendo: 'Ó Deus, tem compaixão de mim pecador!'.")
    add("O que as cinco virgens prudentes levaram consigo em suas vasilhas na Parábola das Dez Virgens?",
        "Azeite reserva em suas vasilhas junto com as lâmpadas", "Pães frescos de trigo", "Água para a caminhada", "Frascos de perfume caro",
        "facil", "Mateus", "Mateus 25:4", "As prudentes levaram azeite em suas vasilhas, com as suas lâmpadas, preparadas para a tardança do noivo.")

    # --- Encontros e Diálogos de Jesus (25) ---
    add("O que Jesus revelou ao mestre da lei Nicodemos na conversa noturna em João 3:3?",
        "'Em verdade te digo que aquele que não nascer de novo não pode ver o Reino de Deus'", "'Precisas doar todo o teu ouro'", "'Deves estudar mais a lei de Moisés'", "'Foge da cidade de Jerusalém'",
        "facil", "João", "João 3:3", "Jesus disse a Nicodemos: 'Aquele que não nascer de novo não pode ver o reino de Deus'.")
    add("Qual é o versículo ápice da Bíblia Sagrada sobre a imensidão do amor de Deus em João 3:16?",
        "'Porque Deus amou o mundo de tal maneira que deu o seu Filho unigênito, para que todo aquele que nele crê não pereça, mas tenha a vida eterna'", "'Deus recompensará apenas os santos de Israel'", "'O amor divino é exclusivo dos sacerdotes'", "'A salvação depende das obras perfeitas'",
        "facil", "João", "João 3:16", "'Porque Deus amou o mundo de tal maneira que deu o seu Filho unigênito, para que todo aquele que nele crê não pereça, mas tenha a vida eterna'.")
    add("Onde Jesus encontrou a mulher samaritana ao meio-dia e lhe ofereceu a Água da Vida?",
        "Junto à fonte do poço histórico de Jacó em Sicar", "No templo de Samaria", "No mercado de Cafarnaum", "Nas portas de Jericó",
        "facil", "João", "João 4:5-14", "Jesus, cansado do caminho, assentara-se junto à fonte de Jacó e disse à mulher: 'Se conheceras o dom de Deus, tu lhe pedirias, e ele te daria água viva'.")
    add("Como os verdadeiros adoradores adorarão o Pai segundo a revelação de Jesus em João 4:23-24?",
        "Em espírito e em verdade", "Com animais de sacrifício no monte", "Apenas no templo físico de Jerusalém", "Com danças e trombetas de ouro",
        "facil", "João", "João 4:23-24", "'Mas a hora vem, e agora é, em que os verdadeiros adoradores adorarão o Pai em espírito e em verdade; porque o Pai procura a tais que assim o adorem'.")
    add("O que Jesus disse à multidão que queria apedrejar a mulher apanhada em flagrante adultério em João 8:7?",
        "'Aquele que dentre vós está sem pecado seja o primeiro que atire pedra contra ela'", "'Apedrejai-a conforme manda a lei'", "'Prendei-a no calabouço'", "'Chamem os sacerdotes para julgá-la'",
        "facil", "João", "João 8:7", "Jesus inclinou-se escrevendo na terra e disse: 'Aquele que dentre vós está sem pecado seja o primeiro que atire pedra contra ela'.")
    add("O que o pequeno Zaqueu, chefe dos publicanos em Jericó, fez para ver Jesus por causa da multidão?",
        "Subiu numa figueira brava (sicômoro) à beira do caminho", "Subiu nos ombros de um amigo", "Pediu aos soldados que o levantassem", "Esperou no terraço do templo",
        "facil", "Lucas", "Lucas 19:3-4", "Sendo de pequena estatura, correu adiante e subiu a uma figueira brava para o ver, porque havia de passar por ali.")
    add("O que Maria de Betânia fez para ungir o Senhor antes de Sua paixão, provocando a indignação de Judas?",
        "Derramou um vaso de alabastro de nardo puro caríssimo sobre a cabeça e pés de Jesus, enxugando com seus cabelos", "Ofereceu uma taça de vinho doce", "Deu cem moedas de prata aos apóstolos", "Lavou as mãos de Jesus com água",
        "facil", "João", "João 12:3; Marcos 14:3", "Maria tomou uma libra de bálsamo de nardo puro de grande preço, ungiu os pés de Jesus e os enxugou com os seus cabelos.")

    # --- Última Ceia, Paixão e Cruz (40) ---
    add("Em qual animal humilde Jesus montou na Sua Entrada Triunfal em Jerusalém no Domingo de Ramos?",
        "Num jumentinho (jumento filho de jumenta)", "Num cavalo branco de guerra", "Num camelo adornado de ouro", "Num carro de combate",
        "facil", "Mateus", "Mateus 21:5-7", "Trouxeram a jumenta e o jumentinho, puseram sobre eles as suas vestes, e Jesus montou, aclamado com ramos de palmeiras.")
    add("O que a multidão e as crianças clamavam ao estender mantos e ramos na entrada triunfal de Jesus?",
        "'Hosana ao Filho de Davi! Bendito o que vem em nome do Senhor! Hosana nas maiores alturas!'", "'Viva o novo imperador de Roma!'", "'Destruição aos inimigos!'", "'Coroa de ouro para o Messias!'",
        "facil", "Mateus", "Mateus 21:9", "A multidão clamava: 'Hosana ao Filho de Davi! Bendito o que vem em nome do Senhor! Hosana nas alturas!'.")
    add("O que Jesus fez ao entrar no Templo e ver cambistas e vendedores profanando o pátio sagrado?",
        "Fez um azorrague de cordas, derrubou as mesas dos cambistas e expulsou a todos declarando: 'A minha casa será chamada casa de oração'", "Pediu metade do lucro das vendas", "Mandou fechar os portões", "Sentou-se para negociar",
        "facil", "Mateus", "Mateus 21:12-13; João 2:15", "Jesus expulsou os que vendiam e compravam e disse: 'Está escrito: A minha casa será chamada casa de oração; vós, porém, a tendes transformado em covil de ladrões'.")
    add("Quanto a viúva pobre depositou no gazofilácio do templo que mereceu o louvor de Jesus acima de todos os ricos?",
        "Duas pequenas moedas de cobre (um lepto/quadrante), dando tudo quanto possuía para o seu sustento", "Dez moedas de prata", "Uma barra de ouro puro", "Cinco denários romanos",
        "facil", "Marcos", "Marcos 12:42-44", "Jesus disse: 'Esta pobre viúva deitou mais do que todos os que deitaram ao tesouro; porque todos deitaram do que lhes sobrava, mas esta deitou tudo o que tinha'.")
    add("Por quantas moedas de prata o traidor Judas Iscariotes concordou em entregar Jesus aos principais sacerdotes?",
        "30 moedas de prata", "20 moedas de prata", "50 moedas de ouro", "100 denários",
        "facil", "Mateus", "Mateus 26:15", "Disseram-lhe: 'Que me quereis dar, e eu vo-lo entregarei?'. E eles lhe pesaram trinta moedas de prata.")
    add("Qual gesto surpreendente de profunda humildade e serviço Jesus realizou antes da Última Ceia?",
        "Cingiu-se com uma toalha e lavou os pés dos Seus doze discípulos", "Distribuiu anéis de prata a todos", "Sentou-se no chão em silêncio", "Mandou que os discípulos lhe banhassem as mãos",
        "facil", "João", "João 13:4-5", "Deitou água na bacia e começou a lavar os pés aos discípulos e a enxugá-los com a toalha com que estava cingido.")
    add("O que o pão e o cálice representam na Santa Ceia instituída por Jesus na véspera de Sua morte?",
        "O Seu corpo entregue por nós e o Seu sangue da Nova Aliança derramado para remissão de pecados", "A fartura das colheitas de trigo e uva", "A lembrança do maná do deserto", "A vitória política de Israel",
        "facil", "Lucas", "Lucas 22:19-20; 1 Coríntios 11:24-25", "'Isto é o meu corpo, que por vós é dado... Este cálice é o novo testamento no meu sangue, que é derramado por vós'.")
    add("Qual discípulo afirmou que jamais negaria a Jesus e foi advertido de que o negaria três vezes antes do galo cantar?",
        "Simão Pedro", "João", "Tomé", "Tiago",
        "facil", "Mateus", "Mateus 26:34-35", "Jesus disse a Pedro: 'Em verdade te digo que, nesta mesma noite, antes que o galo cante, três vezes me negarás'.")
    add("Onde Jesus orou em profunda agonia na noite em que foi preso, enquanto Seu suor caía como gotas de sangue?",
        "No Jardim do Getsêmani (no Monte das Oliveiras)", "No templo em Jerusalém", "No palácio de Herodes", "No deserto da Judeia",
        "facil", "Lucas", "Lucas 22:39-44", "E, posto em agonia, orava mais intensamente; e o seu suor tornou-se em grandes gotas de sangue que corriam até à terra.")
    add("Qual oração de submissão filial perfeita Jesus fez ao Pai no Getsêmani?",
        "'Pai, se queres, afasta de mim este cálice; todavia não se faça a minha vontade, mas a tua'", "'Livra-me desta cruz com legiões de anjos'", "'Destrói os soldados que vêm me prender'", "'Deixa-me fugir para a Galileia'",
        "facil", "Lucas", "Lucas 22:42", "'Pai, se é do teu agrado, afasta de mim este cálice; contudo não se faça a minha vontade, mas a tua'.")
    add("Qual sinal combinado Judas usou para indicar aos soldados armados qual era Jesus no Getsêmani?",
        "Um beijo no rosto", "Um aperto de mão", "Apontou com uma tocha", "Chamou-o em voz alta",
        "facil", "Mateus", "Mateus 26:48-49", "O traidor tinha-lhes dado um sinal: 'Aquele que eu beijar, esse é; prendei-o'. E logo se aproximou de Jesus e o beijou.")
    add("O que Pedro fez ao ver os soldados prenderem Jesus no jardim do Getsêmani?",
        "Puxou da espada e decepou a orelha direita de Malco, servo do sumo sacerdote, que Jesus imediatamente tocou e curou", "Fugiu correndo na escuridão", "Atirou pedras nos guardas", "Pediu ajuda a Pilatos",
        "facil", "João", "João 18:10; Lucas 22:50-51", "Pedro feriu o servo do sumo sacerdote e cortou-lhe a orelha direita; Jesus tocou-lhe a orelha e o curou, ordenando a Pedro que embainhasse a espada.")
    add("Qual governador romano presidiu o julgamento civil de Jesus e lavou publicamente as mãos perante o povo?",
        "Pôncio Pilatos", "Herodes Antipas", "Félix", "Festo",
        "facil", "Mateus", "Mateus 27:2; 24", "Pilatos, vendo que nada aproveitava, tomou água e lavou as mãos diante da multidão dizendo: 'Estou inocente do sangue deste justo'.")
    add("Qual criminoso e agitador sedicioso foi escolhido pela multidão influenciada para ser solto no lugar de Jesus?",
        "Barrabás", "Dimas", "Gestas", "Judas",
        "facil", "Mateus", "Mateus 27:21", "O governador perguntou: 'Qual dos dois quereis que eu vos solte?'. E eles disseram: 'Barrabás!'.")
    add("Quem foi constrangido pelos soldados romanos a carregar a pesada cruz de Jesus a caminho do Calvário?",
        "Simão de Cirene", "José de Arimateia", "Nicodemos", "Zaqueu",
        "facil", "Lucas", "Lucas 23:26", "Quando o levavam, tomaram um certo Simão, cireneu, que vinha do campo, e puseram-lhe a cruz às costas, para que a levasse após Jesus.")
    add("Em qual monte fora dos muros de Jerusalém Jesus foi crucificado entre dois malfeitores?",
        "Gólgota (Lugar da Caveira) / Calvário", "Monte Sinai", "Monte das Oliveiras", "Monte Carmelo",
        "facil", "Lucas", "Lucas 23:33; João 19:17", "Chegando ao lugar chamado Calvário (em hebraico Gólgota), ali o crucificaram a ele e aos malfeitores, um à direita e outro à esquerda.")
    add("Qual promessa maravilhosa de salvação Jesus fez ao ladrão arrependido na cruz ao lado d'Ele?",
        "'Em verdade te digo que hoje estarás comigo no Paraíso'", "'Serás libertado da cruz'", "'Esperarás mil anos nas trevas'", "'Não há perdão para os teus crimes'",
        "facil", "Lucas", "Lucas 23:43", "Disse-lhe Jesus: 'Em verdade te digo que hoje estarás comigo no Paraíso'.")
    add("A qual apóstolo amado Jesus entregou os cuidados filiais de Sua mãe Maria aos pés da cruz?",
        "Ao apóstolo João", "A Pedro", "A Tiago", "A Tomé",
        "facil", "João", "João 19:26-27", "Disse Jesus a sua mãe: 'Mulher, eis aí o teu filho'. Depois disse ao discípulo: 'Eis aí tua mãe'. E desde aquela hora o discípulo a recebeu em sua casa.")
    add("Qual brado solene de vitória consumadora sobre a redenção Jesus deu imediatamente antes de expirar?",
        "'Está consumado!' (Tetelestai)", "'Fui derrotado'", "'Adeus a todos'", "'Voltarei com armas'",
        "facil", "João", "João 19:30", "Quando Jesus tomou o vinagre, disse: 'Está consumado!'. E, inclinando a cabeça, entregou o espírito.")
    add("O que aconteceu sobrenaturalmente no Templo de Jerusalém no exato momento da morte expiatória de Cristo?",
        "O véu do santuário rasgou-se de alto a baixo em duas partes, abrindo o livre acesso a Deus", "As paredes desabaram totalmente", "O candelabro apagou-se para sempre", "A arca moveu-se sozinha",
        "facil", "Mateus", "Mateus 27:51; Hebreus 10:19-20", "E eis que o véu do templo se rasgou em dois, de alto a baixo; e tremeu a terra, e fenderam-se as pedras.")

    # --- Ressurreição e Aparições Gloriosas (15) ---
    add("Quem foram os dois membros ilustres do Sinédrio que sepultaram reverentemente o corpo de Jesus num sepulcro novo esculpido na rocha?",
        "José de Arimateia e Nicodemos com cem libras de mirra e aloés", "Gamaliel e Saulo", "Anás e Caifás", "Zaqueu e Bartimeu",
        "medio", "João", "João 19:38-40", "José de Arimateia e Nicodemos tomaram o corpo de Jesus e o envolveram em lençóis de linho com os aromas, depositando-o num sepulcro novo.")
    add("Em qual dia glorioso da semana o túmulo de Jesus foi encontrado vazio com a pedra removida?",
        "No primeiro dia da semana (domingo de madrugada)", "No sábado à tarde", "Na sexta-feira à noite", "Na segunda-feira de manhã",
        "facil", "Lucas", "Lucas 24:1-2", "No primeiro dia da semana, de madrugada, foram ao sepulcro e acharam a pedra revolvida.")
    add("A quem Jesus apareceu primeiro em ressurreição no jardim junto ao sepulcro?",
        "A Maria Madalena", "A Pedro", "A João", "A Pilatos",
        "facil", "João", "João 20:14-16; Marcos 16:9", "Jesus apareceu primeiramente a Maria Madalena, chamando-a pelo nome: 'Maria!'. Ela voltou-se e disse-lhe: 'Raboni!' (que quer dizer Mestre).")
    add("A quais dois discípulos desconsolados Jesus apareceu caminhando incógnito e explicando as Escrituras no caminho para qual aldeia?",
        "Aldeia de Emaús", "Aldeia de Betânia", "Aldeia de Jericó", "Aldeia de Caná",
        "facil", "Lucas", "Lucas 24:13-31", "Apareceu a dois discípulos a caminho de Emaús, cujos olhos foram abertos ao partir do pão.")
    add("Qual apóstolo duvidou da ressurreição corpórea de Jesus até colocar o dedo nas marcas dos cravos e a mão no Seu lado ferido?",
        "Tomé (Dídimo)", "Pedro", "Filipe", "Natanael",
        "facil", "João", "João 20:24-28", "Tomé exclamou reverente ao tocar nas chagas de Cristo: 'Senhor meu, e Deus meu!'.")
    add("Quantos grandes peixes foram pescados milagrosamente pelos apóstolos na aparição no mar de Tiberíades em João 21?",
        "153 grandes peixes", "100 peixes", "70 peixes", "50 peixes",
        "medio", "João", "João 21:11", "Simão Pedro puxou a rede para terra, cheia de cento e cinquenta e três grandes peixes; e, sendo tantos, não se rompeu a rede.")
    add("Quantas vezes Jesus perguntou a Pedro: 'Simão, filho de Jonas, amas-me?' restaurando-o e dizendo: 'Apascenta as minhas ovelhas'?",
        "Três vezes (restaurando as três negações)", "Sete vezes", "Uma vez", "Dez vezes",
        "facil", "João", "João 21:15-17", "Pela terceira vez Jesus lhe perguntou se o amava, e Pedro entristeceu-se e disse: 'Senhor, tu sabes tudo; tu sabes que eu te amo'.")
    add("Qual é a solene Grande Comissão que Jesus ordenou aos Seus discípulos antes de ascender aos céus em Mateus 28:19?",
        "'Ide, portanto, fazei discípulos de todas as nações, batizando-os em nome do Pai, e do Filho, e do Espírito Santo'", "'Ficai em Jerusalém sem viajar'", "'Guardai o evangelho em segredo'", "'Guerreai contra os pagãos'",
        "facil", "Mateus", "Mateus 28:19-20", "'Ide, ensinai todas as nações, batizando-as em nome do Pai, e do Filho, e do Espírito Santo; ensinando-as a guardar todas as coisas que eu vos tenho mandado'.")

    # --- Mais Evangelhos para completar 200 ---
    add("Quantas gerações a genealogia de Jesus em Mateus 1 divide entre Abraão, Davi e o cativeiro da Babilônia?",
        "Três grupos de 14 gerações cada (42 gerações ao todo)", "Doze grupos de 7 gerações", "Sete gerações principais", "Cinquenta gerações ininterruptas",
        "medio", "Mateus", "Mateus 1:17", "De Abraão até Davi são catorze gerações; de Davi até ao exílio na Babilônia, catorze; e do exílio até Cristo, catorze gerações.")
    add("O que o anjo do Senhor disse a José em sonho sobre a concepção de Maria em Mateus 1:20?",
        "'Não temas receber Maria, tua mulher, porque o que nela está gerado é do Espírito Santo'", "'Leva Maria para Belém imediatamente'", "'Foge sozinho para o deserto'", "'Não tenhas casamento civil'",
        "facil", "Mateus", "Mateus 1:20", "Apareceu-lhe em sonho um anjo do Senhor dizendo: 'José, filho de Davi, não temas receber a Maria, tua mulher'.")
    add("Qual profissão Jesus exercia em Nazaré antes de iniciar Seu ministério público?",
        "Carpinteiro", "Pastor de ovelhas", "Pescador", "Ferreiro",
        "facil", "Marcos", "Marcos 6:3", "Os moradores de Nazaré indagaram com espanto: 'Não é este o carpinteiro, filho de Maria, e irmão de Tiago e de José?'.")
    add("Qual foi a primeira tentação enfrentada por Jesus no deserto em Mateus 4?",
        "Transformar pedras em pães para saciar Sua fome", "Pular do pináculo do templo", "Adorar o diabo em troca dos reinos do mundo", "Construir um palácio de pedra",
        "facil", "Mateus", "Mateus 4:3", "O tentador disse: 'Se tu és o Filho de Deus, manda que estas pedras se tornem em pães'.")
    add("Qual foi a confissão fundamental de Pedro sobre a identidade de Jesus em Cesareia de Filipe em Mateus 16:16?",
        "'Tu és o Cristo, o Filho do Deus vivo'", "'Tu és João Batista ressuscitado'", "'Tu és o profeta Jeremias'", "'Tu és um grande mestre de Israel'",
        "facil", "Mateus", "Mateus 16:16", "Simão Pedro respondeu com revelação do Pai: 'Tu és o Cristo, o Filho do Deus vivo'.")
    add("Quais dois profetas do Antigo Testamento apareceram conversando com Jesus glorificado na Transfiguração no monte?",
        "Moisés e Elias", "Abraão e Isaque", "Davi e Salomão", "Isaías e Jeremias",
        "facil", "Mateus", "Mateus 17:3; Lucas 9:30", "Eis que lhes apareceram Moisés (representando a Lei) e Elias (representando os Profetas), falando com Jesus.")
    add("O que os discípulos não puderam fazer com o jovem epiléptico que Jesus curou logo após a Transfiguração?",
        "Não puderam expulsar o espírito mudo por falta de oração e jejum", "Não conseguiram acordá-lo", "Não tinham azeite de unção", "Não sabiam orar em aramaico",
        "medio", "Mateus", "Mateus 17:19-21; Marcos 9:29", "Jesus disse aos discípulos: 'Por causa da vossa pouca fé... mas esta casta de demônios não se expulsa senão por oração e jejum'.")
    add("Como Jesus pagou o imposto do templo para Si e para Pedro em Cafarnaum em Mateus 17:27?",
        "Mandou Pedro pescar no mar com anzol e retirar uma moeda de prata (um estáter) da boca do primeiro peixe", "Doou dez moedas de ouro do tesouro", "Pediu aos fariseus que o isentassem", "Trabalhou um dia como carpinteiro",
        "facil", "Mateus", "Mateus 17:27", "Disse Jesus a Pedro: 'Lança o anzol e tira o primeiro peixe que subir; e, abrindo-lhe a boca, acharás um estáter; toma-o e dá-o por mim e por ti'.")
    add("Quantas vezes Jesus instruiu a Pedro que devemos perdoar o irmão que pecar contra nós em Mateus 18:21-22?",
        "Não apenas sete vezes, mas até setenta vezes sete", "Apenas uma vez", "Sete vezes no máximo", "Três vezes se houver testemunhas",
        "facil", "Mateus", "Mateus 18:21-22", "Jesus respondeu a Pedro: 'Não te digo que até sete vezes, mas até setenta vezes sete'.")
    add("O que aconteceu na Parábola do Credor Incompassivo com o servo que foi perdoado de uma dívida impagável de 10.000 talentos?",
        "Recusou-se a perdoar um conservo que lhe devia apenas 100 denários e o mandou lançar na prisão", "Perdoou generosamente todos os seus devedores", "Fez um banquete de gratidão", "Doou tudo aos pobres",
        "facil", "Mateus", "Mateus 18:28-30", "Saindo aquele servo, encontrou um dos seus conservos que lhe devia cem denários e, lançando mão dele, sufocava-o dizendo: 'Paga-me o que me deves!'.")
    add("O que os trabalhadores contratados na primeira hora na vinha murmuraram em Mateus 20?",
        "Porque os contratados na última hora receberam o mesmo salário de um denário que eles", "Porque o trabalho foi excessivamente pesado", "Porque não tiveram comida no campo", "Porque foram pagos com atraso",
        "facil", "Mateus", "Mateus 20:11-12", "Murmuravam contra o pai de família dizendo: 'Estes últimos trabalharam somente uma hora, e os igualaste a nós'.")
    add("O que a mãe de Tiago e João (filhos de Zebedeu) pediu de joelhos a Jesus para seus dois filhos em Mateus 20:21?",
        "Que no Seu Reino se assentassem um à Sua direita e outro à Sua esquerda", "Que recebessem os maiores palácios de Jerusalém", "Que nunca sofressem perseguições", "Que fossem sacerdotes do templo",
        "facil", "Mateus", "Mateus 20:20-21", "Ela pediu: 'Manda que no teu reino estes meus dois filhos se assentem, um à tua direita e outro à tua esquerda'.")
    add("O que Jesus disse sobre a verdadeira grandeza no Reino dos Céus em Mateus 20:26-28?",
        "'Quem quiser ser o maior entre vós seja o vosso servo, pois o Filho do Homem não veio para ser servido, mas para servir e dar a sua vida'", "'O maior é aquele que comanda mais soldados'", "'O maior é aquele que tem mais riquezas'", "'O maior é o que se senta à mesa real'",
        "facil", "Mateus", "Mateus 20:26-28", "'Quem quiser ser grande entre vós, seja vosso servo... assim como o Filho do homem não veio para ser servido, mas para servir'.")
    add("O que Jesus fez a uma figueira cheia de folhas, mas sem fruto nenhum, no caminho de Betânia em Mateus 21?",
        "Declarou que nunca mais nascesse fruto dela, e a figueira secou imediatamente", "Arrancou-a pela raiz com as mãos", "Abençoou-a para dar frutos no ano seguinte", "Mandou que os discípulos a regassem",
        "facil", "Mateus", "Mateus 21:19", "Vendo uma figueira à beira do caminho e não achando nela senão folhas, disse-lhe: 'Nunca mais nasça fruto de ti'. E a figueira secou imediatamente.")
    add("Qual é o Grande Mandamento da Lei segundo a resposta de Jesus ao intérprete da lei em Mateus 22:37-38?",
        "'Amarás o Senhor teu Deus de todo o teu coração, de toda a tua alma e de todo o teu entendimento'", "'Guardarás todos os sábados sem viajar'", "'Darás o dízimo da hortelã e do cominho'", "'Construirás altares de pedra pura'",
        "facil", "Mateus", "Mateus 22:37-38", "Jesus disse: 'Amarás o Senhor teu Deus de todo o teu coração, de toda a tua alma e de todo o teu pensamento. Este é o primeiro e grande mandamento'.")
    add("Qual é o segundo grande mandamento semelhante ao primeiro segundo Mateus 22:39?",
        "'Amarás o teu próximo como a ti mesmo'", "'Não emprestarás a juros'", "'Construirás escolas na cidade'", "'Falarás com sabedoria aos reis'",
        "facil", "Mateus", "Mateus 22:39-40", "'E o segundo, semelhante a este, é: Amarás o teu próximo como a ti mesmo. Destes dois mandamentos dependem toda a lei e os profetas'.")
    add("Com que expressão rigorosa Jesus repreendeu a hipocrisia religiosa dos escribas e fariseus em Mateus 23?",
        "'Ai de vós, escribas e fariseus, hipócritas! Sepulcros caiados, formosos por fora, mas cheios de ossos e imundície por dentro'", "'Benditos sois vós pelas vossas vestes nobres'", "'Vosso exemplo é digno de louvor universal'", "'Construístes os melhores monumentos'",
        "facil", "Mateus", "Mateus 23:27", "'Ai de vós, escribas e fariseus, hipócritas! Pois que sois semelhantes aos sepulcros caiados, que por fora parecem formosos, mas por dentro estão cheios de ossos'.")
    add("Qual lamentação comovente Jesus proferiu chorando sobre o destino de Jerusalém em Mateus 23:37?",
        "'Jerusalém, Jerusalém! Quantas vezes quis eu ajuntar os teus filhos como a galinha ajunta os seus pintinhos sob as asas, e tu não quiseste!'", "'Jerusalém será invadida amanhã'", "'Não gosto das tuas muralhas de pedra'", "'Fugirei para a Galileia'",
        "facil", "Mateus", "Mateus 23:37; Lucas 13:34", "'Jerusalém, Jerusalém, que matas os profetas e apedrejas os que te são enviados! Quantas vezes quis eu ajuntar os teus filhos, e não quiseste!'.")
    add("Quem sabe o dia e a hora exata da Segunda Vinda de Cristo segundo Mateus 24:36?",
        "Apenas o Pai nos céus, nem os anjos do céu nem o Filho na Sua condição humana", "Todos os profetas de Israel", "Os doze apóstolos em segredo", "Os reis da terra",
        "facil", "Mateus", "Mateus 24:36", "'Porém daquele dia e hora ninguém sabe, nem os anjos dos céus, nem o Filho, mas unicamente meu Pai'.")
    add("O que o servo infiel e mau fez com o talento que recebera de seu senhor na Parábola dos Talentos em Mateus 25?",
        "Cavou na terra e escondeu o dinheiro por medo, sendo repreendido e lançado nas trevas exteriores", "Investiu no comércio e ganhou mais cinco", "Doou aos pobres da cidade", "Comprou uma casa nova",
        "facil", "Mateus", "Mateus 25:25-30", "O que recebera um talento cavou na terra e escondeu o dinheiro; o senhor o repreendeu como servo mau e negligente.")
    add("O que o Rei dirá aos que estiverem à Sua direita no Julgamento das Nações em Mateus 25:34-40?",
        "'Vinde, benditos de meu Pai, possuí por herança o reino; porque tive fome e me destes de comer, tive sede e me destes de beber... sempre que o fizestes a um destes meus pequeninos irmãos, a mim o fizestes'", "'Vinde os que fostes reis na terra'", "'Entrai os que acumulastes muitas terras'", "'Recebei coroas de prata'",
        "facil", "Mateus", "Mateus 25:34-40", "'Em verdade vos digo que quando o fizestes a um destes meus pequeninos irmãos, a mim o fizestes'.")
    add("Qual fim trágico teve o traidor Judas Iscariotes após devolver as trinta moedas de prata no Templo?",
        "Sentiu remorso, atirou as moedas no santuário, retirou-se e foi enforcar-se", "Fugiu disfarçado para Roma", "Foi coroado governador de Jericó", "Pediu perdão a Pedro",
        "facil", "Mateus", "Mateus 27:3-5; Atos 1:18", "Judas, tocado de remorso, atirou para o templo as trinta moedas de prata e foi enforcar-se.")
    add("Qual campo foi comprado pelos sacerdotes com as trinta moedas de prata de Judas para sepultura de peregrinos?",
        "O Campo do Oleiro / Campo de Sangue (Aceldama)", "O campo de Macpela", "O campo de Boaz em Belém", "A vinha de Nabote",
        "medio", "Mateus", "Mateus 27:7-8; Atos 1:19", "Tomando conselho, compraram com elas o campo do oleiro, para sepultura dos forasteiros; por isso aquele campo foi chamado Campo de Sangue.")
    add("Qual confissão espontânea o centurião romano e os soldados fizeram ao pé da cruz ao verem o terremoto e os sinais?",
        "'Verdadeiramente este era o Filho de Deus!'", "'Este homem era culpado de sedição'", "'Fugiremos de Jerusalém com medo'", "'Pilatos errou no julgamento'",
        "facil", "Mateus", "Mateus 27:54", "O centurião e os que guardavam a Jesus, vendo o terremoto e as coisas que haviam sucedido, tiveram grande temor e disseram: 'Verdadeiramente este era o Filho de Deus'.")
    add("Qual mentira os principais sacerdotes pagaram aos soldados romanos para espalharem sobre a ressurreição em Mateus 28?",
        "Dizerem que os discípulos de Jesus vieram de noite e roubaram o corpo enquanto os guardas dormiam", "Dizerem que Jesus nunca fora crucificado", "Dizerem que o túmulo fora destruído por um raio", "Dizerem que levaram o corpo para Roma",
        "facil", "Mateus", "Mateus 28:12-15", "Deram muito dinheiro aos soldados dizendo: 'Dizei: Vieram de noite os seus discípulos e, dormindo nós, o furtaram'.")
    add("Qual promessa maravilhosa encerra o Evangelho de Mateus no capítulo 28:20?",
        "'E eis que eu estou convosco todos os dias, até à consumação dos séculos. Amém!'", "'Voltarei apenas no ano mil'", "'Ficarei ausente de vós'", "'Não vos deixarei nenhuma paz'",
        "facil", "Mateus", "Mateus 28:20", "'E eis que eu estou convosco todos os dias, até à consumação dos séculos. Amém'.")
    add("Quem foi o autor do Evangelho de Marcos, discípulo e companheiro de Pedro e Paulo?",
        "João Marcos", "Lucas, o médico", "Mateus, o cobrador", "Barnabé",
        "facil", "Marcos", "Marcos 1:1; Atos 12:12", "Marcos registrou com brevidade e dinamismo o ministério de Jesus com base nos relatos orais do apóstolo Pedro.")
    add("Qual palavra aramaica Jesus usou ao abrir os ouvidos e soltar a língua do homem surdo e gago em Marcos 7:34?",
        "'Efatá' (que quer dizer: 'Abre-te!')", "'Talita cumi'", "'Eli, Eli'", "'Maranata'",
        "medio", "Marcos", "Marcos 7:34-35", "Olhando para o céu, suspirou e disse-lhe: 'Efatá' (isto é: Abre-te). E logo se lhe abriram os ouvidos e falava perfeitamente.")
    add("Qual homem rico e influente de Jerusalém procurou Jesus com reverência perguntando: 'Que farei para herdar a vida eterna?'?",
        "O jovem rico", "Zaqueu", "Nicodemos", "Simão fariseu",
        "facil", "Marcos", "Marcos 10:17-22", "Jesus fitou-o e o amou, dizendo: 'Uma coisa te falta: vai, vende tudo quanto tens e dá-o aos pobres; depois vem e segue-me'. E ele retirou-se triste.")
    add("O que Bartimeu fez imediatamente ao ouvir que Jesus o chamava para ser curado em Jericó em Marcos 10:50?",
        "Lançou de si a sua capa de mendigo, levantou-se de um salto e foi ter com Jesus", "Pediu aos amigos que o levassem no leito", "Contou suas esmolas de cobre", "Ficou em silêncio esperando",
        "medio", "Marcos", "Marcos 10:50", "Bartimeu, lançando de si a sua capa, levantou-se e foi ter com Jesus; e Jesus lhe disse: 'Vai, a tua fé te salvou'.")
    add("A quem o Evangelho de Lucas e o livro de Atos dos Apóstolos são formalmente dedicados?",
        "Ao excelentíssimo Teófilo", "Ao imperador César", "Ao sumo sacerdote Anás", "Ao apóstolo Pedro",
        "facil", "Lucas", "Lucas 1:3; Atos 1:1", "Lucas dedicou sua minuciosa pesquisa histórica ao 'excelentíssimo Teófilo', para que tivesse certeza das verdades ensinadas.")
    add("Qual cântico sublime e histórico de louvor a virgem Maria entoou na casa de Isabel em Lucas 1:46-55?",
        "O Magnificat ('A minha alma engrandece ao Senhor, e o meu espírito se alegra em Deus meu Salvador')", "O cântico dos degraus", "A canção da colheita", "O hino de Moisés",
        "facil", "Lucas", "Lucas 1:46-55", "Disse Maria: 'A minha alma engrandece ao Senhor, e o meu espírito se alegra em Deus meu Salvador, porque atentou na baixeza de sua serva'.")
    add("Qual idoso e piedoso ancião tomou o menino Jesus nos braços no Templo e profetizou que Ele seria luz para os gentios?",
        "Simeão", "Zacarias", "Gamaliel", "Nicodemos",
        "facil", "Lucas", "Lucas 2:25-32", "Simeão tomou o menino nos braços e louvou a Deus dizendo: 'Agora, Senhor, despedes em paz o teu servo... porque os meus olhos viram a tua salvação'.")
    add("Qual profetisa idosa de 84 anos servia a Deus no Templo com jejuns e orações dia e noite ao ver o menino Jesus?",
        "Ana, filha de Fanuel, da tribo de Aser", "Hulda", "Miriã", "Débora",
        "medio", "Lucas", "Lucas 2:36-38", "A profetisa viúva Ana dava graças a Deus e falava do Menino a todos os que esperavam a redenção em Jerusalém.")
    add("O que Pedro exclamou prostrado aos pés de Jesus diante da primeira pesca milagrosa em Lucas 5:8?",
        "'Senhor, ausenta-te de mim, porquanto sou um homem pecador!'", "'Construamos três tendas aqui'", "'Quantos denários valem estes peixes?'", "'Vamos pescar no mar Morto'",
        "facil", "Lucas", "Lucas 5:8-10", "Vendo isto Simão Pedro, prostrou-se aos pés de Jesus dizendo: 'Senhor, ausenta-te de mim, pois sou homem pecador'. Jesus disse: 'Não temas; de agora em diante serás pescador de homens'.")
    add("O que Jesus fez ao se deparar com o cortejo fúnebre do jovem filho único de uma viúva na cidade de Naim em Lucas 7?",
        "Moveu-se de íntima compaixão pela mãe viúva, tocou o esquife e disse: 'Jovem, a ti te digo: Levanta-te!', e o morto se sentou", "Acompanhou o cortejo em silêncio", "Doou pão aos enlutados", "Mandou sepultá-lo na gruta",
        "facil", "Lucas", "Lucas 7:12-15", "Vendo-a, o Senhor moveu-se de íntima compaixão para com ela e disse-lhe: 'Não chores'. Tocou o caixão e o jovem ressuscitou.")
    add("O que a mulher pecadora fez aos pés de Jesus na casa de Simão, o fariseu, em Lucas 7:37-38?",
        "Regou os pés de Jesus com lágrimas de arrependimento, enxugou-os com os cabelos, beijou-os e ungiu-os com unguento perfumado", "Pediu esmola aos convidados", "Criticou a comida servida", "Sentou-se à cabeceira da mesa",
        "facil", "Lucas", "Lucas 7:38-47", "Jesus disse a Simão: 'Perdoados lhe são os seus muitos pecados, porque muito amou'.")
    add("Quantos discípulos Jesus enviou de dois em dois à Sua frente para curarem e anunciarem o Reino em Lucas 10?",
        "70 (ou 72) discípulos", "12 discípulos", "10 discípulos", "100 discípulos",
        "medio", "Lucas", "Lucas 10:1", "Depois disto designou o Senhor outros setenta, e os enviou de dois em dois adiante de si a todas as cidades.")
    add("O que Marta reclamava de sua irmã Maria enquanto Jesus ensinava na casa de Betânia em Lucas 10:39-42?",
        "Que Maria ficara assentada aos pés de Jesus ouvindo a Sua palavra deixando todo o serviço doméstico para ela sozinha", "Que Maria gastou todo o dinheiro da compra", "Que Maria não quis receber os apóstolos", "Que Maria dormiu durante a oração",
        "facil", "Lucas", "Lucas 10:40-42", "Jesus disse: 'Marta, Marta, andas ansiosa e afadigada com muitas coisas, mas uma só é necessária; Maria escolheu a boa parte, a qual não lhe será tirada'.")
    add("Qual parábola ensina sobre a persistência na oração através de uma viúva pobre e um juiz que não temia a Deus em Lucas 18?",
        "A Parábola do Juiz Iníquo e da Viúva Persistente", "A Parábola dos Dois Devedores", "A Parábola da Candeia", "A Parábola do Sal da Terra",
        "facil", "Lucas", "Lucas 18:1-8", "Jesus contou esta parábola sobre o dever de orar sempre e nunca esmorecer.")
    add("Qual promessa de restituição Zaqueu fez a Jesus e aos pobres no dia de sua conversão em Lucas 19:8?",
        "'Dou aos pobres metade dos meus bens; e, se em alguma coisa defraudei alguém, restituo quadruplicado'", "'Doarei dez moedas ao templo'", "'Nunca mais cobro impostos'", "'Construirei uma escola em Jericó'",
        "facil", "Lucas", "Lucas 19:8-9", "Zaqueu disse: 'Senhor, eis que eu dou aos pobres metade dos meus bens; e, se defraudei alguém, devolvo quatro vezes mais'. Jesus declarou: 'Hoje veio a salvação a esta casa'.")
    add("Como Jesus chamou o apóstolo João e seu irmão Tiago por causa de seu temperamento impetuoso?",
        "Boanerges (que significa: Filhos do Trovão)", "Barjonas", "Cefas", "Zelotes",
        "medio", "Marcos", "Marcos 3:17", "A Tiago e a João pôs o sobrenome de Boanerges, que significa: Filhos do trovão.")
    add("O que o apóstolo João declara sobre Jesus no prólogo de seu Evangelho em João 1:1?",
        "'No princípio era o Verbo, e o Verbo estava com Deus, e o Verbo era Deus'", "'No princípio criou Deus os céus e a terra'", "'Jesus nasceu em Belém de Judá'", "'João Batista veio pregando arrependimento'",
        "facil", "João", "João 1:1", "O quarto Evangelho abre proclamando a divindade eterna de Cristo: 'No princípio era o Verbo, e o Verbo estava com Deus, e o Verbo era Deus'.")
    add("O que João 1:14 afirma sobre a encarnação do Filho de Deus?",
        "'E o Verbo se fez carne e habitou entre nós, cheio de graça e de verdade'", "'O Verbo permaneceu invisível nos céus'", "'O Verbo assumiu corpo de anjo alado'", "'O Verbo veio em carruagem de fogo'",
        "facil", "João", "João 1:14", "'E o Verbo se fez carne, e habitou entre nós, e vimos a sua glória, como a glória do unigênito do Pai, cheio de graça e de verdade'.")
    add("Quem levou seu irmão Simão Pedro a conhecer Jesus após ouvir João Batista apontar o Cordeiro?",
        "André", "Filipe", "Tiago", "Natanael",
        "facil", "João", "João 1:40-42", "André, irmão de Simão Pedro, achou primeiro a seu irmão Simão e disse-lhe: 'Achamos o Messias'. E levou-o a Jesus.")
    add("Onde Jesus disse ter visto Natanael antes que Filipe o chamasse em João 1:48?",
        "Debaixo da figueira", "Na praia do mar", "No templo de Jerusalém", "Na oficina de Nazaré",
        "medio", "João", "João 1:48-49", "Jesus disse: 'Antes que Filipe te chamasse, te vi eu, estando tu debaixo da figueira'. Natanael exclamou: 'Rabi, tu és o Filho de Deus!'.")
    add("Quantos anos fazia que o homem enfermo jazia paralítico junto ao tanque de Betesda em Jerusalém em João 5?",
        "38 anos", "12 anos", "40 anos", "20 anos",
        "medio", "João", "João 5:5", "Estava ali um homem que, havia trinta e oito anos, jazia enfermo; Jesus disse-lhe: 'Levanta-te, toma o teu leito e anda'.")
    add("Qual grande proclamação messiânica Jesus fez em Cafarnaum após a multiplicação dos pães em João 6:35?",
        "'Eu sou o Pão da Vida; aquele que vem a mim não terá fome, e quem crê em mim nunca terá sede'", "'Eu sou o rei militar de Israel'", "'Eu sou o maná que se compra com prata'", "'Eu sou o senhor do templo'",
        "facil", "João", "João 6:35", "Declarou-lhes Jesus: 'Eu sou o pão da vida; o que vem a mim jamais terá fome, e o que crê em mim nunca terá sede'.")
    add("Qual declaração sobre a luz espiritual Jesus fez no pátio do templo em João 8:12?",
        "'Eu sou a Luz do Mundo; quem me segue não andará em trevas, mas terá a luz da vida'", "'A luz pertence às estrelas'", "'As tochas de prata iluminam o caminho'", "'Não há trevas na terra'",
        "facil", "João", "João 8:12", "Falou-lhes Jesus outra vez, dizendo: 'Eu sou a luz do mundo; quem me segue não andará em trevas, mas terá a luz da vida'.")
    add("O que Jesus disse sobre a verdade libertadora em João 8:32?",
        "'E conhecereis a verdade, e a verdade vos libertará'", "'A verdade é relativa aos homens'", "'A verdade é segredo dos mestres'", "'A mentira às vezes é útil'",
        "facil", "João", "João 8:32", "Disse Jesus aos que creram nEle: 'E conhecereis a verdade, e a verdade vos libertará'.")
    add("Qual revelação de proteção e sacrifício voluntário Jesus faz sobre Si mesmo em João 10:11?",
        "'Eu sou o Bom Pastor; o bom pastor dá a sua vida pelas ovelhas'", "'Eu sou o pastor que cobra impostos'", "'Eu sou o mercenário que foge do lobo'", "'Eu sou o juiz implacável'",
        "facil", "João", "João 10:11", "'Eu sou o bom pastor; o bom pastor dá a sua vida pelas ovelhas. O mercenário, que não é pastor, vê vir o lobo e foge'.")
    add("Qual conforto imortal Jesus disse a Marta diante da perda de Lázaro em João 11:25-26?",
        "'Eu sou a Ressurreição e a Vida; quem crê em mim, ainda que esteja morto, viverá'", "'A morte é o fim irremediável de tudo'", "'Não penses mais no teu irmão'", "'Chora sem esperança'",
        "facil", "João", "João 11:25-26", "Disse-lhe Jesus: 'Eu sou a ressurreição e a vida; quem crê em mim, ainda que esteja morto, viverá; e todo aquele que vive, e crê em mim, nunca morrerá'.")
    add("Qual parábola da semente Jesus usou ao anunciar a necessidade de Sua morte redentora em João 12:24?",
        "'Se o grão de trigo, caindo na terra, não morrer, fica ele só; mas se morrer, dá muito fruto'", "'A oliveira não precisa de podas'", "'A figueira brota sem sementes'", "'O joio alimenta as aves'",
        "facil", "João", "João 12:24", "'Em verdade, em verdade vos digo que, se o grão de trigo, caindo na terra, não morrer, fica ele só; mas se morrer, dá muito fruto'.")
    add("Qual declaração exclusiva sobre o caminho para o Pai celestial Jesus fez a Tomé em João 14:6?",
        "'Eu sou o Caminho, e a Verdade, e a Vida; ninguém vem ao Pai senão por mim'", "'Todos os caminhos levam a Deus igualmente'", "'A sabedoria humana abre as portas do céu'", "'Basta praticar boas obras sem fé'",
        "facil", "João", "João 14:6", "Disse-lhe Jesus: 'Eu sou o caminho, e a verdade e a vida; ninguém vem ao Pai, senão por mim'.")
    add("Qual promessa do Consolador eterno Jesus fez aos discípulos em João 14:16-17?",
        "O Espírito da Verdade (o Parácleto), para estar convosco para sempre", "Um exército de soldados celestes visíveis", "Uma coroa de pedras preciosas", "Riquezas perpétuas",
        "facil", "João", "João 14:16-17", "'E eu rogarei ao Pai, e ele vos dará outro Consolador, para que fique convosco para sempre, o Espírito da verdade'.")
    add("Qual paz incomparável Jesus deixou como herança aos Seus discípulos em João 14:27?",
        "'Deixo-vos a paz, a minha paz vos dou; não vo-la dou como o mundo a dá. Não se turbe o vosso coração'", "'Dou-vos a paz das armas invencíveis'", "'A paz depende do silêncio das nações'", "'Não tereis nenhuma aflição na terra'",
        "facil", "João", "João 14:27", "'Deixo-vos a paz, a minha paz vos dou; não vo-la dou como o mundo a dá. Não se turbe o vosso coração, nem se atemorize'.")
    add("A que Jesus se compara e a que compara os Seus discípulos na alegoria de João 15:5?",
        "'Eu sou a Videira, vós as varas (ramos); quem está em mim, e eu nele, esse dá muito fruto; porque sem mim nada podeis fazer'", "'Eu sou o pastor e vós as cabras'", "'Eu sou o oleiro e vós o ferro'", "'Eu sou o general e vós os arqueiros'",
        "facil", "João", "João 15:5", "'Eu sou a videira, vós as varas; quem está em mim, e eu nele, esse dá muito fruto; porque sem mim nada podeis fazer'.")
    add("Qual palavra de encorajamento triunfal Jesus conclui antes de Sua oração sacerdotal em João 16:33?",
        "'No mundo tereis aflições, mas tende bom ânimo, eu venci o mundo'", "'Nunca passareis por tribulações'", "'O mundo será sempre vosso amigo'", "'Fugi das batalhas'",
        "facil", "João", "João 16:33", "'Tenho-vos dito isto, para que em mim tenhais paz; no mundo tereis aflições, mas tende bom ânimo, eu venci o mundo'.")
    add("O que saiu do lado de Jesus quando o soldado romano traspassou o Seu corpo na cruz com uma lança?",
        "Sangue e água", "Apenas vinagre", "Azeite puro", "Nada saiu",
        "facil", "João", "João 19:34", "Contudo um dos soldados lhe furou o lado com uma lança, e logo saiu sangue e água.")
    add("Qual foi a promessa gloriosa feita aos que creem sem terem visto com os próprios olhos em João 20:29?",
        "'Bem-aventurados os que não viram e creram'", "'Mais valem os que viram pessoalmente'", "'Apenas os apóstolos têm fé verdadeira'", "'Ninguém pode crer sem tocar com as mãos'",
        "facil", "João", "João 20:29", "Disse-lhe Jesus: 'Porque me viste, Tomé, creste; bem-aventurados os que não viram e creram'.")

    # --- 49 Questões Finais dos Evangelhos ---
    add("Qual pergunta os Magos do Oriente fizeram ao chegarem a Jerusalém em Mateus 2:2?",
        "'Onde está aquele que é nascido Rei dos Judeus? Porque vimos a sua estrela no Oriente e viemos adorá-lo'", "'Onde fica o palácio de Herodes?'", "'Quem governa esta cidade?'", "'Onde estão os sacerdotes?'",
        "facil", "Mateus", "Mateus 2:2", "Os magos perguntaram: 'Onde está o rei dos judeus que é nascido? Porque vimos a sua estrela no oriente e viemos a adorá-lo'.")
    add("Qual advertência vigorosa João Batista fez aos fariseus e saduceus que vinham ao batismo em Mateus 3:7-8?",
        "'Produzi, pois, frutos dignos de arrependimento; e já está posto o machado à raiz das árvores'", "'Vinde receber as vossas bênçãos de ouro'", "'Sois a geração mais santa de Judá'", "'Não precisais de arrependimento'",
        "facil", "Mateus", "Mateus 3:7-10", "João advertiu: 'Raça de víboras, quem vos ensinou a fugir da ira futura? Produzi, pois, frutos dignos de arrependimento'.")
    add("O que Jesus ensina sobre a prática da esmola e caridade em Mateus 6:1-3?",
        "Que a tua mão esquerda não saiba o que faz a tua direita, e a tua esmola seja dada em secreto", "Que toques trombetas nas sinagogas e praças", "Que anuncies em alta voz para todos ouvirem", "Que publiques o valor em cartazes",
        "facil", "Mateus", "Mateus 6:1-3", "Jesus ensinou: 'Quando tu deres esmola, não saiba a tua mão esquerda o que faz a tua direita, para que a tua esmola seja dada em secreto'.")
    add("O que Jesus ensina sobre o jejum piedoso em Mateus 6:16-17?",
        "Unge a tua cabeça e lava o teu rosto, para não pareceres aos homens que jejuas, mas a teu Pai em secreto", "Desfigura o teu rosto com cinzas", "Veste roupas rasgadas e sujas", "Chora pelas esquinas da cidade",
        "facil", "Mateus", "Mateus 6:16-17", "'Tu, porém, quando jejuares, unge a tua cabeça, e lava o teu rosto, para não pareceres aos homens que jejuas, mas a teu Pai, que está em secreto'.")
    add("O que Jesus declara sobre as duas portas e caminhos em Mateus 7:13-14?",
        "Larga é a porta e espaçoso o caminho que conduz à perdição; mas estreita é a porta e apertado o caminho que conduz à vida", "Todos os caminhos chegam ao mesmo destino", "A porta larga é a mais segura", "O caminho espaçoso leva à paz",
        "facil", "Mateus", "Mateus 7:13-14", "'Entrai pela porta estreita; porque larga é a porta, e espaçoso o caminho que conduz à perdição... e estreita a porta que conduz à vida'.")
    add("Quem rogou a Jesus dizendo: 'Senhor, a minha filha está horrivelmente atormentada por um demônio', demonstrando grande fé perseverante em Mateus 15?",
        "A mulher cananeia (siro-fenícia)", "A mulher do fluxo de sangue", "A viúva de Naim", "Maria Madalena",
        "facil", "Mateus", "Mateus 15:22-28", "Jesus disse-lhe: 'Ó mulher, grande é a tua fé! Seja isso feito para contigo como tu desejas'. E desde aquela hora a sua filha ficou sã.")
    add("Qual convite suave e consolador Jesus faz a todos os aflitos em Mateus 11:28-30?",
        "'Vinde a mim, todos os que estais cansados e oprimidos, e eu vos aliviarei; tomai sobre vós o meu jugo e aprendei de mim'", "'Construí santuários de mármore'", "'Guerreai contra as nações'", "'Acumulai mais riquezas'",
        "facil", "Mateus", "Mateus 11:28-30", "'Vinde a mim, todos os que estais cansados e sobrecarregados, e eu vos aliviarei... porque o meu jugo é suave, e o meu fardo é leve'.")
    add("Qual pecado imperdoável Jesus advertiu que não tem perdão nem neste século nem no futuro em Mateus 12:31-32?",
        "A blasfêmia contra o Espírito Santo", "A negação de Pedro", "O furto material", "A mentira cotidiana",
        "facil", "Mateus", "Mateus 12:31-32", "'Todo o pecado e blasfêmia se perdoará aos homens; mas a blasfêmia contra o Espírito Santo não será perdoada aos homens'.")
    add("Qual foi o único sinal milagroso que Jesus disse que seria dado àquela geração perversa em Mateus 12:39-40?",
        "O sinal do profeta Jonas (três dias e noites no ventre do peixe, figura da morte e ressurreição)", "O sinal do fogo do céu de Elias", "O sinal do relógio de Acaz", "O sinal da sarça ardente",
        "facil", "Mateus", "Mateus 12:39-40", "'Não se lhe dará outro sinal senão o sinal do profeta Jonas; pois como Jonas esteve três dias e três noites no ventre do grande peixe, assim estará o Filho do homem'.")
    add("O que o homem fez ao encontrar o tesouro escondido no campo na parábola de Mateus 13:44?",
        "Cheio de alegria, foi, vendeu tudo quanto possuía e comprou aquele campo", "Contou o segredo aos vizinhos", "Deixou o tesouro onde estava", "Pediu aos soldados que o guardassem",
        "facil", "Mateus", "Mateus 13:44", "'O reino dos céus é semelhante a um tesouro escondido num campo, o qual um homem achou e escondeu; e, pelo gozo dele, vai, vende tudo quanto tem e compra aquele campo'.")
    add("O que o negociante fez ao encontrar uma pérola de grandíssimo valor em Mateus 13:45-46?",
        "Foi, vendeu tudo quanto tinha e comprou a pérola de grande preço", "Guardou o dinheiro no banco", "Comprou muitas pérolas menores", "Desprezou a joia",
        "facil", "Mateus", "Mateus 13:45-46", "'Achando uma pérola de grande valor, foi, vendeu tudo quanto tinha e comprou-a'.")
    add("Como João Batista foi martirizado pelo tetrarca Herodes Antipas na fortaleza de Maquero?",
        "Foi decapitado na prisão a pedido da filha de Herodias após dançar no banquete de aniversário", "Foi envenenado no calabouço", "Morreu afogado no rio", "Foi exilado em Roma",
        "facil", "Mateus", "Mateus 14:6-10; Marcos 6:21-28", "A filha de Herodias dançou no banquete e pediu num prato a cabeça de João Batista; e Herodes mandou degolá-lo no cárcere.")
    add("O que os discípulos disseram a Jesus quando Ele curou o cego em Betsaida na primeira imposição de mãos em Marcos 8:24?",
        "'Vejo os homens como árvores que andam'", "'Vejo o sol brilhante'", "'Vejo anjos celestiais'", "'Ainda não vejo nada'",
        "medio", "Marcos", "Marcos 8:24", "O cego, olhando para cima, disse: 'Vejo os homens; pois os vejo como árvores que andam'. Depois Jesus pôs outra vez as mãos sobre os olhos dele e ele viu claramente.")
    add("Qual resposta admirável Jesus deu aos fariseus sobre a tributação romana mostrando a moeda com a efígie de César em Marcos 12:17?",
        "'Dai a César o que é de César, e a Deus o que é de Deus'", "'Não pagueis nenhum tributo a Roma'", "'Pagai apenas com moedas de ouro'", "'O imperador não tem autoridade terrena'",
        "facil", "Marcos", "Marcos 12:17", "Jesus lhes respondeu: 'Dai a César o que é de César, e a Deus o que é de Deus'. E maravilharam-se dele.")
    add("O que o anjo do Senhor disse às mulheres no túmulo aberto no primeiro dia da semana em Marcos 16:6?",
        "'Não vos assusteis; buscais a Jesus Nazareno, que foi crucificado; já ressuscitou, não está aqui; eis aqui o lugar onde o puseram'", "'Ele foi levado para a Galileia'", "'O túmulo foi violado por ladrões'", "'Voltai para vossas casas'",
        "facil", "Marcos", "Marcos 16:6", "'Ele ressuscitou; não está aqui; eis o lugar onde o puseram. Mas ide, dizei a seus discípulos e a Pedro que ele vai adiante de vós para a Galileia'.")
    add("O que Maria respondeu ao anjo Gabriel ao saber que seria a mãe do Salvador em Lucas 1:38?",
        "'Eis aqui a serva do Senhor; cumpra-se em mim segundo a tua palavra'", "'Não aceito esta honra'", "'Tenho medo dos vizinhos'", "'Esperarei ficar mais idosa'",
        "facil", "Lucas", "Lucas 1:38", "Disse Maria: 'Eis aqui a serva do Senhor; cumpra-se em mim segundo a tua palavra'. E o anjo ausentou-se dela.")
    add("Qual sacrifício simples e humilde José e Maria ofereceram no Templo aos quarenta dias segundo a Lei em Lucas 2:24?",
        "Um par de rolas ou dois pombinhos (oferta dos pobres)", "Um novilho cevado", "Um cordeiro macho de um ano", "Cem barras de prata",
        "medio", "Lucas", "Lucas 2:24; Levítico 12:8", "Ofereceram sacrifício segundo o que está dito na Lei do Senhor: 'Um par de rolas ou dois pombinhos', demonstrando a simplicidade de sua família.")
    add("O que os ouvintes enfurecidos da sinagoga de Nazaré tentaram fazer a Jesus após Seu sermão inaugural em Lucas 4:28-29?",
        "Levaram-no até o cume do precipício do monte para o precipitarem abaixo, mas Ele passou pelo meio deles e retirou-se", "Apedrejaram-no na praça", "Prenderam-no no calabouço", "Coroaram-no rei da cidade",
        "medio", "Lucas", "Lucas 4:28-30", "Levantando-se, expulsaram-no da cidade e o levaram até ao cume do monte para o precipitarem; Ele, porém, passando pelo meio deles, retirou-se.")
    add("Quais mulheres piedosas seguiam a Jesus e serviam o Seu ministério com seus próprios bens em Lucas 8:1-3?",
        "Maria Madalena, Joana mulher de Cuza procurador de Herodes, e Susana, e muitas outras", "A rainha Vasti e a rainha de Sabá", "As filhas de Ló", "A rainha Jezabel",
        "medio", "Lucas", "Lucas 8:2-3", "Mulheres que haviam sido curadas de espíritos malignos e de enfermidades: Maria chamada Madalena, Joana mulher de Cuza e Susana, as quais o serviam com os seus bens.")
    add("Quantas ovelhas o bom pastor deixou no redil para ir pelo deserto em busca daquela única que se havia extraviado em Lucas 15:4?",
        "Deixou as noventa e nove no deserto e foi atrás da perdida até achá-la", "Deixou dez ovelhas", "Não se importou com a ovelha perdida", "Esperou que a ovelha voltasse sozinha",
        "facil", "Lucas", "Lucas 15:4-7", "Jesus disse: 'Qual de vós, tendo cem ovelhas e perdendo uma delas, não deixa no deserto as noventa e nove e vai após a perdida até que a encontre?'.")
    add("Qual oração de perdão pelos Seus algozes Jesus proferiu na cruz em Lucas 23:34?",
        "'Pai, perdoa-lhes, porque não sabem o que fazem'", "'Faze descer fogo sobre esta cidade'", "'Vinga o meu sangue inocente'", "'Castiga os soldados romanos'",
        "facil", "Lucas", "Lucas 23:34", "Dizia Jesus: 'Pai, perdoa-lhes, porque não sabem o que fazem'. E, repartindo as suas vestes, lançaram sortes.")
    add("Qual foi a última declaração de entrega filial de Jesus ao expirar na cruz em Lucas 23:46?",
        "'Pai, nas tuas mãos entrego o meu espírito'", "'Fui derrotado pelos sacerdotes'", "'Adeus a todos os homens'", "'Minha obra fracassou'",
        "facil", "Lucas", "Lucas 23:46; Salmo 31:5", "Jesus, clamando com grande voz, disse: 'Pai, nas tuas mãos entrego o meu espírito'. E, havendo dito isto, expirou.")
    add("O que os dois discípulos de Emaús disseram ao reconhecerem Jesus ressurreto ao partir do pão em Lucas 24:32?",
        "'Porventura não ardia em nós o nosso coração quando, pelo caminho, nos falava e nos abria as Escrituras?'", "'Pensamos que fosse um fantasma'", "'Não deveríamos ter dado hospedagem'", "'Vamos esquecer o que vimos'",
        "facil", "Lucas", "Lucas 24:32", "Disseram um ao outro: 'Porventura não ardia o nosso coração quando pelo caminho nos falava e quando nos abria as Escrituras?'.")
    add("O que Jesus comeu diante dos apóstolos reunidos no cenáculo em Lucas 24:42-43 para provar Sua ressurreição corpórea?",
        "Um pedaço de peixe assado e um favo de mel", "Pão e azeitonas", "Uvas frescas", "Carne de cordeiro",
        "medio", "Lucas", "Lucas 24:41-43", "Apresentaram-lhe um pedaço de peixe assado e um favo de mel; e ele tomou-o e comeu diante deles.")
    add("Em qual monte ou localidade Jesus ergueu as mãos abençoando os apóstolos e foi elevado às alturas em Lucas 24:50-51?",
        "Em Betânia (no Monte das Oliveiras)", "No cume do Monte Sinai", "Nas margens do mar da Galileia", "No átrio do Templo",
        "facil", "Lucas", "Lucas 24:50-51; Atos 1:9-12", "Levou-os fora até Betânia e, levantando as suas mãos, os abençoou. E aconteceu que, abençoando-os ele, se apartou deles e foi elevado ao céu.")
    add("O que João Batista disse com profunda humildade comparando-se a Jesus em João 3:30?",
        "'É necessário que ele cresça e que eu diminua'", "'Eu sou o Messias esperado'", "'Nós somos dois iguais'", "'Eu devo fundar uma nova seita'",
        "facil", "João", "João 3:30", "João Batista declarou aos seus discípulos: 'É necessário que ele cresça e que eu diminua. Aquele que vem de cima é sobre todos'.")
    add("Quantos pórticos cobertos cercavam o tanque de Betesda onde os enfermos esperavam o mover das águas em João 5:2?",
        "Cinco pórticos", "Sete pórticos", "Doze pórticos", "Três pórticos",
        "medio", "João", "João 5:2", "Ora em Jerusalém há, próximo à porta das ovelhas, um tanque, chamado em hebreu Betesda, o qual tem cinco alpendres.")
    add("O que Pedro respondeu quando Jesus perguntou aos doze se também queriam ir embora em João 6:68-69?",
        "'Senhor, para quem iremos nós? Tu tens as palavras da vida eterna, e nós temos crido que tu és o Cristo'", "'Nós também queremos voltar para as redes'", "'Esperamos outro mestre'", "'Ficaremos apenas mais alguns dias'",
        "facil", "João", "João 6:68-69", "Respondeu-lhe Simão Pedro: 'Senhor, para quem iremos nós? Tu tens as palavras da vida eterna. E nós temos crido e conhecido que tu és o Santo de Deus'.")
    add("O que Jesus disse à mulher flagrada em adultério após todos os acusadores se retirarem em João 8:10-11?",
        "'Nem eu tão pouco te condeno; vai, e não peques mais'", "'Deves pagar uma multa aos sacerdotes'", "'Nunca mais entres no templo'", "'Serás açoitada pelos guardas'",
        "facil", "João", "João 8:10-11", "Jesus disse-lhe: 'Mulher, onde estão aqueles teus acusadores? Ninguém te condenou?'. Ela disse: 'Ninguém, Senhor'. E disse-lhe Jesus: 'Nem eu também te condeno; vai-te, e não peques mais'.")
    add("Qual é o Novo Mandamento que Jesus deu aos Seus discípulos na Última Ceia em João 13:34?",
        "'Que vos ameis uns aos outros; assim como eu vos amei, que também vós vos ameis uns aos outros'", "'Que construais muitas sinagogas'", "'Que façais sacrifícios diários'", "'Que sejais os mais ricos de Jerusalém'",
        "facil", "João", "João 13:34-35", "'Um novo mandamento vos dou: Que vos ameis uns aos outros; como eu vos amei a vós, que também vós uns aos outros vos ameis. Nisto todos conhecerão que sois meus discípulos'.")
    add("O que Jesus prometeu sobre as muitas moradas na Casa de Seu Pai em João 14:2-3?",
        "'Vou preparar-vos lugar; e, se eu for e vos preparar lugar, virei outra vez e vos levarei para mim mesmo'", "'O céu terá apenas doze lugares'", "'Não há moradas suficientes'", "'Ficareis na terra eternamente sem me ver'",
        "facil", "João", "João 14:2-3", "'Na casa de meu Pai há muitas moradas; se não fosse assim, eu vo-lo teria dito. Vou preparar-vos lugar... virei outra vez e vos levarei para mim mesmo'.")
    add("Quem é o Consolador prometido que ensinaria todas as coisas e faria lembrar tudo o que Jesus dissera em João 14:26?",
        "O Espírito Santo, que o Pai enviará em meu nome", "O arcanjo Gabriel", "O apóstolo João", "Moisés ressurreto",
        "facil", "João", "João 14:26", "'Mas aquele Consolador, o Espírito Santo, que o Pai enviará em meu nome, esse vos ensinará todas as coisas, e vos fará lembrar de tudo quanto vos tenho dito'.")
    add("O que Jesus declarou sobre o maior amor que alguém pode demonstrar em João 15:13?",
        "'Ninguém tem maior amor do que este: de dar alguém a sua vida pelos seus amigos'", "'Comprar palácios para os amigos'", "'Doar ouro sem fim'", "'Construir monumentos de vitória'",
        "facil", "João", "João 15:13", "'Ninguém tem maior amor do que este, de dar alguém a sua vida pelos seus amigos. Vós sereis meus amigos, se fizerdes o que eu vos mando'.")
    add("Qual é o tema supremo da Oração Sacerdotal de Jesus em João 17 em favor de todos os crentes?",
        "A unidade e santificação de todos os Seus discípulos: 'Para que todos sejam um, como tu, ó Pai, o és em mim e eu em ti'", "A conquista militar sobre os romanos", "A posse dos bens terrenos", "O domínio sobre as frotas marítimas",
        "facil", "João", "João 17:21", "'Para que todos sejam um, como tu, ó Pai, o és em mim, e eu em ti; que também eles sejam um em nós, para que o mundo creia que tu me enviaste'.")
    add("O que Jesus respondeu aos guardas armados no Getsêmani ao perguntarem por Ele, fazendo-os recuar e cair por terra em João 18:6?",
        "'SOU EU'", "'Não estou aqui'", "'Quem sois vós?'", "'Fugi imediatamente'",
        "medio", "João", "João 18:5-6", "Jesus disse-lhes: 'Sou eu'. Quando lhes disse: 'Sou eu', recuaram e caíram por terra, manifestando a majestade do Santo Nome divino.")
    add("Qual declaração sobre a natureza de Seu Reino Jesus fez ao governador Pilatos em João 18:36?",
        "'O meu Reino não é deste mundo; se o meu reino fosse deste mundo, pelejariam os meus servos'", "'O meu reino é um império bélico na Judeia'", "'Vim para destronar César'", "'Quero ser governador de Samaria'",
        "facil", "João", "João 18:36", "Respondeu Jesus: 'O meu reino não é deste mundo; se o meu reino fosse deste mundo, pelejariam os meus servos, para que eu não fosse entregue aos judeus'.")
    add("Em quais três idiomas oficiais da época foi redigido o título da acusação posto no cimo da cruz de Jesus em João 19:20?",
        "Em hebraico, latim e grego", "Em egípcio, aramaico e persa", "Em babilônio, grego e árabe", "Em fenício, latim e copta",
        "facil", "João", "João 19:20", "A inscrição 'JESUS NAZARENO, O REI DOS JUDEUS' estava escrita em hebraico, latim e grego.")
    add("Qual apóstolo correu mais rápido e chegou primeiro ao túmulo vazio na manhã da ressurreição em João 20:4?",
        "O discípulo a quem Jesus amava (João)", "Simão Pedro", "Tomé", "Tiago",
        "medio", "João", "João 20:4", "Corriam ambos juntos, mas o outro discípulo correu mais apressadamente do que Pedro, e chegou primeiro ao sepulcro.")
    add("O que Jesus disse aos discípulos soprando sobre eles no cenáculo em João 20:22?",
        "'Recebei o Espírito Santo; àqueles a quem perdoardes os pecados lhes são perdoados'", "'Ide guerrear na Judeia'", "'Ficai em silêncio absoluto'", "'Não faleis com ninguém'",
        "facil", "João", "João 20:22-23", "E, havendo dito isto, assoprou sobre eles e disse-lhes: 'Recebei o Espírito Santo'.")
    add("Qual discípulo reconheceu Jesus na praia da Galileia após a pesca milagrosa e disse a Pedro: 'É o Senhor!'?",
        "O discípulo amado (João)", "Tomé", "Bartolomeu", "Simão Zelote",
        "facil", "João", "João 21:7", "Disse aquele discípulo a quem Jesus amava a Pedro: 'É o Senhor!'. E Simão Pedro cingiu-se com a túnica e lançou-se ao mar.")
    add("Qual livro dos quatro evangelhos relata a parábola do Filho Pródigo e a do Bom Samaritano com exclusividade?",
        "Evangelho de Lucas", "Evangelho de Mateus", "Evangelho de Marcos", "Evangelho de João",
        "facil", "Lucas", "Lucas 10 e 15", "Lucas é o único evangelista que preservou as inestimáveis parábolas do Bom Samaritano e do Filho Pródigo.")
    add("Qual dos evangelistas era médico de profissão e companheiro de viagens missionárias do apóstolo Paulo?",
        "Lucas", "Mateus", "Marcos", "João",
        "facil", "Lucas", "Colossenses 4:14", "Paulo o chama carinhosamente em Colossenses 4:14 de 'Lucas, o médico amado'.")
    add("Qual evangelista era cobrador de impostos (publicano) em Cafarnaum antes de seguir o chamado de Jesus?",
        "Mateus (Levi)", "Pedro", "André", "João",
        "facil", "Mateus", "Mateus 9:9", "Jesus viu um homem, chamado Mateus, assentado na recebedoria de impostos, e disse-lhe: 'Segue-me'. E ele, levantando-se, o seguiu.")
    add("Em qual Evangelho Jesus pronuncia as célebres sete declarações que começam com 'Eu Sou' (Pão, Luz, Porta, Bom Pastor, Ressurreição, Caminho, Videira)?",
        "Evangelho de João", "Evangelho de Marcos", "Evangelho de Mateus", "Evangelho de Lucas",
        "facil", "João", "João 6, 8, 10, 11, 14, 15", "O Evangelho de João destaca de modo ímpar as sete grandes afirmações de Cristo 'EU SOU', revelando Sua divindade.")
    add("Qual é o primeiro milagre público de Jesus narrado nos Evangelhos sinóticos (Mateus, Marcos, Lucas)?",
        "A cura do endemoninhado na sinagoga de Cafarnaum e a cura da febre da sogra de Pedro", "A ressurreição de Lázaro", "A transformação de água em vinho", "A caminhada sobre as águas",
        "medio", "Marcos", "Marcos 1:21-31; Lucas 4:31-39", "Nos sinóticos, o ministério público em Cafarnaum inicia com a libertação na sinagoga e a cura da sogra de Pedro.")
    add("Qual declaração resume o propósito explícito pelo qual o apóstolo João escreveu o seu Evangelho em João 20:31?",
        "'Estes foram escritos para que creiais que Jesus é o Cristo, o Filho de Deus, e para que, crendo, tenhais vida em seu nome'", "'Para relatar guerras políticas'", "'Para defender a cultura hebraica'", "'Para catalogar genealogias terrenas'",
        "facil", "João", "João 20:31", "'Estes, porém, foram escritos para que creiais que Jesus é o Cristo, o Filho de Deus, e para que, crendo, tenhais vida em seu nome'.")
    add("Qual cena de ternura ocorreu na casa de Simão o leproso quando uma mulher quebrou um vaso de alabastro sobre Jesus?",
        "Ela ungiu a cabeça e os pés de Jesus para a Sua sepultura antecipadamente", "Ela pediu esmolas para a família", "Ela cantou um hino de guerra", "Ela derramou água fria",
        "facil", "Marcos", "Marcos 14:3-9", "Jesus disse: 'Ela fez uma boa obra... antecipou-se a ungir o meu corpo para a sepultura; onde for pregado este evangelho, será dito o que ela fez'.")
    add("O que o véu do santuário rasgado em duas metades na morte de Cristo simboliza teologicamente?",
        "O livre e irrestrito acesso de todos os crentes à presença de Deus através do sacrifício de Jesus", "A destruição da fé de Israel", "A perda das escrituras sagradas", "A substituição do sábado pelo domingo",
        "facil", "Mateus", "Mateus 27:51; Hebreus 10:19-20", "Simboliza que a barreira de separação foi desfeita e temos plena ousadia para entrar no Santo dos Santos pelo sangue de Jesus.")
    add("Qual foi a última frase de triunfo que ecoou da cruz no Evangelho de João?",
        "'Está consumado!'", "'Tudo acabou'", "'Esperai o futuro'", "'Adeus, mundo'",
        "facil", "João", "João 19:30", "Com 'Tetelestai' ('Está consumado!'), a obra redentora de salvação foi perfeita e cabalmente realizada.")

    return items[:200]

if __name__ == "__main__":
    q_list = get_gospels_questions()
    print(f"Gospels generated: {len(q_list)} questions")
