p = int(input('Qual é a quantidade de produtos que deseja comprar: '))
sem_desc = 0
desc = 0
desc_porcem = 0

if p <= 0:
    print('A quantidade de produtos deve ser maior que zero.')
else:
    for c in range(p):
        precos = float(input(f'Digite o preço do produto {c + 1}: R$'))
        if precos <= 0:
            print('O preço do produto deve ser maior que 0.')
            break
        sem_desc += precos
    
    if sem_desc >= 100:    
        if p == 4:
            desc_porcem = 4
        elif p == 5:
            desc_porcem = 8
        elif p >= 6:
            desc_porcem = 12
        desc = (desc_porcem / 100) * sem_desc
        com_desc = sem_desc - desc

        print(f'Valor compra sem desconto: R${sem_desc: .1f}')
        print(f'Desconto: {desc_porcem}%')
        print(f'Valor desconto: R${desc: .1f}')
        print(f'Valor final a pagar: R${com_desc: .1f}')
    else:
        print(f'Valor a pagar: R${sem_desc: .1f}')
        print(f'O desconto é aplicado somente se a compra for maior que 100.')
