class Eletronico:
    def __init__(self, marca, preço):
        self.marca = marca
        self.preço = preço

    def ligar(self):
        print('Aparelho ligando, carregando OS, aguarde!')


class Smartphone(Eletronico):
    def __init__(self, marca, preço, sistema_operacional):
        super().__init__(marca, preço)
        self.OS = sistema_operacional
        
    def ligar(self):
        super().ligar()
        print(f'Sistema {self.OS} carregando, aguarde!')
        
# --- CRIANDO E TESTANDO OBJETOS ---

#instância da classe mãe
tablet = Eletronico('Samsung', 800.00)

#instância da classe filha
meu_celular = Smartphone('Apple', 1500.00, 'iOS') 

print('-' * 40)
print(f'--- Testando {tablet.marca} ---')
tablet.ligar() 

print('\n' + '-' * 40)
print(f'--- Testando {meu_celular.marca} ---')
meu_celular.ligar()
print('-' * 40)