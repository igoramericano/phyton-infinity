class Veiculo:
    def __init__(self, marca, ano):
        self.marca = marca
        self.ano = ano

    def info(self):
        print(f"Marca: {self.marca}, Ano: {self.ano}")
    
    def detalhes(self):
        print("--- Detalhes do Veículo ---")
        self.info()
    
class moto(Veiculo):
    def __init__(self, marca, ano, cilindradas):
        Veiculo.__init__(self, marca, ano) 
        self.cilindradas = cilindradas

    def detalhes(self):
        Veiculo.detalhes(self) 
        print(f"Tipo: Moto (Cilindradas: {self.cilindradas}cc)")

class caminhão(Veiculo):
    def __init__(self, marca, ano, capacidade_carga):
        Veiculo.__init__(self, marca, ano)
        self.capacidade_carga = capacidade_carga

    def detalhes(self):
        Veiculo.detalhes(self)
        print(f"Tipo: Caminhão (Capacidade de Carga: {self.capacidade_carga} kg)")

moto = moto("Honda", 2024, 300)
caminhão = caminhão("Volvo", 2020, 15000)

print("--- Teste de Polimorfismo ---")
moto.detalhes()
print("-" * 20)
caminhão.detalhes()