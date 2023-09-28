aprovados = 0
reprovados = 0
soma = 0
MM = float('-inf')  #valor negativo
mm = float('inf')  #....

alunos = int(input('Quantos alunos há na turma?\n'))
aluno_atual = 1

while aluno_atual <= alunos:
    nome = input(f'Digite o nome do aluno {aluno_atual}: ')

    n1 = -1
    n2 = -1   #usando valores invalidos para não
    n3 = -1   #contar

    while n1 < 0 or n1 > 10:
        n1 = float(input(f'DIgite a nota 1 do aluno {nome}: '))
    while n2 < 0 or n2 > 10:
        n2 = float(input(f'Digite a nota 2 do aluno {nome}:'))
    while n3 < 0 or n3 >10:
        n3 = float(input(f'Digite a nota 3 do aluno {nome}: '))
    
    media = n1 * 0.2 + n2 * 0.3 + n3 * 0.5
    soma += media
    
    if media >= 7:
       s = '\033[32mAprovado\033[0m'
       aprovados += 1
    else:
       s = '\033[31mReprovado\033[0m'
       reprovados += 1

    if media > MM:
       MM = media
       aluno_MM = nome
    if media < mm:
       mm = media
       aluno_mm = nome
    
    print(f'Média do aluno {nome}: {media: .2f} - situacao: {s}.')
    #editar
    editar = input('Deseja editar a nota deste aluno? (S/N): ').strip().lower()
    if editar == 's':
        continue #retorna ao inicio do loop para reeditar a nota do msm aluno
    
    aluno_atual += 1

porcem_aprov = (aprovados / alunos) * 100
porcem_reprov = (reprovados / alunos) * 100
tt = soma / alunos

print(f'Resultado:')
print(f'Aprovados: {aprovados} ({porcem_aprov: .2f}%)')
print(f'Reprovados: {reprovados} ({porcem_reprov: .2f}%)')
print(f'Média da turma: {tt: .2f}')
print(f'Maior média da turma: {MM: .2f} (aluno: {aluno_MM})')
print(f'Menor média da turma: {mm: .2f} (Aluno: {aluno_mm})')
