def buscar_chaves(dic, buscado):
    lista_chaves = []
    for chave, valor in dic.items():
        if buscado in valor:
            lista_chaves.append(chave)
    return lista_chaves

# operadora = input('Digite sua operadora de celular')
clientes = {
    'nome': 'Ana Maria Braga',
    'endereco': 'Av. Augusta Maria',
    'OperadoraCelular': 'Vivo'
}
valor_buscado = input('Digite valor buscado: ')
chaves = buscar_chaves(clientes, valor_buscado) 
print(chaves)
clientes['OperadoraCelular'] = 'Claro'
clientes['cidade'] = 'Sao paulo'
print(clientes)