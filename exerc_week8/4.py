jef = {"swift", "picpay", "original", "jbs", "friboi", "J&F"}
jbs = {"swift", "friboi", "seara", "rezende", "delícia", "primor", "doriana", "massaleve", "marba"}

num_jef = len(jef)
num_jbs = len(jbs)

print(f"Número de marcas no conjunto J&F: {num_jef}")
print(f"Número de marcas no conjunto JBS: {num_jbs}")

# Interseção dos dois conjuntos (jef, jbs)
intersecao = jef.intersection(jbs)
print("\nMarcas em comum nos dois conjuntos:")
print(intersecao)

# difference para mostrar a diferenca dos dois...
diferentes_em_jef = jef.difference(jbs)
diferentes_em_jbs = jbs.difference(jef)

print("\nValores diferentes em JEF:")
print(diferentes_em_jef)

print("\nValores diferentes em JBS:")
print(diferentes_em_jbs)
