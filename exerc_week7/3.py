egt = int(input('Escreva o número de alunos na escola Germinare TECH: '))
egb = int(input('Escreva o número de alunos na escola Germinare Business: '))

anos = 0

for a in range(1, 1000):
    egt *= 1.50
    egb *= 1.10
    anos += 1

    if egt > egb:
        break

print(f'Em {anos} anos a Germinare TECH ultrapassará a Germinare Business em alunos')