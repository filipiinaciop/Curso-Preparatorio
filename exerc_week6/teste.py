# Inicialização de variáveis
aprovados = 0
reprovados = 0
soma_medias = 0
maior_media = float("-inf")  # Inicializada com valor negativo
menor_media = float("inf")  # Inicializada com valor positivo

# Pergunta quantos alunos têm na turma
numero_alunos = int(input("Quantos alunos têm na turma? "))
aluno_atual = 1

# Use um loop while para receber as notas de cada aluno
while aluno_atual <= numero_alunos:
    nome_aluno = input(f"Digite o nome do aluno {aluno_atual}: ")
    
    # Inicialização das notas
    nota1 = -1
    nota2 = -1
    nota3 = -1

    # Solicita as notas e verifica se estão no intervalo correto (0 a 10)
    while nota1 < 0 or nota1 > 10:
        nota1 = float(input(f"Digite a nota 1 do aluno {nome_aluno}: "))
    
    while nota2 < 0 or nota2 > 10:
        nota2 = float(input(f"Digite a nota 2 do aluno {nome_aluno}: "))
    
    while nota3 < 0 or nota3 > 10:
        nota3 = float(input(f"Digite a nota 3 do aluno {nome_aluno}: "))

    # Calcula a média ponderada
    media_aluno = nota1 * 0.2 + nota2 * 0.3 + nota3 * 0.5
    soma_medias += media_aluno
    
    # Verifica se o aluno foi aprovado ou reprovado
    if media_aluno >= 7.0:
        situacao = "Aprovado"
        aprovados += 1
    else:
        situacao = "Reprovado"
        reprovados += 1
    
    # Atualiza as informações sobre a maior e menor média e os respectivos alunos
    if media_aluno > maior_media:
        maior_media = media_aluno
        aluno_maior_media = nome_aluno
    
    if media_aluno < menor_media:
        menor_media = media_aluno
        aluno_menor_media = nome_aluno
    
    # Exibe a média e a situação do aluno
    print(f"Média do aluno {nome_aluno}: {media_aluno:.2f} - Situação: {situacao}")
    
    # Incrementa o contador do aluno atual e solicita confirmação
    aluno_atual += 1
    input("Pressione Enter para continuar para o próximo aluno...")

# Calcula a porcentagem de aprovados e reprovados
porcentagem_aprovados = (aprovados / numero_alunos) * 100
porcentagem_reprovados = (reprovados / numero_alunos) * 100

# Calcula a média da turma
media_turma = soma_medias / numero_alunos

# Apresenta os resultados finais
print("\nResultados Finais:")
print(f"Total de alunos aprovados: {aprovados} ({porcentagem_aprovados:.2f}%)")
print(f"Total de alunos reprovados: {reprovados} ({porcentagem_reprovados:.2f}%)")
print(f"Média da turma: {media_turma:.2f}")
print(f"Maior média da turma: {maior_media:.2f} (Aluno: {aluno_maior_media})")
print(f"Menor média da turma: {menor_media:.2f} (Aluno: {aluno_menor_media})")
