import math
angulo = float(input('Digite o ângulo que vc deseja: '))
seno= math.sin(math.radians(angulo))
print('O ângulo de {} tem o SENO de {:2f}' .format(angulo, seno))
cosseno= math.cos(math.radians(angulo))
print('O ângulo de {} tem o COSSENO de {:2f}' .format(angulo, cosseno))
tangente= math.tan(math.radians(angulo))
print('O ângulo de {} tem a tangente de {:2f}' .format(angulo, tangente))
