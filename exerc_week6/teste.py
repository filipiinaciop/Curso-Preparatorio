# Inicialização de variáveis
aprovados = 0
reprovados = 0
soma_medias = 0
maior_media = float("-inf")
menor_media = float("inf")

# Pergunta ao usuário quantos alunos têm na turma e armazena essa informação em numero_alunos
numero_alunos = int(input("Quantos alunos têm na turma? "))
aluno_atual = 1

# Inicia um loop while que continuará até que todos os alunos tenham suas notas avaliadas
while aluno_atual <= numero_alunos:
    nome_aluno = input(f"Digite o nome do aluno {aluno_atual}: ")
    
    nota1 = -1
    nota2 = -1
    nota3 = -1

    while nota1 < 0 or nota1 > 10:
        nota1 = float(input(f"Digite a nota 1 do aluno {nome_aluno}: "))
    
    while nota2 < 0 or nota2 > 10:
        nota2 = float(input(f"Digite a nota 2 do aluno {nome_aluno}: "))
    
    while nota3 < 0 or nota3 > 10:
        nota3 = float(input(f"Digite a nota 3 do aluno {nome_aluno}: "))

    media_aluno = nota1 * 0.2 + nota2 * 0.3 + nota3 * 0.5
    soma_medias += media_aluno
    
    if media_aluno >= 7.0:
        situacao = "Aprovado"
        aprovados += 1
    else:
        situacao = "Reprovado"
        reprovados += 1
    
    if media_aluno > maior_media:
        maior_media = media_aluno
        aluno_maior_media = nome_aluno
    
    if media_aluno < menor_media:
        menor_media = media_aluno
        aluno_menor_media = nome_aluno
    
    print(f"Média do aluno {nome_aluno}: {media_aluno:.2f} - Situação: {situacao}")
    
    # Pergunta se o usuário deseja reeditar a nota do aluno
    reeditar = input("Deseja reeditar a nota deste aluno? (S/N): ").strip().lower()
    if reeditar == "s":
        continue  # Retorna ao início do loop para reeditar a nota do mesmo aluno
    
    aluno_atual += 1

porcentagem_aprovados = (aprovados / numero_alunos) * 100
porcentagem_reprovados = (reprovados / numero_alunos) * 100
media_turma = soma_medias / numero_alunos

print("\nResultados Finais:")
print(f"Total de alunos aprovados: {aprovados} ({porcentagem_aprovados:.2f}%)")
print(f"Total de alunos reprovados: {reprovados} ({porcentagem_reprovados:.2f}%)")
print(f"Média da turma: {media_turma:.2f}")
print(f"Maior média da turma: {maior_media:.2f} (Aluno: {aluno_maior_media})")
print(f"Menor média da turma: {menor_media:.2f} (Aluno: {aluno_menor_media})")

