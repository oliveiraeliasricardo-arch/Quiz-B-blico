# -*- coding: utf-8 -*-
"""
Livros Históricos: 160 questões de Josué a Ester
"""

def get_historical_questions():
    items = []
    def add(q, c, w1, w2, w3, diff, book, ref, exp):
        items.append({
            "q": q, "c": c, "w1": w1, "w2": w2, "w3": w3,
            "diff": diff, "book": book, "testament": "VT",
            "section": "Históricos", "ref": ref, "exp": exp
        })

    # --- JOSUÉ (25 questões) ---
    add("Qual exortação Deus repetiu três vezes a Josué no capítulo 1 ao sucedê-lo como líder?",
        "'Esforça-te e tem bom ânimo'", "'Acumula carros de ferro'", "'Cobra ouro dos cananeus'", "'Foge das batalhas campais'",
        "facil", "Josué", "Josué 1:6-9", "Deus ordenou: 'Não to mandei eu? Esforça-te, e tem bom ânimo; não temas, nem te espantes'.")
    add("Quem acolheu e escondeu os dois espias de Israel em sua casa sobre os muros de Jericó?",
        "Raabe", "Débora", "Rute", "Jael",
        "facil", "Josué", "Josué 2:1-4", "Raabe, a estalajadeira em Jericó, escondeu os espias israelitas no eirado de sua casa.")
    add("Qual sinal Raabe deveria amarrar na sua janela para que sua família fosse poupada na invasão de Jericó?",
        "Um cordão de fio de escarlata (vermelho)", "Um lenço de linho branco", "Uma lâmpada de azeite", "Um ramo verde de oliveira",
        "facil", "Josué", "Josué 2:18", "'Atarás este cordão de fio de escarlata à janela por onde nos fizeste descer'.")
    add("O que aconteceu com as águas do rio Jordão quando os sacerdotes que levavam a Arca pisaram na beira das águas?",
        "As águas pararam e amontoaram-se e Israel passou a pé enxuto", "Caiu fogo do céu secando o leito", "Uma ponte de madeira surgiu", "As águas tornaram-se vermelhas",
        "facil", "Josué", "Josué 3:15-17", "As águas que vinham de cima pararam num montão; e todo o Israel passou a seco pelo meio do Jordão.")
    add("Quantas pedras foram retiradas do meio do rio Jordão para servir de memorial perpétuo em Gilgal?",
        "12 pedras (uma para cada tribo)", "7 pedras", "10 pedras", "40 pedras",
        "medio", "Josué", "Josué 4:2-8", "Josué mandou doze homens tirar doze pedras do meio do Jordão para memorial eterno.")
    add("O que cessou no dia seguinte à celebração da primeira Páscoa em Canaã, quando comeram dos frutos da terra?",
        "O maná do céu", "A água da rocha", "A coluna de fogo", "O vento oriental",
        "medio", "Josué", "Josué 5:12", "Cessou o maná no dia seguinte, depois que comeram do trigo da terra; e os israelitas não o tiveram mais.")
    add("Quem apareceu a Josué perto de Jericó com uma espada desembainhada na mão declarando: 'Venho como príncipe do exército do Senhor'?",
        "O Príncipe do Exército do Senhor (teofania)", "O arcanjo Gabriel", "Moisés ressurreto", "O sacerdote Eleazar",
        "medio", "Josué", "Josué 5:13-15", "Respondeu ele: 'Não, mas venho agora como príncipe do exército do Senhor'. E Josué prostrou-se com o rosto em terra.")
    add("Quantos dias o exército de Israel rodeou a cidade de Jericó uma vez ao dia?",
        "6 dias", "3 dias", "7 dias", "12 dias",
        "facil", "Josué", "Josué 6:3-14", "Durante seis dias marcharam ao redor da cidade de Jericó uma vez em cada dia.")
    add("Quantas vezes Israel rodeou os muros de Jericó no sétimo dia antes de tocarem as trombetas e gritarem?",
        "7 vezes", "12 vezes", "3 vezes", "1 vez",
        "facil", "Josué", "Josué 6:15", "No sétimo dia madrugaram ao subir da alva e rodearam a cidade da mesma maneira sete vezes.")
    add("O que aconteceu às portentosas muralhas de Jericó ao soar das trombetas de chifre e ao grande brado do povo?",
        "As muralhas caíram rentes com o chão", "Foram incendiadas por raios", "Abriram-se as portas de ferro", "Afundaram na areia",
        "facil", "Josué", "Josué 6:20", "Gritou o povo e tocaram as trombetas; e o muro caiu abaixo, e o povo subiu à cidade e a tomou.")
    add("Quem cometeu pecado de anátema roubando uma capa babilônica, prata e uma barra de ouro em Jericó, causando a derrota em Ai?",
        "Acã, filho de Carmi", "Corá", "Zinri", "Balaão",
        "medio", "Josué", "Josué 7:20-21", "Acã confessou: 'Pequei... vi entre os despojos uma boa capa babilônica, duzentos siclos de prata e uma cunha de ouro e os escondi'.")
    add("Onde Acã e seus pertences foram apedrejados e sepultados sob um grande montão de pedras?",
        "No vale de Acor", "No vale de Hinom", "No monte Ebal", "No monte Gerizim",
        "dificil", "Josué", "Josué 7:24-26", "Levaram Acã ao vale de Acor; e todo o Israel o apedrejou; por isso se chamou vale de Acor.")
    add("Como os habitantes de Gibeão enganaram Josué e os líderes de Israel para firmarem um tratado de paz?",
        "Fingiram ser de terra mui distante com pães bolorentos, sapatos remendados e odres velhos", "Disfarçaram-se de mercadores egípcios ricos", "Mandaram mulheres com presentes de ouro", "Enviaram diplomatas babilônios",
        "facil", "Josué", "Josué 9:3-15", "Os gibeonitas usaram de astúcia trazendo pão seco e bolorento fingindo vir de terra muito longe, e os líderes não consultaram ao Senhor.")
    add("Qual grande milagre astronômico ocorreu durante a batalha contra os amorreus na descida de Bete-Horom?",
        "O sol se deteve em Gibeão e a lua no vale de Aijalom quase um dia inteiro", "Um eclipse cobriu toda a terra", "Três estrelas caíram sobre o acampamento inimigo", "A noite durou 40 horas",
        "facil", "Josué", "Josué 10:12-13", "Josué disse: 'Sol, detém-te em Gibeão, e tu, lua, no vale de Aijalom'. E o sol se deteve no meio do céu quase um dia inteiro.")
    add("Com que idade Calebe reivindicou a montanha dos gigantes anaquins em Hebrom declarando estar tão forte quanto no dia em que espiara a terra?",
        "85 anos", "70 anos", "100 anos", "60 anos",
        "medio", "Josué", "Josué 14:10-14", "Calebe disse: 'Eis que tenho hoje oitenta e cinco anos; estou ainda tão forte como no dia em que Moisés me enviou... dá-me este monte'.")
    add("O que Otniel conquistou para receber Acsa, filha de Calebe, por mulher?",
        "A cidade de Quiriate-Sefer (Debir)", "A cidade de Hebrom", "A fortaleza de Jericó", "A planície de Bete-Semes",
        "dificil", "Josué", "Josué 15:16-17", "Calebe disse: 'Quem ferir a Quiriate-Sefer e a tomar, darei a minha filha Acsa por mulher'. E tomou-a Otniel.")
    add("Onde o Tabernáculo e a Arca da Aliança foram instalados durante o período da divisão da terra?",
        "Em Siló", "Em Jerusalém", "Em Betel", "Em Hebrom",
        "medio", "Josué", "Josué 18:1", "Toda a congregação dos filhos de Israel se reuniu em Siló, e ali armaram a tenda da congregação.")
    add("Qual célebre declaração de fé Josué fez perante todo o povo reunido em Siquém antes de morrer?",
        "'Eu e a minha casa serviremos ao Senhor'", "'Quem quiser adorar os deuses faça-o'", "'Construí muralhas fortes'", "'Guardai todo o vosso ouro'",
        "facil", "Josué", "Josué 24:15", "'Porém, se vos parece mal aos vossos olhos servir ao Senhor, escolhei hoje... porém eu e a minha casa serviremos ao Senhor'.")
    add("Onde os ossos do patriarca José, trazidos do Egito, foram finalmente sepultados em Canaã?",
        "Em Siquém, no campo que Jacó comprara", "Na cova de Macpela em Hebrom", "Em Belém de Judá", "No monte Sião",
        "medio", "Josué", "Josué 24:32", "Os ossos de José, que os filhos de Israel trouxeram do Egito, foram sepultados em Siquém.")
    add("Qual era a idade de Josué quando faleceu e foi sepultado em Timnate-Sera?",
        "110 anos", "120 anos", "100 anos", "85 anos",
        "medio", "Josué", "Josué 24:29", "Depois destas coisas faleceu Josué, filho de Num, servo do Senhor, com a idade de cento e dez anos.")
    add("Qual cidade foi a segunda tomada por Israel após o pecado de Acã ter sido julgado?",
        "Ai", "Hazor", "Laquis", "Bete-El",
        "facil", "Josué", "Josué 8:1-28", "Após julgar o pecado no vale de Acor, Josué armou emboscada e conquistou totalmente a cidade de Ai.")
    add("Quantos reis ao todo foram derrotados por Josué a oeste do Jordão conforme o registro em Josué 12?",
        "31 reis", "12 reis", "7 reis", "50 reis",
        "dificil", "Josué", "Josué 12:24", "O catálogo de conquistas encerra declarando: 'Ao todo, trinta e um reis'.")
    add("Qual tribo não recebeu quinhão territorial de terras como herança, porque o Senhor e os sacrifícios eram a sua porção?",
        "A tribo de Levi", "A tribo de Judá", "A tribo de Benjamim", "A tribo de Simeão",
        "facil", "Josué", "Josué 13:14; 18:7", "À tribo de Levi não deu herança territorial; os sacrifícios do Senhor e o Seu sacerdócio são a sua herança.")
    add("O que o povo ergueu junto ao rio Jordão quando as duas tribos e meia voltaram para o oriente, gerando quase uma guerra por suspeita de idolatria?",
        "Um grande altar memorial chamado Testemunho (Ed)", "Um bezerro de bronze", "Uma muralha de pedra", "Uma torre de vigilância",
        "dificil", "Josué", "Josué 22:10-34", "Os filhos de Rúben e Gade edificaram um altar grandioso como testemunho entre eles e Israel de que pertenciam ao Senhor.")
    add("O que caiu do céu sobre o exército dos amorreus em Bete-Horom matando mais inimigos do que as espadas de Israel?",
        "Grandes pedras de saraiva (granizo)", "Raios fulminantes", "Cinzas vulcânicas", "Enxames de vespas",
        "medio", "Josué", "Josué 10:11", "O Senhor lançou sobre eles do céu grandes pedras de granizo; e foram mais os que morreram pela saraiva do que pela espada.")

    # --- JUÍZES (30 questões) ---
    add("Quem foi o primeiro juiz de Israel, parente de Calebe, que livrou o povo do rei da Mesopotâmia?",
        "Otniel, filho de Quenaz", "Eúde", "Gideão", "Sangar",
        "medio", "Juízes", "Juízes 3:9-11", "O Senhor suscitou a Otniel, filho de Quenaz, irmão menor de Calebe; e ele julgou a Israel e livrou o povo.")
    add("Qual juiz era canhoto e matou Eglom, o rei excessivamente obeso de Moabe, com uma adaga de dois gumes?",
        "Eúde, filho de Gera", "Sangar", "Baraque", "Tola",
        "facil", "Juízes", "Juízes 3:15-22", "Eúde, homem canhoto, fez para si um punhal de dois gumes de um côvado e feriu o rei Eglom na câmara de verão.")
    add("Qual juiz derrotou seiscentos filisteus usando apenas uma aguilhada de bois?",
        "Sangar, filho de Anate", "Jair", "Ibsã", "Elon",
        "medio", "Juízes", "Juízes 3:31", "Depois dele foi Sangar, filho de Anate, que feriu seiscentos homens dos filisteus com uma aguilhada de bois.")
    add("Qual profetisa e juíza julgava Israel assentada debaixo de uma palmeira entre Ramá e Betel?",
        "Débora", "Miriã", "Hulda", "Ana",
        "facil", "Juízes", "Juízes 4:4-5", "Débora, mulher profetisa, julgava a Israel naquele tempo; e assentava-se debaixo das palmeiras de Débora.")
    add("Quem foi convocado por Débora para comandar o exército no monte Tabor contra Sísera?",
        "Baraque, filho de Abinoão", "Gideão", "Jefté", "Sansão",
        "facil", "Juízes", "Juízes 4:6", "Débora mandou chamar a Baraque e disse: 'Porventura o Senhor não te ordenou: Vai e atrai gente ao monte Tabor?'.")
    add("Qual mulher matou o general Sísera cravando-lhe uma estaca de tenda nas fontes enquanto ele dormia exausto?",
        "Jael, mulher de Héber", "Raabe", "Acsa", "Noemi",
        "facil", "Juízes", "Juízes 4:21", "Jael tomou uma estaca da tenda e um martelo, chegou-se mansamente a ele e cravou-lhe a estaca na têmpora.")
    add("Onde Gideão estava malhando o trigo às escondidas dos midianitas quando o Anjo do Senhor lhe apareceu?",
        "Num lagar de uvas", "No alto de uma torre", "Numa caverna no deserto", "No eirado de casa",
        "facil", "Juízes", "Juízes 6:11", "Gideão estava sacudindo o trigo no lagar, para o salvar dos midianitas, quando o anjo do Senhor lhe apareceu.")
    add("Qual título honroso o Anjo do Senhor usou ao saudar Gideão no lagar?",
        "'O Senhor é contigo, homem valente'", "'Salve, rei de Israel'", "'Desperta, profeta das nações'", "'Bendito sejas guerreiro de Sião'",
        "facil", "Juízes", "Juízes 6:12", "O anjo do Senhor lhe apareceu e lhe disse: 'O Senhor é contigo, homem valente'.")
    add("Qual apelido Gideão recebeu após derrubar o altar de Baal pertencente a seu pai Joás?",
        "Jerubaal ('Contenda Baal contra ele')", "Jerusalém", "Boanerges", "Abimeleque",
        "medio", "Juízes", "Juízes 6:32", "Chamaram a Gideão Jerubaal, dizendo: 'Baal contenda contra ele, pois derribou o seu altar'.")
    add("Qual prova milagrosa com o velo de lã Gideão pediu a Deus para ter certeza de sua missão?",
        "O orvalho na lã e a terra seca ao redor, e na noite seguinte o orvalho no chão e a lã seca", "A lã queimar sem consumir-se", "A lã transformar-se em ouro", "Três gotas de sangue na lã",
        "facil", "Juízes", "Juízes 6:36-40", "Deus fez como Gideão pediu com o velo de lã molhado de orvalho e seco na noite seguinte para confirmação.")
    add("Quantos homens foram originalmente convocados por Gideão e quantos restaram no primeiro filtro dos temerosos?",
        "Havia 32.000 homens; 22.000 voltaram por medo e restaram 10.000", "Havia 50.000 e restaram 5.000", "Havia 10.000 e restaram 1.000", "Havia 20.000 e voltaram todos",
        "medio", "Juízes", "Juízes 7:3", "Proclamou-se que quem fosse medroso voltasse; e voltaram 22.000 homens, ficando apenas 10.000.")
    add("Qual teste nas águas reduziu a tropa final de Gideão para exatamente 300 guerreiros?",
        "Os que levaram a água à boca lambendo com a mão, mantendo-se alertas", "Os que mergulharam o corpo inteiro", "Os que beberam de joelhos com os dois braços", "Os que recusaram a água",
        "facil", "Juízes", "Juízes 7:5-7", "O Senhor separou os 300 que lamberam a água com as mãos vigilantes para dar o livramento contra Midiã.")
    add("Quais eram as armas nas mãos dos 300 de Gideão ao cercarem o arraial de Midiã no meio da noite?",
        "Trombetas e cântaros vazios contendo tochas acesas no seu interior", "Arcos de bronze e flechas envenenadas", "Espadas longas e escudos de couro", "Lanças de ferro e fundas",
        "facil", "Juízes", "Juízes 7:16-20", "Pôs na mão de cada homem uma trombeta e um cântaro vazio com uma tocha dentro; quebraram os cântaros e tocaram as trombetas.")
    add("Qual grito uníssono os trezentos guerreiros de Gideão deram ao quebrarem os cântaros?",
        "'Espada pelo Senhor e por Gideão!'", "'Viva o rei de Israel!'", "'Vitória aos filhos de Jacó!'", "'Fogo sobre os midianitas!'",
        "facil", "Juízes", "Juízes 7:20", "Tocaram as trombetas, despedaçaram os cântaros e clamaram: 'A espada do Senhor e de Gideão!'.")
    add("Qual filho ilegítimo de Gideão assassinou setenta irmãos sobre uma só pedra para proclamar-se rei em Siquém?",
        "Abimeleque", "Jotão", "Gaal", "Zebul",
        "medio", "Juízes", "Juízes 9:1-5", "Abimeleque foi à casa de seu pai em Ofra e matou a seus irmãos, filhos de Jerubaal, setenta homens, sobre uma pedra.")
    add("Como morreu o tirano Abimeleque na torre de Tebes?",
        "Uma mulher atirou um pedaço de mó de moinho sobre sua cabeça quebrando-lhe o crânio", "Foi atravessado por flecha inimiga", "Caiu da muralha nas lanças", "Foi envenenado no banquete",
        "facil", "Juízes", "Juízes 9:53-54", "Uma mulher lançou um pedaço de uma mó sobre a cabeça de Abimeleque e quebrou-lhe o crânio; ele mandou seu escudeiro traspassá-lo.")
    add("Qual juiz fez um voto precipitado ao Senhor de sacrificar a primeira coisa que saísse de sua casa se voltasse vitorioso contra Amom?",
        "Jefté", "Gideão", "Sansão", "Baraque",
        "facil", "Juízes", "Juízes 11:30-34", "Jefté fez um voto de oferecer a primeira criatura que saísse ao seu encontro; e saiu-lhe sua filha única dançando.")
    add("Qual palavra hebraica servia de senha para os homens de Gileade identificarem os efraimitas no vau do Jordão pela pronúncia?",
        "Xibolete (que eles pronunciavam Sibolete)", "Betel", "Mizpá", "Maranata",
        "medio", "Juízes", "Juízes 12:5-6", "Diziam-lhe: 'Dize Xibolete'. E ele dizia 'Sibolete', porque não podia pronunciar direito; e o matavam.")
    add("A qual tribo de Israel pertencia Manoá, o pai de Sansão?",
        "Tribo de Dã", "Tribo de Judá", "Tribo de Efraim", "Tribo de Benjamim",
        "dificil", "Juízes", "Juízes 13:2", "Havia um homem de Zorá, da família dos danitas, cujo nome era Manoá, cuja mulher era estéril.")
    add("Qual voto especial de consagração desde o ventre materno foi ordenado para Sansão?",
        "Voto de Nazireu de Deus (não cortar cabelo, não beber vinho nem tocar em cadáver)", "Voto de celibato perpétuo", "Voto de pobreza monástica", "Consagração sacerdotal levítica",
        "facil", "Juízes", "Juízes 13:5", "'Não passará navalha sobre a sua cabeça, porque o menino será nazireu de Deus desde o ventre materno'.")
    add("O que Sansão fez a um leão novo que rugia contra ele nas vinhas de Timnate?",
        "Despedaçou-o com as mãos limpas como quem despedaça um cabrito", "Matou-o com uma funda de pedra", "Prendeu-o numa armadilha de ferro", "Fugiu subindo numa árvore",
        "facil", "Juízes", "Juízes 14:5-6", "O Espírito do Senhor se apossou de Sansão, e ele rasgou o leão sem ter nada na mão.")
    add("O que Sansão encontrou no corpo seco do leão tempos depois que gerou seu famoso enigma?",
        "Um enxame de abelhas e mel", "Um ninho de cobras", "Um ramo de videira brotado", "Uma flor silvestre",
        "facil", "Juízes", "Juízes 14:8-9", "Sansão apartou-se para ver o corpo do leão morto, e eis que nele havia um enxame de abelhas com mel.")
    add("Qual era o célebre enigma proposto por Sansão aos trinta companheiros filisteus no banquete de casamento?",
        "'Do comedor saiu comida, e doçura saiu do forte'", "'O que é mais doce que o mel e mais forte que o leão?'", "'Quem corre mais que a gazela?'", "'Qual luz brilha sem arder?'",
        "medio", "Juízes", "Juízes 14:14", "Sansão disse-lhes: 'Do comedor saiu comida, e do forte saiu doçura'. E em três dias não puderam decifrar o enigma.")
    add("Quantas raposas Sansão capturou e amarrou com tochas nas caudas para incendiar os trigais e vinhas dos filisteus?",
        "300 raposas", "100 raposas", "50 raposas", "500 raposas",
        "facil", "Juízes", "Juízes 15:4-5", "Sansão caçou trezentas raposas, tomou tochas e amarrou-as cauda com cauda, incendiando as searas dos filisteus.")
    add("Com que objeto rústico Sansão matou mil soldados filisteus em Leí?",
        "Uma queixada fresca de um jumento", "Um cajado de carvalho", "Uma grande pedra de basalto", "Uma barra de ferro",
        "facil", "Juízes", "Juízes 15:15-16", "Achou uma queixada fresca de jumento, estendeu a mão, tomou-a e feriu com ela mil homens.")
    add("O que Sansão arrancou e carregou sobre os ombros até o cume do monte defronte de Hebrom na cidade de Gaza?",
        "As portas da cidade com os seus dois umbrais e tranca", "A estátua do deus Dagom", "O palácio do governador filisteu", "A muralha da torre",
        "medio", "Juízes", "Juízes 16:3", "Sansão deitou-se até à meia-noite; levantou-se, travou das portas da cidade e das ombreiras e levou-as ao monte.")
    add("Quem seduziu e pressionou Sansão diariamente até que ele revelasse o segredo de sua extraordinária força?",
        "Dalila", "Mical", "Acsa", "Tamar",
        "facil", "Juízes", "Juízes 16:4-17", "Dalila o importunava todos os dias e lhe apertava a alma, até que ele lhe abriu todo o seu coração sobre o nazireado.")
    add("O que os filisteus fizeram a Sansão logo após cortarem as sete tranças do seu cabelo e prenderem-no?",
        "Arrancaram-lhe os olhos e puseram-no a girar moinho no cárcere em Gaza", "Cortaram-lhe as duas mãos", "Queimaram-no vivo", "Lançaram-no aos leões",
        "facil", "Juízes", "Juízes 16:21", "Os filisteus prenderam-no, vazaram-lhe os olhos e o puseram a moer na prisão com cadeias de bronze.")
    add("O que Sansão pediu a Deus em sua última oração no templo pagão do deus Dagom?",
        "Força mais uma vez para se vingar dos filisteus pelos seus dois olhos", "Para recuperar a visão", "Para escapar e ser coroado rei", "Para viver cem anos",
        "facil", "Juízes", "Juízes 16:28", "Sansão clamou: 'Senhor Deus, lembra-te de mim, e esforça-me peço-te só esta vez, para que me vingue dos filisteus pelos meus olhos'.")
    add("Como Sansão derrubou o templo de Dagom provocando a morte dos príncipes e milhares de filisteus?",
        "Abraçou as duas colunas centrais que sustentavam o edifício e empurrou-as com toda a força", "Ateou fogo nas vigas mestras de madeira", "Derrubou a estátua sobre a multidão", "Usou a queixada de jumento contra os pilares",
        "facil", "Juízes", "Juízes 16:29-30", "Sansão abraçou as duas colunas do meio em que se sustentava a casa; e a casa caiu sobre os príncipes e todo o povo.")

    # --- RUTE (10 questões) ---
    add("Qual o motivo de Elimeleque, Noemi e seus dois filhos terem migrado de Belém de Judá para Moabe?",
        "Havia grande fome na terra de Judá", "Fugiam de uma invasão filisteia", "Foram expulsos pelos sacerdotes", "Procuravam minas de prata",
        "facil", "Rute", "Rute 1:1-2", "Nos dias em que julgavam os juízes, houve fome na terra; por isso um homem de Belém de Judá foi peregrinar em Moabe.")
    add("Quais eram as duas noras moabitas de Noemi viúvas de Malom e Quiliom?",
        "Orfa e Rute", "Raabe e Dalila", "Ada e Zilá", "Miriã e Zípora",
        "facil", "Rute", "Rute 1:4", "Tomaram para si mulheres moabitas: o nome de uma era Orfa, e o da outra, Rute.")
    add("Qual declaração de amor e lealdade imorredoura Rute fez a Noemi ao recusar deixá-la?",
        "'Aonde quer que fores irei; o teu povo é o meu povo e o teu Deus o meu Deus'", "'Voltarei para os deuses de Moabe'", "'Dá-me metade dos teus bens'", "'Não me importo com o teu destino'",
        "facil", "Rute", "Rute 1:16-17", "Rute declarou: 'O teu povo é o meu povo, e o teu Deus é o meu Deus; onde morreres morrerei eu, e ali serei sepultada'.")
    add("Como Noemi pediu para ser chamada pelas mulheres de Belém, por causa da amargura de suas perdas?",
        "Mara (que significa amargura)", "Hadassa", "Sulamita", "Sara",
        "medio", "Rute", "Rute 1:20", "Ela lhes disse: 'Não me chameis Noemi (agradável); chamai-me Mara, porque grande amargura me tem dado o Todo-Poderoso'.")
    add("Nos campos de quem Rute foi respigar espigas caídas na colheita da cevada em Belém?",
        "Boaz, parente chegado da família de Elimeleque", "Jesse", "Samir", "Eliezer",
        "facil", "Rute", "Rute 2:1-3", "Foi e chegou ao campo de respigar após os segadores; e a sua sorte caiu na parte das terras de Boaz.")
    add("Que ordem generosa Boaz deu aos seus segadores a respeito da jovem viúva Rute?",
        "Deixar cair propositalmente dos manojos e espigas para que ela respigasse em abundância", "Expulsá-la do campo", "Cobrar tributo de cada espiga colhida", "Mandar que ela trabalhasse à noite",
        "facil", "Rute", "Rute 2:15-16", "Boaz deu ordem aos seus moços: 'Deixai cair alguns punhados dos molhos e deixai-os ficar, para que ela os recolha'.")
    add("Onde Rute se deitou aos pés de Boaz, conforme o conselho de Noemi para pedir resgate de parentesco?",
        "Na eira de debulhar cevada", "No palácio do governador", "Na porta da cidade", "No poço de Belém",
        "medio", "Rute", "Rute 3:4-7", "Rute foi mansamente à eira, descobriu-lhe os pés e deitou-se sob o manto de Boaz.")
    add("Qual costume tradicional de confirmação de transferência de direitos e resgate é narrado em Rute 4?",
        "O homem tirava o sapato e dava-o ao outro perante as testemunhas na porta", "Quebravam um vaso de barro", "Cortavam a ponta da capa", "Trocavam anéis de ferro",
        "medio", "Rute", "Rute 4:7-8", "Este era o costume antigo em Israel: o homem descalçava o seu sapato e o dava ao outro, como confirmação de negócio.")
    add("Qual filho nasceu do casamento abençoado entre Boaz e Rute?",
        "Obede", "Jessé", "Davi", "Salomão",
        "facil", "Rute", "Rute 4:17", "As vizinhas deram-lhe nome, dizendo: 'A Noemi nasceu um filho'. E chamaram-no Obede; este é o pai de Jessé, pai de Davi.")
    add("Por que o livro de Rute tem imensa relevância genealógica para toda a história bíblica?",
        "Porque Rute, a estrangeira moabita, tornou-se bisavó do rei Davi e antepassada de Jesus Cristo", "Porque explica as leis das colheitas de trigo", "Porque narra a vitória contra os reis de Moabe", "Porque institui o sacerdócio levita",
        "facil", "Rute", "Rute 4:21-22; Mateus 1:5", "Boaz gerou a Obede, Obede gerou a Jessé, e Jessé gerou a Davi, linhagem messiânica de Jesus.")

    # --- 1 SAMUEL (35 questões) ---
    add("Por que Ana chorava amargamente no Tabernáculo em Siló e derramava sua alma perante Deus?",
        "Porque era estéril e sua rival Penina a provocava continuamente", "Porque seu marido a abandonara", "Porque perdera todas as suas propriedades", "Porque estava gravemente enferma",
        "facil", "1 Samuel", "1 Samuel 1:6-10", "Ana chorava e não comia, e com amargura de alma orou ao Senhor e chorou copiosamente pedindo um filho.")
    add("O que o sacerdote Eli pensou que Ana estava ao vê-la mexer os lábios sem emitir som audível?",
        "Pensou que ela estivesse embriagada", "Pensou que ela fosse louca", "Pensou que estivesse cantando", "Pensou que fosse uma espiã",
        "facil", "1 Samuel", "1 Samuel 1:13-14", "Eli a observava pela boca; e, como Ana falava no coração e não se ouvia voz, teve-a por embriagada.")
    add("Qual voto Ana fez ao Senhor caso recebesse um filho do sexo masculino?",
        "Consagrá-lo ao Senhor por todos os dias de sua vida e não passar navalha em sua cabeça", "Doar cem ovelhas ao santuário", "Construir um altar de ouro puro", "Fazer jejum todos os sábados",
        "facil", "1 Samuel", "1 Samuel 1:11", "Ana votou: 'Se deres à tua serva um filho varão, ao Senhor o darei por todos os dias da sua vida'.")
    add("Qual era o significado do nome Samuel dado ao menino após o seu nascimento?",
        "'Do Senhor o pedi' / 'Ouvido por Deus'", "'Presente de ouro'", "'O pequeno profeta'", "'Criança forte'",
        "medio", "1 Samuel", "1 Samuel 1:20", "Ana chamou o seu nome Samuel, dizendo: 'Porquanto do Senhor o pedi'.")
    add("Quais eram os nomes dos dois filhos perversos de Eli que profanavam as ofertas no santuário?",
        "Hofni e Finéias", "Nadabe e Abiú", "Gérson e Eliezer", "Datã e Abirão",
        "medio", "1 Samuel", "1 Samuel 2:12", "Os filhos de Eli eram homens de Belial e não conheciam o Senhor nem respeitavam os sacrifícios sagrados.")
    add("Como o jovem Samuel respondeu a Deus na terceira vez que foi chamado à noite no Tabernáculo?",
        "'Fala, Senhor, porque o teu servo ouve'", "'Quem me chama no escuro?'", "'Eis-me aqui, Eli'", "'Estou com medo da voz'",
        "facil", "1 Samuel", "1 Samuel 3:9-10", "Samuel respondeu: 'Fala, porque o teu servo ouve'. E o Senhor revelou o juízo sobre a casa de Eli.")
    add("O que aconteceu na trágica batalha contra os filisteus em Afeque em 1 Samuel 4?",
        "Israel foi derrotado, a Arca de Deus foi capturada e Hofni e Finéias foram mortos", "Israel venceu com grande milagre", "O exército filisteu afogou-se no mar", "O sumo sacerdote Eli liderou as tropas",
        "facil", "1 Samuel", "1 Samuel 4:11", "Foi tomada a arca de Deus; e os dois filhos de Eli, Hofni e Finéias, morreram no mesmo dia.")
    add("Como morreu o sacerdote Eli aos noventa e oito anos ao ouvir que a Arca fora capturada pelos filisteus?",
        "Caiu da cadeira para trás junto à porta, quebrou o pescoço e morreu", "Foi morto por soldados inimigos", "Faleceu dormindo tranquilamente", "Morreu afogado no rio",
        "medio", "1 Samuel", "1 Samuel 4:18", "Ao mencionar ele a arca de Deus, Eli caiu da cadeira para trás, quebrou o pescoço e morreu, porque era velho e pesado.")
    add("Qual nome a viúva de Finéias deu ao filho que nasceu antes de morrer no parto, significando 'Foi-se a glória de Israel'?",
        "Icabode", "Samuel", "Ebenézer", "Benjamim",
        "medio", "1 Samuel", "1 Samuel 4:21-22", "Chamou ao menino Icabode, dizendo: 'Foi-se a glória de Israel, porque foi tomada a arca de Deus'.")
    add("O que aconteceu à estátua do ídolo pagão Dagom em Asdode diante da Arca da Aliança?",
        "Caiu com o rosto em terra e na segunda noite sua cabeça e ambas as mãos estavam cortadas", "Foi derretida por fogo divino", "Ficou coberta de lepra", "Desapareceu no abismo",
        "facil", "1 Samuel", "1 Samuel 5:3-4", "Na manhã seguinte Dagom estava caído com o rosto em terra diante da arca do Senhor, com cabeça e mãos cortadas.")
    add("Com que praga humilhante os filisteus das cidades de Asdode, Gate e Ecrom foram afligidos enquanto mantinham a Arca?",
        "Tumores / hemorroidas dolorosas e infestação de ratos na terra", "Gafanhotos e piolhos", "Trevas densas", "Lepra branca",
        "medio", "1 Samuel", "1 Samuel 5:6-9; 6:4-5", "A mão do Senhor se agravou sobre os de Asdode e os assolou com hemorroidas e devastação por ratos.")
    add("O que os filisteus enviaram como oferta pela culpa ao devolverem a Arca da Aliança em um carro novo puxado por vacas?",
        "Cinco tumores de ouro e cinco ratos de ouro (um por cada príncipe filisteu)", "Cem barras de prata pura", "Dez lanças douradas", "Um manto de púrpura",
        "medio", "1 Samuel", "1 Samuel 6:4", "Disseram: 'Cinco hemorroidas de ouro e cinco ratos de ouro, segundo o número dos príncipes dos filisteus'.")
    add("Qual pedra memorial Samuel ergueu entre Mispá e Sem declarando: 'Até aqui nos ajudou o Senhor'?",
        "Ebenézer (Pedra de Ajuda)", "Betel", "Galeede", "Peniel",
        "facil", "1 Samuel", "1 Samuel 7:12", "Tomou Samuel uma pedra e a pôs entre Mispá e Sem e chamou o seu nome Ebenézer, dizendo: 'Até aqui nos ajudou o Senhor'.")
    add("Por que os anciãos de Israel pediram um rei a Samuel, desagradando ao Senhor?",
        "Para serem iguais a todas as outras nações pagãs e terem um rei que marchasse à frente nas guerras", "Porque não tinham leis escritas", "Porque queriam pagar mais tributos", "Porque Samuel era corrupto",
        "facil", "1 Samuel", "1 Samuel 8:5-20", "Disseram: 'Constitui-nos agora um rei sobre nós para nos julgar, como o têm todas as nações'.")
    add("Qual jovem da tribo de Benjamim, mais alto que todo o povo dos ombros para cima, foi ungido por Samuel como o primeiro rei?",
        "Saul, filho de Quis", "Abner", "Davi", "Jônatas",
        "facil", "1 Samuel", "1 Samuel 9:2; 10:1", "Saul era jovem e tão belo que entre os filhos de Israel não havia outro mais belo; desde os ombros para cima sobressaía a todo o povo.")
    add("Qual foi o primeiro grande ato de desobediência de Saul que resultou na perda do reino dinástico?",
        "Ofereceu o holocausto em Gilgal precipitadamente sem esperar Samuel pelo sétimo dia", "Recusou-se a guerrear contra os amonitas", "Adorou bezerros de ouro", "Fugiu da batalha",
        "medio", "1 Samuel", "1 Samuel 13:8-14", "Saul ofereceu o holocausto; Samuel disse: 'Procedeste nesciamente... agora o teu reino não subsistirá; o Senhor buscou para si um homem segundo o seu coração'.")
    add("Quem acompanhado apenas de seu escudeiro escalou as rochas e atacou uma guarnição inteira de filisteus em Micmás com fé audaz?",
        "Jônatas, filho de Saul", "Davi", "Joabe", "Abner",
        "medio", "1 Samuel", "1 Samuel 14:6-14", "Jônatas disse ao seu escudeiro: 'Para o Senhor não há impedimento de livrar com muitos ou com poucos'. E feriram vinte homens.")
    add("O que Jônatas provou na floresta sem saber do juramento precipitado de Saul de que ninguém comeria antes da noite?",
        "Um favo de mel silvestre na ponta de sua vara, clareando-lhe os olhos", "Uma maçã do campo", "Pão achado na tenda", "Uvas silvestres",
        "medio", "1 Samuel", "1 Samuel 14:27", "Jônatas estendeu a ponta da vara e a molhou no favo de mel, e levou a mão à boca; e aclararam-se os seus olhos.")
    add("Qual célebre declaração profética Samuel fez a Saul ao repreender a desobediência de poupar Agague e o gado amalequita?",
        "'Eis que o obedecer é melhor do que o sacrificar, e o atender melhor é do que a gordura de carneiros'", "'Todo rei tem direito aos seus despojos'", "'Mais vale o ouro do que o sacrifício'", "'A vitória apaga todos os erros'",
        "facil", "1 Samuel", "1 Samuel 15:22", "Disse Samuel: 'Tem porventura o Senhor tanto prazer em holocaustos como em que se obedeça à sua palavra? Obedecer é melhor que sacrificar'.")
    add("O que aconteceu quando Samuel rasgou a orla de seu manto ao afastar-se de Saul?",
        "Samuel disse: 'O Senhor rasgou hoje de ti o reino de Israel e o deu ao teu próximo, melhor do que tu'", "Saul pediu perdão e foi restaurado", "Caiu fogo sobre a capa", "Samuel chorou e voltou atrás",
        "facil", "1 Samuel", "1 Samuel 15:27-28", "Saul pegou-lhe pela orla do manto, e este se rasgou; e Samuel lhe disse: 'O Senhor rasgou hoje de ti o reino de Israel'.")
    add("Qual princípio fundamental Deus revelou a Samuel na escolha do novo rei em Belém entre os filhos de Jessé?",
        "'O homem vê o que está diante dos olhos, porém o Senhor olha para o coração'", "'O primogênito sempre receberá a coroa'", "'A força física define o líder'", "'A beleza exterior agrada a Deus'",
        "facil", "1 Samuel", "1 Samuel 16:7", "O Senhor disse a Samuel: 'Não atentes para a sua aparência... porque o Senhor não vê como vê o homem; o homem vê a aparência, mas o Senhor olha o coração'.")
    add("Onde estava o jovem Davi quando Samuel pediu para examinar todos os filhos de Jessé em Belém?",
        "Apascentando as ovelhas no campo", "Dormindo na tenda", "Treinando com espadas", "Viajando para Jerusalém",
        "facil", "1 Samuel", "1 Samuel 16:11-12", "Jessé respondeu: 'Ainda falta o menor, que está apascentando as ovelhas'. E trouxeram Davi, ruivo e de belos olhos, e Samuel o ungiu.")
    add("O que Davi fazia no palácio que acalmava o espírito angustiado e atormentado que vinha sobre Saul?",
        "Tocava harpa com habilidade", "Recitava poesias de guerra", "Oferecia incenso no quarto", "Cantava canções de marcha",
        "facil", "1 Samuel", "1 Samuel 16:23", "Quando o espírito atormentava Saul, Davi tomava a harpa e a dedilhava; então Saul sentia alívio e achava-se melhor.")
    add("De qual cidade filisteia era o gigante Golias e qual era a sua altura aproximada?",
        "Gate; media seis côvados e um palmo (quase 3 metros)", "Asdode; media dois metros", "Gaza; media quatro côvados", "Ecrom; media cinco côvados",
        "medio", "1 Samuel", "1 Samuel 17:4", "Saiu do arraial dos filisteus um campeão chamado Golias, de Gate, que tinha de altura seis côvados e um palmo.")
    add("Quantos dias consecutivos o gigante Golias desafiou com afrontas as tropas do Deus vivo pela manhã e à tarde?",
        "40 dias", "7 dias", "10 dias", "100 dias",
        "medio", "1 Samuel", "1 Samuel 17:16", "Chegava-se o filisteu pela manhã e à tarde, e apresentou-se por quarenta dias diante dos exércitos de Israel.")
    add("O que Davi levou na mão ao enfrentar o gigante Golias, recusando a armadura e espada pesada de Saul?",
        "Seu cajado de pastor, sua funda e cinco pedras lisas do ribeiro", "Uma lança de bronze", "Uma espada de ferro forjado", "Um escudo de couro e arco",
        "facil", "1 Samuel", "1 Samuel 17:40", "Tomou o seu cajado na mão, escolheu para si cinco pedras lisas do ribeiro e a sua funda na mão; e foi ao encontro do filisteu.")
    add("Qual foi a corajosa resposta de Davi às zombarias e maldições de Golias?",
        "'Tu vens a mim com espada, com lança e com escudo; eu, porém, venho a ti em nome do Senhor dos Exércitos'", "'Meu exército é maior que o teu'", "'Minha espada é mais afiada'", "'Foge enquanto há tempo'",
        "facil", "1 Samuel", "1 Samuel 17:45", "Davi disse: 'Tu vens contra mim com espada, com lança e com escudo; mas eu vou contra ti em nome do Senhor dos Exércitos, o Deus de Israel'.")
    add("Onde a pedra arremessada pela funda de Davi atingiu o gigante Golias?",
        "Cravou-se na testa do gigante e ele caiu com o rosto em terra", "No olho esquerdo", "No peito", "No pescoço",
        "facil", "1 Samuel", "1 Samuel 17:49", "Davi meteu a mão no alforge, tirou dali uma pedra e com a funda a atirou, e feriu o filisteu na testa; a pedra encravou-se-lhe na testa.")
    add("Com que arma Davi cortou a cabeça do gigante Golias após derrubá-lo?",
        "Com a própria espada de Golias tirada da bainha", "Com uma adaga de pastor", "Com um machado", "Com uma espada trazida por Saul",
        "facil", "1 Samuel", "1 Samuel 17:51", "Davi correu, pôs-se em pé sobre o filisteu, tomou-lhe a espada, tirou-a da bainha e o matou, cortando-lhe a cabeça.")
    add("O que as mulheres de Israel cantavam com tamborins ao celebrarem a vitória, despertando a fúria ciumenta de Saul?",
        "'Saul feriu os seus milhares, porém Davi os seus dez milhares'", "'Saul é o maior de todos os reis'", "'Davi venceu sozinho a guerra'", "'Eis o novo rei de Sião'",
        "facil", "1 Samuel", "1 Samuel 18:7", "As mulheres cantavam umas às outras: 'Saul feriu os seus milhares, porém Davi os seus dez milhares'. Saul indignou-se muito com isto.")
    add("Qual filha de Saul amava Davi e o ajudou a fugir descendo-o por uma janela quando os guardas cercavam a casa?",
        "Mical", "Merabe", "Tamar", "Acsa",
        "medio", "1 Samuel", "1 Samuel 19:11-12", "Mical desceu a Davi por uma janela; e ele se foi, fugiu e escapou das mãos de Saul.")
    add("Qual sacerdote em Nobe deu a Davi faminto os pães sagrados da proposição e a espada de Golias?",
        "Aimeleque", "Abiatar", "Zadoque", "Eli",
        "medio", "1 Samuel", "1 Samuel 21:1-9", "O sacerdote Aimeleque deu a Davi o pão sagrado e a espada de Golias que estava enrolada num pano atrás do éfode.")
    add("Em qual caverna Davi se refugiou onde congregou quatrocentos homens angustiados, endividados e descontentes?",
        "Caverna de Adulão", "Caverna de Macpela", "Caverna de En-Gedi", "Caverna de Mupim",
        "medio", "1 Samuel", "1 Samuel 22:1-2", "Davi refugiou-se na caverna de Adulão; e juntaram-se a ele todos os homens que se achavam em aperto e dívidas.")
    add("O que Davi cortou furtivamente de Saul na escuridão da caverna de En-Gedi sem tirar sua vida?",
        "A orla do manto de Saul", "A ponta de sua barba", "A correia de sua sandália", "A bainha de sua espada",
        "facil", "1 Samuel", "1 Samuel 24:4", "Davi levantou-se e mansamente cortou a orla do manto de Saul, mas depois bateu-lhe o coração por haver cortado o manto do ungido.")
    add("Qual mulher sábia e prudente intercedeu com presentes generosos impedindo Davi de derramar sangue pela ofensa do tolo Nabal?",
        "Abigail", "Bate-Seba", "Mical", "Tamar",
        "facil", "1 Samuel", "1 Samuel 25:18-35", "Abigail apressou-se, tomou duzentos pães, vinho e comida e prostrou-se diante de Davi com sabedoria; e Davi louvou a Deus por seu conselho.")

    # --- 2 SAMUEL (25 questões) ---
    add("Como Davi reagiu ao receber a notícia da morte de Saul e de seu amigo Jônatas no monte Gilboa?",
        "Rasgou suas vestes, jejuou, chorou e compôs um comovente cântico de lamento", "Celebrou com festas e danças", "Mandou coroar-se imediatamente", "Distribuiu ouro aos soldados",
        "facil", "2 Samuel", "2 Samuel 1:11-17", "Davi lamentou a Saul e a Jônatas com o Cântico do Arco: 'Como caíram os valorosos!'.")
    add("Quantos anos Davi reinou em Hebrom sobre a tribo de Judá antes de ser aclamado rei sobre todo o Israel?",
        "7 anos e 6 meses", "3 anos", "12 anos", "40 anos",
        "medio", "2 Samuel", "2 Samuel 2:11; 5:5", "Davi reinou sete anos e seis meses em Hebrom sobre Judá, e trinta e três anos em Jerusalém sobre todo o Israel.")
    add("Qual fortaleza jebuseia Davi conquistou fazendo dela a capital do reino unificado e a 'Cidade de Davi'?",
        "A fortaleza de Sião (Jerusalém)", "A cidade de Jericó", "A fortaleza de Samaria", "A cidade de Bete-Semes",
        "facil", "2 Samuel", "2 Samuel 5:7-9", "Davi tomou a fortaleza de Sião, esta é a Cidade de Davi; e Davi habitou na fortaleza e edificou em redor.")
    add("O que aconteceu a Uzá quando estendeu a mão para segurar a Arca da Aliança porque os bois tropeçavam no caminho?",
        "Deus o feriu ali mesmo por sua imprudência e ele morreu junto à Arca", "Sua mão secou como pedra", "A Arca virou pó", "Caiu fogo lambendo os bois",
        "medio", "2 Samuel", "2 Samuel 6:6-7", "Uzá estendeu a mão à arca e a segurou; e a ira do Senhor se acendeu contra Uzá e Deus o feriu ali, e morreu junto à arca.")
    add("Na casa de quem a Arca da Aliança permaneceu por três meses, trazendo grande bênção e prosperidade a toda a sua família?",
        "Obede-Edom, o geteu", "Urias", "Ziba", "Mefibosete",
        "facil", "2 Samuel", "2 Samuel 6:11", "Ficou a arca do Senhor na casa de Obede-Edom, o geteu, três meses; e o Senhor abençoou a Obede-Edom e a toda a sua casa.")
    add("Como Davi celebrou a entrada da Arca da Aliança em Jerusalém que causou o desprezo de sua esposa Mical?",
        "Dançava com todas as suas forças perante o Senhor cingido apenas de um éfode de linho", "Vinha montado num trono dourado", "Vestia armadura de prata", "Marchava silencioso e velado",
        "facil", "2 Samuel", "2 Samuel 6:14-16", "Davi saltava e dançava com todas as suas forças perante o Senhor; Mical olhou pela janela, viu-o e o desprezou no seu coração.")
    add("Qual promessa eterna e aliança incondicional Deus fez a Davi através do profeta Natã em 2 Samuel 7?",
        "'A tua casa e o teu reino serão firmes para sempre diante de ti; o teu trono será estabelecido para sempre'", "'Nunca mais haverá seca na terra de Judá'", "'Teus generais conquistarão o império do Nilo'", "'O templo será construído em apenas um ano'",
        "facil", "2 Samuel", "2 Samuel 7:16", "A Aliança Davídica estabelece que a casa, o reino e o trono de Davi serão confirmados para sempre (cumprido no Messias Jesus).")
    add("Qual filho de Jônatas, coxo de ambos os pés, foi acolhido por Davi para comer continuamente à mesa real?",
        "Mefibosete", "Quiliabe", "Absalão", "Adonias",
        "facil", "2 Samuel", "2 Samuel 9:3-13", "Davi acolheu Mefibosete, filho de Jônatas, restituiu-lhe todas as terras de Saul e fê-lo comer à sua mesa como filho do rei.")
    add("Qual mulher casada Davi avistou tomando banho do eirado do seu palácio, caindo em adultério?",
        "Bate-Seba, mulher de Urias, o heteu", "Abigail", "Mical", "Maaca",
        "facil", "2 Samuel", "2 Samuel 11:2-4", "Do eirado viu uma mulher que se estava lavando; e era a mulher mui formosa à vista: Bate-Seba, mulher de Urias.")
    add("Qual instrução traiçoeira Davi enviou numa carta selada ao general Joabe para provocar a morte de Urias?",
        "'Ponde a Urias na frente da maior força da peleja e retirai-vos dele para que seja ferido e morra'", "'Envenenai o vinho de sua tenda'", "'Mandai-o sozinho em missão a Moabe'", "'Prendei-o por traição imaginária'",
        "facil", "2 Samuel", "2 Samuel 11:14-15", "Davi escreveu na carta a Joabe: 'Ponde Urias na frente da mais perigosa batalha e retirai-vos dele, para que seja ferido e morra'.")
    add("Com qual parábola comovente o profeta Natã confrontou Davi revelando o seu terrível pecado perante Deus?",
        "A parábola do homem rico que roubou a única cordeirinha de estimação do homem pobre para servir ao viajante", "A parábola do trigo e do joio", "A parábola do pastor ferido", "A parábola da videira infrutífera",
        "facil", "2 Samuel", "2 Samuel 12:1-4", "Natã contou sobre o rico que tinha muitíssimas ovelhas e roubou a única cordeirinha que comia do bocado do pobre.")
    add("Qual frase direta e cortante Natã disse a Davi após o rei se enfurecer contra o homem rico da parábola?",
        "'Tu és este homem!'", "'Saul voltou dos mortos'", "'Tua coroa foi quebrada'", "'Morte ao pecador!'",
        "facil", "2 Samuel", "2 Samuel 12:7", "Natã disse a Davi: 'Tu és este homem! Assim diz o Senhor Deus de Israel: Eu te ungi rei sobre Israel'.")
    add("Qual Salmo penitencial célebre Davi compôs derramando seu coração em arrependimento pelo adultério com Bate-Seba?",
        "Salmo 51 ('Cria em mim, ó Deus, um coração puro')", "Salmo 23", "Salmo 91", "Salmo 1",
        "facil", "2 Samuel", "Salmo 51:1-10; 2 Sm 12", "Davi compôs o Salmo 51: 'Tem compaixão de mim, ó Deus... cria em mim, ó Deus, um coração puro e renova em mim um espírito reto'.")
    add("Qual nome especial o profeta Natã deu a Salomão por amor do Senhor?",
        "Jedidias ('Amado do Senhor')", "Emanuel", "Roboão", "Zorobabel",
        "dificil", "2 Samuel", "2 Samuel 12:25", "Natã chamou o nome do recém-nascido Jedidias, por amor do Senhor.")
    add("Qual filho de Davi se rebelou contra o pai, roubando o coração do povo nas portas da cidade e usurpando o trono?",
        "Absalão", "Adonias", "Amnon", "Quiliabe",
        "facil", "2 Samuel", "2 Samuel 15:1-12", "Absalão roubava o coração dos homens de Israel com lisonjas e proclamou-se rei em Hebrom rebelando-se contra Davi.")
    add("Como Davi subiu o Monte das Oliveiras ao fugir de Jerusalém por causa do golpe de Absalão?",
        "Chorando, com a cabeça coberta e os pés descalços", "Montado no seu cavalo de batalha", "Com tochas e guardas armados", "Cercado de dançarinos",
        "medio", "2 Samuel", "2 Samuel 15:30", "Davi subiu a encosta das Oliveiras, chorando ao subir, com a cabeça coberta e caminhava descalço.")
    add("Qual conselheiro sábio de Davi aliou-se à rebelião de Absalão, e enforcou-se ao ver seu conselho rejeitado?",
        "Aitofel", "Husai", "Zadoque", "Abiatar",
        "medio", "2 Samuel", "2 Samuel 17:23", "Vendo Aitofel que não se tinha seguido o seu conselho, albardou o jumento, foi para casa e enforcou-se.")
    add("Como Absalão ficou preso indefeso na floresta de Efraim durante a batalha contra os homens de Davi?",
        "Sua cabeça e cabeleira prenderam-se nos galhos espessos de um grande carvalho enquanto a mula passou por baixo", "Caiu numa profunda fossa de caça", "Ficou preso numa armadilha de ferro", "Seu cavalo quebrou a pata",
        "facil", "2 Samuel", "2 Samuel 18:9", "A cabeça de Absalão prendeu-se nos ramos de um grande carvalho e ele ficou suspenso entre o céu e a terra, e o mulo passou adiante.")
    add("Quem desobedeceu a ordem expressa de Davi e matou Absalão cravando-lhe três dardos no coração enquanto pendia do carvalho?",
        "Joabe, comandante do exército", "Abisai", "Benaia", "Husai",
        "facil", "2 Samuel", "2 Samuel 18:14", "Joabe tomou três dardos e os traspassou no coração de Absalão, estando ele ainda vivo no meio do carvalho.")
    add("Qual foi o choro dilacerante de Davi ao saber da morte trágica de seu filho Absalão?",
        "'Meu filho Absalão, meu filho, meu filho Absalão! Quem me dera que eu morrera por ti!'", "'Justiça foi feita ao traidor'", "'Cantai hinos de vitória militar'", "'Fechem os portões da cidade'",
        "facil", "2 Samuel", "2 Samuel 18:33", "O rei subiu à câmara e chorou: 'Meu filho Absalão, meu filho! Quem me dera que eu morrera por ti, Absalão meu filho!'.")
    add("Qual herói dos valentes de Davi desceu numa cova num dia de neve e matou um leão?",
        "Benaia, filho de Joiada", "Eleazar", "Samá", "Abisai",
        "medio", "2 Samuel", "2 Samuel 23:20", "Benaia feriu dois fortes leões de Moabe; desceu também e matou um leão numa cova no tempo da neve.")
    add("O que três valentes de Davi arriscaram a vida para trazer de Belém atravessando o arraial inimigo dos filisteus?",
        "Água fresca da cisterna que estava junto à porta de Belém", "Pães frescos da padaria", "A espada do gigante de Belém", "Frutos das oliveiras",
        "medio", "2 Samuel", "2 Samuel 23:15-17", "Os três valentes romperam o arraial dos filisteus e tiraram água da cisterna de Belém; Davi não a quis beber, mas derramou-a perante o Senhor.")
    add("O que Davi fez ao receber a água da cisterna de Belém trazida com risco de vida por seus três valentes?",
        "Não a bebeu, mas a derramou como libação ao Senhor em reverência ao sangue e vida daqueles homens", "Bebeu-a com deleite e gratidão", "Deu-a aos seus cavalos", "Lavou suas mãos e pés",
        "facil", "2 Samuel", "2 Samuel 23:16-17", "Davi recusou beber e a derramou perante o Senhor dizendo: 'Longe de mim, ó Senhor, fazer tal coisa; beberia eu o sangue dos homens que arriscaram a vida?'.")
    add("Qual pecado Davi cometeu motivado por orgulho bélico que trouxe peste sobre o povo de Israel?",
        "Realizou um censo militar para contar o número de guerreiros em Israel e Judá", "Casou com uma princesa moabita", "Derrubou o altar de Siló", "Recusou dar o dízimo da colheita",
        "medio", "2 Samuel", "2 Samuel 24:1-10", "Davi disse a Joabe: 'Percorre todas as tribos de Israel e conta o povo'. Mas depois bateu-lhe o coração e confessou haver pecado gravemente.")
    add("O que Davi comprou do jebuseu Araúna pelo justo preço para edificar um altar ao Senhor e cessar a peste em Jerusalém?",
        "A eira e os bois para o sacrifício", "Uma vinha com oliveiras", "Uma casa com poço d'água", "Uma carruagem de bronze",
        "facil", "2 Samuel", "2 Samuel 24:24", "Davi comprou a eira e os bois por cinquenta siclos de prata dizendo: 'Não oferecerei ao Senhor holocaustos que não me custem nada'.")

    # --- 1 e 2 REIS / CRÔNICAS (40 questões) ---
    add("O que o jovem rei Salomão pediu a Deus em sonho em Gibeão no início de seu reinado?",
        "Um coração compreensivo e sabedoria para julgar o povo e discernir entre o bem e o mal", "Riquezas sem fim e palácios", "A morte de todos os seus inimigos", "Longa vida de cem anos",
        "facil", "1 Reis", "1 Reis 3:9", "Salomão pediu: 'Dá ao teu servo um coração entendido para julgar a teu povo, para que prudentemente discirna entre o bem e o mal'.")
    add("Como Salomão solucionou com sabedoria a disputa entre duas mulheres que reivindicavam a maternidade do mesmo bebê vivo?",
        "Mandou trazer uma espada para dividir a criança viva em duas metades, revelando a verdadeira mãe que implorou para poupar o filho", "Fez um sorteio com pedras sagradas", "Mandou as duas criarem a criança juntas", "Entregou a criança a uma terceira mãe",
        "facil", "1 Reis", "1 Reis 3:24-27", "A verdadeira mãe comoveu-se nas entranhas e disse: 'Dai-lhe a criança viva e de modo nenhum a mateis'. Salomão declarou: 'Esta é sua mãe'.")
    add("Quantos anos durou a edificação do magnífico Templo de Salomão em Jerusalém?",
        "7 anos", "12 anos", "40 anos", "3 anos",
        "facil", "1 Reis", "1 Reis 6:38", "No ano undécimo foi a casa acabada em todas as suas partes; assim a edificou em sete anos.")
    add("Qual monarca estrangeira viajou de muito longe com ouro e especiarias para provar a sabedoria de Salomão com enigmas?",
        "A Rainha de Sabá", "A Rainha de Nínive", "A Rainha de Babilônia", "A Rainha do Egito",
        "facil", "1 Reis", "1 Reis 10:1-2", "A rainha de Sabá ouviu da fama de Salomão e foi a Jerusalém prová-lo com perguntas difíceis.")
    add("O que a Rainha de Sabá exclamou maravilhada ao contemplar a sabedoria e a glória de Salomão?",
        "'Não me contaram a metade da tua sabedoria e prosperidade!'", "'Esperava encontrar mais ouro'", "'Os teus deuses são iguais aos meus'", "'Prefiro os palácios do meu reino'",
        "facil", "1 Reis", "1 Reis 10:7", "'Eu não acreditava no que ouvia, até que vim e os meus olhos viram; e eis que não me disseram a metade!'.")
    add("Qual foi a causa principal da apostasia espiritual de Salomão na sua velhice?",
        "Suas muitas mulheres estrangeiras lhe perverteram o coração para seguir deuses estranhos como Astarote e Moloque", "Perdeu todo o seu ouro em guerras", "Foi derrotado pelos assírios", "Ficou louco no deserto",
        "facil", "1 Reis", "1 Reis 11:1-4", "O rei Salomão amou muitas mulheres estrangeiras... e suas mulheres lhe perverteram o coração para seguir outros deuses.")
    add("Como o reino de Israel foi dividido após a morte de Salomão?",
        "Reino do Norte (Israel com 10 tribos sob Jeroboão) e Reino do Sul (Judá com 2 tribos sob Roboão)", "Em quatro províncias governadas por generais", "Em doze reinos independentes", "Permaneceu unido por duzentos anos",
        "facil", "1 Reis", "1 Reis 12:16-20", "Dez tribos separaram-se sob Jeroboão formando o Reino do Norte, ficando apenas Judá e Benjamim com Roboão.")
    add("Que ídolos de ouro Jeroboão colocou em Dã e Betel para impedir que o povo do norte fosse adorar em Jerusalém?",
        "Dois bezerros de ouro", "Duas serpentes aladas", "Dois leões de prata", "Duas estátuas de Baal",
        "facil", "1 Reis", "1 Reis 12:28-29", "O rei fez dois bezerros de ouro e disse ao povo: 'Basta de subir a Jerusalém; eis aqui teus deuses, ó Israel!'. E pôs um em Betel e outro em Dã.")
    add("Qual rei ímpio de Israel se casou com a princesa fenícia Jezabel e introduziu o culto a Baal?",
        "Acabe", "Onri", "Jeú", "Jeroboão",
        "facil", "1 Reis", "1 Reis 16:30-31", "Acabe, filho de Onri, fez o que era mau aos olhos do Senhor... casou com Jezabel, filha de Etbaal, e foi servir a Baal.")
    add("O que o profeta Elias tisbita profetizou com autoridade perante o rei Acabe no início de seu ministério?",
        "'Nos anos seguintes não haverá orvalho nem chuva senão segundo a minha palavra'", "'Cairá granizo de fogo sobre Samaria'", "'O templo de Baal será queimado amanhã'", "'O rio Jordão secará'",
        "facil", "1 Reis", "1 Reis 17:1", "Elias disse a Acabe: 'Tão certo como vive o Senhor Deus de Israel, nestes anos não haverá orvalho nem chuva, senão segundo a minha palavra'.")
    add("Como Deus sustentou Elias milagrosamente junto ao ribeiro de Querite durante a seca?",
        "Os corvos lhe traziam pão e carne pela manhã e à tarde, e ele bebia do ribeiro", "Anjos visíveis lhe serviam banquetes", "Manna caía sobre sua tenda", "Comia raízes da floresta",
        "facil", "1 Reis", "1 Reis 17:4-6", "Deus ordenou aos corvos que o sustentassem ali; e os corvos traziam-lhe pão e carne pela manhã e à tarde.")
    add("Qual milagre contínuo de provisão aconteceu na casa da viúva pobre de Sarepta através de Elias?",
        "A farinha da panela não se acabou e o azeite da botija não faltou até o dia da chuva", "Moedas de ouro brotavam do chão", "Pães prontos apareciam na mesa", "A casa encheu-se de trigo",
        "facil", "1 Reis", "1 Reis 17:14-16", "'A farinha da panela não se acabará, e o azeite da botija não faltará'... e comeram ela, ele e sua casa muitos dias.")
    add("O que Elias fez quando o filho da viúva de Sarepta adoeceu e faleceu?",
        "Estendeu-se três vezes sobre a criança clamando a Deus, e a alma do menino voltou ao corpo", "Sepultou o menino na montanha", "Mandou chamar os médicos de Tiro", "Chorou sem orar",
        "facil", "1 Reis", "1 Reis 17:21-22", "Elias estendeu-se sobre o menino três vezes e clamou ao Senhor; o Senhor ouviu a voz de Elias e a alma do menino tornou a ele, e reviveu.")
    add("Quantos falsos profetas de Baal Elias desafiou publicamente no cume do Monte Carmelo?",
        "450 profetas de Baal", "100 profetas", "70 profetas", "1.000 profetas",
        "facil", "1 Reis", "1 Reis 18:19", "Elias convocou todo o Israel ao monte Carmelo, juntamente com os 450 profetas de Baal e os 400 de Aserá.")
    add("Qual era o critério de vitória acordado no desafio do Monte Carmelo para provar quem era o Deus verdadeiro?",
        "O Deus que respondesse com fogo consumindo o holocausto no altar", "O deus que fizesse chover primeiro", "O deus que fizesse tremer a montanha", "O deus que fizesse secar o mar",
        "facil", "1 Reis", "1 Reis 18:24", "Elias disse: 'O deus que responder por meio de fogo, esse seja Deus'. E todo o povo respondeu: 'É boa esta palavra'.")
    add("O que aconteceu quando Elias orou fervorosamente no Monte Carmelo ao cair da tarde?",
        "O fogo do Senhor desceu e consumiu o holocausto, a lenha, as pedras, o pó e lambeu toda a água da vala", "Uma chuva fina começou a cair", "Houve um grande terremoto", "Os profetas de Baal fugiram",
        "facil", "1 Reis", "1 Reis 18:38", "Caiu fogo do Senhor e consumiu o holocausto, a lenha, as pedras e o pó, e ainda lambeu a água que estava no rego.")
    add("O que todo o povo clamou com o rosto em terra ao ver o fogo consumidor no Carmelo?",
        "'O Senhor é Deus! O Senhor é Deus!'", "'Baal é poderoso!'", "'Viva o rei Acabe!'", "'Fugirei para Samaria!'",
        "facil", "1 Reis", "1 Reis 18:39", "Vendo isto, todo o povo caiu com o rosto em terra e disse: 'O Senhor é Deus! O Senhor é Deus!'.")
    add("O que o servo de Elias viu no mar da sétima vez que foi olhar enquanto o profeta orava de cabeça entre os joelhos?",
        "Uma pequena nuvem do tamanho da palma da mão de um homem subindo do mar", "Um relâmpago de ouro", "Um navio mercante", "Três pássaros brancos",
        "facil", "1 Reis", "1 Reis 18:44", "À sétima vez disse o moço: 'Eis que sobe do mar uma nuvem pequena como a palma da mão de um homem'. E logo veio grande chuva.")
    add("Por que Elias fugiu para o deserto e deitou-se debaixo de um zimbro pedindo para morrer?",
        "Porque Jezabel jurou matá-lo dentro de 24 horas pela morte dos profetas de Baal", "Porque o rei Acabe o perseguiu com carros", "Porque estava enfermo", "Porque o povo o abandonou",
        "facil", "1 Reis", "1 Reis 19:1-4", "Jezabel jurou: 'Façam-me os deuses o que quiserem se amanhã a estas horas não fizer com a tua vida como fizeste a um deles'. Elias temeu e fugiu ao deserto.")
    add("Como Deus alimentou Elias no deserto concedendo-lhe forças para caminhar quarenta dias até o monte Horebe?",
        "Um anjo tocou nele e proveu um bolo assado sobre as brasas e uma botija de água", "Caiu maná fresco na areia", "Corvos voltaram a alimentá-lo", "Encontrou uma vinha silvestre",
        "facil", "1 Reis", "1 Reis 19:5-8", "O anjo tocou-o e disse: 'Levanta-te e come, porque muito longo te será o caminho'. Com a força daquela comida caminhou 40 dias até Horebe.")
    add("Como Deus falou a Elias na caverna do monte Horebe após o vento forte, o terremoto e o fogo?",
        "Num cicio suave e tranquilo (uma voz mansa e delicada)", "Num trovão ensurdecedor", "Num raio flamejante", "Num coro celestial retumbante",
        "facil", "1 Reis", "1 Reis 19:11-12", "Depois do vento, um terremoto; mas o Senhor não estava no terremoto. Depois do fogo, uma voz mansa e delicada.")
    add("Quantos fiéis em Israel Deus revelou a Elias que não haviam dobrado os joelhos a Baal?",
        "7.000 homens", "144.000 homens", "120 homens", "500 homens",
        "facil", "1 Reis", "1 Reis 19:18", "Deus disse: 'Deixei ficar em Israel sete mil: todos os joelhos que não se dobraram a Baal, e toda boca que não o beijou'.")
    add("Quem Elias encontrou arando a terra com doze juntas de bois e lançou sobre ele a sua capa profética?",
        "Eliseu, filho de Safate", "Geazi", "Obadias", "Hazael",
        "facil", "1 Reis", "1 Reis 19:19", "Elias achou a Eliseu que arava com doze juntas de bois; Elias passou por ele e lançou a sua capa sobre ele.")
    add("O que a ímpia rainha Jezabel fez para roubar a vinha de Nabote em Jezreel para Acabe?",
        "Subornou falsas testemunhas acusando Nabote de blasfemar contra Deus e o rei, apedrejando-o até a morte", "Pagou o triplo do valor da vinha", "Incendiou a casa de Nabote", "Prendeu Nabote no calabouço",
        "facil", "1 Reis", "1 Reis 21:7-14", "Jezabel escreveu cartas seladas com o sinete real para que homens perversos testemunhassem falsamente contra Nabote, que foi apedrejado.")
    add("Como o rei Acabe morreu na batalha de Ramote-Gileade contra os sírios, apesar de estar disfarçado?",
        "Um soldado atirou uma flecha ao acaso que penetrou entre as junturas da sua couraça", "Foi cercado por cem cavaleiros", "Caiu do carro e afogou-se", "Foi envenenado por seu escudeiro",
        "facil", "1 Reis", "1 Reis 22:34", "Um homem armou o arco e atirou ao acaso, e feriu o rei de Israel entre as junturas da couraça; e ele morreu ao entardecer.")
    add("Como o profeta Elias subiu ao céu no final de sua jornada terrena?",
        "Num redemoinho ao céu após o aparecimento de um carro e cavalos de fogo que o separaram de Eliseu", "Foi sepultado no monte Nebo", "Faleceu pacificamente em Siló", "Desapareceu no deserto",
        "facil", "2 Reis", "2 Reis 2:11", "Eis que um carro de fogo e cavalos de fogo os separaram um do outro; e Elias subiu ao céu num redemoinho.")
    add("O que Eliseu pediu a Elias antes que este fosse tomado para o céu?",
        "Uma porção dobrada do espírito profético que estava sobre Elias", "Riquezas e terras em Canaã", "Poder para derrotar reis", "Uma vida de cem anos",
        "facil", "2 Reis", "2 Reis 2:9", "Eliseu disse: 'Peço-te que haja porção dobrada do teu espírito sobre mim'.")
    add("Qual foi o primeiro milagre de Eliseu após herdar a capa de Elias que caíra?",
        "Feriu as águas do Jordão com a capa e o rio se abriu para ele passar", "Curou um leproso", "Fez cair fogo do céu", "Multiplicou pães",
        "facil", "2 Reis", "2 Reis 2:14", "Eliseu tomou a capa de Elias que lhe caíra, feriu as águas e disse: 'Onde está o Senhor Deus de Elias?'. E as águas se dividiram.")
    add("Como Eliseu purificou as águas mortais e a terra estéril da cidade de Jericó?",
        "Lançou sal num prato novo diretamente na nascente das águas", "Derramou azeite de oliva", "Bateu na fonte com seu cajado", "Orou durante sete dias",
        "facil", "2 Reis", "2 Reis 2:20-22", "Eliseu disse: 'Trazei-me um prato novo e ponde nele sal'. Foi ao manancial e deitou o sal, e as águas ficaram sãs até hoje.")
    add("O que Eliseu multiplicou milagrosamente para uma viúva pobre pagar suas dívidas e não perder os filhos como escravos?",
        "Uma botija de azeite que encheu todas as vasilhas que ela tomara emprestadas dos vizinhos", "Pães de cevada", "Moedas de prata no jarro", "Sementes de trigo",
        "facil", "2 Reis", "2 Reis 4:1-7", "O azeite jorrou continuamente enchendo todas as vasilhas trazidas até que não houve mais vaso; e ela vendeu o azeite e pagou a dívida.")
    add("O que a mulher sunamita e seu marido construíram no eirado de sua casa para acolher o profeta Eliseu?",
        "Um pequeno quarto mobiliado com cama, mesa, cadeira e candeeiro", "Uma grande sala de banquetes", "Uma torre de oração", "Um jardim com fonte",
        "medio", "2 Reis", "2 Reis 4:10", "A sunamita disse: 'Façamos-lhe um pequeno quarto de tijolos, e ponhamos-lhe nele uma cama, uma mesa, uma cadeira e um candeeiro'.")
    add("Como Eliseu ressuscitou o filho falecido da mulher sunamita?",
        "Subiu ao quarto, deitou-se sobre a criança pondo a boca sobre sua boca e olhos sobre seus olhos até a carne aquecer, e o menino espirrou sete vezes", "Tocou nele com seu bordão de longe", "Mandou chamar os sacerdotes", "Orou na porta da cidade",
        "medio", "2 Reis", "2 Reis 4:32-35", "Eliseu deitou-se sobre o menino e a carne aqueceu; depois o menino espirrou sete vezes e abriu os olhos.")
    add("Como Eliseu purificou a panela de ensopado comunitário envenenado por ervas bravas colhidas no campo?",
        "Lançou farinha na panela e o veneno foi anulado", "Derramou vinho doce", "Ferveu com água pura", "Jogou fora o ensopado",
        "medio", "2 Reis", "2 Reis 4:40-41", "Clamaram: 'Homem de Deus, há morte na panela!'. Ele disse: 'Trazei farinha'. E deitou-a na panela e não houve mais mal algum.")
    add("Qual comandante ilustre do exército da Síria sofria de lepra e foi buscar cura através de Eliseu?",
        "Naamã", "Hazael", "Ben-Hadade", "Senaqueribe",
        "facil", "2 Reis", "2 Reis 5:1", "Naamã, capitão do exército do rei da Síria, era homem grande e valoroso, porém leproso.")
    add("O que a pequena menina hebréia cativa disse à esposa de Naamã que motivou sua viagem?",
        "'Tomara que o meu senhor estivesse diante do profeta que está em Samaria, pois ele o curaria da sua lepra'", "'Os deuses da Síria são impotentes'", "'Nenhum remédio pode curá-lo'", "'Foge para o deserto'",
        "facil", "2 Reis", "2 Reis 5:2-3", "A menina disse à sua senhora: 'Oxalá o meu senhor estivesse diante do profeta que está em Samaria; ele o restauraria da sua lepra'.")
    add("Que ordem de Eliseu indignou a princípio o orgulhoso comandante Naamã?",
        "Mergulhar sete vezes no rio Jordão para ser purificado", "Pagar dez talentos de ouro puro", "Ficar em quarentena quarenta dias", "Queimar suas armas de guerra",
        "facil", "2 Reis", "2 Reis 5:10-14", "Eliseu mandou dizer: 'Vai, e lava-te sete vezes no Jordão e a tua carne sarará'. Naamã desceu, mergulhou sete vezes e ficou limpo.")
    add("O que aconteceu a Geazi, servo de Eliseu, por ter mentido e corrido atrás de Naamã para obter prata e vestes por cobiça?",
        "A lepra de Naamã apegou-se a ele e à sua descendência tornando-o branco como a neve", "Foi preso pelo rei de Israel", "Ficou mudo instantaneamente", "Perdeu o ouro conquistado",
        "facil", "2 Reis", "2 Reis 5:26-27", "Eliseu disse a Geazi: 'A lepra de Naamã se apegará a ti e à tua semente para sempre'. E saiu da presença dele leproso como a neve.")
    add("Como Eliseu recuperou um machado de ferro emprestado que caíra nas águas profundas do Jordão?",
        "Cortou um pedaço de pau e lançou-o no lugar, e o ferro flutuou milagrosamente à tona", "Mergulhou e resgatou com a mão", "Secou as águas do rio", "Pediu aos soldados que cavassem",
        "facil", "2 Reis", "2 Reis 6:5-7", "Eliseu cortou um pau, lançou-o ali e fez flutuar o ferro; e o discípulo estendeu a mão e o tomou.")
    add("O que Eliseu orou para que Deus fizesse pelo seu servo atemorizado pelo exército sírio que cercava a cidade de Dotã?",
        "'Senhor, abre-lhe os olhos para que veja os cavalos e carros de fogo ao redor de Eliseu'", "'Faze descer raios sobre os sírios'", "'Dá-nos asas para fugir'", "'Manda terremoto na planície'",
        "facil", "2 Reis", "2 Reis 6:15-17", "Eliseu orou: 'Senhor, abre-lhe os olhos para que veja'. E viu o moço o monte cheio de cavalos e carros de fogo ao redor de Eliseu.")
    add("Qual piedoso rei de Judá removeu os altos idólatras e despedaçou a serpente de bronze feita por Moisés que o povo idolatrava chamando-a de Neustã?",
        "Ezequias", "Josafá", "Asa", "Josias",
        "medio", "2 Reis", "2 Reis 18:4", "Ezequias removeu os altos, quebrou as estátuas e despedaçou a serpente de bronze porque os israelitas lhe queimavam incenso, e chamou-a Neustã.")

    return items[:160]

if __name__ == "__main__":
    q_list = get_historical_questions()
    print(f"Historical generated: {len(q_list)} questions")
