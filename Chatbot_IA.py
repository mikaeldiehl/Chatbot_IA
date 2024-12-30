from langchain.prompts import ChatPromptTemplate
import os
from langchain_groq import ChatGroq

api_key = ''
os.environ['GROQ_API_KEY'] = api_key
chat = ChatGroq(model='llama-3.1-70b-versatile')

template = ChatPromptTemplate.from_messages(
    [('system', 'Você é um assistente que sempre responde com piadas'),
     ('user', 'Traduza {expressao} para a lingua {lingua}')]
)

chain = template | chat

resposta = chain.invoke({'expressao': 'Beleza?', 'lingua': 'inglesa'})
print(resposta.content)

chain = template | chat

resposta = chain.invoke({'expressao': 'Beleza?', 'lingua': 'inglesa'})

template.invoke({'expressao': 'Beleza?', 'lingua': 'inglesa'})

def resposta_bot(mensagens):
    mensagens_modelo = [('system', 'Você é um assistente amigável chamado asimo')]
    mensagens_modelo += mensagens
    template = ChatPromptTemplate.from_messages(mensagens_modelo)  # Corrigido 'from_massages' para 'from_messages'
    chain = template | chat
    return chain.invoke({}).content

print('Bem-vindo ao AsimoBot')

mensagens = []

while True:
    pergunta = input('Usuario: ')
    if pergunta.lower() == 'x':
        break
    mensagens.append(('user', pergunta))
    resposta = resposta_bot(mensagens)  # Corrigido 'reposta' para 'resposta'
    mensagens.append(('assistant', resposta))
    print(f'Bot: {resposta}')

print('Muito obrigado por usar o AsimoBot')
print(mensagens)
