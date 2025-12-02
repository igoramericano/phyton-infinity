import streamlit as st

st.sidebar.title("Menu Principal")

# Menu principal
secao = st.sidebar.radio("Seção:", ["Vendas", "Estoque", "Relatórios"])

# Submenus condicionais
if secao == "Vendas":
    subsecao = st.sidebar.selectbox(
        "Vendas - Opções:",
        ["Nova Venda", "Histórico", "Cancelamentos"]
    )
    st.title(f"Vendas > {subsecao}")
    
elif secao == "Estoque":
    subsecao = st.sidebar.selectbox(
        "Estoque - Opções:",
        ["Consultar", "Entrada", "Saída"]
    )
    st.title(f"Estoque > {subsecao}")
    
elif secao == "Relatórios":
    subsecao = st.sidebar.selectbox(
        "Relatórios - Opções:",
        ["Financeiro", "Produtos", "Clientes"]
    )
    st.title(f"Relatórios > {subsecao}")