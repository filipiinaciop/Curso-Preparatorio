codigos = [345, 765, 100, 910, 344, 642]
precos = [11.36, 13.98, 9.86, 19.98, 13.96, 16.98]
estoques = [2, 4, 1, 25, 0, 12]

def menu():
    print("\x1b[2J")  #print acima é para limpar a tela do terminal
    print(f'\033[1;33mCódigo --|--            Produto            --|-- Preço(R$) --|-- Estoque\033[0;0m')
    print(f'\n{codigos[0]:^7}--|--{"Presunto Fatiado 180g":^31}--|--{precos[0]:^11}--|--{estoques[0]:^6}',
    f'\n{codigos[1]:^7}--|--{"Coxinha da Asa Empanadas 400g":^31}--|--{precos[1]:^11}--|--{estoques[1]:^6}',
    f'\n{codigos[2]:^7}--|--{"Chicken Supreme 300g":^31}--|--{precos[2]:^11}--|--{estoques[2]:^6}',
    f'\n{codigos[3]:^7}--|--{"Hambúrguer Polpetone 320g ":^31}--|--{precos[3]:^11}--|--{estoques[3]:^6}',
    f'\n{codigos[4]:^7}--|--{"Filé de Tilápia 250g":^31}--|--{precos[4]:^11}--|--{estoques[4]:^6}',
    f'\n{codigos[5]:^7}--|--{"Filé de Peito Empanado 400g":^31}--|--{precos[5]:^11}--|--{estoques[5]:^6}'
    f'\n\033[1;31m{999:^7}---->{"FINALIZAR O PROGRAMA":^31}\033[0;0m'
    )
menu()

print()
indice = 0
while True:
    codigo = int(input('Digite o código do produto que deseja: '))
    if codigo in codigos:
        indice += 1
        break
    if codigo == 999:
        print('Compra finalizada')
    else:
        print('O código não existe. Digite um código do produto que deseja adquirir.')
        codigo = int(input('Digite o código do produto que deseja: '))
        continue
print('O estoque não pode ser abaixo de 0')
while True:
    quantidade = int(input('Digite a quantidade de produtos que deseja: '))
    if quantidade in estoques:
        print(f'Você comprou {quantidade} de {"Presunto Fatiado 180g"[0]}')
    else:
        print('Essa quantidade é maior do que temos em nosso estoque.')
        quantidade = int(input('Por favor digite novamente a quantidade que deseja comprar: '))

# FILIPI INACIO PENHA DOS SANTOS