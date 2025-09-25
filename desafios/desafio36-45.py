# DESAFIO 36
valor_casa = float(input('Valor da casa: R$'))
salario = float(input('Seu salário: R$'))
anos = int(input('Anos para pagar: '))

prestacao = valor_casa / (anos * 12)
limite = salario * 0.30

if prestacao <= limite:
    print(f'APROVADO! A prestação será de R${prestacao:.2f}.')
else:
    print(f'NEGADO! A prestação de R${prestacao:.2f} é maior que o limite de R${limite:.2f}.')

# DESAFIO 37
n = int(input('Digite um número: '))
base = int(input('Escolha a base de conversão (1- Binário, 2- Octal, 3- Hexadecimal): '))
if base == 1:
    print(f'{n} convertido para BINÁRIO é {bin(n)[2:]}.')
elif base == 2:
    print(f'{n} convertido para OCTAL é {oct(n)[2:]}.')
elif base == 3:
    print(f'{n} convertido para HEXADECIMAL é {hex(n)[2:]}.')
else:
    print('Opção inválida!')

# DESAFIO 38
n1 = int(input('Primeiro número inteiro: '))
n2 = int(input('Segundo número inteiro: '))

if n1 > n2:
    print(f'O maior número é {n1}.')
elif n2 > n1:
    print(f'O maior número é {n2}.')
else:
    print('Os dois números são iguais.')

# DESAFIO 39
from datetime import date
ano_nasc = int(input('Ano de nascimento: '))
ano_atual = date.today().year
idade = ano_atual - ano_nasc
if idade < 18:
    print(f'Você tem {idade} anos. Ainda faltam {18 - idade} anos para o alistamento.')
elif idade == 18:
    print('Você tem 18 anos. É hora de se alistar!')
else:
    print(f'Você tem {idade} anos. Já passou {idade - 18} anos do alistamento.')

# DESAFIO 40
nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
nota3 = float(input('Terceira nota: '))
media = (nota1 + nota2 + nota3) / 3

if media < 5.0:
    print(f'Média: {media:.1f}. REPROVADO.')
elif 5.0 <= media < 7.0:
    print(f'Média: {media:.1f}. RECUPERAÇÃO.')
else:
    print(f'Média: {media:.1f}. APROVADO.')

# DESAFIO 41
from datetime import date
ano_nasc = int(input('Ano de nascimento: '))
ano_atual = date.today().year
idade = ano_atual - ano_nasc
if idade <= 9:
    categoria = 'MIRIM'
elif idade <= 14:
    categoria = 'INFANTIL'
elif idade <= 19:
    categoria = 'JUNIOR'
elif idade <= 25:
    categoria = 'SÊNIOR'
else:
    categoria = 'MASTER'
print(f'Idade: {idade} anos. Categoria: {categoria}.')

# DESAFIO 42
a = float(input('Primeiro lado do triângulo: '))
b = float(input('Segundo lado do triângulo: '))
c = float(input('Terceiro lado do triângulo: '))
if a < b + c and b < a + c and c < a + b:
    print('Os lados formam um triângulo.')
    if a == b == c:
        tipo = 'EQUILÁTERO'
    elif a == b or b == c or a == c:
        tipo = 'ISÓSCELES'
    else:
        tipo = 'ESCALENO'
    print(f'Tipo do triângulo: {tipo}.')
else:
    print('Os lados não formam um triângulo.')

# DESAFIO 43
peso = float(input('Peso (kg): '))
altura = float(input('Altura (m): '))
imc = peso / (altura ** 2)
print(f'Seu IMC é {imc:.1f}.', end=' ')
if imc < 18.5:
    print('Abaixo do peso.')
elif 18.5 <= imc < 25:
    print('Peso ideal.')
elif 25 <= imc < 30:
    print('Sobrepeso.')
elif 30 <= imc < 40:
    print('Obesidade.')
else:
    print('Obesidade mórbida.')

# DESAFIO 44

preco = float(input('Preço do produto: R$'))
print('''Formas de pagamento:
[1] - À vista (dinheiro/cheque): 10% de desconto
[2] - À vista (cartão): 5% de desconto
[3] - Em até 2x no cartão: preço normal
[4] - 3x ou mais no cartão: 20% de juros''')
opcao = int(input('Escolha a opção (1-4): '))
if opcao == 1:
    total = preco * 0.90
    print(f'Total a pagar: R${total:.2f}.')
elif opcao == 2:
    total = preco * 0.95
elif opcao == 3:
    total = preco
    print(f'Total a pagar: R${total:.2f}.')
elif opcao == 4:
    total = preco * 1.20
    print(f'Total a pagar: R${total:.2f}.')
else:
    print('Opção inválida!')

#Desafio 45
import random

itens = ['Pedra', 'Papel', 'Tesoura']
escolha_jogador = int(input('Escolha [1]-Pedra, [2]-Papel, [3]-Tesoura: ')) - 1
jogador = itens[escolha_jogador]
computador = random.choice(itens)
450
print(f'Você escolheu: {jogador}')
print(f'Computador escolheu: {computador}')

if jogador == computador:
    print('Empate!')
elif (jogador == 'Pedra' and computador == 'Tesoura') or \
     (jogador == 'Papel' and computador == 'Pedra') or \
     (jogador == 'Tesoura' and computador == 'Papel'):
    print('Você venceu!')
else:
    print('Computador venceu!')