c = float(input('Digite o depósito inicial: R$'))
i = float(input('Agora, digite a taxa de juros de uma poupança: '))
t = 1   # Contador dos meses
c2 = None
while t <= 24:
    m = c * (1 + (i / 100)) ** t
    if t == 1:
        print(f'\nNo mês {t}, o valor dos juros será igual a R${m:.2f}')
    else:
        print(f'\nNo mês {t}, o valor dos juros será igual a R${m:.2f}')

    if t == 24:
        break

    t = t + 1

    op = input(f'Deseja realizar um depósito para o {t}° mês[S/N]? ').strip().upper()[0]

    while op != 'S' and op != 'N':
        op = input(f'OPÇÃO INVÁLIDA! Deseja realizar um depósito para o {t}° mês[S/N]? ').strip().upper()[0]

    if op == 'S':
        c2 = float(input(f'Digite o valor do depósito do {t}° mês: R$'))

    else:
        c2 = 0
    c = c2 + m

j = c * (1 + (i / 100)) ** t
print(f'No total, a quantidade de reais ganha com os JUROS COMPOSTOS será igual a R${j - c:.2f}')
