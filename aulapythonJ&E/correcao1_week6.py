def validar_nota(nome):
    while True:
        nota = float(input(f'Digite a nota de  {nome}'))
        if nota >= 0 and nota <= 10:
            break
        else:
            print('Nota inválida. A nota deve ser de 0 a 10.')

alunos = int(input('Quantos alunos tem na turma: '))
cont = 0
soma = 0
aprov = 0

while cont < alunos:
    nome = input('Qual o nome do aluno:')
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

