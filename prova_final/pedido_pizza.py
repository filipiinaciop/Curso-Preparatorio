# EXERCÍCIO PEDIDO PIZZA
sabor = []
tamanho = []
refrigerante= []
op = 0
while op != 4:
    print('Menu:')
    print('''    1. Escolher sabor de pizza
    2. Escolher tamanho de pizza 
    3. Adicionar refrigerante
    4. Finalizar pedido''')
    op = int(input('Escolha uma opção: '))
    if op == 1:
        print('''    1. Mussarela 
        2. Calabresa
        3. Frango com Catupiry  ''')
        opcao = int(input('Escolha um sabor (1/2/3): '))
        if opcao == 1:
            sabor.append('Mussarela')
        elif opcao == 2:
            sabor.append('Calabresa')
        elif opcao == 3:
            sabor.append('Frango com Catupiry')
        else:
            print('Opção invalida. escolha novamente.')
    elif op == 2:
        print('''    1. Pequena
        2. Média
        3. Grande''')
        ops = int(input('Escolha uma tamanho(1/2/3): '))
        if ops == 1:
            tamanho.append('Pequena')
        elif ops == 2:
            tamanho.append('Média')
        elif ops == 3:
            tamanho.append('Grande')
        else:
            print('Opção invalida. escolha novamente.')
    elif op == 3:
        refri = input('Deseja adicionar refrigerante (S/N)? ')
        if refri in 'Ss':
            refrigerante.append('Refrigerante adicionado ao pedido.')
        else:
            refrigerante.append('Refrigerante não adicionado ao pedido.')
    elif op == 4:
        print(f'Sabor da pizza: {sabor}')
        print(f'Tamanho da pizza: {tamanho}')
        print(refrigerante)
    else:
        continue