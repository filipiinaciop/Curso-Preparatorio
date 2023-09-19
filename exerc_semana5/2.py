import random

# Função para jogar o jogo de adivinhação
def jogo(nivel):
    if nivel == 'FÁCIL':
        limite = 10
    elif nivel == 'MÉDIO':
        limite = 50
    elif nivel == 'DIFÍCIL':
        limite = 100
    else:
        print('Nível inválido.')
        return

    n = random.randint(1, limite)

    print(f'Bem-vindo ao jogo de adivinhação ({nivel})!')
    print(f'Eu escolhi um número entre 1 e {limite}. Tente adivinhar.')

    tentativas = 0

    #while True para fazer algo indeterminadas vezes
    while True:
        tentativa = int(input('Tentativa: '))

        if tentativa == n:
            print(f'Parabéns! Você acertou o número {n} em {tentativas + 1} tentativas.')
            break
        elif tentativa < n:
            print('O número é maior.')
        else:
            print('O número é menor.')
        
        tentativas += 1

# Programa principal
print('Escolha o nível de dificuldade: FÁCIL, MÉDIO ou DIFÍCIL.')
nivel = input('Digite o nível: ').upper()
jogo(nivel)
