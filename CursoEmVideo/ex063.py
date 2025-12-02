# Criando uma tupla com informações de um carro
# Tuplas usam parênteses () e são ideais para dados fixos.
carro = ("Ford", "Mustang", 1969)

print("--- Informações do Carro ---")

# Acessando os elementos da tupla pelos seus índices
print(f"Marca: {carro[0]}")
print(f"Modelo: {carro[1]}")
print(f"Ano: {carro[2]}")

print("\n--- Tentando modificar a tupla ---")

try:
    # Esta linha vai causar um erro!
    # Tuplas são imutáveis, ou seja, seus valores não podem ser alterados.
    carro[2] = 1970
    
except TypeError as e:
    print(f"ERRO: Não é possível modificar uma tupla. O erro é: {e}")