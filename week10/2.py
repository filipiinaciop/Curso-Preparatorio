def compra(conta, valor):
    conta['transações'] += 1
    conta['saldo'] -= valor
    conta['media'] = conta['saldo'] / conta['transações']

conta = {
    'transações': 0,
    'saldo': 1000,
    'media': 0
}

print(f'Saldo atual = \033[32m{conta["saldo"]}\033[0m')
while True:
    vc = float(input('Digite o valor da compra (ou negativo para encerrar):\n'))
    if vc <= 0:
        break
    compra(conta, vc)
    if conta['saldo'] > 0:
        print(f'Transações: {conta["transações"]}\nSaldo: \033[32m{conta["saldo"]}\033[0m\nMédia: {conta["media"]:.1f}')
    else:
            print(f'Transações: {conta["transações"]}\nSaldo: \033[31m{conta["saldo"]:.1f}\033[0m\nMédia: {conta["media"]:.1f}')

print()