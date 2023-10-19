def filtrar_clientes():
    clientes_filtrados = []
    
    while True:
        nome = input('Digite o nome do cliente (ou digite "parar" para encerrar): ')
        if nome.lower() == 'parar':
            break
        idade = int(input('Digite a idade do cliente: '))
        cidade = input('Digite a localização do cliente: ')
        compras = float(input('Digite o valor de compras realizadas pelo cliente: R$ '))
        
        # Verifica se o cliente atende aos critérios
        if idade_min <= idade <= idade_max and cidade == localizacao and compras >= valor_min_compras:
            cliente = (nome, idade, cidade, compras)
            clientes_filtrados.append(cliente)

    return clientes_filtrados

idade_min = 25
idade_max = 35
localizacao = 'Sao paulo'
valor_min_compras = 1000
clientes_filtrados = filtrar_clientes()

if clientes_filtrados:
    print('\nClientes que atendem aos critérios:')
    for cliente in clientes_filtrados:
        print(cliente)
else:
    print('Nenhum cliente atende aos critérios especificados.')

