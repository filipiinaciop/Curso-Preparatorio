import datetime

salario_inicial = float(input('Digite o salário inicial do funcionário: $'))
ano = int(input('Digite o ano de contratação do funcionário: '))

#percentual aumento
pa = 0.015 

hoje = datetime.datetime.now().year #date 2023

#NO PRIMEIRO ANO O PERCENTUAL DE AUMENTO SERA DE    1,5%, A PARTIR DO SEGUNDO ANO OS AUMENTOS SALARIAIS SERAO PROGRESSIVOS COM UM ACRESIMO DE 10% SOBRE O PERCENTUAL DO AUMENTO ANTERIOR.DEVE-SE EXIBIR  O SALARIO ATUAL DO FUNCIONARIO E QUANTOS % TEVE EM RELACAO AO SALARIO INICIAL

while ano < hoje:
    aumento = salario_inicial * pa
    salario_inicial += aumento
    pa += 0.015
    ano += 1

total_aumento = ((salario_inicial - 1000) / 1000) * 100
print(f'O salário atual do funcionário é ${salario_inicial:.2f}')  #Salario final arrendondado
print(f'A porcentagem total em relação ao salário inicial é {total_aumento:.2f}%')
