# Pede ao usuário para digitar a idade e converte o valor para um número inteiro.
idade = int(input('Digite sua idade: '))

# Verifica se o voto é proibido.
if idade < 16:
    print('Você não pode votar. O voto é proibido para menores de 16 anos.')


# Verifica se o voto é opcional (para jovens).
elif idade >= 16 and idade < 18:
    print('Seu voto é opcional.')


# Verifica se o voto é obrigatório.
elif idade >= 18 and idade <= 70:
    print('Seu voto é obrigatório.')


# Verifica se o voto é opcional (para idosos).
elif idade > 70:
    print('Seu voto é opcional.')