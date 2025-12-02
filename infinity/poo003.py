class forma:
    def calcular_area():
        return 0
class retangulo(forma):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    
    def calcular_area(base, altura):
        return base * altura

class circulo(forma):
    def __init__(self, raio)
        self.raio = raio

    def calcular_area(raio):
        return 3.14 * raio ** 2
    
ret1 = retangulo(3,4)
print(f"Área do retângulo {ret1.calcular_area}")
cir1 = circulo(5)
print(f"Área do circulo {cir1.calcular_area}")