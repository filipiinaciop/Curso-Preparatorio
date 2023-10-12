def retençao(assinantes,cancelamentos,acessos_canal_rural):
    z = 0
    m = 1
    for x in range(6):
        retençao = (assinantes[0+z] - cancelamentos[0+z]) / assinantes[0+z] * 100
        print(f'\033[1mA retenção de assinantes no mês {m} foi de {retençao:.2f}%') #comum
        retençao2 = (acessos_canal_rural[0+z] - cancelamentos[0+z]) / acessos_canal_rural[0+z] * 100
        print(f'A rentenção de Acessos no Canal Rural no mês {m} foi de {retençao2:.2f}%\033[0m')
        print()
        m += 1
        z += 1


assinantes = (10000,10500,11000,11200,11500,11800)
x = max(assinantes)
x = assinantes.index(x)
x += 1 

cancelamentos = (500,450,500,200,300,200)

acessos_canal_rural = (2000,2200,2500,2600,2700,2800)
y = max(acessos_canal_rural)
y = acessos_canal_rural.index(y)
y += 1

retençao(assinantes,cancelamentos,acessos_canal_rural)
print(f'\033[35;1mO {x}° mês teve maior taxa de renteção de Assinantes:')
print(f'O {y}° mês teve maior taxa de renteção de Acessos ao Canal Rural:\033[0m')