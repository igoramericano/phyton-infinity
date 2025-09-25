sexo = str(input('Informe seu sexo [M/F]: ')).strip().upper()[0]

while sexo not in 'MmFf':
    sexo = str(input('Dados inválidos. Por favor, informe seu sexo [M/F]: ')).strip().upper()[0]
    
if sexo == 'M':
    sexo = 'Masculino'
    
elif sexo == 'F':
    sexo = 'Feminino'
    
else:
    sexo = 'Geração Z'
print(f'Sexo {sexo} registrado com sucesso.')