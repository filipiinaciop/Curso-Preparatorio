# INCOMPLETO 

def att(estoque2,pedidos,media):
    media = int(input('Digite o valor minímo do estoque: '))

es1 = int(input('Digite a quantidade do estoque de (Camisas): '))
pc1 = float(input('Digite o preço de cada Camisa: $'))
es2 = int(input('Digite a quantidade do estoque de (Calças Jeans): '))
pc2 = float(input('Digite o preço de cada Calça: $'))
es3 = int(input('Digite a quantidade do estoque de (Tênis): '))
pc3 = float(input('Digite o preço de cada Tênis: $'))

e1 = {
    ("Camiseta", pc1, es1),
    ("Calça Jeans", pc2, es2),
    ("Tênis", pc3, es3)
    }
e2 = (
    ("Camiseta", pc1, es1),
    ("Calça Jeans", pc2, es2),
    ("Tênis", pc3,  es3),
)


print('Seu estoque atual é ',e1)

p = 1
for x in range(9999):
    print(f'{p}° Pedido:')
    p1 = int(input('Digite a quantidade de Camisas: '))
    p2 = int(input('Digite a quantidade de Calças Jeans: '))
    p3 = int(input('Digite a quantidade de Tênis: '))
    if p1 and p2 and p3 >= 0:
        if p1 < es1 and p2 < es2 and p3 < es3:
            p += 1
            pedidos = (
            ("Camiseta", p1),
            ("Tênis", p2),
            ("Calça Jeans", p3)
            )
            att (e2,pedidos, 0)