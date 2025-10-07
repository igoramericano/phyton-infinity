salario = float(input('Digite o valor do salário: R$'))
if salario > 1250:
    novo = salario * 1.1
if salario <= 1250:
    novo = salario * 1.15
print('O salário passou de R${:.2f} para R${:.2f}.'.format(salario,novo))

