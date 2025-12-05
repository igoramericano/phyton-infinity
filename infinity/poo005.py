class Documento:
    """
    Classe base que representa um documento genérico.
    """
    def __init__(self):
        # Construtor vazio, pois não precisamos de atributos iniciais
        pass 
        
    def abrir(self):
        # Este é o método padrão que será sobrescrito
        print('Acessando o arquivo de forma genérica (Documento Base).')

class PDF(Documento):
    def __init__(self):
        Documento.__init__(self)
    
    def abrir(self):
        print('Abrindo documento PDF!')
    
class Word(Documento):
    def __init__(self):
        Documento.__init__(self)
    
    def abrir(self):
        print('Abrindo documento Word!')
        
class Excel(Documento):
    def __init__(self):
        Documento.__init__(self)
        
    def abrir(self):
        print('Abrindo documento Excel!')
        
        
def abrir_lista_documentos(lista_doc):
    print('-' * 40)
    print('PROCESSANDO LISTA DE DOCUMENTOS'.center(40))
    print('-' * 40)
    
    for doc in lista_doc:
        doc.abrir() # O Python chama o método correto para cada objeto
        time.sleep(0.5) # Adicionando um pequeno delay para visualização
    print('-' * 40)

# --- PROGRAMA PRINCIPAL DE TESTE ---
import time

# 1. Cria as instâncias (objetos)
pdf = PDF()
word = Word()
excel = Excel()
doc = Documento()

# 2. Cria a lista de documentos (aceita todos os tipos!)
lista_de_arquivos = [word, pdf, excel, doc]

# 3. Chama a função final
abrir_lista_documentos(lista_de_arquivos)