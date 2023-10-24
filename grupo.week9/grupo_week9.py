# Ana Clara  Wolf / Carolina Mendes / Filipi Inacio / Marina Peixoto

import random
codigo = []
autor = []
titulo = []
def entrada():
    for i in range(999):
        tit = input('Qual é o nome do livro? ')
        aut = input('Qual é o autor do livro desejado? ')
        cod = random.randint(1000, 9999)
        # cod = titulo, autor
        titulo.append(tit)
        autor.append(aut)
        codigo.append(cod)
        print(codigo)
        break
    # if titulo and autor < 3:
    #     return False 
    # else:
    #     return True

def remover_livro():
    remover = int(input('Digite o codigo do livro que deseja remover: '))
    codigo.remove(remover)
    print(codigo)

# def ordem_cadastro():
#     ordem = codigo.list()
#     print(codigo)
# def crescente():
#     cres = codigo.sort()
#     print(codigo)
# def alfa_titulo():
#     alfabetica_titulo = codigo.sort(titulo)

op = 0
while op != 7:
    print('''[ 1 ] Adicionar livro
    [ 2 ] Mostrar os livros por ordem de cadastro.
    [ 3 ] Mostrar os livros por ordem alfabética por titulo.
    [ 4 ] Mostrar livros por ordem alfabética pelo autor
    [ 5 ] Mostrar os livros em ordem crescente do código.
    [ 6 ] Remover livro.''')
    op = int(input('Qual opção voce quer?'))
    if op == 1:
        entrada()
    # if op == 2:
    #     ordem_cadastro()
    # if op == 5:
    #     crescente()
    if op == 6:
        remover_livro()
