import random

def jogo(nivel):
    if nivel == 'FÁCIL' :
       limite = 10
    elif nivel == 'MÉDIO':
       limite = 50
    elif nivel == 'DIFÍCIL':
       limite = 100
    else:
       print('Nivel inválido. ')
       return
    
    n = random.randint(1, limite)
    while True:
        valor = int(input('Digite um valor até o número correto: '))
        x += 1
        if valor == n:
            print('Parabéns voce acertou!')
            print(f'Foram {x} tentativas até o acerto!')
            break
        elif valor < n:
            print('Um pouco mais!')
        else:
         print('Um pouco menos!')
