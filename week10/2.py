def compra(conta, valor):
    conta['transações'] += 1
    conta['saldo'] -= valor
    conta['media'] = conta['saldo'] / conta['transações']

conta = {
    'transações': 0,
    'saldo': 1000,
    'media': 0
}

print(f'Saldo atual = {conta["saldo"]}')
while True:
    vc = float(input('Digite o valor da compra (ou negativo para encerrar):\n'))
    if vc <= 0:
        break
    compra(conta, vc)
    print(f'Transações: {conta["transações"]}\nSaldo: {conta["saldo"]}\nMédia: {conta["media"]:.1f}')

print()