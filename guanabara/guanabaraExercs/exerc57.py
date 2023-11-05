sexo = input('Informe seu sexo: [M/F] ').strip().upper()[0]
while sexo not in 'MmFf':
    sexo = input('Dados invalidos. Por favor informe seu sexo: ').strip().upper()[0]
print(f'Seu {sexo} registrado com sucesso.')