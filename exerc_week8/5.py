import random

def itens_repetidos(tupla):
    for item in tupla:
        if tupla.count(item) > 1:
            return True
    return False

def pesquisar_e_contar_valor(tupla, valor):
    if valor in tupla:
        return tupla.count(valor)
    else:
        return 0
def tupla_random(tamanho, min, max):
    return tuple(random.randint(min, max) for _ in range(tamanho))

tupla_aleatoria = tupla_random(10, 1, 10)

while True:
    print('Foi criada uma tupla aleatória.')
    escolha = input("Deseja verificar itens repetidos nesta tupla? (S/N): ")
    
    if escolha.lower() == "s":
        if itens_repetidos(tupla_aleatoria):
            print("A tupla possui itens repetidos.")
        else:
            print("A tupla não possui itens repetidos.")
    
    valor_pesquisa = input("Digite um valor para pesquisar na tupla: ")
    try:
        valor_pesquisa = int(valor_pesquisa)
        ocorrencias = pesquisar_e_contar_valor(tupla_aleatoria, valor_pesquisa)
        if ocorrencias > 0:
            print(f"O valor {valor_pesquisa} foi encontrado na tupla e ocorre {ocorrencias} vez(es).")
        else:
            print(f"O valor {valor_pesquisa} não foi encontrado na tupla.")
    except ValueError:
        print("Entrada inválida. Por favor, digite um número.")
    
    continuar = input("Deseja continuar? (S/N): ")
    if continuar.lower() != "s":
        break
