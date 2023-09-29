def validar_nota(nome):
    while True:
        nota = float(input(f'Digite a nota de  {nome}: '))
        if nota >= 0 and nota <= 10:
            break
        else:
            print('Nota inválida. A nota deve ser de 0 a 10.')

alunos = int(input('Quantos alunos tem na turma: '))
cont = 0
soma = 0
aprov = 0

while cont < alunos:
    nome = input('Qual o nome do aluno: ')
    while True:
        n1 = validar_nota(nome)
        n2 = validar_nota(nome)
        n3 = validar_nota(nome)
        media = n1 * 0.2 + n2 * 0.3 + n3 * 0.5
        print(f'Média de {nome} = {media: .2f}')
        if media >= 7:
            print('Aprovado')
        else:
            print('Reprovado')
        p = input('Continuar proximo: (S/N)')
        if p == 's':
            break
        soma += media
        if media >= 7:
            aprov += 1
        if cont == 1:
            maiorMed = media
            nome_MM = nome
            menormed = media 
            nome_mm = nome
        elif media > maiorMed:
            MM = media
            nome_MM = nome
        elif media < menormed:
            mm = media
            nome_mm = nome 
        media_turma = soma / alunos
        reprov = alunos - aprov
        pa = aprov / alunos * 100
        pr = reprov / alunos * 100

print(f'Resultado: \n Aprovados: {aprov} [{pa:.2f}%] \n Reprovados: {reprov} [{pr:.2f}%]')
print(f'\nMaior média: {maiorMed:.1f} de {nome_MM}!\nMenor média: {menormed:.1f} de {nome_mm}!')
