i_0_25 = 0
i_26_50 = 0
i_51_75 = 0
i_76_100 = 0

while True:
    print('\033[33mBem vindo! faça o seguinte:\nDigite números e depois veja quantos números voce digitou esta em 4 tipos de intervalo!\033[0m')
    n = int(input('Digite um número positivo (ou negativo para finalizar):'))
    if n < 0:
        break #para sair
    if n <= 25:
        i_0_25 += 1
    elif n <= 50:
        i_26_50 += 1
    elif n <= 75:
        i_51_75 +=1
    elif n <= 100:
        i_76_100 += 1
    else:
        print('Número inválido.')
        continue

print(f"Números no intervalo [0-25]: {i_0_25}")
print(f"Números no intervalo [26-50]: {i_26_50}")
print(f"Números no intervalo [51-75]: {i_51_75}")
print(f"Números no intervalo [76-100]: {i_76_100}")
