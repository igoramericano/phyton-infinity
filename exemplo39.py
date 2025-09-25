# Frutas de João e Maria
frutas_joao = {"a", "b", "c", "d"}
frutas_maria = {"c", "d", "e", "f"}

# A diferença
# O operador - mostra os itens que estão em 'frutas_joao' mas não em 'frutas_maria'
apenas_joao = frutas_joao - frutas_maria

print(f"Frutas que o João tem e a Maria não tem: {apenas_joao}")
# Saída: Frutas que o João tem e a Maria não tem: {'a', 'b'}