conjunto = ('Zero', 'Um', 'Dois', 'Três', 'Quatro',   'Cinco', 'Seis', 'Sete', 'Oito',  'Nove', 'Dez','Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')
while True:
    numero = int(input('Digite um número entre 0 e 20: '))
    if 0 <= numero <= 20:
        print(f'Você digitou o número {conjunto[numero]}.')
    else:
        print('Número inválido.')
    continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
            break