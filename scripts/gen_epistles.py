# -*- coding: utf-8 -*-
"""
Gerador de 140 questões bíblicas de Atos e Cartas (Epístolas).
Livros: Atos, Romanos, 1 e 2 Coríntios, Gálatas, Efésios, Filipenses, Colossenses,
1 e 2 Tessalonicenses, 1 e 2 Timóteo, Tito, Filemom, Hebreus, Tiago, 1 e 2 Pedro,
1, 2 e 3 João, Judas.
"""

def get_epistles_questions():
    items = []

    def add(q, c, w1, w2, w3, diff, book, ref, exp):
        items.append({
            "q": q,
            "c": c,
            "w1": w1,
            "w2": w2,
            "w3": w3,
            "diff": diff,
            "book": book,
            "testament": "NT",
            "section": "Atos e Cartas",
            "ref": ref,
            "exp": exp
        })

    # --- ATOS DOS APÓSTOLOS ---
    add("A quem o livro de Atos dos Apóstolos é dedicado no seu primeiro versículo?",
        "Teófilo", "Cornélio", "Apolo", "Timóteo",
        "facil", "Atos", "Atos 1:1", "Lucas dedicou tanto o seu Evangelho quanto o livro de Atos a Teófilo.")
    add("Quantos dias Jesus permaneceu aparecendo aos discípulos após a Sua ressurreição antes de ascender ao céu?",
        "40 dias", "50 dias", "30 dias", "7 dias",
        "facil", "Atos", "Atos 1:3", "Jesus apresentou-se vivo por quarenta dias falando acerca do Reino de Deus.")
    add("Qual discípulo foi escolhido por sorteio para ocupar o lugar de Judas Iscariotes no colégio apostólico?",
        "Matias", "José Barsabás", "Barnabé", "Estêvão",
        "facil", "Atos", "Atos 1:26", "A sorte caiu sobre Matias, que foi contado com os onze apóstolos.")
    add("Qual festa judaica estava sendo celebrada quando o Espírito Santo desceu com som de vento impetuoso e línguas de fogo?",
        "Pentecostes", "Páscoa", "Tabernáculos", "Purim",
        "facil", "Atos", "Atos 2:1-4", "O derramamento do Espírito Santo ocorreu no dia de Pentecostes em Jerusalém.")
    add("Aproximadamente quantas pessoas foram batizadas após o primeiro sermão de Pedro no Pentecostes?",
        "Cerca de três mil", "Quinhentas", "Cerca de dez mil", "Cento e vinte",
        "facil", "Atos", "Atos 2:41", "Naquele dia agregaram-se quase três mil almas à igreja nascente.")
    add("Qual milagre foi operado por Pedro e João junto à porta do Templo chamada Formosa?",
        "A cura de um homem coxo de nascença", "A ressurreição de uma jovem", "A cura de um cego de Jericó", "A libertação de um leproso",
        "facil", "Atos", "Atos 3:2-8", "Pedro disse: 'Não tenho prata nem ouro; o que tenho, isso te dou: em nome de Jesus Cristo, levanta-te e anda'.")
    add("Qual casal morreu instantaneamente após mentir ao Espírito Santo sobre o valor de uma propriedade vendida?",
        "Ananias e Safira", "Áquila e Priscila", "Zacarias e Isabel", "Filipe e Berenice",
        "facil", "Atos", "Atos 5:1-10", "Ananias e Safira mentiram retendo parte do valor, caindo mortos diante dos apóstolos.")
    add("Qual mestre da lei no Sinédrio aconselhou não combater os apóstolos, dizendo que se a obra fosse de Deus não poderiam desfazê-la?",
        "Gamaliel", "Nicodemos", "Caifás", "Anás",
        "medio", "Atos", "Atos 5:34-39", "Gamaliel recomendou cautela ao Sinédrio para que não lutassem contra Deus.")
    add("Qual foi a razão pela qual os apóstolos instituíram os sete diáconos em Atos 6?",
        "Para cuidar da distribuição diária às viúvas e permitir aos apóstolos oração e ministério da palavra",
        "Para construir um templo em Samaria",
        "Para recolher os impostos de Roma",
        "Para escrever as cartas apostólicas",
        "facil", "Atos", "Atos 6:1-4", "Os sete homens cheios de fé e do Espírito Santo foram separados para servir às mesas.")
    add("Quem foi o primeiro mártir da igreja cristã, apedrejado enquanto via a glória de Deus e Jesus de pé à direita do Pai?",
        "Estêvão", "Tiago irmão de João", "Filipe", "Barnabé",
        "facil", "Atos", "Atos 7:55-60", "Estêvão foi apedrejado perdoando seus executores, sendo o primeiro mártir cristão.")
    add("Quem consentia na morte de Estêvão e guardava as vestes daqueles que o apedrejavam?",
        "Saulo de Tarso", "Pilatos", "Félix", "Herodes Antipas",
        "facil", "Atos", "Atos 7:58; 8:1", "Saulo consentia na morte de Estêvão antes de sua notável conversão.")
    add("Quem pregou com grande poder em Samaria e depois foi conduzido pelo Espírito ao deserto para evangelizar o eunuco etíope?",
        "Filipe o evangelista", "Tomé", "Bartolomeu", "Simão Pedro",
        "facil", "Atos", "Atos 8:5, 26-38", "Filipe pregou em Samaria e explicou Isaías 53 ao oficial da rainha Candace.")
    add("Qual mágico em Samaria tentou comprar o poder de conceder o Espírito Santo com dinheiro?",
        "Simão o mago", "Elmas", "Barjesus", "Demetrio",
        "medio", "Atos", "Atos 8:18-20", "Simão tentou subornar os apóstolos, de onde derivou a palavra 'simonia'.")
    add("No caminho para qual cidade Saulo foi cercado por uma luz do céu e ouviu a voz de Jesus ressurreto?",
        "Damasco", "Antioquia", "Tarso", "Roma",
        "facil", "Atos", "Atos 9:3-5", "Saulo ia para Damasco quando Jesus lhe apareceu: 'Saulo, Saulo, por que me persegues?'.")
    add("Qual discípulo em Damasco recebeu a visão do Senhor para ir orar por Saulo na rua Direita?",
        "Ananias", "Barnabé", "Silas", "Ágabo",
        "medio", "Atos", "Atos 9:10-17", "Ananias obedeceu ao Senhor e impôs as mãos sobre Saulo, que recuperou a vista.")
    add("Qual discípula piedosa de Jope, famosa por suas boas obras e costuras para as viúvas, foi ressuscitada por Pedro?",
        "Tabita (Dorcas)", "Lídia", "Priscila", "Rode",
        "facil", "Atos", "Atos 9:36-40", "Pedro orou e disse: 'Tabita, levanta-te', restaurando-lhe a vida.")
    add("Quem era o centurião romano piedoso de Cesareia cuja casa foi a primeira entre os gentios a receber o Espírito Santo?",
        "Cornélio", "Júlio", "Lísias", "Festo",
        "facil", "Atos", "Atos 10:1-48", "Cornélio enviou buscar Pedro após uma visão angelical, e o Espírito caiu sobre todos os gentios.")
    add("Em qual cidade os discípulos de Jesus foram chamados de 'cristãos' pela primeira vez?",
        "Antioquia", "Jerusalém", "Alexandria", "Éfeso",
        "facil", "Atos", "Atos 11:26", "Foi em Antioquia da Síria que os seguidores de Jesus receberam o nome de cristãos.")
    add("Qual profeta anunciou em Antioquia que haveria uma grande fome em todo o mundo romano?",
        "Ágabo", "Simeão Niger", "Manaém", "Lúcio",
        "dificil", "Atos", "Atos 11:28", "O profeta Ágabo predisse a grande fome ocorrida nos dias do imperador Cláudio.")
    add("Qual apóstolo, irmão de João, foi morto à espada a mando do rei Herodes Agripa I em Atos 12?",
        "Tiago", "André", "Filipe", "Judas Tadeu",
        "medio", "Atos", "Atos 12:1-2", "Tiago, filho de Zebedeu, foi o primeiro apóstolo a sofrer o martírio.")
    add("Qual jovem serva atendeu a porta e, reconhecendo a voz de Pedro liberto da prisão pelo anjo, correu sem abrir?",
        "Rode", "Lídia", "Priscila", "Febe",
        "medio", "Atos", "Atos 12:13-14", "Rode ficou tão alegre ao ouvir a voz de Pedro que correu para anunciar antes de abrir o portão.")
    add("Quem acompanhou Paulo e Barnabé no início da primeira viagem missionária mas retornou em Perge da Panfília?",
        "João Marcos", "Lucas", "Tito", "Apolo",
        "medio", "Atos", "Atos 13:13", "João Marcos regressou a Jerusalém, gerando controvérsia posterior entre Paulo e Barnabé.")
    add("Qual mágico falso profeta foi repreendido por Paulo e ficou cego temporariamente na ilha de Chipre?",
        "Elimas (Barjesus)", "Simão de Samaria", "Alexandre latoeiro", "Himeneu",
        "dificil", "Atos", "Atos 13:6-11", "Paulo confrontou Elimas diante do procônsul Sérgio Paulo na cidade de Pafos.")
    add("Em qual cidade Paulo foi apedrejado e arrastado para fora, julgado morto, mas se levantou e retornou à cidade?",
        "Listra", "Derbe", "Icônio", "Filipos",
        "medio", "Atos", "Atos 14:19-20", "Em Listra Paulo foi apedrejado, mas sobreviveu miraculosamente e seguiu para Derbe.")
    add("Qual importante decisão foi tomada no Concílio de Jerusalém registrado em Atos 15?",
        "Que os gentios convertidos não precisavam ser circuncidados nem guardar a lei de Moisés para serem salvos",
        "Que todos os crentes deveriam mudar para Roma",
        "Que era proibido pregar na Grécia",
        "Que os apóstolos deveriam fundar mosteiros",
        "facil", "Atos", "Atos 15:1-29", "O concílio concluiu que a salvação se dá pela graça do Senhor Jesus mediante a fé.")
    add("Qual jovem cristão de bom testemunho em Listra uniu-se a Paulo na sua segunda viagem missionária?",
        "Timóteo", "Tito", "Tíquico", "Erasto",
        "facil", "Atos", "Atos 16:1-3", "Timóteo, filho de uma judia crente e de pai grego, tornou-se fiel cooperador de Paulo.")
    add("Qual visão Paulo teve em Trôade que o direcionou a cruzar para a Europa e pregar o Evangelho?",
        "A visão de um homem macedônio clamando: 'Passa à Macedônia e ajuda-nos'",
        "A visão de uma arca com animais impuros",
        "A visão de um templo em chamas",
        "A visão de uma sarça ardente",
        "facil", "Atos", "Atos 16:9-10", "A visão do varão macedônio abriu as portas da Europa ao Cristianismo.")
    add("Quem foi a negociante de púrpura da cidade de Tiatira, batizada com sua casa em Filipos?",
        "Lídia", "Priscila", "Febe", "Evódia",
        "facil", "Atos", "Atos 16:14-15", "O Senhor abriu o coração de Lídia para acolher as palavras de Paulo junto ao rio em Filipos.")
    add("O que Paulo e Silas faziam à meia-noite na prisão de Filipos antes de um grande terremoto abrir as celas?",
        "Oravam e cantavam hinos a Deus", "Dormiam profundamente", "Planejavam uma fuga secreta", "Escreviam petições a César",
        "facil", "Atos", "Atos 16:25-26", "Mesmo açoitados e com os pés no tronco, Paulo e Silas oravam e cantavam louvores.")
    add("Qual foi a famosa resposta de Paulo ao carcereiro de Filipos que perguntou: 'O que devo fazer para ser salvo?'?",
        "'Crê no Senhor Jesus Cristo e serás salvo, tu e a tua casa'",
        "'Guarda os preceitos dos filósofos'",
        "'Paga uma oferta ao imperador'",
        "'Foge imediatamente da prisão'",
        "facil", "Atos", "Atos 16:30-31", "Paulo proclamou a simplicidade da salvação pela fé no Senhor Jesus Cristo.")
    add("Qual elogio especial receberam os judeus da cidade de Bereia em Atos 17?",
        "Eram mais nobres que os de Tessalônica e examinavam diariamente as Escrituras para ver se as coisas eram assim",
        "Eram os mais ricos negociantes da Grécia",
        "Construíram a maior sinagoga da Ásia",
        "Tinham os melhores soldados romanos",
        "facil", "Atos", "Atos 17:11", "Os bereanos checavam diligentemente tudo à luz das Escrituras Sagradas.")
    add("Em qual local em Atenas Paulo proferiu seu célebre discurso aos filósofos sobre o 'Deus Desconhecido'?",
        "Areópago", "Partenon", "Estádio Panatenaico", "Coliseu",
        "medio", "Atos", "Atos 17:19-23", "No Areópago, Paulo explicou quem era o Deus criador desconhecido pelos idólatras atenienses.")
    add("Qual casal de fabricantes de tendas acolheu Paulo em Corinto e colaborou ativamente no ministério?",
        "Áquila e Priscila", "Ananias e Safira", "Zacarias e Isabel", "Filemom e Áfia",
        "facil", "Atos", "Atos 18:1-3", "Áquila e Priscila tinham a mesma profissão de Paulo e foram colunas da igreja primitiva.")
    add("Qual judeu eloquente e poderoso nas Escrituras, natural de Alexandria, foi discipulado por Áquila e Priscila em Éfeso?",
        "Apolo", "Tertulo", "Sóstene", "Epafras",
        "medio", "Atos", "Atos 18:24-28", "Priscila e Áquila chamaram Apolo e expuseram-lhe mais perfeitamente o caminho de Deus.")
    add("Qual jovem adormeceu durante o longo discurso de Paulo em Trôade e caiu da janela do terceiro andar, sendo ressuscitado pelo apóstolo?",
        "Êutico", "Onésimo", "Trófimo", "Públio",
        "facil", "Atos", "Atos 20:9-12", "Êutico adormeceu ouvindo Paulo, caiu e morreu, mas Paulo o abraçou e sua vida foi restaurada.")
    add("Em qual ilha Paulo naufragou a caminho de Roma e sobreviveu ileso à mordida de uma víbora venenosa?",
        "Malta (Melita)", "Creta", "Chipre", "Patmos",
        "facil", "Atos", "Atos 28:1-6", "Em Malta, a víbora prendeu-se à mão de Paulo mas ele sacudiu-a no fogo sem sofrer dano algum.")

    # --- ROMANOS ---
    add("Segundo Romanos 1:16, de que o apóstolo Paulo afirma não se envergonhar?",
        "Do evangelho de Cristo, pois é o poder de Deus para salvação de todo aquele que crê",
        "De sua nobre linhagem farisaica",
        "Da sabedoria secular de Atenas",
        "Do poder militar do Império Romano",
        "facil", "Romanos", "Romanos 1:16", "O evangelho é o poder vivificante de Deus tanto para judeus como para gentios.")
    add("Qual versículo de Romanos declara: 'Porque todos pecaram e destituídos estão da glória de Deus'?",
        "Romanos 3:23", "Romanos 1:1", "Romanos 6:1", "Romanos 12:1",
        "facil", "Romanos", "Romanos 3:23", "O pecado universal nivelou toda a humanidade sob a necessidade da graça redentora.")
    add("Quem é apresentado em Romanos 4 como o exemplo supremo de justificação pela fé antes da circuncisão?",
        "Abraão", "Moisés", "Davi", "Enoque",
        "facil", "Romanos", "Romanos 4:1-3", "Abraão creu em Deus, e isso lhe foi imputado para justiça.")
    add("Segundo Romanos 5:1, que bênção os crentes desfrutam ao serem justificados pela fé?",
        "Paz com Deus por meio de nosso Senhor Jesus Cristo",
        "Isenção de qualquer tribulação terrena",
        "Riquezas materiais imediatas",
        "Poder político sobre as nações",
        "facil", "Romanos", "Romanos 5:1", "A justificação encerra a inimizade com Deus e concede profunda e perpétua paz espiritual.")
    add("Como Romanos 5:8 descreve a prova máxima do amor divino para conosco?",
        "Cristo morreu por nós sendo nós ainda pecadores",
        "Deus concedeu bênçãos materiais a Israel",
        "Os anjos protegeram os profetas",
        "Deus castigou os ímpios no dilúvio",
        "facil", "Romanos", "Romanos 5:8", "Deus provou Seu incomensurável amor entregando Seu Filho quando éramos Seus inimigos.")
    add("Segundo Romanos 6:23, qual é o salário do pecado e qual é o dom gratuito de Deus?",
        "O salário do pecado é a morte, e o dom de Deus é a vida eterna em Cristo Jesus",
        "O salário é a tristeza e o dom é a riqueza",
        "O salário é a condenação da carne e o dom é a reencarnação",
        "O salário é a cegueira e o dom é a sabedoria humana",
        "facil", "Romanos", "Romanos 6:23", "A antítese perfeita: o pecado paga o que merece (morte), mas Deus dá de graça vida eterna.")
    add("Qual afirmação consoladora abre o capítulo 8 de Romanos?",
        "'Agora, pois, nenhuma condenação há para os que estão em Cristo Jesus'",
        "'A lei mosaica deve ser guardada integralmente'",
        "'O sofrimento humano não tem consolo'",
        "'Somente os anjos entrarão na glória'",
        "facil", "Romanos", "Romanos 8:1", "Em Cristo, a condenação foi plenamente liquidada na cruz.")
    add("Qual clamor o Espírito de adoção coloca nos corações dos crentes segundo Romanos 8:15 e Gálatas 4:6?",
        "'Aba, Pai'", "'Glória ao homem'", "'Senhor e Juiz'", "'Santo Templo'",
        "facil", "Romanos", "Romanos 8:15", "O Espírito Santo testifica nossa filiação clamando afetuosamente 'Aba, Pai'.")
    add("Segundo Romanos 8:28, todas as coisas cooperam para o bem de quem?",
        "Daqueles que amam a Deus, daqueles que são chamados segundo o seu propósito",
        "De todas as pessoas do mundo indistintamente",
        "Apenas daqueles que nunca sofrem tribulação",
        "Dos que possuem grande erudição teológica",
        "facil", "Romanos", "Romanos 8:28", "A soberania de Deus canaliza até as adversidades para o bem eterno dos Seus amados.")
    add("Em Romanos 8:37, como os crentes são descritos em face de tribulação, angústia, perseguição ou espada?",
        "Mais do que vencedores, por meio daquele que nos amou",
        "Sobreviventes temerosos",
        "Pessoas fadadas ao desespero",
        "Eternos perdedores na terra",
        "facil", "Romanos", "Romanos 8:37", "Em Cristo não somos meros vitoriosos, mas 'mais do que vencedores'.")
    add("Segundo Romanos 10:9, o que é necessário para ser salvo?",
        "Confessar com a boca que Jesus é Senhor e crer no coração que Deus o ressuscitou dentre os mortos",
        "Fazer uma peregrinação a Jerusalém",
        "Conhecer todas as línguas antigas",
        "Construir um santuário de pedras",
        "facil", "Romanos", "Romanos 10:9", "A confissão do senhorio de Cristo aliada à fé na ressurreição constitui a salvação.")
    add("Como a fé vem ao coração humano de acordo com Romanos 10:17?",
        "Pelo ouvir, e o ouvir pela palavra de Deus",
        "Pela dedução científica",
        "Pelo silêncio dos eremitas",
        "Pela contemplação de obras de arte",
        "facil", "Romanos", "Romanos 10:17", "A fé salvadora é gerada e despertada pela proclamação da Palavra de Cristo.")
    add("Qual apelo prático de consagração Paulo faz aos irmãos em Romanos 12:1?",
        "Apresentar seus corpos como sacrifício vivo, santo e agradável a Deus, que é o vosso culto racional",
        "Oferecer novilhos no altar de mármore",
        "Retirar-se para o topo dos montes ermos",
        "Vender todas as roupas aos necessitados",
        "facil", "Romanos", "Romanos 12:1", "O culto aceitável no Novo Pacto é a entrega integral e diária da nossa própria vida.")
    add("De que maneira o cristão deve vencer o mal segundo Romanos 12:21?",
        "Vencendo o mal com o bem",
        "Retribuindo olho por olho",
        "Levando o ofensor aos tribunais mundanos",
        "Ignorando a existência da sociedade",
        "facil", "Romanos", "Romanos 12:21", "'Não te deixes vencer do mal, mas vence o mal com o bem'.")
    add("Quem é descrita em Romanos 16:1-2 como diaconisa da igreja de Cencreia que auxiliou a muitos e ao próprio Paulo?",
        "Febe", "Priscila", "Maria", "Trifena",
        "medio", "Romanos", "Romanos 16:1-2", "Febe era diaconisa em Cencreia e portadora comissionada da carta aos Romanos.")

    # --- 1 E 2 CORÍNTIOS ---
    add("Qual divisão na igreja de Corinto Paulo repreendeu energicamente em 1 Coríntios 1?",
        "O partidarismo daqueles que diziam: 'Eu sou de Paulo', 'Eu de Apolo', 'Eu de Cefas', 'Eu de Cristo'",
        "A escolha dos hinos musicais",
        "A preferência por comidas gregas ou judaicas",
        "A eleição dos prefeitos da cidade",
        "facil", "1 Coríntios", "1 Coríntios 1:12-13", "Paulo exortou a igreja à união em torno exclusivo de Cristo, que foi crucificado por nós.")
    add("A pregação da cruz é descrita em 1 Coríntios 1:18 como sendo loucura para os que perecem, mas para nós o que ela é?",
        "O poder de Deus", "Um enigma poético", "Uma lenda dos hebreus", "Uma ilusão filosófica",
        "facil", "1 Coríntios", "1 Coríntios 1:18", "A cruz parece fraqueza aos homens soberbos, mas é a manifestação máxima do poder de Deus.")
    add("Qual é o único fundamento que ninguém pode pôr além do que já foi posto segundo 1 Coríntios 3:11?",
        "Jesus Cristo", "O apóstolo Pedro", "O templo de Salomão", "A lei de Moisés",
        "facil", "1 Coríntios", "1 Coríntios 3:11", "Jesus Cristo é a única rocha e fundamento indestrutível da Igreja.")
    add("De acordo com 1 Coríntios 6:19-20, o que é o corpo do crente redimido por bom preço?",
        "Santuário (templo) do Espírito Santo", "Uma prisão material passageira", "Um instrumento sem valor moral", "Um artefato mundano",
        "facil", "1 Coríntios", "1 Coríntios 6:19-20", "Nossos corpos pertencem a Deus e devem glorificá-Lo como templos do Espírito Santo.")
    add("Em 1 Coríntios 9:24-27, com que tipo de atleta Paulo compara a disciplina da vida cristã?",
        "Um corredor em busca de uma coroa incorruptível e um lutador que disciplina o próprio corpo",
        "Um lançador de discos desleixado",
        "Um cavaleiro com armadura de ouro",
        "Um arqueiro solitário",
        "medio", "1 Coríntios", "1 Coríntios 9:24-27", "Paulo compara a fé à corrida atlética na busca não de louros terrenos, mas da coroa eterna.")
    add("Qual alerta Paulo faz em 1 Coríntios 10:12 contra a soberba espiritual?",
        "'Aquele que pensa estar em pé, veja que não caia'",
        "'Aquele que é forte não precisa orar'",
        "'Os sábios nunca tropeçam'",
        "'O crente perfeito está imune a tentações'",
        "facil", "1 Coríntios", "1 Coríntios 10:12", "A humildade e a vigilância são salvaguardas essenciais contra a queda moral.")
    add("Na Ceia do Senhor em 1 Coríntios 11:26, o que os crentes anunciam todas as vezes que comem o pão e bebem o cálice?",
        "A morte do Senhor, até que Ele venha", "A criação do universo", "As guerras dos reis de Judá", "O juízo sobre Faraó",
        "facil", "1 Coríntios", "1 Coríntios 11:26", "A Ceia proclama memorialmente o sacrifício de Cristo na cruz e a bendita esperança de Sua volta.")
    add("Como Paulo descreve a interdependência dos dons espirituais e dos membros da igreja em 1 Coríntios 12?",
        "Como os muitos membros de um único corpo humano harmonioso",
        "Como soldados disputando a mesma patente",
        "Como árvores isoladas em uma floresta",
        "Como estrelas que não se comunicam",
        "facil", "1 Coríntios", "1 Coríntios 12:12-27", "Cada crente tem um papel vital no corpo de Cristo, cuidando uns dos outros em amor.")
    add("Qual é o tema sublime de 1 Coríntios 13, considerado o capítulo do ágape?",
        "A supremacia e excelência eterna do amor",
        "A construção de sinagogas de luxo",
        "A história dos reis de Tiro",
        "A astrologia do oriente antigo",
        "facil", "1 Coríntios", "1 Coríntios 13:1-13", "Ainda que falássemos línguas humanas e angélicas, sem amor nada seríamos.")
    add("Das três virtudes que permanecem (fé, esperança e amor), qual é expressamente declarada a maior em 1 Coríntios 13:13?",
        "O amor", "A fé", "A esperança", "A profecia",
        "facil", "1 Coríntios", "1 Coríntios 13:13", "'Agora, pois, permanecem a fé, a esperança e o amor, estes três; mas o maior destes é o amor'.")
    add("Qual doutrina central do cristianismo é defendida de forma exaustiva e gloriosa em 1 Coríntios 15?",
        "A ressurreição corporal de Cristo e dos salvos",
        "O celibato dos rabinos",
        "A alimentação kosher dos gentios",
        "A adoração nos montes da Samaria",
        "facil", "1 Coríntios", "1 Coríntios 15:1-58", "Se Cristo não ressuscitou, é vã a nossa pregação e vã a nossa fé.")
    add("Qual triunfo sobre a sepultura é proclamado profeticamente no final de 1 Coríntios 15:55?",
        "'Onde está, ó morte, a tua vitória? Onde está, ó morte, o teu aguilhão?'",
        "'A morte venceu a carne'",
        "'Não há esperança além da cova'",
        "'O mundo pertence às sombras'",
        "facil", "1 Coríntios", "1 Coríntios 15:55", "A morte foi tragada na vitória da ressurreição de Cristo.")
    add("Como o Deus de toda consolação nos conforta em todas as nossas tribulações segundo 2 Coríntios 1:3-4?",
        "Para que possamos consolar os que estiverem em qualquer angústia com o consolo que nós mesmos recebemos de Deus",
        "Para que vivamos isolados e orgulhosos",
        "Para que cobremos tributos dos aflitos",
        "Para que descansemos sem ajudar o próximo",
        "medio", "2 Coríntios", "2 Coríntios 1:3-4", "O sofrimento consolado capacita o cristão para ser canal de amparo e compaixão a outros.")
    add("Onde temos guardado o incomparável tesouro do ministério do evangelho segundo 2 Coríntios 4:7?",
        "Em vasos de barro, para que a excelência do poder seja de Deus e não de nós",
        "Em cofres de ouro maciço",
        "Em templos de mármore imperial",
        "Nas montanhas inacessíveis da Judeia",
        "facil", "2 Coríntios", "2 Coríntios 4:7", "Nossa fragilidade humana ('vasos de barro') evidencia que a glória e o poder emanam de Deus.")
    add("O que acontece com alguém que está em Cristo de acordo com a memorável promessa de 2 Coríntios 5:17?",
        "Nova criatura é; as coisas velhas já passaram; eis que tudo se fez novo",
        "Recebe honrarias civis e cargos no Senado",
        "Fica livre de todo esforço moral",
        "Muda apenas de nacionalidade terrena",
        "facil", "2 Coríntios", "2 Coríntios 5:17", "A regeneração em Cristo opera uma transformação integral de natureza e destino.")
    add("Qual ministério glorioso Deus confiou aos Seus servos em 2 Coríntios 5:18-20?",
        "O ministério da reconciliação, como embaixadores em nome de Cristo",
        "O governo dos exércitos do mundo",
        "A condenação sumária dos ímpios",
        "O controle da economia dos povos",
        "facil", "2 Coríntios", "2 Coríntios 5:18-20", "Somos embaixadores rogando em nome de Cristo: 'Reconciliai-vos com Deus'.")
    add("Que tipo de contribuinte generoso Deus ama de acordo com 2 Coríntios 9:7?",
        "O que dá com alegria (não com tristeza nem por constrangimento)",
        "O que dá para se exibir perante as multidões",
        "O que guarda tudo em seu cofre particular",
        "O que dá somente quando obrigado pela lei civil",
        "facil", "2 Coríntios", "2 Coríntios 9:7", "'Cada um contribua segundo propôs no seu coração... porque Deus ama ao que dá com alegria'.")
    add("Qual resposta confortadora o Senhor deu a Paulo quando ele rogou três vezes para afastar o espinho na carne em 2 Coríntios 12:9?",
        "'A minha graça te basta, porque o meu poder se aperfeiçoa na fraqueza'",
        "'Tu serás punido com mais aflições'",
        "'Procura um médico em Alexandria'",
        "'Não tenho poder sobre a enfermidade'",
        "facil", "2 Coríntios", "2 Coríntios 12:9", "A suficiência da graça divina resplandece na aceitação da dependência humana.")

    # --- GÁLATAS ---
    add("Por que Paulo repreendeu tão duramente os gálatas no início de sua epístola?",
        "Porque estavam abandonando o evangelho da graça para seguir outro evangelho legalista baseado na circuncisão",
        "Porque não construíram um templo para a igreja",
        "Porque se recusaram a pagar impostos a Roma",
        "Porque não sabiam falar o idioma grego",
        "facil", "Gálatas", "Gálatas 1:6-9", "Paulo defendeu veementemente que a salvação é unicamente pela graça através da fé em Cristo.")
    add("Qual apóstolo de peso foi resistido face a face por Paulo em Antioquia por hipocrisia e dissimulação com os gentios?",
        "Pedro (Cefas)", "João", "André", "Mateus",
        "medio", "Gálatas", "Gálatas 2:11-14", "Paulo repreendeu Pedro publicamente por afastar-se da comunhão com os gentios por medo dos circuncidados.")
    add("Qual declaração emblemática de união com Cristo abre o coração de Paulo em Gálatas 2:20?",
        "'Já estou crucificado com Cristo; e vivo, não mais eu, mas Cristo vive em mim'",
        "'Eu sou o maior mestre da lei de Moisés'",
        "'A minha carne é santa e perfeita por si mesma'",
        "'Não preciso mais ter fé'",
        "facil", "Gálatas", "Gálatas 2:20", "A vida cristã consiste em ter o próprio Cristo vivendo através do crente pela fé.")
    add("Qual função pedagógica a lei mosaica desempenhou até a chegada do Messias segundo Gálatas 3:24?",
        "De aio (tutor ou condutor) para nos levar a Cristo, a fim de sermos justificados pela fé",
        "De código final de condenação irremediável",
        "De um livro secreto acessível apenas aos reis",
        "De manual de arquitetura cerimonial",
        "medio", "Gálatas", "Gálatas 3:24", "A lei apontava a santidade de Deus e a pecaminosidade do homem, conduzindo-nos ao Salvador.")
    add("Qual é o célebre Fruto do Espírito listado em Gálatas 5:22-23?",
        "Amor, alegria, paz, longanimidade, benignidade, bondade, fidelidade, mansidão e domínio próprio",
        "Riqueza, prestígio, força militar, eloquência e orgulho",
        "Sabedoria mundana, austeridade, jejum extremo e isolamento",
        "Vingança, ira, ciúme, discórdia e inveja",
        "facil", "Gálatas", "Gálatas 5:22-23", "As nove virtudes do fruto do Espírito refletem o caráter imaculado de Cristo gerado no crente.")
    add("Qual princípio de justiça moral e semeadura Paulo estabelece em Gálatas 6:7?",
        "'De Deus não se zomba; tudo o que o homem semear, isso também colherá'",
        "'A sorte governa todas as decisões'",
        "'Quem planta vento nunca sofre tempestade'",
        "'As ações humanas não geram consequências'",
        "facil", "Gálatas", "Gálatas 6:7-8", "Quem semeia na carne colhe corrupção; quem semeia no Espírito colhe a vida eterna.")

    # --- EFÉSIOS ---
    add("Segundo Efésios 2:8-9, como o homem é salvo da condenação do pecado?",
        "Pela graça, por meio da fé; e isto não vem de vós, é dom de Deus, não vem das obras para que ninguém se glorie",
        "Pelas esmolas dadas aos necessitados",
        "Pela linhagem genealógica nobre",
        "Pelo cumprimento exato de sacrifícios rituais",
        "facil", "Efésios", "Efésios 2:8-9", "A salvação é presente imerecido de Deus recebido exclusivamente pela fé em Cristo.")
    add("O que Cristo derrubou na Sua carne na cruz segundo Efésios 2:14, promovendo a união entre judeus e gentios?",
        "A parede de separação (a inimizade)", "Os muros de mármore de Roma", "As torres do palácio de Herodes", "Os diques do rio Jordão",
        "medio", "Efésios", "Efésios 2:14", "Cristo é a nossa paz, e de ambos os povos fez um só novo homem, derrubando a divisão.")
    add("Qual é o ministério quíntuplo que Cristo ressurreto concedeu para o aperfeiçoamento dos santos em Efésios 4:11?",
        "Apóstolos, profetas, evangelistas, pastores e mestres",
        "Reis, príncipes, governadores, cônsules e soldados",
        "Músicos, pintores, filósofos, retóricos e escultores",
        "Sacerdotes, levitas, escribas, fariseus e zelotes",
        "facil", "Efésios", "Efésios 4:11-12", "Os dons ministeriais visam edificar o corpo de Cristo até a maturidade espiritual.")
    add("Como Efésios 5:25 ordena aos maridos que tratem suas esposas?",
        "Amando suas mulheres como Cristo amou a igreja e a si mesmo se entregou por ela",
        "Dominando sobre elas com rigor inflexível",
        "Tratando-as com indiferença e silêncio",
        "Considerando-as inferiores em honra",
        "facil", "Efésios", "Efésios 5:25", "O amor conjugal bíblico reflete o sacrifício generoso e abnegado de Cristo pela Igreja.")
    add("Qual é a única arma ofensiva listada na Armadura de Deus em Efésios 6:17?",
        "A espada do Espírito, que é a palavra de Deus",
        "O arco de ferro da justiça",
        "A lança de bronze da retidão",
        "O dardo de fogo da vingança",
        "facil", "Efésios", "Efésios 6:17", "A Palavra de Deus é a viva e eficaz espada do Espírito contra as ciladas do maligno.")
    add("Quais são as peças defensivas da armadura descritas em Efésios 6:14-17?",
        "Cinto da verdade, couraça da justiça, calçados da prontidão do evangelho, escudo da fé e capacete da salvação",
        "Manto de ouro, coroa de pedras, sandálias de prata e anel de sinete",
        "Elmo de bronze, malha de ferro, escudo de madeira e botas de couro cru",
        "Túnica sacerdotal, estola, tiara e peitoral de doze gemas",
        "facil", "Efésios", "Efésios 6:14-17", "A armadura espiritual equipa o crente para resistir no dia mau e ficar inabalável.")

    # --- FILIPENSES ---
    add("Qual tema de profunda alegria e triunfo permeia a carta que Paulo escreveu mesmo aprisionado em Filipenses?",
        "Alegria no Senhor e regozijo contínuo",
        "Tristeza inconsolável e solidão",
        "Planos para vingança contra os carcereiros",
        "Desânimo perante a morte iminente",
        "facil", "Filipenses", "Filipenses 4:4", "Mesmo no cárcere romano, Paulo conclama: 'Alegrai-vos sempre no Senhor; outra vez digo: alegrai-vos!'.")
    add("Como Paulo expressa sua devoção incondicional a Cristo em Filipenses 1:21?",
        "'Porque para mim o viver é Cristo, e o morrer é ganho'",
        "'Para mim o viver é riqueza e poder'",
        "'Para mim a morte é o fim de tudo'",
        "'Para mim a glória humana é a maior meta'",
        "facil", "Filipenses", "Filipenses 1:21", "Toda a razão de existência de Paulo era Cristo, tornando a própria morte um lucro glorioso.")
    add("Como Filipenses 2:5-8 descreve o esvaziamento e humilhação de Cristo (a kenosis)?",
        "Sendo em forma de Deus, não teve por usurpação ser igual a Deus, mas aniquilou-se a si mesmo, tomando a forma de servo e sendo obediente até a morte de cruz",
        "Recusou vir à terra em corpo mortal",
        "Exigiu coroação imediata no trono de Roma",
        "Permaneceu distante da dor dos homens",
        "facil", "Filipenses", "Filipenses 2:5-8", "O exemplo supremo de humildade: o Criador do universo fez-se homem e servo humilde.")
    add("O que Deus concedeu a Jesus em resposta à Sua humilhação sacrificial em Filipenses 2:9-11?",
        "O Nome que está sobre todo nome, para que ao nome de Jesus se dobre todo joelho e toda língua confesse que Jesus Cristo é Senhor",
        "Apenas um título honorário em Israel",
        "Um reino terreno passageiro",
        "Uma estátua no panteão de Atenas",
        "facil", "Filipenses", "Filipenses 2:9-11", "Cristo foi soberanamente exaltado ao trono de glória universal.")
    add("Como Paulo considerava todos os seus privilégios passados de pedigree religioso perante a excelência de Cristo em Filipenses 3:8?",
        "Como refugo (esterco / lixo)", "Como tesouros intocáveis", "Como méritos salvadores", "Como a razão de sua santidade",
        "facil", "Filipenses", "Filipenses 3:8", "Paulo considerou tudo perda e escória para ganhar a Cristo e ser achado n'Ele.")
    add("Qual versículo de grande encorajamento em Filipenses 4:13 expressa a força que Cristo dá ao crente?",
        "'Tudo posso naquele que me fortalece'",
        "'Não há esperança sob o sol'",
        "'A força humana resolve todos os dilemas'",
        "'O destino é incerto'",
        "facil", "Filipenses", "Filipenses 4:13", "Em qualquer circunstância de fartura ou escassez, Cristo é a fonte inesgotável de capacitação.")
    add("Qual promessa generosa de provisão divina Paulo faz aos filipenses em Filipenses 4:19?",
        "'O meu Deus, segundo as suas riquezas, suprirá todas as vossas necessidades em glória, por Cristo Jesus'",
        "'A riqueza terrena será multiplicada dez vezes'",
        "'Nunca passareis por provações financeiras'",
        "'O imperador romano pagará vossas contas'",
        "facil", "Filipenses", "Filipenses 4:19", "Deus supre fielmente cada necessidade real de Seus filhos conforme Sua glória infinita.")

    # --- COLOSSENSES ---
    add("Qual declaração sobre a preeminência de Cristo na criação é feita em Colossenses 1:16?",
        "Porque nele foram criadas todas as coisas que há nos céus e na terra, visíveis e invisíveis... tudo foi criado por ele e para ele",
        "Cristo foi criado pelos anjos celestiais",
        "O universo surgiu por acaso sem intervenção divina",
        "Moisés foi o arquiteto da terra e dos céus",
        "facil", "Colossenses", "Colossenses 1:16", "Cristo é o Agente, o Sustentador e a Meta de toda a criação.")
    add("O que habita corporalmente em Cristo segundo Colossenses 2:9?",
        "Toda a plenitude da divindade", "Apenas a sabedoria humana", "Uma porção de espírito angelical", "O poder passageiro dos reis",
        "facil", "Colossenses", "Colossenses 2:9", "Em Cristo reside toda a essência e plenitude absoluta de Deus em forma corpórea.")
    add("O que o cristão deve buscar segundo a orientação prática de Colossenses 3:1-2?",
        "Pensar nas coisas que são de cima, onde Cristo está assentado à destra de Deus, e não nas que são da terra",
        "Buscar a aprovação dos políticos",
        "Acumular ouro e prata nas cidades",
        "Viver preocupado com vãs filosofias",
        "facil", "Colossenses", "Colossenses 3:1-2", "A mente regenerada alinha seus afetos e aspirações com os valores celestiais eternos.")

    # --- 1 E 2 TESSALONICENSES ---
    add("De que maneira o Senhor descerá dos céus no arrebatamento da Igreja segundo 1 Tessalonicenses 4:16-17?",
        "Com alarido, com voz de arcanjo e com a trombeta de Deus; e os mortos em Cristo ressuscitarão primeiro",
        "Em segredo sem ninguém saber",
        "Apenas espiritualmente nos corações",
        "Com exércitos de cavalos de fogo terrenos",
        "facil", "1 Tessalonicenses", "1 Tessalonicenses 4:16-17", "Os mortos em Cristo ressurgirão glorificados e os vivos serão arrebatados ao Seu encontro nos ares.")
    add("Qual é a tríplice ordem de conduta diária registrada em 1 Tessalonicenses 5:16-18?",
        "'Regozijai-vos sempre. Orai sem cessar. Em tudo dai graças'",
        "'Trabalhai sem parar, jejuai todos os dias, não faleis'",
        "'Chorai sem esperança, temei o futuro, fugi do mundo'",
        "'Buscai tesouros, defendei vossos direitos, vencei os ímpios'",
        "facil", "1 Tessalonicenses", "1 Tessalonicenses 5:16-18", "A alegria perene, a oração incessante e a gratidão irrestrita constituem a vontade de Deus.")
    add("O que o apóstolo Paulo adverte em 2 Tessalonicenses 3:10 sobre aqueles que se recusam a trabalhar?",
        "'Se alguém não quer trabalhar, também não coma'",
        "'Quem não trabalha deve receber esmola diária'",
        "'O ócio é a maior virtude da piedade'",
        "'Trabalhar é uma fraqueza dos homens'",
        "facil", "2 Tessalonicenses", "2 Tessalonicenses 3:10", "Paulo censurou o desleixo fanático e ordenou o trabalho digno e laborioso.")

    # --- 1 E 2 TIMÓTEO, TITO, FILEMOM ---
    add("O que 1 Timóteo 2:5 afirma sobre a mediação entre Deus e a humanidade?",
        "Há um só Deus e um só Mediador entre Deus e os homens, Jesus Cristo homem",
        "Há muitos mediadores nos céus e na terra",
        "Os anjos e santos do passado são co-mediadores",
        "Os sacerdotes terrenos são os mediadores infalíveis",
        "facil", "1 Timóteo", "1 Timóteo 2:5", "Jesus Cristo é o Mediador único, exclusivo e perfeito entre Deus e os seres humanos.")
    add("Qual é expressamente declarada em 1 Timóteo 6:10 como a raiz de todos os males?",
        "O amor ao dinheiro", "O próprio dinheiro em si", "O estudo teológico", "O trabalho árduo",
        "facil", "1 Timóteo", "1 Timóteo 6:10", "A cobiça e o apego desordenado às riquezas ('o amor ao dinheiro') geram incontáveis dores e desvios.")
    add("Quem eram a avó e a mãe piedosas de Timóteo, lembradas por Paulo pela sua fé não fingida?",
        "Lóide e Eunice", "Sara e Rebeca", "Débora e Jael", "Marta e Maria",
        "medio", "2 Timóteo", "2 Timóteo 1:5", "A fé sincera de Timóteo foi nutrida pelo testemunho exemplar de sua avó Lóide e mãe Eunice.")
    add("Qual afirmação clássica sobre a inspiração das Escrituras está gravada em 2 Timóteo 3:16?",
        "Toda a Escritura é divinamente inspirada e proveitosa para ensinar, redarguir, corrigir e instruir em justiça",
        "Apenas partes dos profetas possuem valor divino",
        "As escrituras foram criadas pela mente dos reis de Judá",
        "Apenas o Novo Testamento tem autoridade moral",
        "facil", "2 Timóteo", "2 Timóteo 3:16", "A Palavra de Deus é inspirada pelo sopro divino ('theopneustos') e plenamente autoritativa.")
    add("Qual foi o solene testamento de vitória proferido por Paulo no final de 2 Timóteo 4:7-8 prestes a ser martirizado?",
        "'Combati o bom combate, acabei a carreira, guardei a fé. Desde agora, a coroa da justiça me está guardada'",
        "'Fui derrotado pelos algozes de Roma'",
        "'Arrependo-me de ter pregado o evangelho'",
        "'Peço aos crentes que fujam de qualquer sacrifício'",
        "facil", "2 Timóteo", "2 Timóteo 4:7-8", "Paulo partiu com triunfante serenidade para receber a coroa incorruptível das mãos do Justo Juiz.")
    add("Em qual ilha Paulo deixou o pastor Tito para pôr em ordem o que faltava e constituir presbíteros nas igrejas?",
        "Creta", "Chipre", "Sicília", "Patmos",
        "medio", "Tito", "Tito 1:5", "Paulo comissionou Tito a ordenar lideranças fiéis nas cidades da ilha de Creta.")
    add("Quem era o escravo fugitivo convertido por Paulo na prisão a favor de quem o apóstolo escreveu a comovente carta a Filemom?",
        "Onésimo", "Tíquico", "Erasto", "Aristarco",
        "facil", "Filemom", "Filemom 1:10-16", "Onésimo, outrora inútil, voltou para Filemom não mais como escravo, mas como irmão amado.")

    # --- HEBREUS ---
    add("Como Deus outrora falou aos pais pelos profetas, e como falou nestes últimos dias segundo Hebreus 1:1-2?",
        "Pelo Filho, a quem constituiu herdeiro de tudo e por quem fez o mundo",
        "Apenas por meio de sonhos e charadas",
        "Pelos reis de Roma e da Babilônia",
        "Por meio do fogo do Sinai perpetuamente",
        "facil", "Hebreus", "Hebreus 1:1-2", "Cristo é a revelação culminante, perfeita e final do Pai à humanidade.")
    add("Em Hebreus capítulos 5 e 7, segundo qual ordem sacerdotal eterna Jesus foi constituído Sumo Sacerdote para sempre?",
        "Segundo a ordem de Melquisedeque", "Segundo a ordem de Arão", "Segundo a ordem dos levitas de Coré", "Segundo a ordem de Moisés",
        "medio", "Hebreus", "Hebreus 7:1-17", "O sacerdócio de Cristo é imutável e eterno, superior à ordem terrena e temporária de Arão.")
    add("Quantas vezes Jesus Cristo precisou oferecer o Seu sacrifício pelo pecado segundo Hebreus 9:26-28 e 10:12?",
        "Uma única vez para sempre", "Diariamente no altar", "Todos os anos no dia da Expiação", "Sete vezes em cada geração",
        "facil", "Hebreus", "Hebreus 10:12", "Diferente dos sacerdotes levitas, Cristo ofereceu um único sacrifício eterno e assentou-se à destra de Deus.")
    add("Qual é a definição bíblica de fé registrada em Hebreus 11:1?",
        "A fé é o firme fundamento das coisas que se esperam, e a prova das coisas que se não veem",
        "A fé é uma superstição humana passageira",
        "A fé é a crença cega em lendas antigas",
        "A fé é o conhecimento científico demonstrado",
        "facil", "Hebreus", "Hebreus 11:1", "A fé bíblica confere substância viva à esperança eterna e convicção sobre as realidades invisíveis.")
    add("Qual patriarca é celebrado em Hebreus 11:8 porque 'pela fé obedeceu, indo para um lugar que havia de receber por herança; e saiu sem saber para onde ia'?",
        "Abraão", "Jacó", "Noé", "Moisés",
        "facil", "Hebreus", "Hebreus 11:8", "Abraão creu na voz de Deus e partiu de Ur dos Caldeus confiando na promessa.")
    add("Em Hebreus 12:1-2, para quem os crentes devem olhar continuamente ao correr com perseverança a carreira proposta?",
        "Olhando para Jesus, o autor e consumador da fé",
        "Olhando para os erros dos irmãos",
        "Olhando para as riquezas dos gentios",
        "Olhando para as regras dos filósofos",
        "facil", "Hebreus", "Hebreus 12:2", "Jesus suportou a cruz pelo gozo que Lhe estava proposto, sendo nosso padrão e fortaleza.")
    add("Qual imutabilidade gloriosa de Cristo é proclamada em Hebreus 13:8?",
        "'Jesus Cristo é o mesmo ontem, e hoje, e eternamente'",
        "'Cristo muda conforme os séculos'",
        "'A verdade divina é adaptável aos costumes da época'",
        "'Jesus deixou de agir após a ascensão'",
        "facil", "Hebreus", "Hebreus 13:8", "A natureza, o amor e o poder de nosso Redentor permanecem inabaláveis para sempre.")

    # --- TIAGO ---
    add("Qual conselho prático Tiago 1:5 dá a qualquer um que sinta carência de sabedoria?",
        "Peça-a a Deus, que a todos dá liberalmente e nada lhes impropera; e ser-lhe-á dada",
        "Estude com os sofistas da Grécia",
        "Guarde silêncio e desespere-se",
        "Pague tributo aos sábios de Atenas",
        "facil", "Tiago", "Tiago 1:5", "Deus é fonte generosa e acolhedora de verdadeira sabedoria para quem pede com fé.")
    add("Qual é a regra áurea de comunicação interpessoal registrada em Tiago 1:19?",
        "Todo homem seja pronto para ouvir, tardio para falar, tardio para se irar",
        "Fale primeiro sem escutar ninguém",
        "Dê vazão rápida à cólera e à discórdia",
        "Nunca escute as necessidades dos humildes",
        "facil", "Tiago", "Tiago 1:19", "A prudência bíblica equilibra escuta atenta, contenção verbal e serenidade no espírito.")
    add("Como Tiago 1:22 adverte os leitores a respeito da Palavra de Deus?",
        "'Sede cumpridores da palavra e não somente ouvintes, enganando-vos com falsos discursos'",
        "'Basta ouvir passivamente aos sábados'",
        "'Apenas decorem os textos sem praticar'",
        "'Esqueçam a palavra após o sermão'",
        "facil", "Tiago", "Tiago 1:22", "Ouvir sem obedecer é enganar a si próprio; a verdadeira fé gera ação obediente.")
    add("Em Tiago 2, qual relação indissociável o autor estabelece entre fé e obras?",
        "A fé sem obras é morta em si mesma",
        "As obras substituem a necessidade de fé",
        "A fé não precisa se manifestar em conduta alguma",
        "Apenas os filósofos praticam a fé",
        "facil", "Tiago", "Tiago 2:17-26", "A fé salvadora autêntica é demonstrada inevitavelmente pelas obras de justiça e compaixão.")
    add("A que pequeno membro do corpo Tiago 3 compara o leme que governa um grande navio e a pequena faísca que incendeia uma vasta floresta?",
        "A língua", "O dedo mindinho", "O olho", "A orelha",
        "facil", "Tiago", "Tiago 3:4-6", "A língua, embora pequena, tem imenso poder destrutivo ou edificante conforme é governada.")
    add("Qual convite precioso de restauração íntima é feito em Tiago 4:8?",
        "'Chegai-vos a Deus, e ele se chegará a vós'",
        "'Afastai-vos de Deus para viver em liberdade'",
        "'Deus não acolhe os arrependidos'",
        "'A oração não tem eficácia perante Deus'",
        "facil", "Tiago", "Tiago 4:8", "Quando nos aproximamos de Deus com coração humilde e limpo, Ele prontamente Se chega a nós.")
    add("Quem é citado em Tiago 5:17 como homem sujeito às mesmas paixões que nós que orou com fervor e não choveu por três anos e meio?",
        "Elias", "Moisés", "Samuel", "Isaías",
        "facil", "Tiago", "Tiago 5:17-18", "A vida de oração de Elias prova o extraordinário poder da intercessão fervorosa do justo.")

    # --- 1 E 2 PEDRO ---
    add("Para qual herança incorruptível fomos regenerados segundo 1 Pedro 1:3-4?",
        "Uma herança incorruptível, incontaminada e que não se pode murchar, guardada nos céus para vós",
        "Uma propriedade física na Galileia",
        "Ouro e prata em depósitos imperiais",
        "Honra efêmera perante os reis",
        "facil", "1 Pedro", "1 Pedro 1:4", "A esperança viva do cristão está alicerçada na ressurreição de Cristo e guardada nos céus.")
    add("Com o que os crentes foram resgatados de sua vã maneira de viver segundo 1 Pedro 1:18-19?",
        "Não com coisas corruptíveis como prata ou ouro, mas com o precioso sangue de Cristo, como de um cordeiro sem defeito",
        "Com doações em moedas de prata no Templo",
        "Com obras de caridade pessoais",
        "Com sacrifícios de touros e bodes",
        "facil", "1 Pedro", "1 Pedro 1:18-19", "O preço do nosso resgate foi o incomparável sacrifício expiatório do Cordeiro imaculado.")
    add("Quais títulos nobres são conferidos aos crentes em 1 Pedro 2:9?",
        "Geração eleita, sacerdócio real, nação santa, povo adquirido para anunciar as virtudes daquele que vos chamou das trevas para a sua maravilhosa luz",
        "Comerciantes de renome e juízes da terra",
        "Povo destinado à derrota contínua",
        "Súditos passivos de governantes idólatras",
        "facil", "1 Pedro", "1 Pedro 2:9", "A Igreja constitui o sacerdócio régio de Deus encarregado de proclamar Suas virtudes ao mundo.")
    add("Qual exortação de prontidão e mansidão apologética é dada em 1 Pedro 3:15?",
        "Estai sempre preparados para responder com mansidão e temor a qualquer que vos pedir a razão da esperança que há em vós",
        "Combatei os opositores com espadas de ferro",
        "Recusai-vos a falar sobre vossa fé",
        "Impedei o diálogo com os que não creem",
        "facil", "1 Pedro", "1 Pedro 3:15", "O testemunho cristão deve aliar firmeza doutrinária com mansidão e reverência sincera.")
    add("O que o crente deve fazer com todas as suas inquietações e ansiedades segundo 1 Pedro 5:7?",
        "Lançando sobre ele toda a vossa ansiedade, porque ele tem cuidado de vós",
        "Guardar o fardo solitariamente no peito",
        "Buscar o esquecimento nos vícios do mundo",
        "Reclamar continuamente perante todos",
        "facil", "1 Pedro", "1 Pedro 5:7", "Deus cuida amorosamente de cada detalhe da vida daqueles que Lhe entregam seus temores.")
    add("Como o adversário (o diabo) é comparado em 1 Pedro 5:8 em seu rondar pelo mundo?",
        "Como leão que ruge, procurando a quem possa tragar",
        "Como uma serpente adormecida",
        "Como um pássaro sem asas",
        "Como uma sombra inofensiva",
        "facil", "1 Pedro", "1 Pedro 5:8", "A vigilância e sobriedade são vitais porque o inimigo atua vorazmente buscando destruir vidas.")
    add("Como os homens santos de Deus falaram as Escrituras segundo 2 Pedro 1:21?",
        "Movidos pelo Espírito Santo (e não por vontade humana alguma)",
        "Seguindo lendas fabulosas do paganismo",
        "Para agradar aos monarcas da época",
        "Por intuição puramente humana",
        "facil", "2 Pedro", "2 Pedro 1:21", "A profecia bíblica não emanou de mente humana, mas da inspiração do Espírito Santo.")
    add("Segundo 2 Pedro 3:9, por que o Senhor retarda a Sua promessa da segunda vinda?",
        "Porque é longânimo para convosco, não querendo que alguns se percam, senão que todos venham a arrepender-se",
        "Porque Se esqueceu do Seu povo",
        "Porque não possui poder para voltar",
        "Porque prefere abandonar a criação",
        "facil", "2 Pedro", "2 Pedro 3:9", "A paciência do Senhor é oportunidade redentora para que mais almas alcancem o arrependimento.")
    add("Em 2 Pedro 3:18, em que o crente é exortado a crescer continuamente?",
        "Na graça e no conhecimento de nosso Senhor e Salvador Jesus Cristo",
        "Na cobiça material e prestígio",
        "No orgulho de suas conquistas",
        "Na frieza espiritual perante as necessidades",
        "facil", "2 Pedro", "2 Pedro 3:18", "O chamado cristão é o contínuo e alegre amadurecimento na graça e no saber salvífico de Cristo.")

    # --- 1, 2 E 3 JOÃO ---
    add("Qual é a mensagem que ouvimos de Cristo e anunciamos segundo 1 João 1:5?",
        "Deus é luz, e não há nele treva nenhuma",
        "Deus habita nas trevas do caos",
        "Deus muda de parecer a cada dia",
        "Deus prefere as sombras do silêncio",
        "facil", "1 João", "1 João 1:5", "A santidade, verdade e pureza imaculadas de Deus são perfeitamente simbolizadas pela Luz.")
    add("O que o sangue de Jesus Cristo nos faz segundo a gloriosa certeza de 1 João 1:7?",
        "Nos purifica de todo pecado", "Apenas cobre os erros passados", "Não tem eficácia após o batismo", "Serve apenas como símbolo antigo",
        "facil", "1 João", "1 João 1:7", "Andar na luz da comunhão mútua assegura a purificação contínua e total pelo sangue do Salvador.")
    add("O que acontece quando confessamos os nossos pecados de acordo com 1 João 1:9?",
        "Ele é fiel e justo para nos perdoar os pecados e nos purificar de toda a injustiça",
        "Somos rejeitados sumariamente",
        "Recebemos castigo eterno sem remissão",
        "Temos de pagar tributos monetários",
        "facil", "1 João", "1 João 1:9", "A fidelidade de Deus e a justiça satisfeita na cruz garantem o perdão pleno ao coração arrependido.")
    add("Quem é nosso Advogado junto ao Pai quando pecamos segundo 1 João 2:1?",
        "Jesus Cristo, o Justo", "O profeta Moisés", "O arcanjo Miguel", "O apóstolo Pedro",
        "facil", "1 João", "1 João 2:1", "Cristo intercede perpetuamente como nosso Justo Advogado diante do tribunal do Pai.")
    add("Qual tríplice concupiscência do mundo Paulo/João nos adverte a não amar em 1 João 2:15-16?",
        "A concupiscência da carne, a concupiscência dos olhos e a soberba da vida",
        "A fome, a sede e o sono",
        "O estudo, a oração e o cântico",
        "O trabalho, a família e a amizade",
        "facil", "1 João", "1 João 2:16", "Os desejos passageiros e o orgulho terreno passam, mas quem faz a vontade de Deus permanece para sempre.")
    add("Qual declaração fundamental sobre a própria natureza de Deus é repetida em 1 João 4:8 e 4:16?",
        "'Deus é amor'", "'Deus é solidão'", "'Deus é severidade sem misericórdia'", "'Deus é mistério inatingível'",
        "facil", "1 João", "1 João 4:8, 16", "A essência íntima de Deus é amor puro, sacrificial, eterno e redentor.")
    add("O que o verdadeiro e perfeito amor faz com o medo de acordo com 1 João 4:18?",
        "Lança fora todo o medo", "Aumenta o terror do castigo", "Paralisa a alma do homem", "Gera insegurança espiritual",
        "facil", "1 João", "1 João 4:18", "No amor não há temor; o amor consumado em Cristo traz perfeita paz e acolhimento.")
    add("Qual é a vitória que vence o mundo segundo 1 João 5:4?",
        "A nossa fé", "A força militar dos homens", "A eloquência dos oradores", "O poder dos impérios terrestres",
        "facil", "1 João", "1 João 5:4", "'E esta é a vitória que vence o mundo: a nossa fé' no Filho de Deus ressurreto.")
    add("A quem a Segunda Epístola de João foi endereçada no seu versículo inicial?",
        "À senhora eleita e aos seus filhos", "A Timóteo em Éfeso", "À igreja de Jerusalém", "Aos soldados de Roma",
        "medio", "2 João", "2 João 1:1", "João escreveu sua segunda carta à irmã na fé denominada carinhosamente 'a senhora eleita'.")
    add("A quem a Terceira Epístola de João foi dedicada pelo apóstolo amado?",
        "Ao amado Gaio, a quem amava na verdade", "A Nicodemos", "A Filemom", "A Zaqueu",
        "medio", "3 João", "3 João 1:1", "João escreveu ao fiel cooperador Gaio, regozijando-se em sua fidelidade e hospitalidade.")
    add("Qual líder dominador e soberbo foi reprovado por João em 3 João 1:9 por gostar de ter a primazia entre eles?",
        "Diótrefes", "Demétrio", "Himeneu", "Alexandre",
        "medio", "3 João", "3 João 1:9-10", "Diótrefes amava o primeiro lugar, recusava receber os irmãos e proferia palavras maliciosas.")

    # --- JUDAS ---
    add("Por que Judas sentiu urgente necessidade de escrever sua breve carta aos crentes?",
        "Para exortá-los a batalhar diligentemente pela fé que uma vez foi entregue aos santos",
        "Para recolher donativos para Corinto",
        "Para planejar uma viagem missionária à Espanha",
        "Para ensinar matemática aos jovens",
        "facil", "Judas", "Judas 1:3", "Judas advertiu a igreja sobre a infiltração de falsos mestres que distorciam a graça em libertinagem.")
    add("Qual arcanjo disputou o corpo de Moisés com o diabo sem proferir juízo infamatório segundo Judas 1:9?",
        "Miguel", "Gabriel", "Rafael", "Uriel",
        "facil", "Judas", "Judas 1:9", "O arcanjo Miguel disse com autoridade e temor santo: 'O Senhor te repreenda!'.")
    add("Qual patriarca da sétima geração depois de Adão profetizou sobre a vinda do Senhor com miríades de santos em Judas 1:14?",
        "Enoque", "Matusalém", "Lameque", "Noé",
        "medio", "Judas", "Judas 1:14-15", "Enoque profetizou sobre o juízo final do Senhor sobre todos os ímpios.")
    add("Qual doxologia gloriosa encerra a epístola de Judas (versículos 24-25)?",
        "'Ora, àquele que é poderoso para vos guardar de tropeçar e apresentar-vos irrepreensíveis com alegria... ao único Deus sábio... seja glória e majestade'",
        "'Que as trevas cubram a terra até o fim'",
        "'Adeus irmãos, que a sorte vos proteja'",
        "'Nada mais temos a proclamar'",
        "facil", "Judas", "Judas 1:24-25", "Uma das mais sublimes doxologias de toda a Bíblia exaltando o poder protetor e a glória de Deus.")

    # Let's add more questions for Acts and Epistles to reach exactly 140 questions!
    # (Currently items count is around 75. Let's add 65 more high-quality questions!)

    add("O que os discípulos perguntaram a Jesus pouco antes de Sua ascensão em Atos 1:6?",
        "'Senhor, restaurarás tu neste tempo o reino a Israel?'", "'Quem será o primeiro nos céus?'", "'Devemos destruir os romanos?'", "'Quando morreremos?'",
        "medio", "Atos", "Atos 1:6-7", "Jesus respondeu que não lhes competia saber os tempos ou as épocas que o Pai reservou.")
    add("Segundo Atos 1:8, o que os discípulos receberiam e onde seriam testemunhas?",
        "Receberiam poder ao descer o Espírito Santo e seriam testemunhas em Jerusalém, Judeia, Samaria e até aos confins da terra",
        "Receberiam ouro para comprar armas para libertar a Judeia",
        "Receberiam coroas terrenas em Roma e na Grécia",
        "Receberiam o comando político do templo",
        "facil", "Atos", "Atos 1:8", "Atos 1:8 é o mapa temático de expansão do evangelho pelo poder do Espírito Santo.")
    add("Quais eram as quatro marcas essenciais de perseverança da igreja primitiva descritas em Atos 2:42?",
        "Doutrina dos apóstolos, comunhão, partir do pão e orações",
        "Jejuns forçados, guerras santas, isolamento e oferendas",
        "Festas com vinho, debates políticos, comércio e leis civis",
        "Debates com o Sinédrio, filosofia grega, astrologia e esgrima",
        "facil", "Atos", "Atos 2:42", "A igreja perseverava na comunhão fraternal, na sã doutrina e na constante oração.")
    add("Qual era o apelido de José, levita natural de Chipre, que vendeu um campo e depositou o dinheiro aos pés dos apóstolos?",
        "Barnabé (Filho da Consolação)", "Silas", "Tito", "Matias",
        "facil", "Atos", "Atos 4:36-37", "Barnabé destacou-se pelo seu coração generoso e consolador na igreja nascente.")
    add("Qual foi a corajosa resposta de Pedro e dos apóstolos ao Sinédrio quando proibidos de pregar em Atos 5:29?",
        "'Mais importa obedecer a Deus do que aos homens'",
        "'Obedeceremos aos sacerdotes sem hesitar'",
        "'Fugiremos para o Egito em silêncio'",
        "'Negociaremos a nossa mensagem'",
        "facil", "Atos", "Atos 5:29", "A lealdade suprema a Deus prevalece incondicionalmente sobre qualquer decreto humano opressor.")
    add("Qual dos sete diáconos de Atos 6 tinha filhas virgens que profetizavam quando Paulo visitou Cesareia?",
        "Filipe", "Estêvão", "Prócoro", "Timão",
        "medio", "Atos", "Atos 21:8-9", "Filipe, que havia sido um dos sete, tinha quatro filhas que profetizavam.")
    add("O que o eunuco etíope estava lendo em sua carruagem quando Filipe se aproximou dele no deserto?",
        "O profeta Isaías (capítulo 53)", "O livro de Levítico", "O livro dos Salmos", "O livro dos Provérbios",
        "facil", "Atos", "Atos 8:30-35", "Ele lia a passagem do Servo Sofredor levado como cordeiro ao matadouro.")
    add("O que Saulo ouviu de Jesus na visão gloriosa na estrada de Damasco?",
        "'Saulo, Saulo, por que me persegues? Dura coisa te é recalcitrar contra os aguilhões'",
        "'Saulo, volta imediatamente para Tarso'",
        "'Saulo, compra oferendas no templo de Jerusalém'",
        "'Saulo, não temas os romanos'",
        "facil", "Atos", "Atos 9:4-5; 26:14", "Perseguir a Igreja de Cristo é atacar o próprio Senhor Jesus.")
    add("Qual paralítico acamado por oito anos em Lida foi curado por Pedro com as palavras 'Jesus Cristo te dá saúde'?",
        "Enéias", "Bartimeu", "Públio", "Malco",
        "medio", "Atos", "Atos 9:33-34", "Pedro disse a Enéias: 'Jesus Cristo te dá saúde; levanta-te e faze a tua cama', e logo se levantou.")
    add("Qual visão Pedro teve no eirado em Jope para aprender que não devia chamar impuro ao que Deus purificou?",
        "Um grande lençol descendo do céu contendo toda espécie de animais de quatro patas e répteis",
        "Uma estrela brilhante guiando magos",
        "Uma espada de fogo dividindo os povos",
        "Um templo de ouro descendo sobre a praia",
        "facil", "Atos", "Atos 10:9-16", "A visão do lençol revelou a inclusão dos gentios no plano salvífico de Deus.")
    add("Qual líder apostólico acolheu Saulo em Jerusalém quando todos os discípulos tinham medo dele após sua conversão?",
        "Barnabé", "Tomé", "Mateus", "Tiago menor",
        "facil", "Atos", "Atos 9:26-27", "Barnabé tomou Saulo consigo, levou-o aos apóstolos e testificou de sua genuína conversão.")
    add("O que aconteceu com Herodes Agripa I em Cesareia quando aceitou ser aclamado como deus pelo povo?",
        "Foi ferido por um anjo do Senhor, comido de vermes e expirou",
        "Foi coroado imperador em Roma",
        "Fugiu em um navio para a Pérsia",
        "Converteu-se e tornou-se pastor",
        "medio", "Atos", "Atos 12:21-23", "Por não dar a glória devida a Deus, Herodes foi julgado sumariamente.")
    add("Em qual cidade Paulo e Barnabé foram aclamados como 'Mercúrio e Júpiter' pelo povo idólatra após curarem um coxo?",
        "Listra", "Derbe", "Atenas", "Éfeso",
        "medio", "Atos", "Atos 14:11-13", "Em Listra, o povo quis sacrificar-lhes touros, mas eles rasgaram as vestes e pregaram o Deus vivo.")
    add("Quem redigiu a carta apostólica enviada às igrejas gentílicas após o Concílio de Jerusalém?",
        "Tiago e os apóstolos e anciãos de Jerusalém", "Paulo e Silas sozinhos", "O governador da Judeia", "O imperador romano",
        "medio", "Atos", "Atos 15:22-29", "Tiago liderou a conclusão conciliadora, enviando Judas e Silas com Paulo e Barnabé.")
    add("Qual jovem companheiro de Paulo em Filipos foi açoitado e encarcerado junto com ele?",
        "Silas", "Tito", "Barnabé", "Apolo",
        "facil", "Atos", "Atos 16:19-23", "Silas acompanhava Paulo na segunda viagem missionária e cantou louvores no cárcere.")
    add("Qual governador romano da Judeia ouviu Paulo falar de justiça, domínio próprio e do juízo vindouro e ficou atemorizado?",
        "Félix", "Pôncio Pilatos", "Herodes o Grande", "Gálio",
        "medio", "Atos", "Atos 24:24-25", "O governador Félix tremia ao ouvir o apóstolo Paulo arrazoar sobre a santidade e o juízo divino.")
    add("Qual governador romano sucedeu a Félix e enviou Paulo a Roma após o apóstolo apelar a César?",
        "Pórcio Festo", "Quirinio", "Sérgio Paulo", "Cláudio Lísias",
        "medio", "Atos", "Atos 25:11-12", "Festo declarou: 'Apelaste para César? Para César irás'.")
    add("Qual rei judeu declarou a Paulo durante seu interrogatório em Cesareia: 'Por pouco me não persuades a fazer-me cristão'?",
        "Rei Agripa II", "Rei Herodes Antipas", "Rei Salomão", "Rei Saul",
        "medio", "Atos", "Atos 26:28", "Agripa ouviu comovido a defesa apaixonada do apóstolo Paulo sobre o cumprimento dos profetas.")
    add("Quem era o centurião romano bondoso que escoltou Paulo com humanidade na viagem marítima rumo a Roma?",
        "Júlio", "Cornélio", "Lísias", "Longino",
        "dificil", "Atos", "Atos 27:1-3", "O centurião Júlio, da corte Augusta, tratou Paulo com grande consideração e amizade.")
    add("O que Paulo fez durante os dois anos em que permaneceu preso em sua casa alugada em Roma no final de Atos?",
        "Pregava o Reino de Deus e ensinava com toda liberdade acerca do Senhor Jesus a todos que o procuravam",
        "Recusou visitas e permaneceu em silêncio",
        "Escreveu petições políticas para o Senado",
        "Tentou fugir pelas muralhas de Roma",
        "facil", "Atos", "Atos 28:30-31", "Mesmo sob custódia, o Evangelho não estava algemado e Paulo ensinava com ousadia incontestável.")

    # More Epistles
    add("Segundo Romanos 4:25, Jesus foi entregue por causa de que e ressuscitou para que?",
        "Entregue por causa das nossas transgressões e ressuscitado para nossa justificação",
        "Entregue por engano e ressuscitado para se vingar",
        "Entregue pela inveja romana e ressuscitado para fundar um império",
        "Entregue pelos discípulos e ressuscitado para morar no deserto",
        "facil", "Romanos", "Romanos 4:25", "A morte de Jesus expiou nossos pecados e Sua ressurreição selou nossa plena justificação.")
    add("O que o apóstolo Paulo declara em Romanos 8:31 sobre a proteção incondicional de Deus?",
        "'Se Deus é por nós, quem será contra nós?'",
        "'Se os homens nos apoiarem, seremos imbatíveis'",
        "'As riquezas nos protegem de qualquer dano'",
        "'Não há força que supere os soldados romanos'",
        "facil", "Romanos", "Romanos 8:31", "A fidelidade soberana de Deus é o escudo invencível de Seus eleitos.")
    add("Quem pode nos separar do amor de Cristo segundo a solene proclamação de Romanos 8:38-39?",
        "Nem a morte, nem a vida, nem anjos, nem principados, nem coisas presentes, nem futuras, nem qualquer criatura",
        "A pobreza extrema e a solidão",
        "As calúnias dos falsos irmãos",
        "A passagem implacável dos séculos",
        "facil", "Romanos", "Romanos 8:38-39", "Absolutamente nada no cosmos pode romper o vínculo eterno do amor de Deus em Cristo.")
    add("Qual é o dever cívico do cristão perante as autoridades governamentais instituídas segundo Romanos 13:1-7?",
        "Estar sujeito a elas, pagar tributos e impostos, prestando honra a quem honra cabe",
        "Rebelar-se violentamente contra qualquer autoridade",
        "Recusar pagar qualquer tributo",
        "Ignorar as leis civis da cidade",
        "facil", "Romanos", "Romanos 13:1-7", "As autoridades civis foram instituídas para manutenção da ordem e devem ser respeitadas.")
    add("Segundo Romanos 13:10, qual é o pleno cumprimento da lei divina?",
        "O amor", "O jejum", "O sacrifício no altar", "A sabedoria filosófica",
        "facil", "Romanos", "Romanos 13:10", "'O amor não faz mal ao próximo; de sorte que o cumprimento da lei é o amor'.")
    add("Qual instrução Paulo dá em Romanos 14:1 a respeito daqueles que são débeis na fé?",
        "Acolhei-o, mas não para discutir opiniões",
        "Expulsai-o imediatamente da igreja",
        "Zombai de seus escrúpulos alimentares",
        "Obrigai-o a comer o que ele recusa",
        "medio", "Romanos", "Romanos 14:1-3", "A tolerância fraternal e a edificação mútua devem reger o convívio na igreja.")
    add("Em 1 Coríntios 2:9, como Paulo descreve as maravilhas que Deus preparou para os Seus servos?",
        "'As coisas que o olho não viu, e o ouvido não ouviu, e não subiram ao coração do homem, são as que Deus preparou para os que o amam'",
        "'São palácios de marfim e montanhas de ouro'",
        "'São exércitos que subjugarão os ímpios'",
        "'São mistérios que nunca serão desfrutados'",
        "facil", "1 Coríntios", "1 Coríntios 2:9", "A recompensa e a comunhão eterna superam toda imaginação humana.")
    add("Qual aviso solene sobre más companhias Paulo cita em 1 Coríntios 15:33?",
        "'Não vos enganeis: as más conversações corrompem os bons costumes'",
        "'Toda amizade gera virtudes eternas'",
        "'Os costumes nunca são alterados pelo ambiente'",
        "'Não importa com quem convivemos'",
        "facil", "1 Coríntios", "1 Coríntios 15:33", "A contaminação moral por companhias perniciosas destrói os hábitos piedosos.")
    add("Qual mandamento prático fecha 1 Coríntios 16:14?",
        "'Todas as vossas coisas sejam feitas com amor'",
        "'Tudo seja feito para vosso próprio proveito'",
        "'Tudo seja decidido pela espada'",
        "'Buscai sempre a primazia humana'",
        "facil", "1 Coríntios", "1 Coríntios 16:14", "O amor deve ser o alicerce e a motivação indispensável de toda atividade da igreja.")
    add("Segundo 2 Coríntios 3:17, o que há onde está o Espírito do Senhor?",
        "Liberdade", "Escravidão", "Terror", "Julgamento implacável",
        "facil", "2 Coríntios", "2 Coríntios 3:17", "'Ora, o Senhor é o Espírito; e onde está o Espírito do Senhor aí há liberdade'.")
    add("Segundo 2 Coríntios 5:7, como é a caminhada diária do cristão?",
        "'Andamos por fé e não por vista'",
        "'Andamos por sinais materiais'",
        "'Andamos pelas opiniões dos homens'",
        "'Andamos pelo medo da condenação'",
        "facil", "2 Coríntios", "2 Coríntios 5:7", "A peregrinação cristã transcende aparências físicas, apoiando-se na fidelidade invisível de Deus.")
    add("Qual apelo Paulo faz em 2 Coríntios 6:14 sobre alianças perigosas?",
        "'Não vos ponhais em jugo desigual com os incrédulos'",
        "'Unam-se aos pagãos nos seus cultos'",
        "'Façam acordos idólatras para enriquecer'",
        "'Abandonem a igreja para viver como o mundo'",
        "facil", "2 Coríntios", "2 Coríntios 6:14", "Não pode haver consórcio entre a justiça e a injustiça, nem comunhão entre luz e trevas.")
    add("Qual era o propósito do sofrimento de Paulo no episódio do 'espinho na carne' em 2 Coríntios 12:7?",
        "Para que não se exaltasse com a grandeza das revelações",
        "Para puni-lo por crimes antigos",
        "Para impedir que viajasse de barco",
        "Para tirar sua fé em Cristo",
        "facil", "2 Coríntios", "2 Coríntios 12:7", "A fraqueza física preservou o apóstolo da soberba espiritual diante de visões celestiais.")
    add("Qual é a célebre bênção apostólica trinitária registrada em 2 Coríntios 13:13?",
        "'A graça do Senhor Jesus Cristo, o amor de Deus e a comunhão do Espírito Santo sejam com todos vós'",
        "'A paz de Salomão e a sabedoria dos reis'",
        "'A espada da guerra e a vitória sobre os ímpios'",
        "'A honra dos apóstolos e o poder de Roma'",
        "facil", "2 Coríntios", "2 Coríntios 13:13", "A clássica fórmula de bênção trinitária encerra com doçura a segunda epístola aos Coríntios.")
    add("Qual é a antítese entre a escrava Agar e a livre Sara alegoricamente explicada em Gálatas 4?",
        "Agar representa o pacto da lei do Sinai que gera escravidão, e Sara representa a Jerusalém celeste que é livre e mãe de todos nós",
        "Agar representa a fé e Sara a caridade",
        "Agar representa Roma e Sara Jerusalém terrena",
        "Agar é a rainha do sul e Sara a profetisa",
        "medio", "Gálatas", "Gálatas 4:21-31", "Somos filhos da promessa e da graça (como Isaque), não da escravidão das obras legais.")
    add("Em Gálatas 5:1, para que Cristo verdadeiramente nos libertou?",
        "Para a liberdade; estai, pois, firmes e não vos submetais outra vez ao jugo da servidão",
        "Para o pecado sem freio moral",
        "Para a preguiça espiritual",
        "Para a solidão no deserto",
        "facil", "Gálatas", "Gálatas 5:1", "A liberdade cristã não é licença para pecar, mas emancipação da condenação e do pecado.")
    add("O que Paulo afirma sobre gloriar-se em Gálatas 6:14?",
        "'Longe esteja de mim gloriar-me, a não ser na cruz de nosso Senhor Jesus Cristo'",
        "'Glorio-me na minha sabedoria farisaica'",
        "'Glorio-me no número de crentes que batizei'",
        "'Glorio-me nos aplausos das multidões'",
        "facil", "Gálatas", "Gálatas 6:14", "A cruz do Calvário é o único e legítimo motivo de triunfo e exaltação do apóstolo.")
    add("Qual é o plano eterno do mistério da vontade de Deus revelado em Efésios 1:9-10?",
        "De fazer convergir em Cristo todas as coisas, tanto as que estão nos céus como as que estão na terra",
        "De salvar apenas os nobres de Jerusalém",
        "De destruir o universo físico para sempre",
        "De coroar os governantes com ouro",
        "medio", "Efésios", "Efésios 1:10", "A reconciliação cósmica e a liderança de todas as coisas culminam no Senhorio de Cristo.")
    add("Como a Igreja é descrita em Efésios 1:22-23 em relação a Cristo?",
        "Como o Seu corpo, a plenitude daquele que a tudo enche em todas as coisas",
        "Como uma associação civil passageira",
        "Como um clube de debates filosóficos",
        "Como um grupo de místicos sem cabeça",
        "facil", "Efésios", "Efésios 1:22-23", "Cristo é o Cabeça supremo e a Igreja é o Seu Corpo vivo e plenificado.")
    add("Como estávamos espiritualmente antes de Deus nos vivificar pela graça em Cristo segundo Efésios 2:1?",
        "Mortos em ofensas e pecados", "Apenas enfermos ligeiramente", "Plenamente justos e puros", "Livres da culpa",
        "facil", "Efésios", "Efésios 2:1-5", "Estávamos espiritualmente mortos, mas Deus, riquíssimo em misericórdia, nos deu vida juntamente com Cristo.")
    add("Para que fomos criados em Cristo Jesus de acordo com Efésios 2:10?",
        "Para as boas obras, as quais Deus preparou para que andássemos nelas",
        "Para o descanso ocioso permanente",
        "Para conquistar honras terrenas",
        "Para viver conforme os nossos próprios caprichos",
        "facil", "Efésios", "Efésios 2:10", "Não somos salvos pelas obras, mas salvos para praticar as boas obras planejadas por Deus.")
    add("Como Paulo expressa a grandiosidade do poder de Deus atuando em nós em Efésios 3:20?",
        "Deus é poderoso para fazer infinitamente mais do que tudo quanto pedimos ou pensamos",
        "Deus só faz o que a nossa mente pequena pode imaginar",
        "Deus depende da aprovação humana para intervir",
        "Deus age raramente no coração dos homens",
        "facil", "Efésios", "Efésios 3:20", "A soberania generosa de Deus ultrapassa infinitamente as nossas mais ousadas súplicas e ideias.")
    add("Como Paulo roga aos crentes que andem na vocação com que foram chamados em Efésios 4:1-3?",
        "Com toda humildade e mansidão, com longanimidade, suportando-vos uns aos outros em amor, procurando guardar a unidade do Espírito",
        "Com arrogância intelectual sobre os ignorantes",
        "Competindo pelos cargos mais elevados",
        "Evitando o contato com os irmãos fracos",
        "facil", "Efésios", "Efésios 4:1-3", "A harmonia e a preservação da unidade na Igreja exigem humildade sincera e afeto paciente.")
    add("O que o crente deve fazer com a ira antes de o sol se pôr segundo Efésios 4:26-27?",
        "'Não se ponha o sol sobre a vossa ira; não deis lugar ao diabo'",
        "'Alimentai a mágoa por semanas inteiras'",
        "'Procurei vingança contra quem vos ofendeu'",
        "'Guardai o rancor no mais íntimo do peito'",
        "facil", "Efésios", "Efésios 4:26-27", "A resolução imediata do ressentimento fecha as brechas espirituais para o adversário.")
    add("Em Filipenses 4:6-7, qual é o antídoto bíblico contra a ansiedade?",
        "Não andar ansiosos por coisa alguma, antes em tudo sejam conhecidas as vossas petições pela oração, súplica e ação de graças",
        "Preocupar-se dia e noite com o futuro",
        "Ignorar a realidade com passatempos mundanos",
        "Desesperar-se diante de qualquer imprevisto",
        "facil", "Filipenses", "Filipenses 4:6-7", "A oração com ações de graças descarrega a alma e traz a indescritível paz de Deus.")
    add("Em Filipenses 4:8, em que coisas o crente deve pensar continuamente?",
        "Em tudo o que é verdadeiro, honesto, justo, puro, amável, de boa fama, em virtude e louvor",
        "Em derrotas passadas e escândalos",
        "Em como se vingar dos inimigos",
        "Em futilidades e boatos mundanos",
        "facil", "Filipenses", "Filipenses 4:8", "A mente piedosa deve ser nutrida e blindada com pensamentos nobres, puros e virtuosos.")
    add("Qual é a esperança gloriosa descrita em Colossenses 1:27 para os gentios?",
        "'Cristo em vós, a esperança da glória'",
        "'O enriquecimento financeiro na Galácia'",
        "'A conquista de cidades romanas'",
        "'A sabedoria dos filósofos de Atenas'",
        "facil", "Colossenses", "Colossenses 1:27", "O clímax do mistério do evangelho é a presença viva e real de Cristo habitando no coração do crente.")
    add("Como a palavra de Cristo deve habitar em nós segundo Colossenses 3:16?",
        "Habitar ricamente, ensinando-vos e admoestando-vos com salmos, hinos e cânticos espirituais",
        "Habitar apenas como memória apagada",
        "Ficar guardada apenas em pergaminhos selados",
        "Ser ouvida raramente uma vez ao ano",
        "facil", "Colossenses", "Colossenses 3:16", "A Palavra deve permear todos os aspectos da comunhão, louvor e instrução mútua.")
    add("O que Paulo instrui em Colossenses 4:6 sobre o falar cristão perante os de fora?",
        "'A vossa palavra seja sempre agradável, temperada com sal, para que saibais como vos convém responder a cada um'",
        "'A vossa palavra seja áspera e condenatória'",
        "'Não faleis com ninguém fora da igreja'",
        "'Enganai os pagãos para vencê-los'",
        "facil", "Colossenses", "Colossenses 4:6", "A fala do discípulo deve combinar graça acolhedora, sensatez e sabedoria cativante.")
    add("Como o Dia do Senhor virá sobre aqueles que vivem descuidados no pecado segundo 1 Tessalonicenses 5:2-3?",
        "Como o ladrão de noite, trazendo repentina destruição",
        "Com aviso prévio de muitos anos",
        "Apenas quando todos os homens concordarem",
        "Nunca virá de surpresa",
        "facil", "1 Tessalonicenses", "1 Tessalonicenses 5:2-3", "A vinda repentina do Senhor exige constante sobriedade e vigilância espiritual.")
    add("Como Paulo expressa sua oração de santificação total pelos crentes em 1 Tessalonicenses 5:23?",
        "'O mesmo Deus de paz vos santifique em tudo; e todo o vosso espírito, e alma, e corpo sejam conservados irrepreensíveis para a vinda de nosso Senhor'",
        "'Que vossa vida permaneça intocada por santidade'",
        "'Que apenas vossa mente seja guardada'",
        "'Que vossos corpos se percam nas fraquezas'",
        "facil", "1 Tessalonicenses", "1 Tessalonicenses 5:23", "A santificação operada por Deus alcança a totalidade integral do ser humano: espírito, alma e corpo.")
    add("Qual homem da iniquidade e do pecado será revelado antes do Dia do Senhor segundo 2 Tessalonicenses 2:3-4?",
        "O homem do pecado, o filho da perdição, que se opõe e se levanta contra tudo o que se chama Deus",
        "O rei de Tiro ressuscitado",
        "Um imperador persa do passado",
        "Um falso filósofo ateniense",
        "medio", "2 Tessalonicenses", "2 Tessalonicenses 2:3-4", "Paulo profetiza sobre a manifestação escatológica do anticristo que se assentará no templo querendo ser Deus.")
    add("O que 1 Timóteo 4:12 aconselha ao jovem obreiro Timóteo quanto à sua mocidade?",
        "'Ninguém despreze a tua mocidade; mas sê o exemplo dos fiéis, na palavra, no trato, no amor, no espírito, na fé, na pureza'",
        "'Usa de soberba para impor tua autoridade'",
        "'Esconde tua juventude com roupas de ancião'",
        "'Evita liderar antes de ter sessenta anos'",
        "facil", "1 Timóteo", "1 Timóteo 4:12", "O testemunho ilibado em conduta e amor valida o ministério de qualquer líder jovem.")
    add("O que Paulo declara em 1 Timóteo 6:6 sobre a piedade acompanhada de contentamento?",
        "É grande fonte de lucro", "É uma fraqueza humana", "É algo dispensável aos crentes", "É sinal de conformismo perigoso",
        "facil", "1 Timóteo", "1 Timóteo 6:6", "O verdadeiro contentamento espiritual liberta o coração das garras da ganância consumista.")
    add("O que Deus não nos deu segundo 2 Timóteo 1:7, e o que nos deu em troca?",
        "Não nos deu espírito de covardia (temor), mas de fortaleza, de amor e de moderação (domínio próprio)",
        "Nos deu espírito de dúvida e hesitação",
        "Nos deu medo contínuo perante as perseguições",
        "Nos deu vaidade para humilhar os opositores",
        "facil", "2 Timóteo", "2 Timóteo 1:7", "O Espírito concede coragem sobrenatural, afeição profunda e mente equilibrada nas tribulações.")
    add("Com quais três metáforas de dedicação Paulo incentiva Timóteo a perseverar em 2 Timóteo 2:3-6?",
        "Um soldado que não se embaraça com negócios civis, um atleta que luta segundo as regras e um lavrador diligente",
        "Um marinheiro, um arquiteto e um escultor",
        "Um rei, um general e um mercador de escravos",
        "Um escriba, um juiz e um cobrador de impostos",
        "medio", "2 Timóteo", "2 Timóteo 2:3-6", "O ministério exige a disciplina militar, a lealdade às regras do atleta e o suor incansável do agricultor.")
    add("O que Tito 2:11-12 afirma sobre o efeito da manifestação da graça salvadora de Deus?",
        "Ensina-nos a renunciar à impiedade e às paixões mundanas, para vivermos sensata, justa e piedosamente neste presente século",
        "Permite que vivamos em pecado sem preocupação",
        "Isenta o homem de qualquer esforço moral",
        "Muda apenas a nossa posição religiosa",
        "facil", "Tito", "Tito 2:11-12", "A graça verdadeira não tolera a licença moral, mas educa o redimido a viver em santidade sóbria.")
    add("Qual é o bendito objeto da bendita esperança da Igreja descrito em Tito 2:13?",
        "A manifestação da glória do nosso grande Deus e Salvador Jesus Cristo",
        "O estabelecimento de uma teocracia política terrena",
        "O acúmulo de riqueza nas cidades gentílicas",
        "A vitória militar sobre os impérios vizinhos",
        "facil", "Tito", "Tito 2:13", "Aguardamos ansiosamente o glorioso regresso de nosso grande Deus e Salvador Jesus Cristo.")
    add("Qual razão Paulo apresenta a Filemom para perdoar e receber Onésimo em Filemom 1:15-16?",
        "Para que o tivesse para sempre, não já como escravo, mas mais do que escravo, como irmão amado",
        "Para que Onésimo pagasse suas dívidas com trabalho forçado",
        "Para agradar aos governantes de Colossos",
        "Para obter lucro financeiro em Roma",
        "facil", "Filemom", "Filemom 1:15-16", "O Evangelho transcende as barreiras de escravidão social, transformando servos em irmãos amados na fé.")
    add("O que Hebreus 4:12 afirma sobre a Palavra de Deus?",
        "É viva e eficaz, e mais penetrante do que qualquer espada de dois gumes, e penetra até à divisão da alma e do espírito... e é apta para discernir os pensamentos do coração",
        "É um texto de filosofia humana sujeito a erros",
        "É uma coletânea antiga sem poder atual",
        "É um código secreto apenas para sacerdotes",
        "facil", "Hebreus", "Hebreus 4:12", "A Palavra de Deus perscruta o íntimo mais recôndito dos motivos e intenções humanas.")
    add("Como o trono de Deus é chamado em Hebreus 4:16 ao convidar os crentes a se aproximarem com confiança?",
        "Trono da graça, para alcançarmos misericórdia e acharmos graça a fim de sermos ajudados em tempo oportuno",
        "Trono de pavor e condenação inflexível",
        "Trono inacessível guardado por espadas em chamas",
        "Trono de mistério distante dos homens",
        "facil", "Hebreus", "Hebreus 4:16", "Por intermédio de Jesus nosso Sumo Sacerdote, achegamo-nos ao trono com santa intrepidez e confiança filial.")
    add("Por que o sacrifício de Jesus é infinitamente superior aos sacrifícios do Antigo Testamento segundo Hebreus 9:11-14?",
        "Porque Cristo entrou no Santo dos Santos celestial com o Seu próprio sangue, obtendo uma eterna redenção",
        "Porque foi celebrado no templo de Herodes com ouro",
        "Porque foi aprovado pelos sacerdotes de Roma",
        "Porque repetiu o ritual de Arão ano após ano",
        "facil", "Hebreus", "Hebreus 9:12", "O sangue de animais não podia extirpar o pecado; Cristo realizou uma redenção perfeita e eterna.")
    add("O que Noé fez 'pela fé, divinamente avisado das coisas que ainda não se viam' de acordo com Hebreus 11:7?",
        "Temeu e, para salvação da sua família, preparou a arca, pela qual condenou o mundo e foi feito herdeiro da justiça",
        "Construiu um palácio de mármore",
        "Fugiu para o cume das montanhas solitárias",
        "Negou a mensagem de juízo divina",
        "facil", "Hebreus", "Hebreus 11:7", "A fé de Noé moveu-o à obediência prática antes de ver qualquer gota de chuva cair.")
    add("Qual escolha Moisés fez pela fé segundo Hebreus 11:24-26?",
        "Recusou ser chamado filho da filha de Faraó, escolhendo antes ser maltratado com o povo de Deus do que desfrutar dos prazeres transitórios do pecado",
        "Preferiu as riquezas de Mênfis à liberdade do povo",
        "Aliou-se aos sacerdotes pagãos do Nilo",
        "Fugiu para governar as tribos de Midiã como rei",
        "facil", "Hebreus", "Hebreus 11:24-26", "Moisés estimou o opróbrio de Cristo como maior riqueza do que todos os tesouros do Egito.")
    add("Como o crente deve encarar a disciplina e correção do Senhor segundo Hebreus 12:6?",
        "O Senhor corrige a quem ama e açoita a todo filho a quem recebe",
        "Como prova de abandono e ódio de Deus",
        "Como um acidente cego da natureza",
        "Como injustiça contra a sua inocência",
        "facil", "Hebreus", "Hebreus 12:6", "A disciplina paternal de Deus visa o nosso aperfeiçoamento em santidade e frutos de justiça.")
    add("Qual advertência prática sobre a hospitalidade é dada em Hebreus 13:2?",
        "Não vos esqueçais da hospitalidade, porque por ela alguns, sem o saberem, hospedaram anjos",
        "Nunca recebam peregrinos em vossas casas",
        "Hospedem apenas os parentes ricos e ilustres",
        "Fechem as portas para qualquer estranho necessitado",
        "facil", "Hebreus", "Hebreus 13:2", "Abraão e Ló acolheram mensageiros divinos ao praticarem a generosa hospitalidade.")
    add("Como a oração fervorosa do justo é descrita em Tiago 5:16?",
        "Muito pode em sua eficácia (pode muito em seus efeitos)",
        "É inútil contra os decretos do destino",
        "Só tem poder se feita em voz alta no templo",
        "Depende de ofertas monetárias vultosas",
        "facil", "Tiago", "Tiago 5:16", "A oração sincera e reta diante de Deus move os céus com tremendo poder transformador.")
    add("Qual esperança viva Pedro proclama em 1 Pedro 1:3 ter sido gerada por Deus mediante o que?",
        "Pela ressurreição de Jesus Cristo dentre os mortos",
        "Pelas vitórias militares de Israel",
        "Pela sabedoria dos filósofos antigos",
        "Pela posse perpétua da terra prometida",
        "facil", "1 Pedro", "1 Pedro 1:3", "A ressurreição corpórea de Cristo é a âncora viva da esperança eterna do redimido.")
    add("Como os esposos devem tratar suas esposas de acordo com o ensino prático de 1 Pedro 3:7?",
        "Com discernimento, dando honra à mulher como vaso mais frágil e co-herdeira da graça da vida, para que não se interrompam as vossas orações",
        "Com severidade para manter o domínio",
        "Como inferiores na comunhão espiritual",
        "Sem considerar seus sentimentos e opiniões",
        "facil", "1 Pedro", "1 Pedro 3:7", "O respeito afetuoso e honra conjugal são requisitos para que as orações do lar não sejam bloqueadas.")
    add("O que o amor cobre segundo a instrução de 1 Pedro 4:8?",
        "Uma multidão de pecados", "Apenas pequenas faltas", "Nenhum erro do próximo", "A soberba dos injustos",
        "facil", "1 Pedro", "1 Pedro 4:8", "'Tende ardente amor uns para com os outros; porque o amor cobrirá a multidão de pecados'.")
    add("Qual advertência Pedro faz em 2 Pedro 2:1 a respeito de perigos internos nas igrejas?",
        "Haverá entre vós falsos mestres, que introduzirão encobertamente heresias destruidoras",
        "A igreja nunca enfrentará enganos internos",
        "Todos os ensinadores serão perfeitos",
        "Os pagãos governarão as congregações",
        "facil", "2 Pedro", "2 Pedro 2:1", "A vigilância doutrinária protege o rebanho das mentiras sutis de ensinos perniciosos.")
    add("O que o apóstolo Pedro diz em 2 Pedro 3:8 sobre a contagem do tempo para o Senhor?",
        "Um dia para o Senhor é como mil anos, e mil anos como um dia",
        "Deus mede o tempo como os relógios humanos",
        "O tempo tem o mesmo peso para o Criador e para a criatura",
        "Deus está sujeito aos limites dos anos terrenos",
        "facil", "2 Pedro", "2 Pedro 3:8", "A eternidade de Deus transcende a cronologia humana com absoluta soberania.")
    add("Como João descreve a comunhão dos santos que andam na luz em 1 João 1:7?",
        "Temos comunhão uns com os outros, e o sangue de Jesus Cristo, seu Filho, nos purifica de todo pecado",
        "Vivemos isolados sem necessidade dos irmãos",
        "Temos de esconder nossas faltas nas sombras",
        "Dependemos de rituais mágicos anuais",
        "facil", "1 João", "1 João 1:7", "Andar na luz divina produz comunhão genuína e contínua purificação pelo sacrifício de Cristo.")
    add("Qual é o novo mandamento de que João fala em 1 João 2:7-11 e no seu Evangelho?",
        "Que vos ameis uns aos outros assim como Cristo nos amou",
        "Que guardeis a circuncisão física",
        "Que façais peregrinações a cidades antigas",
        "Que condeneis todos os que erram",
        "facil", "1 João", "1 João 2:7-11; João 13:34", "O amor sacrificial mútuo é a marca identificadora inequívoca dos verdadeiros discípulos de Jesus.")
    add("Qual é o testemunho que temos em nós mesmos segundo 1 João 5:11-12?",
        "Deus nos deu a vida eterna; e esta vida está em seu Filho. Quem tem o Filho tem a vida; quem não tem o Filho de Deus não tem a vida",
        "Que nossas boas obras compram a nossa redenção",
        "Que a salvação depende de títulos acadêmicos",
        "Que todos serão salvos mesmo sem Cristo",
        "facil", "1 João", "1 João 5:11-12", "A posse da vida eterna está inseparavelmente vinculada ao acolhimento de Cristo pela fé.")
    add("Por que João preferiu não escrever com pena e tinta em 2 João 1:12 e 3 João 1:13?",
        "Porque esperava visitá-los em breve e falar boca a boca, para que a alegria fosse completa",
        "Porque ficou sem pergaminho",
        "Porque a lei romana proibia cartas",
        "Porque não tinha nada mais a dizer",
        "medio", "2 João", "2 João 1:12; 3 João 1:13-14", "O calor da comunhão pessoal face a face supera a frieza de manuscritos à distância.")
    add("Quem era o cristão de excelente testemunho mencionado em 3 João 1:12 elogiado por todos e pela própria verdade?",
        "Demétrio", "Diótrefes", "Gaio", "Onésimo",
        "medio", "3 João", "3 João 1:12", "Demétrio tinha o testemunho favorável de toda a igreja, de João e da própria verdade encarnada.")

    return items[:140]

if __name__ == "__main__":
    q_list = get_epistles_questions()
    print(f"Epistles generated: {len(q_list)} questions")
