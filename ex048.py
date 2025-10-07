# Definindo os números para a divisão
dividendo = 17
divisor = 5

# Usando o operador de módulo (%) para encontrar o resto
resto = dividendo % divisor

# Exibindo o resultado no console
print(f'O resto da divisão de {dividendo} por {divisor} é: {resto}')

# Exemplo prático: checar se um número é par ou ímpar
numero = 10

if (numero % 2) == 0:
  print(f'O número {numero} é par.')
else:
  print(f'O número {numero} é ímpar.')

# Outro exemplo: encontrar o resto de uma divisão exata
divisao_exata = 15 % 5
print(f'O resto de 15 dividido por 5 é: {divisao_exata}') # O resultado será 0