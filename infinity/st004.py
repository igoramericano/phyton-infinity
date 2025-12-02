import streamlit as st
import pandas as pd
# A lista 'dados' global é removida, pois usaremos st.session_state['livros']
# dados = [] 

# Configuração e Inicialização
st.set_page_config(page_title="Meu App Biblioteca", layout="centered")
st.title(':books: Meu App Biblioteca')

if 'livros' not in st.session_state:
    st.session_state['livros'] = []

# Menu de Navegação
st.header("MENU")
pagina = st.selectbox(
    "Escolha a página:",
    ("Cadastrar Livros", "Ler Cadastro", "Excluir Livro"),
    index=0
)

# Página de Cadastro
if pagina == "Cadastrar Livros":
    st.subheader("Adicionar novo Livro")
    
    # 1. Correção: idLivro usa len(st.session_state['livros'])
    idLivro = len(st.session_state['livros']) + 1
    
    # 2. Mantemos as chaves minúsculas aqui, mas usaremos 'Título' para consistência
    titulo = st.text_input("Título do Livro: ")
    autor = st.text_input("Autor do Livro: ")
    data = st.number_input("Ano de lançamento:", step=1, format="%d", value=2024) # Adicionado valor padrão

    btCadastrar = st.button("Cadastrar")

    if btCadastrar:
        if titulo and autor:
            # 3. Correção: Alinhamento das chaves para 'Título' e 'Autor'
            dicLivro = {"ID": idLivro, 'Título': titulo, 'Autor': autor, 'Ano': data}
            
            # 4. Correção: Adiciona ao st.session_state['livros']
            st.session_state['livros'].append(dicLivro)
            
            st.success("Livro Cadastrado com sucesso")
            st.experimental_rerun() # Para limpar os campos
        else:
            st.error("Informe o título e autor do livro!")

# Página de Leitura
elif pagina == "Ler Cadastro":
    st.subheader("Livros Cadastrados :scroll:")
    
    if st.session_state['livros']:
        df_livros = pd.DataFrame(st.session_state['livros'])
        st.dataframe(df_livros, use_container_width=True, hide_index=True)
        st.info(f"Total de livros: {len(st.session_state['livros'])}")
    else:
        st.warning("Nenhum livro cadastrado.")
yes
# Página de Exclusão
elif pagina == "Excluir Livro":
    st.subheader("Excluir Livro do Cadastro :x:")

    if not st.session_state['livros']:
        st.warning("Não há livros cadastrados para exclusão.")
    else:
        # Correção: O list comprehension agora usa a chave 'Título'
        titulos_disponiveis = [livro['Título'] for livro in st.session_state['livros']]
        
        livro_a_excluir = st.selectbox(
            "Selecione o livro que deseja excluir:",
            options=["Selecione um título..."] + titulos_disponiveis
        )
        
        if livro_a_excluir != "Selecione um título...":
            st.warning(f"Confirme a exclusão de: **{livro_a_excluir}**.")
            
            if st.button("Excluir Permanentemente"):
                livros_antes = len(st.session_state['livros'])
                
                # Correção: O filtro agora usa a chave 'Título'
                st.session_state['livros'] = [
                    livro for livro in st.session_state['livros'] 
                    if livro['Título'] != livro_a_excluir
                ]
                
                livros_depois = len(st.session_state['livros'])
                
                if livros_depois < livros_antes:
                    st.success(f"O livro '{livro_a_excluir}' foi excluído com sucesso.")
                else:
                    st.error("Erro ao tentar excluir o livro.")
                
                st.experimental_rerun()