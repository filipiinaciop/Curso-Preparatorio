carros = []
consu = []
num_carros = int(input("Quantos carros deseja comparar? "))

for i in range(num_carros):
    nome_carro = input(f"Digite o nome do carro {i+1}: ")
    consumo = float(input(f"Digite o consumo do {nome_carro} (km por litro): "))
    carros.append(nome_carro)
    consu.append(consumo)

preco_combustivel = 2.25 #gasosa

consu1000 = [1000 / c for c in consu]
custo1000 = [c * preco_combustivel for c in consu1000]

menor_consu = consu.index(max(consu))
mais_consu = consu.index(min(consu))

print('Comparativo de Consumo de Combustível')
for i in range(len(carros)):
    print(f"{i+1} - {carros[i]:<10} - {consu[i]:>5.1f} - {consu1000[i]:>6.1f} litros - R$ {custo1000[i]:>7.2f}") #contaix

print(f'O menor consumo é do {carros[menor_consu]}')
print(f'O maior consumo é do {carros[mais_consu]}')