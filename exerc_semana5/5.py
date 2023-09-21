def div(div_inici,pay):
    m = 1 #aqui tempo em meses.
    div = div_inicial
    while div > 0:    #se.
        divi0 = div
        if div >= pay: #se div maior ou igual money
            div -= pay #div diminui menos money?
        else:        # se não.
            div = 0
        print(f"Mês {m}:")      #info
        print(f"Valor da dívida antes do pagamento: R${divi0:.2f}")
        print(f"Valor da dívida após o pagamento: R${div:.2f}\n")
        m += 1 #tempo em mes.
div_inicial = float(input("Digite o valor da dívida inicial: \nR$"))
pay= float(input("Digite o valor do pagamento mensal: \nR$"))
div(div_inicial,pay)
