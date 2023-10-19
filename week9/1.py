conts = [0] * 9 # *9 pois cria 9 casas, e todos inicializados como 0.
#por isso amo Guanabara heheh
salarios = [470, 320, 420, 590, 680, 750, 860, 920, 1050]

for s in salarios:
    indice = (s - 200) // 100
    if 0 <= indice < len(conts):
        conts[indice] += 1

for i, cont in enumerate(conts):
    if i == 8:
        print(f"{i + 1} posição: $1000 em diante - {cont} vendedores")
    else:
        print(f"{i + 1} posição: ${200 + i * 100} - ${299 + i * 100} - {cont} vendedores")
