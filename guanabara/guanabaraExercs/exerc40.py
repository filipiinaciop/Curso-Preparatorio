nota = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
media = (nota + nota2) / 2
print(f'Tirando {nota: .1f} e {nota2: .1f}, a media do aluno é {media: .1f}')
if 7 > media >= 5:
    print('O aluno está em RECUPERAÇÃO.0')
elif media < 5:
    print('O aluno está REPROVADO.')
elif media >= 7:
    print('O Aluno está APROVADO.')
