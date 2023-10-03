imovel = float(input('Valor do imóvel: '))
i = float(input('Investimento mensal: '))
taxa_mensal = float(input('Taxa de juros mensal (em porcentagem): '))

if i < 0.01 * imovel:
    print('O investimento mensal não é viável para comprar o imóvel.')
else:
    m = 0
    saldo = 0

    for c in range(1, 1000): #1 ate 1000 para ano ser loop infinito!!!
        saldo += i
        saldo *= (1 + taxa_mensal / 100)
        m += 1
        if saldo >= imovel:
            break
    print(f'Tempo necessário para comprar o imóvel é de {m} meses.')

