#desafio 17

co= float(input('Comprimento do cateto oposto: '))
ca= float(input('Comprimento do cateto adjacente: '))
#forma 1
'''
hi = (co ** 2 + ca ** 2) ** (1/2)
print('A hipotenusa vai medir {}' .format(hi))
'''

#forma 2

import math
hi= math.hypot(ca, co)