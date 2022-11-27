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

conversa.train([
    '1',
    'Informe motivo da agendamento?',
    'Meu sistema está fora do ar',
    'Enviaremos o suporte imediato para resolver o problema da senhor(a). Mais alguma coisa senhor(a)?',
    'Sim',
    'Oque o senhor(a) deseja?'
    ' |1 - Agendar Suporte| '
    ' |2 - Reparo no dispositivo| '
    ' |3 - Outros |',
])

conversa.train([
    '1',
    'Informe motivo da agendamento?',
    'Sistema está apresentando error em algumas funções',
    'Enviaremos o suporte imediato para resolver o problema da senhora. Mais alguma coisa senhor(a)?',
    'Não',
])

conversa.train([
    '1',
    'Informe motivo da agendamento?',
    'Banco de dados está fora do ar',
    'Enviaremos o suporte imediato para resolver o problema da senhora. Mais alguma coisa senhor(a)?',
])

conversa.train([
    '2',
    'Informe motivo do reparo?',
    'Meu computador parou de vez',
    'Envie seu dispositivo até nossa sede que iremos fazer o reparo. '
    'Em breve enviaremos o orçamento para seu email! Mais alguma coisa senhor(a)?',
])

conversa.train([
    '2',
    'Informe motivo do reparo?',
    'Meu computador deu tela azul',
    'Envie seu dispositivo até nossa sede que iremos fazer o reparo. '
    'Em breve enviaremos o orçamento para seu email! Mais alguma coisa senhor(a)?',
])

conversa.train([
    '2',
    'Informe motivo do reparo?',
    'Meu computador apresentou problema no HD',
    'Envie seu dispositivo até nossa sede que iremos fazer o reparo. '
    'Em breve enviaremos o orçamento para seu email! Mais alguma coisa senhor(a)?',
])

conversa.train([
    '2',
    'Informe motivo do reparo?',
    'Meu computador não conecta à Internet',
    'Envie seu dispositivo até nossa sede que iremos fazer o reparo. '
    'Em breve enviaremos o orçamento para seu email! Mais alguma coisa senhor(a)?',
])

conversa.train([
    '3',
    'Informe motivo do contato?',
    'Desejo fala com um atendente',
    'Nossos atendentes irão entrar em contato através de ligação ou whatsapp, peço que o senhor(a) fique atendendo',
    'Certo',
    f'Senhor(a) {user} deseja mais alguma coisa?',
])

conversa.train([
    '3',
    'Informe motivo do contato?',
    'Quero fala com um atendente',
    'Nossos atendentes irão entrar em contato através de ligação ou whatsapp, peço que o senhor(a) fique atendendo',
    'Ok',
    f'Senhor(a) {user} deseja mais alguma coisa?',
])

conversa.train([
    '3',
    'Informe motivo do contato?',
    'Estou com problemas no meu computador',
    'Selecione a opção de Reparo',
])

conversa.train([
    '3',
    'Informe motivo do contato?',
    'Estou com problemas no meu dispositivo',
    'Selecione a opção de Reparo',
])

conversa.train([
    '3',
    'Informe motivo do contato?',
    'Estou com problemas no meu site',
    'Selecione a opção de Suporte Técnico',

])

conversa.train([
    '3',
    'Informe motivo do contato?',
    'Quero efetuar o pagamento',
    'Para realizar o pagamento nosso [PIX] é 111.222.333.444-00',
    'OK',
    f'Senhor(a) {user} deseja mais alguma coisa?',

])

conversa.train([
    '3',
    'Informe motivo do contato?',
    'Quero efetuar o pagamento',
    'Para realizar o pagamento nosso [PIX] é 111.222.333.444-00',
    'Certo',
    f'Senhor(a) {user} deseja mais alguma coisa?',

])

conversa.train([
    '3',
    'Informe motivo do contato?',
    'Quero emitir a segunda via do boleto',
    'Enviaremos a segunda via do boleto para o e-mail do senhor',
])

conversa.train([
    'Não',
    'Já finalizamos o seu atendimento e gostaríamos que você pudesse responder uma rápida pesquisa sobre o nosso atendimento.'
    '\n Para continuarmos prestando um excelente serviço, gostaríamos de saber o que você achou do nosso atendimento. De A a C, o quanto você ficou satisfeito?'
    '\n [A - Insatisfeito]  [B - Satisfeito] [C - Muito satisfeito]',
    'A',
    'Obrigada pelo contato! Estamos sempre à disposição para quando você precisar. Até mais!',

])

conversa.train([
    'Não',
    'Já finalizamos o seu atendimento e gostaríamos que você pudesse responder uma rápida pesquisa sobre o nosso atendimento.'
    '\n Para continuarmos prestando um excelente serviço, gostaríamos de saber o que você achou do nosso atendimento. De A a C, o quanto você ficou satisfeito?'
    '\n [A - Insatisfeito]  [B - Satisfeito] [C - Muito satisfeito]',
    'B',
    'Obrigada pelo contato! Estamos sempre à disposição para quando você precisar. Até mais!',

])

conversa.train([
    'Não',
    'Já finalizamos o seu atendimento e gostaríamos que você pudesse responder uma rápida pesquisa sobre o nosso atendimento.'
    '\n Para continuarmos prestando um excelente serviço, gostaríamos de saber o que você achou do nosso atendimento. De A a C, o quanto você ficou satisfeito?'
    '\n [A - Insatisfeito]  [B - Satisfeito] [C - Muito satisfeito]',
    'C',
    'Obrigada pelo contato! Estamos sempre à disposição para quando você precisar. Até mais!',

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