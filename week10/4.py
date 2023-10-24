a = {}

def validar_tel(tel):
    if len(tel) == 11:
        return True
    else:
        return False
def incluir_novo_tel(nome, tels):
        tsv = [tel for tel in tels if validar_tel(tel)]
        if not tsv:
            print(f'\033[1mNúmero invalido para {nome}\033[0m')
            return
        if nome not in a:
            a[nome] = tels
        else:
            a[nome].extend(tels)
def incluir_tel(nome, tel):
    if validar_tel(tel):
        incluir_novo_tel(nome, [tel])
    else:
        print('\033[1mTelefone inválido.\033[0m')
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
    op = input('Escolha uma opção: ')

    if op == '1':
        print('\033[1mFormato do telefone(XX XXXXXXXXX)\033[0m')
        nome = input('Digite o nome: ')
        tels = input('Digite os telefones: ')
        incluir_novo_tel(nome, tels)
    elif op == '2':
        nome = input('Digite o nome: ')
        tel = input('Digite o telefone: ')
        incluir_novo_tel(nome, tel)
    elif op == '3':
        nome = input('Digite o nome: ')
        tel = input('Dgite o telefone a ser excluído: ')
        excluir_tel(nome, tel)
    elif op == '4':
        nome = input('Digite o nome a ser excluído: ')
        excluir_nome(nome)
    elif op == '5':
        for nome, tel in a.items():
            print(f'{nome}: {", ".join(tel)}')
    elif op == '6':
        break
    else:
        print('\033[1mTente novamente!\033[0m')
