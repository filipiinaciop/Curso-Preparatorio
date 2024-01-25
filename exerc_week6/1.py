import sys
alunos = int(input('Quantos alunos há na turma?\n'))
cont = 0
aprovados = 0
reprovados = 0
soma = 0
medmax = -float('inf')
medmin = float('inf')
while True:
   nome = input(f'Digite o nome do aluno: ')
   n1 = float(input('Digite a primeira nota: '))
   n2 = float(input('Digite a segunda nota: '))
   n3 = float(input('Digite a terceira nota: '))
    
   if n1 < 0 or n2 < 0 or n3 < 0:
      print('Somente são aceitos valores de 0 a 10')
      break
   elif n1 > 10 or n2 > 10 or n3 > 10:
      print('Somente são aceitos valores de 0 a 10')
      break
   media = n1 * 0.2 + n2 * 0.3 + n3 * 0.5
   cont += 1
   print(f'Média do aluno {nome}: {media: .2f}')
   while True:
      fim = input('Deseja continuar? N/S')
      fim = fim.lower()
      if fim == 'n':
         print(f'Digite novamente as notas de {nome}')
         n1 = float(input('Digite a primeira nota: '))
         n2 = float(input('Digite a segunda nota: '))
         n3 = float(input('Digite a terceira nota: ')) 
         if n1 < 0 or n2 < 0 or n3 < 0:
            print('Somente são aceitos valores de (0.00 a 10.0)')
            sys.exit()   #COMO NAO É POSSIVEL BREAK USAMOS EXIT QUE FECHA TUDO  
         elif n1 > 10 or n2 > 10 or 3 > 10:
            print('Somente são aceitos valores de (0.00 a 10.0)')
            sys.exit()
         media = n1 * 20/100 + n2 * 30/100 + n3 * 50/100
         print(f'Média do aluno {nome}: {media: .2f}')
      else:
         break
   if media >= 7:
      aprovados += 1
   else:
      reprovados += 1
   if media > medmax:
      medmax = media
      nomemax = nome
   if media < medmin:
      medmin = media
      nomemin = nome
   porcem_aprov = (aprovados / alunos) * 100
   porcem_reprov = (reprovados / alunos) * 100
   tt = soma / alunos
   if cont == alunos:
      print()
      print(f'Resultado: \n Aprovados: {aprovados} [{porcem_aprov:.2f}%] \n Reprovados: {reprovados} [{porcem_reprov:.2f}%]')
      print(f'\nMaior média: {medmax:.1f} de {nomemax}!\nMenor média: {medmin:.1f} de {nomemin}!')
      break
   else:
      continue
