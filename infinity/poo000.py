# --- Classe base (superclasse) ---
class Animal:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def fazer_som(self):
        print("O animal faz um som")

    def apresentar(self):
        print(f"Nome: {self.nome}, Idade: {self.idade} anos")

# --- Classe derivada (subclasse) ---
class Cachorro(Animal):
    def __init__(self, nome, idade, raca):
    # Chama o construtor da classe pai
        Animal.__init__(self, nome, idade)
        self.raca = raca

    # Sobrescrevendo o método da classe pai
    def fazer_som(self):
        print(f"{self.nome} late: Au au!")

    # Método específico da classe Cachorro
    def buscar_bola(self):
        print(f"{self.nome} está buscando a bola!")

# --- Outra classe derivada ---
class Gato(Animal):
    def __init__(self, nome, idade, cor):
        Animal.__init__(self, nome, idade)
        self.cor = cor

    def fazer_som(self):
        print(f"{self.nome} mia: Miau!")
    
    # Método específico da classe Gato
    def arranhar(self):
        print(f"{self.nome} está arranhando o sofá!")

class Sogra(Animal):
    def __init__(self, nome, idade, lingua):
        Animal.__init__(self, nome, idade)
        self.cor = cor

    def fazer_som(self):
        print(f"{self.nome} ESTA MUDA!")
    
  # --- Testando as classes ---
rex = Cachorro("Rex", 5, "Labrador")
rex.apresentar()# Método herdado
rex.fazer_som()# Método sobrescrito
rex.buscar_bola()# Método próprio
print()
mimi = Gato("Mimi", 3, "Branco")
mimi.apresentar()# Método herdado
mimi.fazer_som()# Método sobrescrito
mimi.arranhar()# Método próprio
sherazade = Sogra("Sherazade", 200, 1000)
sherazade.apresentar()
sherazade.fazer_som()