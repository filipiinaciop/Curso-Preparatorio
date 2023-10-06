egt = int(input('Escreva o número de alunos na escola Germinare TECH: '))
egb = int(input('Escreva o número de alunos na escola Germinare Business: '))

if egt > egb:
    print('ja é maior')
else:
    for a in range(1, 1000):
        egt *= 1.50
        egb *= 1.10

        if egt > egb:
            break

print(f'Em {a} anos a Germinare TECH ultrapassará a Germinare Business em alunos')