assinantes = (10000, 10500, 11000, 11200, 11500, 11800)
cancelamentos = (500, 450, 500, 200, 300, 200)
acessos_canal_rural = (2000, 2200, 2500, 2600, 2700, 2800)

taxa_ret_base_total = []
for i in range(1, len(assinantes)):
    taxa_ret = (assinantes[i] - cancelamentos[i]) / assinantes[i - 1] * 100
    taxa_ret_base_total.append(taxa_ret)

taxa_ret_canal_rural = []
for i in range(1, len(acessos_canal_rural)):
    taxa_ret = (acessos_canal_rural[i] - cancelamentos[i]) / acessos_canal_rural[i - 1] * 100
    taxa_ret_canal_rural.append(taxa_ret)

# Encontrar o mês com a maior retenção para a base total de assinantes
mes_maior_ret_base_total = taxa_ret_base_total.index(max(taxa_ret_base_total)) + 1

# Encontrar o mês com a maior retenção para os assinantes que acessam o Canal Rural
mes_maior_ret_canal_rural = taxa_ret_canal_rural.index(max(taxa_ret_canal_rural)) + 1

# Imprimir os resultados
print("Taxa de retenção para a base total de assinantes:")
for i, taxa in enumerate(taxa_ret_base_total):
    print(f"Mês {i + 2}: {taxa:.2f}%")
print(f"Mês com a maior retenção na base total: Mês {mes_maior_ret_base_total + 1}")

print("\nTaxa de retenção para os assinantes que acessam o Canal Rural:")
for i, taxa in enumerate(taxa_ret_canal_rural):
    print(f"Mês {i + 2}: {taxa:.2f}%")
print(f"Mês com a maior retenção no Canal Rural: Mês {mes_maior_ret_canal_rural + 1}")
