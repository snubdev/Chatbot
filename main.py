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

conversa.train([
    'Oi',
    'Eae',
    'Qual o seu nome?',
    'Irineu, você não sabe e nem eu',
    'Prazer em te conhecer',
    'Igualmente meu patrão',
])

user = str(input('Infome seu nome: '))

while True:
    try:
        resposta = bot.get_response(input(f"{user}: "))
        if float(resposta.confidence) > 0.5:
            print("Atendente: ", resposta)
        elif resposta == "Obrigado":
            break
        else:
            print("Eu não entendi :(")
    except(KeyboardInterrupt, EOFError, SystemExit):
        break