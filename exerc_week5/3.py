soma = 0
while True:
    n = int(input('Digite um número inteiro positivo (ou um valor negativo para sair): '))
    
    if n < 0:
        break

# %(resto da divisão) diferente de 0
    if n % 2 != 0:
        soma += n

print(f'A soma dos números impares entre 1 e o número digitado é: {soma}')
