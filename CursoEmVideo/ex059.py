# Importa a biblioteca 'random' para gerar números aleatórios.
import random

# --- INICIALIZAÇÃO DO JOGO ---
# Mensagem de boas-vindas.
print('--- Jogo de Adivinhação ---')
print('Você tem 10 tentativas para adivinhar o número secreto.')

# Gera um número secreto aleatório entre 1 e 100.
numero_secreto = random.randint(1, 100)

# Contador de tentativas, inicializado em zero.
tentativas = 0

# --- LOOP PRINCIPAL DO JOGO ---
# O laço "infinito" continua até que o jogador acerte o número ou as tentativas acabem.
while tentativas < 10:
    try:
        # Aumentamos o contador de tentativas a cada palpite válido.
        tentativas += 1

        # Pedimos o palpite do usuário.
        chute = int(input(f'\nTentativa #{tentativas}: Digite seu chute (entre 1 e 100): '))

    except ValueError:
        print("Entrada inválida. Por favor, digite apenas um número.")
        # Se a entrada for inválida, diminuímos o contador para não contar como uma tentativa.
        tentativas -= 1
        continue
    
    # --- CONDIÇÕES PARA O CHUTE ---
    if chute == numero_secreto:
        print(f'\nParabéns! Você acertou em {tentativas} tentativas!')
        # A instrução 'break' encerra o laço.
        break
    elif chute < numero_secreto:
        print('Seu chute é muito baixo. Tente um número maior.')
    else:
        print('Seu chute é muito alto. Tente um número menor.')
    
# --- FIM DO JOGO ---
# Verifica se o laço terminou porque as tentativas acabaram.
if tentativas >= 10 and chute != numero_secreto:
    print(f'\nQue pena! Suas 10 tentativas acabaram. O número secreto era {numero_secreto}.')
else:
    print('\nFim do jogo.')