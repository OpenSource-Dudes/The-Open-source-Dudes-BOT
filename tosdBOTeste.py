#import Stuff
#A TOSD (The Open-source Dudes) creation
import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import random

Client = discord.Client()
#command_prefix = "$" vai defenir o prefixo do bot (ex: $play)
client = commands.Bot(command_prefix = "$")

#quando executado o comando '$FRASE' o bot vem buscar uma frase random a este array
frases = [
	"Traição não é traição, quando você trai uma pessoa - Pedro Fatorelli, 2018",
	"Todos deviam aprender a programar, pois nos ensina a pensar - Steve Jobs",
	"Coding your own game is easier than you think. With Udemy... - Cara da Udemy",
	"Mozzila is dead... :pensive: - Vitor e Eric (e muitas outras pessoas)",
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
	"Quero ser um herói legal que enfrenta os problemas com um sorriso, tal como você - Deku",
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
	"DekuFly? Aprende a falar!",
	"Pão e água mantêm uma pessoa, mas o importante é o café.",
	"Se a Terra é plana porque é que Marte é redondo?",
	"I'm sexy and I know it",
	"Drop the bass...",
	"The social network é o melhor filme EVER!!",
	"Quer ver o meu pénis MICRO e SOFT? - Bill Gates",
	"DC ou Marvel?",
	"Vai programar em vez de estares aqui a spammar as frases!!!",
	"O Vitor devia ser CEO",
	"Ei secretária? Bora 01100110 01101111 01100100 01100101 01110010?? :smirk:",
	"Pimbaaa",
	"Não pode isso produção, e o family friendly fica onde?",
	"Tá pegando fogo bixo!",
	"Dá que eu dou outra!",
	"Que informação dramática... (meme de Portugal)",
	"Não vale a pena chorar no Twitter...",
	"XBOX ou PS4?",
	"Coca-cola ou Pepsi?",
	"Java, C++, Fortran... tudo dá dor de cabeça, até JS né Vitor?",
	"48!!",
	"Você já procurou bots na internet?",
	"Kushima o hacker que não sabia programar e nem falar ingles - Grupo TOSD",
	"HTML é uma linguagem de programação!",
	"Não existe linguagem melhor que outra",
	"JOÃO NÃO MEXAS NO BOT",
	"ERIC NÃO DERRUBES O SERVIDOR!",
	"Por amor de Deus... O DEKUFLY NÃO SABE MEXER NO GITHUB!"
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
	await client.change_presence(game=discord.Game(name="com o tema do VSCODE"))

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
		await client.send_message(mensagem.channel, "<@%s> , não é preciso ter vergonha de pedir ajuda por isso é que estou aqui! Com o comando '$frase' podes ver frases inspiradoras! (e outras nem um pouco) Com o comando '$ola' recebes uma mensagem carinhosa do nosso bot com um 'Olá' numa lingua diferente. Por fim, com o comando '$rep' podes ver o GitHub do grupo e ver códigos open-source da comunidade, até mesmo o source-code do nosso bot!!" % (userID))
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

'''
dentro dos " " tem um token secreto que vai ser diferente no bot original.
caso queiras saber o token do teu bot basta ires a este link: 
'https://discordapp.com/developers/applications/me' , clicar no teu bot e revelar
o teu token!! :D 
'''

client.run("Seu token aqui!")
