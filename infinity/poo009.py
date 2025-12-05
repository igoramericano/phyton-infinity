class base:
    def __init__(self, nome, cpf, salario_base, data_admissão):
        self.nome = nome
        self.cpf = cpf
        self.salario = salario_base
        self.data = data_admissão
    
    def calcular_salario(self):
        return self.salario
    
    def bater_ponto(self):
        print(f'Funcionário {self.nome} registrado.')
        
    def exibir_info(self):
        print('-'*30)
        print('DADOS DO FUNCIONÁRIO')
        print(f"Nome: {self.nome}")
        print(f"CPF: {self.cpf}")
        print(f"Salário Base: R${self.salario:.2f}")
        print(f"Data de Admissão: {self.data}")
        print('-'*30)
        
class Mecanico(base):
    def __init__(self, nome, cpf, salario_base, data_admissão, especialidade, quantidade_servicos_mes):
        super().__init__(nome, cpf, salario_base, data_admissão)
        self.especialidade = especialidade
        self.quantidade_servicos_mes = quantidade_servicos_mes
        
    def realizar_diagnostico(self):
        print('Diagnóstico realizado com sucesso pelo mecânico!')
    
    def calcular_salário(self):
        return self.salario + (self.quantidade_servicos_mes * 50)

class Funileiro(base):
    def __init__(self, nome, cpf, salario_base, data_admissão, nivel_experiência, usa_equipamento_solda):
        self.nivel_experiência = nivel_experiência
        self.usa_equipamento_solda = usa_equipamento_solda
        super().__init__(nome, cpf, salario_base, data_admissão)
    def calcular_salário(self):
        
        multiplicadores = {
            "junior": 1.0,
            "pleno": 1.3,
            "senior": 1.6
        }
        fator = multiplicadores.get(self.nivel_experiencia.lower(), 1.0)
        bonus_solda = 0
        if self.usa_equipamento_solda:
            bonus_solda = 200
        
        salario_liquido = (self.salario * fator) + bonus_solda
        return salario_liquido
    
    def exibir_info(self):
        super().exibir_info()
        print(f"Nível de Experiência: {self.nivel_experiencia}")
        print(f"Usa Equipamento de Solda: {'Sim' if self.usa_equipamento_solda else 'Não'}")
    
    def reparar_lataria(self):
        print(f"Funileiro {self.nome}iniciando reparo de lataria")
        
funcionarios_cadastrados = []

def cadastrar_funcionario():
    tipo = int(input('Para cadastrar Mecânico digite (1) ou Funileiro (2): '))
    
    print("\n--- DADOS GERAIS ---")
    nome = input('Nome: ')
    cpf = input('CPF: ')
    salario_base = float(input('Salário Base: R$'))
    data_admissao = input('Data de Admissão (dd/mm/aaaa): ')
    
    
    if tipo == 1:
        # --- LÓGICA DO MECÂNICO ---
        print("\n--- DADOS MECÂNICO ---")
        especialidade = input('Especialidade: ')
        servicos = int(input('Quantidade de Serviços no Mês: '))
        
        novo_mecanico = Mecanico(nome, cpf, salario_base, data_admissao, especialidade, servicos)
        funcionarios_cadastrados.append(novo_mecanico)
        print("Mecânico cadastrado com sucesso!")

    elif tipo == 2:
        # --- LÓGICA DO FUNILEIRO ---
        print("\n--- DADOS FUNILEIRO ---")
        
        # Converte a resposta do usuário (1/2/3) para a STRING que a classe espera ('Junior', 'Pleno', 'Senior')
        niveis = {1: 'Junior', 2: 'Pleno', 3: 'Senior'}
        nivel_experiencia = input('Nível ((1)Junior/(2)Pleno/(3)Senior): ').capitalize()
        

        usa_solda_str = input('Usa equipamento solda? (S/N): ').upper().strip()[0]
        usa_solda_bool = True if usa_solda_str == 'S' else False
        
        novo_funileiro = Funileiro(nome, cpf, salario_base, data_admissao, nivel_experiencia, usa_solda_bool)
        funcionarios_cadastrados.append(novo_funileiro)
        print("Funileiro cadastrado com sucesso!")

    else:
        print("Opção de funcionário inválida.")