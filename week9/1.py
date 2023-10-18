conts = [0] * 9
vendas = [300, 470, 550, 600, 720, 850, 950, 1100]

for v in vendas:
    s = 200 + 0.09 * v
    posicao = int(min((s - 200) // 100, 8))
    conts[posicao] += 1

for i, cont in enumerate(conts):
    if i == 8:
        print(f"9ª posição: $1000 em diante: {cont} vendedores")
    else:
        print(f"{i+1}ª posição: ${200 + i*100} - ${299 + i*100}: {cont} vendedores")
# ARRUMAR CONTA
