a = {}

def incluir_novo_tel(nome, tels):
    if nome not in a:
        a[nome] = tels
    else:
        a[nome].extend(tels)

def incluir_tel(nome, tel):
    if nome in a:
        a[nome].append(tel)
    else:
        incluir_novo_tel(nome, [tel])

def excluir_tel(nome, tel):
    if nome in a and tel in a[nome]:
        a[nome].remove(tel)
        if not a[nome]:
            del a[nome]

def excluir_nome(nome):
    if nome in a:
        del a[nome]

while True:
    print('Agenda de Telefones')
    print('1 - Incluir Novo Contato')
    print('2 - Incluir Telefone em Contato Existente')
    print('3 - Excluir Telefone de Contato')
    print('4 - Excluir Contato')
    print('5 - Listar Agenda')
    print('6 - Sair')
    op = input('\033[1mEscolha uma opção: \033[0m')

    if op == '1':
        nome = input('Digite o nome: ')
        tels = input('Digite os telefones: ').split(',')
        incluir_novo_tel(nome, tels)
    elif op == '2':
        nome = input('Digite o nome: ')
        tel = input('Digite o telefone: ')
        incluir_tel(nome, tel)
    elif op == '3':
        nome = input('Digite o nome: ')
        tel = input('Digite o telefone a ser excluído: ')
        excluir_tel(nome, tel)
    elif op == '4':
        nome = input('Digite o nome a ser excluído: ')
        excluir_nome(nome)
    elif op == '5':
        for nome, tels in a.items():
            print(f'\033[1m{nome}: {", ".join(tels)}\033[0m')
    elif op == '6':
        print()
        break
    else:
        print('Tente novamente.')
