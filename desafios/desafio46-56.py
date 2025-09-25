#Desafio 46
import time 
tempo = 10
print('Contagem regressiva para o estouro de fogos!')

for c in range(tempo, 0, -1):
    print(c)
    time.sleep(1) # 2. Pausa o código por 1 segundo

print('BOOOM!') 

#Desafio 47
for c in range(0, 52, 2):
    print(c)
print('FIM!')

#Desafio 48
soma = 0
for numero in range(1, 501):
    if numero % 2 != 0 and numero % 3 == 0:
        soma += numero
print(f"A soma de todos os números ímpares múltiplos de 3 entre 1 e 500 é: {soma}")

#Desafio 49
n = int(input('Digite um número para ver sua tabuada: '))
print(f'Tabuada do {n}:')
for c in range(1, 11):
    print(f'{n} x {c} = {n * c}')
    
#Desafio 50
soma = 0
for i in range(6):
    numero = int(input(f'Digite o {i+1}º número inteiro: '))
    if numero % 2 == 0:
        soma += numero
print(f'A soma dos números pares digitados foi: {soma}')

#Desafio 51
# Pede o primeiro termo e a razão da PA ao usuário
primeiro_termo = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))

# Variável para acompanhar o termo atual na progressão
termo_atual = primeiro_termo

# O laço 'for' vai se repetir 10 vezes para mostrar os 10 termos
for i in range(10):
    # Imprime o termo atual
    print(f'O {i+1}º termo é: {termo_atual}')
    
    # Adiciona a razão para calcular o próximo termo
    termo_atual += razao


#Desafio 52
numero = int(input("Digite um número inteiro: "))

e_primo = True

if numero <= 1:
    e_primo = False
else:
    for i in range(2, numero):
        if numero % i == 0:
            e_primo = False
            break

if e_primo:
    print(f"O número {numero} é primo!")
else:
    print(f"O número {numero} não é primo.")
    
#Desafio 53
frase = input("Digite uma frase: ").strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = junto[::-1]
if junto == inverso:
    print("A frase é um palíndromo!")
else:
    print("A frase não é um palíndromo.")

#Desafio 54
from datetime import datetime
ano_atual = datetime.now().year
contador_maior = 0
contador_menor = 0
for i in range(7):
    ano_nascimento = int(input(f'Digite o ano de nascimento da {i+1}ª pessoa: '))
    idade = ano_atual - ano_nascimento
    if idade >= 18:
        contador_maior += 1
    else:
        contador_menor += 1
print(f'Total de pessoas maiores de idade: {contador_maior}')
print(f'Total de pessoas menores de idade: {contador_menor}')

#Desafio 55
primeiro_peso = float(input('Digite o peso da 1ª pessoa: '))
maior_peso = primeiro_peso
menor_peso = primeiro_peso

for i in range(4):
    peso_atual = float(input(f'Digite o peso da {i+2}ª pessoa: '))
    
    if peso_atual > maior_peso:
        maior_peso = peso_atual
    
    if peso_atual < menor_peso:
        menor_peso = peso_atual

print('--------------------')
print(f'O maior peso digitado foi: {maior_peso}kg')
print(f'O menor peso digitado foi: {menor_peso}kg')

#Desafio 56
# Inicializando as variáveis que vamos usar
soma_idades = 0
idade_homem_mais_velho = 0
nome_homem_mais_velho = ''
mulheres_menos_20 = 0

# O laço vai se repetir 4 vezes para ler os dados de 4 pessoas
for i in range(1, 5):
    print(f'----- {i}ª PESSOA -----')
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().lower()

    # Acumula a idade de todas as pessoas
    soma_idades += idade

    # Verifica se é o homem mais velho
    if sexo == 'm' and idade > idade_homem_mais_velho:
        idade_homem_mais_velho = idade
        nome_homem_mais_velho = nome

    # Verifica se é uma mulher com menos de 20 anos
    if sexo == 'f' and idade < 20:
        mulheres_menos_20 += 1

# Calculando a média de idade do grupo
media_idades = soma_idades / 4

# Mostrando os resultados finais
print('--------------------')
print(f'A média de idade do grupo é de {media_idades:.1f} anos.')

# Verificamos se algum homem foi cadastrado antes de mostrar o nome
if nome_homem_mais_velho:
    print(f'O homem mais velho se chama {nome_homem_mais_velho}.')
else:
    print('Nenhum homem foi cadastrado.')

print(f'Ao todo são {mulheres_menos_20} mulher(es) com menos de 20 anos.')