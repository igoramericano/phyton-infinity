print('-' * 30)
print('Bem vindo ao 24/7 AMERICAN BANK')
print('-' * 30)
print('CEDULAS DISPONÍVEIS: \n R$100, R$50, R$20')
print('-' * 30)
valor = int(input('Digite o valor a ser sacado: R$ '))

total = valor
totalcedulas = 0
ced = [100, 50, 20]

for cedula in ced: #aqui define uma váriavel cedula que vai percorrer a lista ced
    if total >= cedula:
        #aqui define uma váriavel cedula que vai receber o valor da cedula atual
        quant_cedulas = total // cedula
        
        #agora o total passa pra próxima cedula com o resto da divisão
        total = total % cedula

        #imprime os valores de cedulas
        print(f'{quant_cedulas} notas de R${cedula}')
print('-' * 30)
print('Obrigado por ultilizar nossos serviços!')
print('-' * 30)