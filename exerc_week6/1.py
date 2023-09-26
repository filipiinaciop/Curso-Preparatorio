alunos = int(input('Qual o número de alunos na sala?  '))
cont = 0
aprovado = 0
reprovado = 0
MM = -float('inf')
mm = float('inf')
while True:
    nome = input('Nome aluno: ')
    n1 = float(input(f'Digite a primeira nota do {nome}: '))
    if n1 > 10 or n1 < 0:
        print('Digite somente valores entre 0 e 10.')
        break
    else:
        ''    
    n2 = float(input(f'Digite a segunda nota do {nome}: '))
    if n2 > 10 or n2 < 0:
        print('Digite somente valores entre 0 e 10.')
        break
    else:
        ''        
    n3 = float(input(f'Digite a terceira nota do {nome}: '))
    if n3 > 10 or n3 < 0:
        print('Digite somente valores entre 0 e 10.')
        break
    else:
        ''    
    cont += 1
    media = n1 * 20/100 + n2 * 30/100 + n3 * 50/100
    print(f'A média final do aluno {nome} foi {media:.1f}')
    fim = input("Deseja continuar? N\S  ")
    fim2 = fim.lower()
    if media > MM:
        MM = media
        nomeMM = nome
    if media < mm:
        mm = media
        nomemm = nome    
    if fim2 == 'n' and  alunos == 1:
        print(f'Digite novamente as notas de {nome}')
        n1 = float(input(f'Digite a primeira nota do {nome}: '))
        n2 = float(input(f'Digite a segunda nota do {nome}: '))
        n3 = float(input(f'Digite a terceira nota do {nome}: ')) 
        media = n1 * 20/100 + n2 * 30/100 + n3 * 50/100
        if media >=  7:
            aprovado += 1
        else:
            reprovado += 1
        print(f'A média final do aluno {nome} foi {media:.1f}')
        print(f'A turma teve:\nAprovados: {aprovado}\nReprovados: {reprovado}')
        break
    elif alunos == cont :
        if media >=  7:
            aprovado += 1
        else:
            reprovado += 1
        print(f'A turma teve:\nAprovados: {aprovado}\nReprovados: {reprovado}\nMaior média: {MM:.1f} do aluno/a {nomeMM}\nMenor média: {mm:.1f} do aluno {nomemm}')
        break
    elif fim2 == 'n' and alunos >= 2: 
        #PROCESSO EM CASO DE MAIS DE UM ALUNO E DIGITADO N
        print(f'Digite novamente as notas de {nome}')
        n1 = float(input('Digite a primeira nota: '))
        n2 = float(input('Digite a segunda nota: '))
        n3 = float(input('Digite a terceira nota: ')) 
        media = n1 * 20/100 + n2 * 30/100 + n3 * 50/100
        if media >=  7:
            aprovado += 1
        else:
            reprovado += 1
        print(f'A média final do aluno {nome} foi {media:.1f}')
        print(f'A turma teve:\nAprovados: {aprovado}\nReprovados: {reprovado}')
        cont
    else:
        print('')
        
#nao consegui fazer uma parte do aprovado e desaprovado