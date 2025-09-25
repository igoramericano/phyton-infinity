n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
opção = 0

print('''Escolha uma das opções abaixo:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa''')

while opção != 5:
    opção = int(input('Qual é a sua opção? '))
    
    if opção == 1:
        soma = n1 + n2
        print(f'A soma entre {n1} e {n2} é {soma}')
    
    elif opção == 2:
        produto = n1 * n2
        print(f'O resultado de {n1} x {n2} é {produto}')
    
    elif opção == 3:
        if n1 > n2:
            maior = n1
            print(f'Entre {n1} e {n2}, o maior valor é {maior}')
        elif n2 > n1:
            maior = n2
            print(f'Entre {n1} e {n2}, o maior valor é {maior}')
        else:
            print('Os dois números são iguais!')
    
    elif opção == 4:
        print('Informe os números novamente:')
        n1 = int(input('Digite o primeiro número: '))
        n2 = int(input('Digite o segundo número: '))
    
    elif opção == 5:
        print('Finalizando...')
    
    else:
        print('Opção inválida. Tente novamente.')
    print('=-=' * 10)