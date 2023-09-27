while True:
    aplicacao = float(input('Digite o valoe da aplicacao: R$'))

    if aplicacao < 0:
        break
    n_meses = int(input('Digite o número de meses de aplicação: '))

    if aplicacao <= 2000:
        taxa = 0.005
    elif aplicacao <= 10000:
        taxa = 0.01
    else:
        taxa = 0.015

    resgate = aplicacao * (1 + taxa) ** n_meses
    print(f'O valor do resgate após {n_meses} meses será de R${resgate: .2f}')
