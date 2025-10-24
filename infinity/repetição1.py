from random import randint
numeros = list()

for c in range(0, 10):
    numero_sorteado = randint(1, 100)
    numeros.append(numero_sorteado)

multiplosde7 = []
impares = []
pares = []
soma_total = quantidade_total = 0

numeros.sort()

print("-" * 40)
print(f"Lista de números sorteados (ordenada): {numeros}")
print("-" * 40)

for num in numeros:
  if num % 7 == 0:
    print(f' \n {num} é divisivel por 7')
    multiplosde7.append(num)
  else:
    print(f' \n {num} NÃO é divisível por 7')
    
  if num % 2 != 0:
    print(f' \n {num} é impar')
    impares.append(num)
  else:
    print(f' \n {num} é par')
    pares.append(num)

  soma_total += num
  quantidade_total += 1


tupla_divisiveis_por_sete = tuple(multiplosde7)
lista_impares = impares

resumo_dados = {
    'quantidade_numeros': quantidade_total,
    'soma_total': soma_total
}

print('\n' + '=' * 30)
print('RESULTADOS DO PROCESSAMENTO'.center(30))
print('=' * 30)
print(f'A tupla dos divisíveis por 7 é: {tupla_divisiveis_por_sete}')
print(f'A lista dos ímpares é: {lista_impares}')
print(f'O dicionário de resumo é: {resumo_dados}')
print('=' * 30)