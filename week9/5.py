def tab_tabuleiro(tabuleiro):
    for linha in tabuleiro:
        print(' '.join(linha)) #join p/ concatenar linha
    print()
def verific_win(tabuleiro, jogador):
    for linha in tabuleiro:
        if all(c == jogador for c in linha):
            return True
    
    for coluna in range(3):
        if all(tabuleiro[linha][coluna] == jogador for linha in range(3)):
            return True
    
    if all(tabuleiro[i][i] == jogador for i in range(3))or all(tabuleiro[i][2 -i] == jogador for i in range(3)):
        return True
    return False

def jogo():
    tabuleiro = [['-' for _ in range(3)] for _ in range(3)]
    jogador = 'X'
    rodadas = 0
    while True:
        tab_tabuleiro(tabuleiro)

        linha = int(input(f'Jogador {jogador}\nLinha:')) - 1
        coluna = int(input('Coluna: ')) - 1

        if 0 <= linha < 3 and 0 <= coluna < 3 and tabuleiro[linha][coluna] == '-':
            tabuleiro[linha][coluna] = jogador
            rodadas += 1

            if verific_win(tabuleiro, jogador):
                tabuleiro(tabuleiro)
                print(f'Jogador {jogador} ganhou após {rodadas} rodadas.')
                break
            if rodadas == 9:
                tabuleiro(tabuleiro)
                print('Deu velha.')
            
            jogador = 'X' if jogador == 'O' else 'O'
        else:
            print('Opção inválida. Jogue de novo!')
jogo()