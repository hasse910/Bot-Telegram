import telepot
from Chatbot import Chatbot

telegram = telepot.Bot("1204740512:AAHMY2lSMhEK-oY9_2-7PM18803olpLMpoE")
bot = Chatbot ("Hasse9Bot")

def recebendoMsg(msg):
	frase = msg['text']
	for palavra in ('Bot','start'):
		if palavra in frase:
			if 'Bot' in frase:
				frase = frase[4:]
			frase = bot.escuta(frase)
			resp = bot.pensa(frase)
			bot.fala(resp)
			tipoMsg, tipoChat, chatID = telepot.glance(msg)
			telegram.sendMessage(chatID, resp)

telegram.message_loop(recebendoMsg)

while True:
	pass
