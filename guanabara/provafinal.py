# EXERCÍCIO IMPOSTO DE RENDA
def calcular_imposto_renda(salario):
    if salario <= 1000:
        print('\033[1mSeu imposto de renda é isento.\033[0m')
    elif salario >= 1001 and salario <= 3000:
       salario += (salario*10/100)
    elif salario >= 3001 and salario <= 5000:
        salario += (salario*20/100)
    else:
        salario += (salario*30/100)
    return salario

salario = int(input('Qual é seu salário bruto?\nR$'))
imposto = calcular_imposto_renda(salario)
print(f'\033[1mO imposto de renda a ser pago é R${imposto:.0f}\033[0m')
print('\033[32;1mCaso seu imposto de renda seja isento você não pagará.\033[0m')


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


# EXERCÍCIO ESTACIONAMENTO
esc = 0
placa = []
while True:
    placa_usuario = int(input('Qual a placa do seu carro? '))
    e_or_s = input('Entrada ou saída(E/S)? ')
    if e_or_s in 'Ee':
        placa.append(placa_usuario)
        hora = int(input("Digite a hora de entrada (0-23): "))
        min = int(input("Digite o minuto de entrada (0-59): "))
    elif e_or_s in 'Ss':
        plac = int(input('Digite a placa: '))
        if plac in placa:
            hora_saida = int(input("Digite a hora de saída (0-23): "))
            minuto_saida = int(input("Digite o minuto de saída (0-59): "))
        else:
            plac = int(input('A placa anterior não existia, por favor colocar um que ja tenha sido colocada.'))
    # tempo_entrada_em_minutos = hora * 60 + min
    # tempo_saida_em_minutos = hora_saida * 60 + minuto_saida
    # tempo_total_em_horas = (tempo_saida_em_minutos - tempo_entrada_em_minutos) / 60