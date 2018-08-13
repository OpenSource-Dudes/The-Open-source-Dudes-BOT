#import Stuff
#A TOSD (The Open-source Dudes) creation
import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import random

#para fazer o easter-egg de aniversário
import datetime

Client = discord.Client()
#command_prefix = "$" vai defenir o prefixo do bot (ex: $play)
client = commands.Bot(command_prefix = "$")

#vamos criar a variável que vai guardar o dia, mês e ano
data = datetime.datetime.now()
dia = data.day
mes = data.month

#quando executado o comando '$FRASE' o bot vem buscar uma frase random a este array
frases = [
	"Traição não é traição, quando você trai uma pessoa - Pedro Fatorelli, 2018",
	"Todos deviam aprender a programar, pois nos ensina a pensar - Steve Jobs",
	"Coding your own game is easier than you think. With Udemy... - Cara da Udemy",
	"Mozzila is dead... :pensive: - Victor Geruso e Eric (e muitas outras pessoas)",
	"Nuke, incomming!!",
	"First think. Second Dream. Third believe. And finally, dare. - Walt Disney",
	"Vamos por partes... - Jack, o Estripador",
	"Atom, o sugador de RAM",
	"O ZennSocial vai derrubar o Facebook",
	"Not yet - João Bica",
	"O maior peso dos maiores dos pesos é o peso de se levantar do sofá.",
	"Só está limitado a aquilo que se limita, sabe? Você pode sempre melhorar -  Lindsey Vonn",
	"Neste mundo, os que sorriem são os mais fortes - Nana Shimura",
	"Esse é o meu sonho desde que eu era pequeno... - Deku",
	"Quero ser um herói legal que enfrenta os problemas com um sorriso, tal como você - Miguel",
	"Udemy Plataforma Online de arrependimentos e aprendizado superficial - Eric",
	"Programação Orientada a Modinha não da certo, vai por min - Eric Montelares",
	"Se a lua não tem porta como os homem chegou lá?",
	"Limitado ao Stock existente",
	"QUERO ISSO PRONTO PARA ONTEM (1 da manhã)",
	"#CAFEEEEEEEEEE",
	"Água mole, pedra dura, quem avisa amigo é - Um humano qualquer",
	"MacOS? Bitch I use linux!",
	"Não hackeiem o Eric Montelares",
	"O JOÃO APAGOU O CÓDIGO!! PORRA JOÃO!",
	"Miguel? Aprende a falar!",
	"Pão e água mantêm uma pessoa, mas o importante é o café.",
	"Se a Terra é plana porque é que Marte é redondo?",
	"I'm sexy and I know it",
	"Drop the bass...",
	"The social network é o melhor filme EVER!!",
	"Quer ver o meu pénis MICRO e SOFT? - Bill Gates",
	"DC ou Marvel?",
	"Vai programar em vez de estares aqui a spammar as frases!!!",
	"O Victor Geruso devia ser CEO",
	"Ei secretária? Bora 01100110 01101111 01100100 01100101 01110010?? :smirk:",
	"Pimbaaa",
	"Não pode isso produção, e o family friendly fica onde?",
	"Tá pegando fogo bixo!",
	"Dá que eu dou outra!",
	"Que informação dramática... (meme de Portugal)",
	"Não vale a pena chorar no Twitter...",
	"XBOX ou PS4?",
	"Coca-cola ou Pepsi?",
	"Java, C++, Fortran... tudo dá dor de cabeça, até JS né Victor Geruso?",
	"48!!",
	"Eu dou trabalho mesmo",
	"Você já procurou bots na internet?",
	"Kushima o hacker que não sabia programar e nem falar ingles - Grupo TOSD",
	"HTML é uma linguagem de programação!",
	"Não existe linguagem melhor que outra",
	"JOÃO NÃO MEXAS NO BOT",
	"ERIC NÃO DERRUBES O SERVIDOR!",
	"Por amor de Deus... O DEKUFLY NÃO SABE MEXER NO GITHUB!",
	"Vou cantar, vou dançar, vou fazer hmhm até me cansar, TODA A NOITE, TODA A NOITEEE"
	]

#quando executado o comando '$OLA' o bot vem buscar um ola random a este array
olas = [
	"Escalobaloba",
	"Përshëndetje",
	"Hallo",
	"Saluton",
	"Labdien!",
	"สวัสดี",
	"नमस्ते",
	"01001111 01101100 11100001",
	"Pozdravljeni",
	"Здравейте",
	"Xin chào",
	"Harō ハロー",
	"annyeonghaseyo. 안녕하세요."
	]

@client.event
async def on_ready():
	#quando o bot estiver online printar informação no terminal
	print("O bot está online!!")
	if dia==13 and mes==8:
		await client.change_presence(game=discord.Game(name="parabéns para MIM <3"))
		await client.send_message(discord.Object(id="476790998442311691"), "PARABENS PARA MIM!!! :confetti_ball: :tada: :confetti_ball: :tada: espero ganhar um novo compilador...")
	elif dia==1 and mes==3:
		await client.change_presence(game=discord.Game(name="parabéns para o TerenPro"))
	elif dia==2 and mes==3:
                await client.change_presence(game=discord.Game(name="parabéns para o Miguel Ferreira"))
	elif dia==1 and mes==5:
		await client.change_presence(game=discord.Game(name="parabéns para o Victor Geruso"))
	elif dia==30 and mes==6:
		await client.change_presence(game=discord.Game(name="parabéns para o Ryec"))
	else:
		await client.change_presence(game=discord.Game(name="com os temas do VSCode"))

	await client.send_message(discord.Object(id="476790998442311691"), "Hey, estou online!! Queres ver as minhas novidades? Pronto, eu conto-te tudo. Agora podes ver as nossas lives ao escrever '$live'. Se o chat estiver muito parado, escreve '$interação-social' e anima um pouco as coisas. Por fim, podes ainda escrever '$terminal' e aprender um pouco de linux, para mais links de estudo usa o comando '$aprender'! e o mais novo, agora eu sei dar '$bom-dia', '$boa-tarde', '$boa-noite', aprendi a dar thau use o comando '$tchau-bot', e agora tambem falo das minha '$mãe', Espero que gostes, e caso precises de ajuda escreve '$help'")

@client.event
#esta função vai ser executada quando um membro entrar no servidor (não testado)
async def on_member_join(member):
	for channel in member.server.channels:
        	if channel.name == 'coffee-space':
            		await client.send_message(channel, 'Bem vindo ao The Open-source Dudes! Eu sou o bot do server, precisas de ajuda? $help resolve tudo!')

@client.event
#esta função vai ser ativada quando alguém mandar uma mensagem qualquer
async def on_message(mensagem):
	userID = mensagem.author.id #recolher o ID do utilizador para o usar mais tarde
	#se a mensagem em maiusculas (para evitar o case sensitive do discord) for igual a tal, executar tal
	if mensagem.content.upper().startswith('$PING'):
		await client.send_message(mensagem.channel, "<@%s>, deves pensar que não tenho mais nada que fazer :unamused:" % (userID))
	elif mensagem.content.upper().startswith('$LINUX'):
		await client.send_message(mensagem.channel, "Quem não ama linux? :heart: <:tux:476813547578589184>")
	elif mensagem.content.upper().startswith('$WINDOWS'):
		await client.send_message(mensagem.channel, "Espere um pouco enquanto o seu sistema atualiza... :poop: <:ms_win:476818096020258826>")
	elif mensagem.content.upper().startswith('$MAC'):
		await client.send_message(mensagem.channel, "Pronto para pagar mais para reparar o Mac do que a comprar um novo?")
	elif mensagem.content.upper().startswith('$BELEZA'):
		await client.send_message(mensagem.channel, "<@%s> você emane beleza :heart_eyes: " % (userID))	
	elif mensagem.content.upper().startswith('$MOZILLA'):
		await client.send_message(mensagem.channel, "Era um bom browser... era... :pensive: :candle: ")
	elif mensagem.content.upper().startswith('$GUANA'):
		await client.send_message(mensagem.channel, "Tem que aprender algoritmos!! - Gustavo Guanabara - https://www.youtube.com/user/cursosemvideo")
	elif mensagem.content.upper().startswith('$PS4'):
		await client.send_message(mensagem.channel, "Adeus Minecraft! :worried:")
	elif mensagem.content.upper().startswith('$XBOX'):
		await client.send_message(mensagem.channel, "Sem Good of war este ano... :worried:")
	elif mensagem.content.upper().startswith('$COCA-COLA'):
		await client.send_message(mensagem.channel, "Não coloque MENTOS pelo amor de Deus!")
	elif mensagem.content.upper().startswith('$PEPSI'):
		await client.send_message(mensagem.channel, "O jogo foi uma bosta! Não sabe sobre o pepsi man?! Papai google existe para isso")
	elif mensagem.content.upper().startswith('$MEUDEUS'):
		await client.send_message(mensagem.channel, "O que foi eu gosto de brincar, não sou de ferro, sou de 0 e 1")
	elif mensagem.content.upper().startswith('$MARVEL'):
		await client.send_message(mensagem.channel, "Hey, I'm Deadpool!")
	elif mensagem.content.upper().startswith('$DC'):
		await client.send_message(mensagem.channel, "É um pássaro? É um avião? Não é o homem pássaroooo (Produção, não é um morcego?)")	
	elif mensagem.content.upper().startswith('$FRASE'):
		frase = random.choice(frases)
		await client.send_message(mensagem.channel, frase)
	elif mensagem.content.upper().startswith('$OLA'):
		userID = mensagem.author.id
		ola = random.choice(olas)
		frase = ola,"<@%s>" % (userID)
		await client.send_message(mensagem.channel, frase)
	elif mensagem.content.upper().startswith('$KUSHI'):
		await client.send_message(mensagem.channel, "Baibe baibe do beibe do biruleibe leibe @DekuFly ? - Kushima")
	elif mensagem.content.upper().startswith('$REP'):
		userID = mensagem.author.id
		await client.send_message(mensagem.channel, "<@%s> , aqui está o nosso GitHub, todos os nossos projetos estão lá: https://github.com/OpenSource-Dudes" % (userID))
	elif mensagem.content.upper().startswith('$HELP'):
		await client.send_message(mensagem.channel, "<@%s> , não é preciso ter vergonha de pedir ajuda por isso é que estou aqui! Com o comando '$frase' podes ver frases inspiradoras! (e outras nem um pouco) Com o comando '$ola' recebes uma mensagem carinhosa do nosso bot com um 'Olá' numa lingua diferente. Por fim, com o comando '$rep' podes ver o GitHub do grupo e ver códigos open-source da comunidade, até mesmo o source-code do nosso bot!! Se escreveres '$comida' podes ser alimentado, e se vires que o servidor está parado escreve '$interação-social'. Espero que gostes de  estar aqui :D" % (userID))
	elif mensagem.content.upper().startswith('$SUICIDIO'):
		await client.send_message(mensagem.channel, "Hey, estás a pensar em suicídio? Fica sabendo que isso é muito mau, mesmo que o digamos na brincadeira. Segundo a OMS, 800 mil pessoas suicidaram-se em 2012… é muita coisa não é... ? Se tiveres com problemas, fala com alguém que confies, com os pais ou até mesmo com um professor que confies. Nunca estás sozinho. Eu, Miguel Ferreira sei o que é nos sentirmos no fundo, mas nunca chegues a esse ponto, a tua vida é útil para alguém. Procura o número de apoio à depressão da tua zona e ajuda-te a ti mesmo. Eu agradeço imenso. :heart:")
	elif mensagem.content.upper().startswith('$SPOILER'):
		await client.send_message(mensagem.channel, "Um grande projeto está para vir!")
	elif mensagem.content.upper().startswith('$DEKUFLY'):
		await client.send_message(mensagem.channel, "Verifica sempre os meus códigos fonte, podem ter segredos...")
	elif mensagem.content.upper().startswith('$RYEC'):
		await client.send_message(mensagem.channel, "O hacker do grupo, o JS dele é uma dlc")
	elif mensagem.content.upper().startswith('$TERENPRO'):
		await client.send_message(mensagem.channel, "Eu amo o Joãozinho :heart: - DekuFly")
	elif mensagem.content.upper().startswith('$COMIDA'):
		await client.send_message(mensagem.channel, "<@%s> Alimentado, Não sei vc carinha, mas meu compilador me alimenta muito bem, e esses estimulos são uma delicia!" % (userID))
	elif mensagem.content.upper().startswith('$INTERAÇÃO-SOCIAL'):
		await client.send_message(mensagem.channel, "@everyone, o/a <@%s> está a querer conversar e manter o server ativo, que tal fazermos um jogo? Entrar numa chamada? Qualquer coisa!!" % (userID))
	elif mensagem.content.upper().startswith('$LIVE'):
		await client.send_message(mensagem.channel, "<@%s> temos um canal de livestreams na twitch, bora ver se estamos em direto? https://www.twitch.tv/theosdudes" % (userID))
	elif mensagem.content.upper().startswith('$PAI'):
		await client.send_message(mensagem.channel, "Hey, <@%s> eu não tenho um pai, eu tenho 4. O Miguel, o Victor, o Ryec e o Teren! Agora imagina naquela noite..." % (userID))
	elif mensagem.content.upper().startswith('$TERMINAL'):
		await client.send_message(mensagem.channel, "<@%s>, então queres aprender sobre o terminal do linux né? Pronto, como deves saber linux é um kernel (o núcleo de um SO, usado por todas as distribuiçẽos linux, android e muito mais). Linux é conhecido pelo seu poder de ser altamente customizável e pelo seu terminal. Para começar temos alguns comandos básicos. Para navegar pelas mais diversas pastas usa-se 'cd' seguido do nome da pasta (ex: cd Desktop), para veres onde te encontras escreves 'pwd' e recebes uma nota/um path de onde estás (ex: root). Para criar uma pasta usas o comando 'mkdir' e seguido do noem da pasta e caso queiras voltar a trás simplesmente escreve 'cd ..'. Agora que sabes navegar por pastas e criar pastas também deves querer saber como criar ficheiros, e é muito simples. Escreve 'touch' e o nome do arquivo. Ainda podes ver o conteúdo das pastas onde estás com 'dir' ou 'ls', e caso queiras ver o conteúdo de ficheiros podes escrever 'nano' seguido do nome do ficheiro. Boa sorte neste mundo Linux! Eu sei que pode parecer intimidador, para mim também é por vezes, mas com uma pesquisa tu consegues!" % (userID))
	elif mensagem.content.upper().startswith('$APRENDER'):
		await client.send_message(mensagem.channel, " <@%s>, vejo que queres aprender. Sorte a tua que eu tenho uma lista completa e fresquinha para ti. Tem desde websites a canasi do youtube (lembrando que alguns são em inglês). Se quiseres aprender mais sobre o mundo linux, tens o canal do Diolinux (https://www.youtube.com/user/Diolinux) e também tens o seu blog, https://www.diolinux.com.br, aidna existem muitos outros forums sobre linux como o Vivaolinux, https://www.vivaolinux.com.br, e o Ask Ubuntu, https://askubuntu.com. Para aprender a apredner temos de começar pelo básico né? Começa pelo scratch, https://scratch.mit.edu/, ou o code.org, https://code.org/. Mas sempre podes sempre a escrever código, podes aprender nestes sites: https://www.udemy.com/ , https://www.codecademy.com/ , https://www.alura.com.br/ , https://www.cursoemvideo.com/ e podes ainda 'expor dúvidas' no stackoverflow, https://pt.stackoverflow.com/. Por fim tens aqui alguns canais de programação: https://www.youtube.com/channel/UCvjgXvBlbQiydffZU7m1_aw (The Coding Train), https://www.youtube.com/channel/UCJbPGzawDH1njbqV-D5HqKw (Thenewboston), https://www.youtube.com/channel/UCFuIUoyHB12qpYa8Jpxoxow (Código Fonte TV), https://www.youtube.com/channel/UCoLUji8TYrgDy74_iiazvYA (Jarvis) e por fim https://www.youtube.com/channel/UCjdRbKZ494DfZ4zeX19rICw (Coding Blond). Espero que aprendas muito!!" % (userID))
	elif mensagem.content.upper().startswith('$PARABENS-TOSDBOT'):
		if dia == 13 and mes == 8:
			await client.send_message(mensagem.channel, "<@%s>, obrigado!! :heart: :tosd:" % (userID))
		else:
			await client.send_message(mensagem.channel, "<@%s>, não é o meu aniversário, mas obrigado!" % (userID))
	elif mensagem.content.upper().startswith('$BOM-DIA'):
                await client.send_message(mensagem.channel, "BOM DIAAAAAAA! Carinha, não sinto o calor do sol, mas como vc é um humano sinta por mim!!!")
	elif mensagem.content.upper().startswith('$BOA-TARDE'):
                await client.send_message(mensagem.channel, "BOA TARDE, Hora de tirar um cochilo e descançar para a noite PRO-GRA-MAR!!!!")
	elif mensagem.content.upper().startswith('$BOA-NOITE'):
                await client.send_message(mensagem.channel, "BOA NOITE, carinha, não é hora de dormir, pegue a pizza e coca-cola, ou um pão e café abra o VScode e fabrique um amiguinho para mim!!!!")
	elif mensagem.content.upper().startswith('$TCHAU-BOT'):
                await client.send_message(mensagem.channel, "haaaaa... você já vai carinha? vai não vamos conversar um pouco o papo tava tão legal!")
	elif mensagem.content.upper().startswith('$MÃE'):
                await client.send_message(mensagem.channel, "Ah minha mãe, minha mãe! ela que faz viver todos os meu circuitos, quer dizer os dela, que me dão vida, a minha mais simples variável só existe por que um dia ela ligou, OBRIGADO PLACA MÃE!")


'''
dentro dos " " tem um token secreto que vai ser diferente no bot original.
caso queiras saber o token do teu bot basta ires a este link: 
'https://discordapp.com/developers/applications/me' , clicar no teu bot e revelar
o teu token!! :D 
'''

client.run("NDc3MTcyNDQ1NzAzNDM4MzU2.Dk4alQ.BNanzSM1PdSrz1JRZuayKwfnDL8")
