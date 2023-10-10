produtos = (
    "Pão de queijo 400g",
    "Salsicha Hot-dog 500g",
    "Pão de alho baguete 400g",
    "Filé de Peito de Frango 1Kg",
    "Isca de Frango 300g",
    "Linguiça toscana 700g",
    "Pedaço de Filé de Salmão 500g",
    "Filé de Tilápia 250g",
    "Bife de Filé Mignon MAIS 900g",
    "Carne moída patinho 900g")

precos = (
    10.76,
    09.96,
    10.96,
    19.96,
    13.96,
    17.96,
    54.96,
    13.96,
    89.96,
    39.97)

def menu(produtos, precos):
    print("\033[33;1mBem-vindo à loja Swift!\033[0m")
    print("\033[33;1mMenu de Produtos:\033[0m")
    for i, produto in enumerate(produtos):
        print(f"\033[1m{i + 1}. {produto}\033[0m - \033[32mR${precos[i]:.2f}\033[0m")
    print("0. Sair")

def p_mais_caro_barato(produtos, precos):
    caro_index = precos.index(max(precos))
    barato_index = precos.index(min(precos))
    return produtos[caro_index], precos[caro_index], produtos[barato_index], precos[barato_index]
# soma dos produtos nos índices pares
def spip(precos):
    soma = sum(precos[::2])
    return soma

while True:
    menu(produtos, precos)
    escolha = int(input("Escolha um produto (0 para sair): "))
    
    if escolha == 0:
        break
    elif escolha > 0 and escolha <= len(produtos):
        produto_index = escolha - 1
        print(f"Você escolheu: {produtos[produto_index]} - R${precos[produto_index]:.2f}")
    else:
        print("Escolha inválida. Tente novamente.")

produto_mais_caro, preco_mais_caro, produto_mais_barato, preco_mais_barato = p_mais_caro_barato(produtos, precos)
print(f"Produto mais caro: {produto_mais_caro} - R${preco_mais_caro:.2f}")
print(f"Produto mais barato: {produto_mais_barato} - R${preco_mais_barato:.2f}")

soma_pares = spip(precos)
print(f"Soma dos preços dos produtos nos índices pares: R${soma_pares:.2f}")