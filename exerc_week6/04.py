dim = float(input('Digite a quantia para investimento: R$'))
meses = int(input('Digite a quantidade de meses: '))
if dim <= 2000:
    juros = 0.005          #Até R$ 2.000,00 0,5%
elif dim <= 10000:
    juros = 0.01          #Entre R$ 2.000,00 e R$ 10.000,00 1,0%
else:
    juros = 0.015           #A partir de R$ 10.000,00 1,5%
temp = 0
l1 = 2000
l2 = 10000     #AGORA APLICAR ISSO NO WHILE DEFINDO LIMITES
while temp < meses:
    fim = dim * (1 + juros) **meses # FORMULA JUROS COMPOSTO
    if fim >= l1 and fim < l2:
        juros = 0.01
    elif fim >= l2:
        juros = 0.015     
    temp += 1
print(f'A quantia de R${dim} em {meses} meses terminou em R${fim:.2f}')
