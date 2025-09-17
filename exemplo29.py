# Criando uma tupla com o nome de 5 cidades
cidades = ("São Paulo", "Rio de Janeiro", "Belo Horizonte", "Salvador", "Fortaleza")

# Exibe o primeiro e o último elemento
print(f"Primeira cidade: {cidades[0]}")
print(f"Última cidade: {cidades[-1]}")

# Exibe todos os elementos, um por linha
print("\nTodas as cidades:")
for cidade in cidades:
    print(cidade)

# Exibe a quantidade total de elementos
print(f"\nTotal de cidades: {len(cidades)}")

# Verifica se "Salvador" existe na tupla
if "Salvador" in cidades:
    print("\n'Salvador' está na lista de cidades.")
else:
    print("\n'Salvador' NÃO está na lista de cidades.")