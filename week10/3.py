def letras(palavra):
    cl = {}
    palavra = palavra.upper()

    for letra in palavra:
        if letra.isalpha():
            if letra in cl:
                cl[letra] += 1
            else:
                cl[letra] = 1
    
    for letra, contagem in cl.items():
        print(f'Letra {letra} aparece {contagem} vezes.')
    
x = input('Digite uma palavra que deseja contar as letras:\n')
letras(x)
