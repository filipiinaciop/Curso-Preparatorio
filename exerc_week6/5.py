import random
print()
print('Bem-vindo/a ao jogo')
print('REGRAS\n[1] - Saldo inical 100.00\n[2] - Nâo é possivel apostar amais que o saldo atual\n[3] - Em caso de perda somente 20.00 pontos serão retirados')
print()
ganhas = 0
percas = 0
valor = 100.00
while True:
    aposta = float(input('Digite o valor de sua aposta: '))
    d1 = random.randint(1, 6)
    d2 = random.randint(1, 6)
    d3 = d1 + d2
    if aposta > valor:
        print(f'O valor apostado não pode ser superior ao saldo atual \033[33m{valor:.2f}\033[0m: Jogadas ganhas {ganhas} perdidas {percas}')
        break
    elif d3 == 7 and 11:
        ganhas += 1
        print(f'São {d1} e {d2} os valores dos dados jogados')
        aposta = aposta * 2
        saldo = aposta + valor
        valor = saldo
        print(f'Parabéns você dobrou sua aposta!\033[32mSaldo atual R${saldo:.2f}\033[0m')
        cont = input('Deseja continuar? (s/n) ')
        cont = cont.lower()
        print()
        if cont == 's':
            continue
        else:
            print(f'Valor final \033[33m{saldo:.2f}\033[0m número de jogadas ganhas {ganhas} e perdidas \033[31m{percas}\033[0m')
            break
    elif d3 != 7 and 11:
        print(f'São {d1} e {d2} os valores dos dados jogados')
        saldo = valor - 20
        valor = saldo
        print(f'Shiii você perdeu!\033[31mSaldo atual {saldo}\033[0m')
        percas += 1
        print()
        cont = input('Deseja continuar? (s/n) ')
        if 0 >= valor:
            print('Fim do jogo, você zerou seus pontos.')
            print(f'Informaçoês finais: Jogos ganhos {ganhas} Jogos perdidos {percas}')
            break 
        if cont == 's':
            continue
        else:
            print(f'Valor final \033[33m{saldo:.2f}\033[0m número de jogadas ganhas {ganhas} e perdidas \033[31m{percas}\033[0m')
            break
