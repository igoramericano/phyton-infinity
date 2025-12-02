def fatorial(n, show=False):
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(' x ')
            else:
                print(' = ', end='')
        f *= c
    return f
n = int(input('Insira o valor para calcular o fatorial: '))
print(fatorial(n))