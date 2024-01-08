# EXERCÍCIO ESTACIONAMENTO
esc = 0
placa = []
while True:
    placa_usuario = int(input('Qual a placa do seu carro? '))
    e_or_s = input('Entrada ou saída(E/S)? ')
    if e_or_s in 'Ee':
        placa.append(placa_usuario)
        hora = int(input("Digite a hora de entrada (0-23): "))
        min = int(input("Digite o minuto de entrada (0-59): "))
    elif e_or_s in 'Ss':
        plac = int(input('Digite a placa: '))
        if plac in placa:
            hora_saida = int(input("Digite a hora de saída (0-23): "))
            minuto_saida = int(input("Digite o minuto de saída (0-59): "))
        else:
            plac = int(input('A placa anterior não existia, por favor colocar um que ja tenha sido colocada.'))
    # tempo_entrada_em_minutos = hora * 60 + min
    # tempo_saida_em_minutos = hora_saida * 60 + minuto_saida
    # tempo_total_em_horas = (tempo_saida_em_minutos - tempo_entrada_em_minutos) / 60