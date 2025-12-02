import streamlit as st

# --- 1. Funções para as Páginas (Melhor Prática) ---

def pagina_inicio():
    """Define o conteúdo da página 'Início'."""
    st.header("🏠 Bem-vindo(a)!")
    st.write("Esta é uma aplicação de exemplo aprimorada, demonstrando como estruturar um app Streamlit com **múltiplas visualizações**.")
    st.info("💡 Use o menu de navegação lateral para explorar as funcionalidades.")
    st.balloons()
    
def pagina_calculadora():
    """Define o conteúdo e a lógica da página 'Calculadora'."""
    st.header("🧮 Calculadora Simples")
    
    # 1.1. Inputs e Seleção de Operação
    col1, col2 = st.columns(2)
    with col1:
        num1 = st.number_input("Primeiro número:", value=0.0, format="%.2f", key="calc_num1")
    with col2:
        num2 = st.number_input("Segundo número:", value=0.0, format="%.2f", key="calc_num2")
        
    operacao = st.selectbox(
        "Selecione a operação:",
        ["Somar (+)", "Subtrair (-)", "Multiplicar (×)", "Dividir (÷)"]
    )
    
    # 1.2. Lógica de Cálculo
    if st.button("Calcular", type="primary"):
        resultado = None
        erro = False
        
        if operacao == "Somar (+)":
            resultado = num1 + num2
        elif operacao == "Subtrair (-)":
            resultado = num1 - num2
        elif operacao == "Multiplicar (×)":
            resultado = num1 * num2
        elif operacao == "Dividir (÷)":
            # 1.3. Tratamento de Erro (Divisão por Zero)
            if num2 != 0:
                resultado = num1 / num2
            else:
                st.error("🚫 Erro: Não é possível dividir por zero!")
                erro = True
                
        # 1.4. Exibição do Resultado
        if resultado is not None and not erro:
            st.success(f"✅ Resultado da operação: **{resultado:.2f}**") # Formatando para 2 casas decimais

def pagina_sobre():
    """Define o conteúdo da página 'Sobre'."""
    st.header("ℹ️ Sobre esta aplicação")
    st.markdown("""
    Esta mini-aplicação foi criada para demonstrar o poder e a **facilidade do Streamlit** para construir aplicações web interativas com **Python puro**.
    """)
    st.write("---")
    st.write("✨ **Desenvolvida com:** Streamlit (Aplicações Web em Python)")
    st.write("🏷️ **Versão:** 1.1 (Aprimorada)")
    st.write("👤 **Autor:** Igor Americano")

# --- 2. Estrutura Principal da Aplicação ---

# Título principal e configuração da página
st.set_page_config(page_title="App Aprimorado", layout="centered")
st.title("🌟Calculadora Premium")

# Navegação usando o st.sidebar (Melhora a UX)
st.sidebar.title("Menu de Navegação")

# Adicionando ícones na seleção
opcoes_navegacao = {
    "🏠 Início": pagina_inicio,
    "🧮 Calculadora": pagina_calculadora,
    "ℹ️ Sobre": pagina_sobre
}

pagina_selecionada = st.sidebar.selectbox(
    "Escolha uma página:", 
    list(opcoes_navegacao.keys())
)

# 3. Chamar a função da página selecionada
opcoes_navegacao[pagina_selecionada]()