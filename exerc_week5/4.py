def eh_par_impar(num):
    if num % 2 == 0:
        return 'par'
    else:
        return 'impar'

def eh_primo(num):
    if num <= 1:
        return False
    #formulinha numeros primos,(range) para imprimir os numeros do meio dos resultados (1,3,5...)
    for x in range(2, int(num**0.5) + 1):
        if num % x == 0:
            return False
    return True

def eh_amstrong(num):
    n_str = str(num)
    #len = contagem de caracteres em uma lista
    n = len(n_str)
    soma = sum(int(digit) ** n for digit in n_str)
    return soma == num

def eh_quadrado_perfeito(num):
    if num < 0:
        return False 
    raiz = int(num ** 0.5)
    return raiz * raiz == num

def eh_palindromo(num):
    n_str = str(num)
    return n_str  == n_str[::-1]

def tem_fibonacci(num):
    a, b = 0, 1
    while a < num:
        a, b = a, b + b
        return a == num
    
num = int(input('Digite um número inteiro positivo: '))

print(f'{num} é um número {eh_par_impar(num)}.')
print(f"{num} é um número {'primo' if eh_primo(num) else 'não primo'}.")
print(f"{num} é um número {'de amstrong' if eh_amstrong(num) else 'não de Amsmtrong'}.")
print(f"{num} é um número {'quadrado perfgeito' if eh_quadrado_perfeito(num) else 'não quadrado perfeito'}.")
print(f"{num} é um número {'palindromo' if eh_palindromo(num) else 'não palindromo'}.")
print(f"{num} {'faz parte' if tem_fibonacci(num) else 'não faz parte'} da sequencia Fibonacci.")
