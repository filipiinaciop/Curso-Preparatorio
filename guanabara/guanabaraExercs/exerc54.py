from datetime import date
atual= date.today().year
maior18 = 0
menor18 = 0
for c in range(0,7):
    nasc = int(input('Em que ano a pessoa nasceu? '))
    idade = atual - nasc
    if idade >= 18:
        maior18 += 1
    else:
        menor18 += 1
print(f'Há {menor18} menores de idade.\nE há {maior18} maiores de idade.')