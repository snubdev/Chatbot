from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from spacy.cli import download

download("en_core_web_sm")

class ENGSM:
  ISO_639_1 = 'en_core_web_sm'


bot = ChatBot(
    'Atendente', tagger_language=ENGSM,
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    database_uri='sqlite:///database.sqlite3'
)

conversa = ListTrainer(bot)

print()
print('-' * 30)
print('[- CHATBOT -]')
print('-' * 30)
print()

user = str(input('Infome seu nome: '))

conversa.train([
    'Oi',
    'Oi! Seja bem-vindo(a) ao atendimento da [TECH]. Em que podemos te ajudar?'
    '\n |1 - Agendar Suporte|'
    '\n |2 - Reparo no dispositivo|'
    '\n |3 - Outros |',
])

while True:
    try:
        resposta = bot.get_response(input(f"{user}: "))
        if float(resposta.confidence) > 0.5:
            print("Atendente: ", resposta)
        elif resposta == 'Não':
            print('Encerrando....')
            break
        else:
            print("Eu não entendi :(")
    except(KeyboardInterrupt, EOFError, SystemExit):
        break
