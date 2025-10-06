def converter_temperatura(c):
    f = (c * 1.8) + 32 
    return f

resultado = converter_temperatura(float(input('Digite o valor em celcius para converter: ')))
print(f'A temperatura em celcius é {resultado} farenheint')
