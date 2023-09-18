print('Mercado J&F - Promoção FRIBOI')
print('1- Filé Duplo \n2- Alcatra \n3- Picanha')

c = int(input('Digite o tipo que deseja levar (1, 2 ou 3): '))
c2 = float(input('Digite a quantidade comprada (em Kg): '))
c3 = int(input('A compra será realizada com cartão de débito? \n1 - SIM  \n2 - NÃO  \n'))

if c3 == 1:
    x = 'SIM'
    desc = 0.05
    print('Sua escolha foi: 1')
else:
    x = 'NÃO'
    desc = 1
    print('Sua escolha foi: 2')

print()
print('**************CUPOM FISCAL**************')

if c == 1:
    subs = 'Filé Duplo'
    preco_kg = 4.90
elif c == 2:
    subs = 'Alcatra'
    preco_kg = 5.90
elif c == 3:
    subs = 'Picanha'
    preco_kg = 6.90

print(f'* Carne: {subs} ')
print(f'* Quantidade: {c2} Kg')

# Cálculo do preço com base na quantidade
if c2 <= 5:
    subs = preco_kg * c2
elif c2 > 5:
    subs = 5.80 * c2  # Preço por Kg com desconto para mais de 5 Kg

print(f'* Preço: R${subs:.2f}')
print(f'* Cartão de Débito: {x}')

z = subs - (subs * desc)
if desc == 1:
    print(f'* Total sem desconto: R${subs:.2f}')
else:
    print(f'* Total com desconto: R${z:.2f}')