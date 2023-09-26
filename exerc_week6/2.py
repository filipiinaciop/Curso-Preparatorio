def opcoes():
    print("[1] Lucas")
    print("[2] Wellington")
    print("[3] Gabriella")
    print("[4] Voto em branco")
    print("[5] Voto nulo")
    
def eleicao():
    candidatos = {
        1: 'Lucas',
        2: 'Wellington',
        3: 'Gabriella',
        4: 'Voto em branco',
        5: 'Voto nulo' 
    }
    votos = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0}

    while True:
        opcoes()
        print("Escolha um candidato (ou 4 para voto em branco, 5 para voto nulo)")
        voto = int(input('Digite o número do candito (ou 0 para encerrar a votação): '))

        if voto == 0:
            break
        
        if voto in candidatos:
            votos[voto] += 1
        else:
            votos[5] += 1 #voto nulo..
        
        tv = sum(votos.values())
        v_validos = tv - votos[4] - votos[5]

        if tv == 0:
            print('Nenhum voto válido registrado.')
        else:
            #max como um dicionario, votos.get é usada para obter o valor associado a uma chave no dicionário.
            vencedor = max(votos, key=votos.get)
            porcetagem_vencedor = (votos[vencedor] / v_validos) * 100

            print(f'Quantidade de votos válidos: {v_validos}')
            print(f'Vencedor: {candidatos[vencedor]}')
            print(f'Porcentagem de votos do vencedor: {porcetagem_vencedor: .2f}%')
eleicao()