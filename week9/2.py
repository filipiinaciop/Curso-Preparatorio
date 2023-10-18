s = "Aprovado"
no = "Reprovado"
boletim = []
print('Boletins!\n')
c1 = int(input('Digite a quantidade de alunos na sala: ')) #inicio
c2 = 1 #Contagem para num de aluno
c3 = 0 #Contar pra finalizar,fim!
while c1 != c3:
    n = input(f'Digite o nome do(a) {c2}° aluno(a): ')
    n1 = float(input(f'Digite a 1° nota de {n}: '))
    n2 = float(input(f'Digite a 2° nota de {n}: '))
    if  n1 <= 10 and n1 >= 0 and n2 <= 10 and n2 >= 0:  
        fim = input("Deseja continuar? N/S  ")
        if fim.lower() == 'n':
            while fim.lower() == 'n':
                n1 = float(input(f'Digite a 1° nota de {n}: '))
                n2 = float(input(f'Digite a 2° nota de {n}: '))
                fim = input("Deseja continuar? N/S  ")
                if fim.lower() == 's':
                    break
        if fim.lower() == 's':
            c2 += 1
            c3 += 1
            n3 = (n1 + n2) / 2
            if n3 >= 7:
                t = s
            else:
                t = no    
            cj = (f'{n:6}   {n1:5}    {n2:5}    {n3:5}         {t:8}')  
            boletim.append(cj)
            #print(f'{c1,c3}')
            if c1 != c3:
               continue 
print('\033[1mN:    Alunos:    Nota1:    Nota2:    Média:    Conceito\033[0m')
for indice,a in enumerate(boletim, start=1):
    a = f'{indice}     {a}'
    print(a)
