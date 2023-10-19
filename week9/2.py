s = "Aprovado"
no = "Reprovado"
boletim = []
c1 = int(input('Digite a quantidade de alunos na sala: ')) 
c2 = 0 #Contagem para num de aluno
c3 = 0 #Contar pra finalizar,fim!
for c in range(c1):
    n = input(f'Digite o nome do(a) {c2+1}° aluno(a): ')
    n1 = float(input(f'Digite a 1° nota de {n}: '))
    n2 = float(input(f'Digite a 2° nota de {n}: '))
    if  n1 <= 10 and n1 >= 0 and n2 <= 10 and n2 >= 0:
        c3 += 1
        c2 += 1
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
print('\033[1mN:    Alunos:  Nota1:    Nota2:   Média:       Conceito\033[0m')
for i,a in enumerate(boletim, start=1):
    a = f'{i}     {a}'
    print(a)
