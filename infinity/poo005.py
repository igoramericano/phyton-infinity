class cachorro:
    # 🛠️ Corrigido: Removido o parâmetro 'raça'
    def __init__(self, nome):
        self.nome = nome
    def fazer_som(self):
        print(f'{self.nome} late: Au au!')

class gato:
    # 🛠️ Corrigido: Removido o parâmetro 'raça'
    def __init__(self, nome):
        self.nome = nome
    def fazer_som(self):
        print(f'{self.nome} mia: Miau!')

class pássaro:
    # 🛠️ Corrigido: Removido o parâmetro 'raça'
    def __init__(self, nome):
        self.nome = nome
    def fazer_som(self):
        print(f'{self.nome} canta: Piu piu!')

    
def orquestra_animal(lista_animais):
    for animal in lista_animais:
        animal.fazer_som()

# ✅ Instanciação corrigida (apenas com o argumento 'nome')
letty = cachorro("Letty")
tom = gato("Tom")
xexéu = pássaro("Xexéu")

lista = [letty, tom, xexéu]

print("--- A Orquestra dos Animais ---")
orquestra_animal(lista)