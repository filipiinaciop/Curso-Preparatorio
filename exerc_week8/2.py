# INCOMPLETO 

es1 = int(input('Digite a quantidade do estoque de Camisas: '))
ps1 = float(input('Digite o preço de cada Camisa: R$'))
es2 = int(input('Digite a quantidade do estoque de Calças Jeans: '))
ps2 = float(input('Digite o preço de cada Calça: R$'))
es3 = int(input('Digite a quantidade do estoque de Tênis: '))
ps3 = float(input('Digite o preço de cada Tênis: R$'))

estoque1 = {
    ("Camiseta", ps1, es1),
    ("Calça Jeans", ps2, es2),
    ("Tênis", ps3, es3)
    }
estoque2 = (
    ("Camiseta", ps1, es1),
    ("Calça Jeans", ps2, es2),
    ("Tênis", ps3,  es3),
)
print('Seu estoque atual é ',estoque1)

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
