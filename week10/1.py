def buscar(clientes,f):
    c = 0
    x = 0 
    y = 0
    z = 0
    for xx in range(n):
    #for x in clientes.keys():
        if f in clientes[1+c]["Nome"]:
            x += 1
        if f in clientes[1+c]["Endereço"]:
            y += 1
        if f in clientes[1+c]["OperadoraCelular"]:
            z += 1
        c += 1
    print('Chaves localizadas?\n')
    if x >= 1:
        print('Nome')
    if y >= 1:
        print('Endereço\n')
    if z >= 1:
        print('OperadoraCelular')                
    if y == 0 and z == 0 and x == 0:
        print('Nenhuma chave localizada!\n') 

clientes = {}
n = int(input('Quantos clientes deseja anotar? '))
x = 0
while x < n :
    n1 = str(input('Digite o nome do cliente: '))
    n2 = input('Digite o endereço do cliente: ')
    n3 = str(input('Digite a operadora do cliente: '))
    cliente = {
        "Nome":n1,
        "Endereço":n2,
        "OperadoraCelular":n3
    } 
    x += 1
    clientes[x] = cliente
    print('!Salvo!\n') 
f = input('Digite um valor para localizar as chaves interligadas:\n')

buscar(clientes,f)
