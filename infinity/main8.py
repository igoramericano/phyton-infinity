import streamlit as st
"""BACKEND"""
class ItemPedido:
    def __init__(self, nome_produto, preco_unitario, quantidade):
        self.nome_produto = nome_produto
        self.quantidade = quantidade
        self.preco_unitario = float(preco_unitario) 
        self.desconto_percentual = 0.0
        self.avaliacao_cliente = 0
    
    def aplicar_desconto(self, percentual):
        self.desconto_percentual = percentual 
        
    def calcular_total(self):
        bruto = self.preco_unitario * self.quantidade
        desconto_fator = (1 - self.desconto_percentual/100)
        total = bruto * desconto_fator
        return total
    
    def avaliar_item(self, nota):
        if 0 <= nota <= 5:
            self.avaliacao_cliente = nota
            return f"Avaliação de {nota} registrada com sucesso!"
        else:
            return f"ERRO! A nota {nota} é inválida. Digite um valor entre 0 e 5."
        
    def preco_final_formatado(self):
        preco_final = self.calcular_total()
        return f'R$ {preco_final:.2f}'.replace('.', ',')
"""FRONTEND, streamlit basis"""

st.set_page_config(page_title="Pedidos Online", page_icon="🛒")
st.title("🛒 Sistema de Pedidos Online")
st.write("Gerencie seus itens e calcule descontos.")
st.header("1. Detalhes do Produto")

col1, col2, col3 = st.columns(3)
with col1:
    nome = st.text_input("Nome do Produto", value="Camiseta Python")

with col2:
    preco = st.number_input("Preço Unitário (R$)", min_value=0.0, value=50.00, format="%.2f")

with col3:
    qtd = st.number_input("Quantidade", min_value=1, step=1, value=2)

item = ItemPedido(nome, preco, qtd)
st.divider()
st.header("2. Configurações e Descontos")

desconto = st.slider("Desconto (%)", 0, 100, 10)
item.aplicar_desconto(desconto)

st.divider()
st.header("3. Resumo do Pedido")

res_col1, res_col2 = st.columns(2)

with res_col1:
    bruto = item.preco_unitario * item.quantidade
    st.metric(label="Valor Bruto", value=f"R$ {bruto:.2f}".replace('.', ','))

with res_col2:
    economia = bruto - item.calcular_total()
    st.metric(label="Valor Final (Com Desconto)", 
              value=item.preco_final_formatado(), 
              delta=f"- R$ {economia:.2f}".replace('.', ','))

if desconto > 0:
    st.success(f"Você aplicou {desconto}% de desconto no item **{item.nome_produto}**!")
else:
    st.info("Nenhum desconto aplicado.")