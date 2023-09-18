import random
import datetime
from validate_docbr import CPF

def validar_email(email):
    arroba = email.find('@') != -1
    com = email.lower().find('.com') != -1
    return arroba and com

def gerar_extrato():
    nome = input('Digite o nome do cliente: ')
    agencia = int(input('Digite o número da agencia: '))
    conta_corrente = int(input('Digite o número da conta corrente: '))
    para = input('Digite o nome do destinatário da transferencia: ')
    instituicao = input('Digite o nome da instituicao: ')
    chave = input('Digite a chave: ')
    cpf = input('Digite o CPF (apenas números): ')
    valor = float(input('Digite o valor da transferencia: '))

    data_transferencia = datetime.date.today()
    agencia_formatada = f'{agencia:04d}'
    cpf_formatado = CPF().mask(cpf)
    id_aleatorio = random.randint(1000000, 9999999)

    if valor > 1500:
        cor_valor = '\033[34m' #AZUL
    else:
        cor_valor = '\033[31m' #VERMELHO
    
    #cores, \033[32m (verde) - \033[1m (negrito) - \033[0m (para fechar até onde vai a cor!)
    print('\033[32mDADOS DO CLIENTE\033[0m')
    print(f'\033[1mNome:\033[0m {nome}')
    print(f'\033[1mAgencia:\033[0m {agencia_formatada} ')
    print(f'\033[1mConta corrente:\033[0m {conta_corrente}')
    print('-' * 25)
    
    print(f'\033[32mDADOS DA TRANSFERENCIA\033[0m')
    print(f'\033[1mPara:\033[0m {para}')
    print(f'\033[1mInstituição:\033[0m {instituicao}')
    print(f'\033[1mChave:\033[0m {chave}')
    print(f'\033[1mCPF:\033[0m {cpf_formatado}')
    print(f'\033[1mValor:{cor_valor}R${valor:.2f}\033[0m')
    print('-' * 25)

    print(f'\033[32mID/Transação\033[0m')
    print(f'\033[1mID:\033[0m {id_aleatorio}')
    print(f'\033[1mData:\033[0m {data_transferencia}')

gerar_extrato()