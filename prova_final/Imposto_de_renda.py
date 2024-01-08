# EXERCÍCIO IMPOSTO DE RENDA
def calcular_imposto_renda(salario):
    if salario <= 1000:
        print('\033[1mSeu imposto de renda é isento.\033[0m')
    elif salario >= 1001 and salario <= 3000:
       salario += (salario*10/100)
    elif salario >= 3001 and salario <= 5000:
        salario += (salario*20/100)
    else:
        salario += (salario*30/100)
    return salario

salario = int(input('Qual é seu salário bruto?\nR$'))
imposto = calcular_imposto_renda(salario)
print(f'\033[1mO imposto de renda a ser pago é R${imposto:.0f}\033[0m')
print('\033[32;1mCaso seu imposto de renda seja isento você não pagará.\033[0m')