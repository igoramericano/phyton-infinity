# Uma lista para guardar os dados dos animais
animais_cadastrados = []

print("--- Cadastro de Animais ---")
print("Digite 'fim' no nome para encerrar.")

# Loop para pedir os dados dos animais
while True:
    nome = input("Nome do animal: ")
    
    # Sai do loop se o nome for 'fim'
    if nome.lower() == 'fim':
        break
        
    tipo = input("Tipo: ")
    idade = int(input("Idade: "))
    
    # Cria uma tupla com os dados e adiciona à lista
    animal = (nome, tipo, idade)
    animais_cadastrados.append(animal)
    print("Animal cadastrado!")

# Exibe todos os animais da lista
print("\n--- Animais Cadastrados ---")
for animal in animais_cadastrados:
    print(f"Nome: {animal[0]}, Tipo: {animal[1]}, Idade: {animal[2]}")