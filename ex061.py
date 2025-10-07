import random

# --- Exemplo de 'while' (Jogo de adivinhação) ---
# Este loop continua rodando 'enquanto' a condição for verdadeira.
# A condição aqui é que o palpite do usuário seja diferente do número secreto.

# Geramos um número aleatório entre 1 e 10.
numero_secreto = random.randint(1, 10)
palpite = 0

print("--- Jogo de Adivinhação ---")
print("Tente adivinhar o número secreto entre 1 e 10.")

# O loop 'while' continuará enquanto o palpite não for igual ao número secreto.
while palpite != numero_secreto:
    try:
        # Pede ao usuário para digitar um número.
        palpite = int(input("Digite seu palpite: "))
        
        # Compara o palpite com o número secreto.
        if palpite < numero_secreto:
            print("Muito baixo! Tente novamente.")
        elif palpite > numero_secreto:
            print("Muito alto! Tente novamente.")
        
    except ValueError:
        # Trata o erro se o usuário digitar algo que não é um número.
        print("Entrada inválida. Por favor, digite um número.")

# O loop 'while' termina aqui, pois a condição 'palpite != numero_secreto' se tornou falsa.
print(f"Parabéns! Você acertou o número secreto, que era {numero_secreto}.")

print("\n" + "="*40 + "\n")

# --- Exemplo de 'for' (Contagem regressiva) ---
# Este loop é usado para iterar sobre uma sequência conhecida de números.
# O 'range(5, 0, -1)' cria uma sequência de 5, 4, 3, 2, 1.

print("--- Contagem Regressiva para Lançamento ---")

# O loop 'for' percorre cada número na sequência gerada por 'range'.
for numero in range(5, 0, -1):
    # 'end="... "' evita que a função print pule para a próxima linha.
    print(f"{numero}...", end=" ")
    
# Uma pausa para simular a emoção do lançamento.
import time
time.sleep(1)

# Esta linha será executada após o loop 'for' terminar de percorrer todos os números.
print("\nLançamento!")