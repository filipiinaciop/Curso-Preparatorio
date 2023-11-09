def validar_idade():
    while True:
        try:
            idade = int(input("Por favor, digite sua idade: "))
            if idade >= 0 and idade <= 120:
                return idade  # Retorna a idade válida
            else:
                print("Idade fora do intervalo válido (0-120). Tente novamente.")
        except ValueError:
            print("Entrada inválida. Digite um número inteiro válido.")

# Chama a função para obter uma idade válida
idade_valida = validar_idade()
print("Sua idade é:", idade_valida)
