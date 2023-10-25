from random import randint
def inverter_es(estoque):
    estoque_invertido = {}
    for cod, nome in estoque.items():
        if nome not in estoque_invertido:
            estoque_invertido[nome] = [cod]
        else:
            estoque_invertido[nome].append(cod)
    return estoque_invertido

estoque = {}
n_produtos = int(input("Quantos produtos deseja adicionar ao estoque? "))
for _ in range(n_produtos):
    cod = randint(1000, 9999)
    nome = input("Digite o nome do produto: ")
    if nome in estoque:
        print("Produto com nome duplicado. O código será gerado aleatoriamente.")
        cod = randint(1000, 9999)
    estoque[cod] = nome

estoque_invertido = inverter_es(estoque)

print("Estoque atual:")
for cod, nome in estoque.items():
    print(f"CÓDIGO: {cod}, PRODUTO: {nome}")
print("\nEstoque invertido:")
for nome, cods in estoque_invertido.items():
    print(f"PRODUTO: {nome}, CÓDIGO: {', '.join(map(str, cods))}")
