import math

# Solicitar horário de entrada e saída ao usuário
hora = int(input("Digite a hora de entrada (0-23): "))
min = int(input("Digite o minuto de entrada (0-59): "))
hora_saida = int(input("Digite a hora de saída (0-23): "))
minuto_saida = int(input("Digite o minuto de saída (0-59): "))

# Calcular o tempo total de estacionamento em minutos
tempo_entrada_em_minutos = hora * 60 + min
tempo_saida_em_minutos = hora_saida * 60 + minuto_saida

# Lidar com a saída no dia seguinte
if tempo_entrada_em_minutos > tempo_saida_em_minutos:
    tempo_saida_em_minutos += 24 * 60

# Calcular o tempo total de estacionamento em horas
tempo_total_em_horas = (tempo_saida_em_minutos - tempo_entrada_em_minutos) / 60

# Arredondar o tempo total de estacionamento para cima
tempo_total_arredondado = math.ceil(tempo_total_em_horas)

# Calcular o preço com base no tempo total
if tempo_total_arredondado <= 2:
    preco = tempo_total_arredondado * 1.00
elif tempo_total_arredondado <= 4:
    preco = 2 * 1.00 + (tempo_total_arredondado - 2) * 1.40
else:
    preco = 2 * 1.00 + 2 * 1.40 + (tempo_total_arredondado - 4) * 2.00

# Exibir o preço cobrado pelo estacionamento
print(f"O preço cobrado pelo estacionamento é R${preco:.2f}")