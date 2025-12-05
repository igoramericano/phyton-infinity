class SerVivo:
    def __init__(self, raça, idade, peso):
        self.raça = raça
        self.idade = idade
        self.peso = peso
    
    def apresentar(self):
        print(f'Olá, pertenço à raça {self.raça}, tenho {self.idade} anos e peso {self.peso}kg')
        
class Animal(SerVivo):
    def __init__(self, raça, idade, peso):
        super().__init__(raça, idade, peso)
    
    def apresentar(self):
        super().apresentar()
        print("E sou da classe Animal.")
        
class Mamifero(Animal):
    def __init__(self, raça, idade, peso):
        super().__init__(raça, idade, peso)
    
    def apresentar(self):
        super().apresentar()
        print("E sou um mamífero!")

# --- TESTE FINAL ---
print('-' * 40)
cachorro = Mamifero('Canina', 5, 30) 
print('--- APRESENTAÇÃO EM CASCATA ---')
cachorro.apresentar()
print('-' * 40)