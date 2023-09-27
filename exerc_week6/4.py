while True:
    aplicacao = float(input('Digite o valor da aplicacao: R$'))

    if aplicacao < 0:
        break
    n_meses = int(input('Digite o número de meses de aplicação: '))

    if aplicacao <= 2000:
        taxa = 0.005
    elif aplicacao <= 10000:
        taxa = 0.01
    else:
        taxa = 0.015

    temp = 0
    a1 = 2000
    a2 = 10000
    if temp < n_meses:
        resgate = aplicacao * (1 + taxa) ** n_meses

    if resgate >= a1 and resgate < a2:
            taxa == 0.01
    elif resgate >= a2:
            taxa = 0.015
    temp += 1
    
    print(f'O valor do resgate após {n_meses} meses será de R${resgate: .2f}')
