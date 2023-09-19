import random

def difficult_easy():
    n = random.randint(1, 10)
    adivinhe = int(input('Adivinhe o número de 1 a 10?'))
    while (n != adivinhe):
       if (n > adivinhe):
          print(f'Errado, o número {adivinhe} é maior que o correto. Tente novamente')
          