x = 0
maior = float('-inf')
menor = float('inf')
bebe = 0
crianca = 0
pre = 0
adoles = 0
jovem = 0
adult = 0
idoso = 0

for c in range(1, 9):
    idade = int(input('Digite a idade: '))

    if idade <= 2:
        bebe += 1

    elif idade <= 10:
        crianca += 1

    elif idade <= 14:
        pre += 1

    elif idade < 18:
        adoles += 1 

    elif idade < 21:
        jovem += 1 

    elif idade < 60:
        adult += 1

    elif idade >= 60:
        idoso += 1

    if idade > maior:
        maior = idade
    if idade < menor:
        menor = idade

x += idade
media = x / 8

print()
print(f'Bebes: {bebe}\nCrianças: {crianca}\nPré-adolecentes: {pre}\nAdolecentes: {adoles}\nJovens: {jovem}\nAdultos: {adult}\nIdosos: {idoso}')
print()
print(media)
print(f'A maior idade digita foi {maior}\nA menor foi {menor}')