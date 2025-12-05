from abc import ABC, abstractmethod

class Pagamento(ABC):
    
    @abstractmethod # <-- Torna este método obrigatório
    def processar(self):
        # Esta função não faz nada na classe mãe, apenas define o contrato
        pass
    
class Cartão(Pagamento):
    def __init__(self):
        Pagamento.__init__(self)
        
    def processar(self):
        print("Verificando saldo e bandeira -->Processando pagamento via Cartão<-- ")
        
class Pix(Pagamento):
    def __init__(self):
        Pagamento.__init__(self)
        
    def processar(self):
        print('Pagamento via PIX realizado com sucesso!')
        
class Dinheiro(Pagamento):
    def __init__(self):
        Pagamento.__init__(self)
        
    def processar(self):
        print('Dinheiro recebido, obrigado e volte sempre!')
        

pagamento_cartão = Cartão()
pagamento_pix = Pix()
pagamento_dinheiro = Dinheiro()

print('-'*30)
pagamento_cartão.processar()
pagamento_pix.processar()
pagamento_dinheiro.processar()
print('-'*30)
