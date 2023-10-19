def filtrar_clientes(clientes, idade_min, idade_max, localizacao, valor_min_compras):
    clientes_filtrados = set()

    for cliente in clientes:
        nome, idade, cidade, compras = cliente

        # Verifica se o cliente atende aos critérios
        if idade_min <= idade <= idade_max and cidade == localizacao and compras >= valor_min_compras:
            clientes_filtrados.add(cliente)

    return clientes_filtrados

# Solicita informações ao usuário
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
localizacao = input("Digite sua localização (cidade ou estado): ")
valor_compra = float(input("Digite o valor da compra: R$ "))

# Base de dados fictícia de clientes
base_de_dados = [
    ("Cliente1", 30, "Sao Paulo", 1500),
    ("Cliente2", 25, "Rio de Janeiro", 800),
    ("Cliente3", 40, "Sao Paulo", 1200),
    ("Cliente4", 28, "Sao Paulo", 900),
]

idade_min = idade - 5
idade_max = idade + 5
valor_min_compras = valor_compra

clientes_filtrados = filtrar_clientes(base_de_dados, idade_min, idade_max, localizacao, valor_min_compras)

# Exibir os clientes filtrados
print("\nClientes filtrados:")
for cliente in clientes_filtrados:
    print(cliente)
