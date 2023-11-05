# num = (2, 5, 9, 1)
# num[2] = 2
# print(num)   #erro pois é tupla

num = [2, 5, 9, 1]
num[2] = 3
num.append(7) # add 7 (num[4] = 7)nao funciona
num.sort() 
print(num)
num.sort(reverse=True)
print(num)
num.insert(2, 2)
# num.remove(4) #vai dar erro pois nao tem
print(num)
print(f'Essa lista tem {len(num)} elementos.')

valores = []
# valores.append(5)
# valores.append(9)
# valores.append(4)
# OU
for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))

# for v in valores:
#     print(f'{v}...', end='')
# OU
for c, v in enumerate(valores):
    print(f'Na posicao {c+1} encontrei o valor {v}.')
print('Cheguei ao final da lista.')

#O python liga listas:
a = [2, 3, 4, 7]
# b = a # faz a ligacao
b = a[:] # nao faz a ligacao
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')

