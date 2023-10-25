agenda = {}

def validar_tel(tel):
    tel = ''.join(filter(str.isdigit, tel))
    return len(tel) == 11

def incluir_novo_tel(nome, tels):
    tels_validos = [tel for tel in tels if validar_tel(tel)]
    
    if not tels_validos:
        print(f'\033[1mTelefone inválido para {nome}.\033[0m')
        return
    
    if nome not in agenda:
        agenda[nome] = tels_validos
    else:
        agenda[nome].extend(tels_validos)

def incluir_tel(nome, tel):
    if validar_tel(tel):
        incluir_novo_tel(nome, [tel])
    else:
        print('\033[1mTelefone inválido. Não foi possível adicionar à agenda.\033[0m')

def excluir_tel(nome, tel):
    if nome in agenda and tel in agenda[nome]:
        agenda[nome].remove(tel)
        if not agenda[nome]:
            del agenda[nome]

def excluir_nome(nome):
    if nome in agenda:
        del agenda[nome]

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
        print('\033[1mTelefone dever ser digitado (DDNNNNNNNNN)\033[0m')
        nome = input('Digite o nome: ')
        tels = input('Digite os telefones: ').split(',')
        incluir_novo_tel(nome, tels)
    elif op == '2':
        print('\033[1mTelefone dever ser digitado (DDNNNNNNNNN)\033[0m')
        nome = input('Digite o nome: ')
        tel = input('Digite o telefone: ')
        incluir_tel(nome, tel)
    elif op == '3':
        print('\033[1mTelefone dever ser digitado (DDNNNNNNNNN)\033[0m')
        nome = input('Digite o nome: ')
        tel = input('Digite o telefone a ser excluído: ')
        excluir_tel(nome, tel)
    elif op == '4':
        nome = input('Digite o nome a ser excluído: ')
        excluir_nome(nome)
    elif op == '5':
        for nome, tels in agenda.items():
            print(f'{nome}: {", ".join(tels)}')
    elif op == '6':
        break
    else:
        print('\033[1mTente novamente.\033[0m')
