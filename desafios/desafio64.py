n = cont = soma = 0 #primeira vez que declaramos 3 variáveis na mesma linha
n = int(input('Digite um número [DIGITE 999 para parar]: '))

while n != 999:
    soma += n
    cont += 1
    n = int(input('Digite um número [DIGITE 999 para parar]: '))
    
print(f'Você digitou {cont} números e a soma entre eles foi {soma}.')