
imc_mais_alto = 0
imc_mais_baixo = 0

def calculos(altura, peso):
    imc = peso / (altura**2)

for p in range(0, 10000):
    print('Numero negativo para acabar.')
    nome = input(f'Digite o nome do paciente {p + 1}: ')
    altura = float(input(f'Digite a altura do paciente(em metros): '))
    peso = float(input('digite o peso do paciente (em KG): '))
    calculos(altura, peso)
    imc = peso / (altura**2)
    print(f'O imc de {nome} é {imc}')

media = (imc + p) / p
nome_imc_mais_baixo = 0
nome_imc_mais_alto = 0

print(f'O imc mais alto é de: {imc_mais_alto} do paciente {nome_imc_mais_alto}')
print(f'O imc mais baixo é de: {imc_mais_baixo} do paciente {nome_imc_mais_baixo}')
