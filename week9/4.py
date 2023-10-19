carros = ["CAMARO", "CRETA", "UNO", "CIVIC", "ONIX"]
consu = [7, 10, 12.5, 9, 14.5]

preco_combustivel = 2.25 #gasosa

consu1000km = [1000 / c for c in consu]
custo1000km = [c * preco_combustivel for c in consu1000km]

menor_consu = consu.index(max(consu))
mais_consu = consu.index(min(consu))

print("Comparativo de Consumo de Combustível")
for i in range(len(carros)):
    print(f"{i+1} - {carros[i]:<10} - {consu[i]:>5.1f} - {consu1000km[i]:>6.1f} litros - R$ {custo1000km[i]:>7.2f}") #contaix

print(f"O menor consumo é do {carros[menor_consu]}")
print(f"O maior consumo é do {carros[mais_consu]}")
#É isso