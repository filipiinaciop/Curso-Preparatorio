p = [0, 0, 0, 0, 0, 0, 0, 0, 0]
#OU
# p = [0]*9
#1ª posição: $200 - $299
#2ª posição: $300 - $399
#3ª posição: $400 - $499
#4ª posição: $500 - $599
#5ª posição: $600 - $699
#6ª posição: $700 - $799
#7ª posição: $800 - $899
#8ª posição: $900 - $999
#9ª posição: $1000 em diante
# NãO FAÇA COM IFS ALINHADOS.

def att(valor):
    posicao = int((valor - 200) / 100)
    
    if posicao < 0:
        posicao = 0
    elif posicao > 8:
        posicao = 8
    
    p[posicao] += 1
    return posicao + 1

while True:
    v = float(input('Insira um valor (ou digite uma valor negativo para encerrar): '))
    if v < 0:
        break
    valor = (0.09 * v) + 200 #pega a porcentagem e ja soma
    posicao = att(valor)
for posicao, contagem in enumerate(p):
    print(f'Posição {posicao + 1} - {contagem} entradas')
