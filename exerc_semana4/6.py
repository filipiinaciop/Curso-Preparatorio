import random

def gerar_pergunta():
    a = random.randint(1, 20)
    b = random.randint(1,20)
    resultado = a * b
    return a, b, resultado

#Verificacao de respostas
def verificar_resposta(pergunta, resposta):
    a, b, resultado = pergunta
    if resposta == resultado:
        return True
    else:
        return False

acertos = 0
print('Bem vindo ao teste de multiplicação!')

#realizar as perguntas
for i in range(5):
    pergunta = gerar_pergunta()
    a, b, resultado = pergunta
    print(f'Pergunta: {a} X {b} = ?', end=' ')
    resposta = int(input())

    if verificar_resposta(pergunta, resposta):
        print('Acertou')
        acertos += 1
    else:
        print(f'Errou\nA resposta correta era {resultado}')

    print(f'Acertos atuais: {acertos}\n')
    print(f"Você acertou um total de {acertos} perguntas.")