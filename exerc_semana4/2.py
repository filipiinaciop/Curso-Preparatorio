def main():
    # Solicitar informações do cliente
    valor_emprestimo = float(input("Quanto voce deseja pegar emprestado? "))
    renda = float(input("Qual sua renda mensal atual? "))
    
    #Perguntar ao cliente e obter respostas
    score = input("Seu Score de crédito é acima de 450 pontos? (SIM ou NÃO): \n").upper()
    dividas_ativas = input("Voce não possui dívidas ativas? (SIM ou NÃO): \n").upper()
    funcionario_publico = input("Voce é funcionário público? (SIM ou NÃO): \n").upper()
    open_banking = input("Voce concorda em compartilhar seus dados de outros bancos através do open banking? (SIM ou NÃO): \n").upper()
    
    # Validação adicional da renda
    renda_suficiente = renda >= 2 * valor_emprestimo
    
    # Contar respostas positivas
    respostas_positivas = 0
    if score == "SIM":
        respostas_positivas += 1
    if dividas_ativas == "SIM":
        respostas_positivas += 1
    if funcionario_publico == "SIM":
        respostas_positivas += 1
    if open_banking == "SIM":
        respostas_positivas += 1
    
    # Verificar a situação de aprovação
    if respostas_positivas >= 3:
        if renda_suficiente:
            situacao = "Aprovação total, valor aprovado"
            valor_aprovado = valor_emprestimo
        else:
            situacao = 'Aprovado com desconto, valor aprovado'
            valor_aprovado = valor_emprestimo * 0.6
    elif respostas_positivas >= 2:
        situacao = 'Aprovado com restrições, valor aprovado'
        valor_aprovado = valor_emprestimo * 0.2
    else:
        situacao = 'Não aprovado'
        valor_aprovado = valor_emprestimo * 0.0

    #Exibir resultado
    print(f"Sua pontuação foi de {respostas_positivas}")
    print(f"{situacao} R${valor_aprovado:.2f}")

if __name__ == "__main__":
    main()