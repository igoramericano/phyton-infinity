import streamlit as st

st.title("🔐 Sistema de Login com Session State")

# Inicializar estados
if 'logado' not in st.session_state:
    st.session_state.logado = False
if 'usuario' not in st.session_state:
    st.session_state.usuario = None
if 'tentativas' not in st.session_state:
    st.session_state.tentativas = 0

# Usuários simulados (em produção, use banco de dados!)
usuarios_validos = {
    'admin': '123456',
    'usuario': 'senha123',
    'convidado': 'guest'
}

# Função para fazer login
def fazer_login(username, password):
    if username in usuarios_validos and usuarios_validos[username] == password:
        st.session_state.logado = True
        st.session_state.usuario = username
        st.session_state.tentativas = 0
        return True
    else:
        st.session_state.tentativas += 1
        return False

# Função para fazer logout
def fazer_logout():
    st.session_state.logado = False
    st.session_state.usuario = None

# Interface
if not st.session_state.logado:
    # Tela de Login
    st.subheader("Faça Login")
    
    with st.form("form_login"):
        username = st.text_input("Usuário:")
        password = st.text_input("Senha:", type="password")
        submit = st.form_submit_button("Entrar", type="primary")
        
        if submit:
            if fazer_login(username, password):
                st.success(f"Bem-vindo, {username}!")
                st.rerun()
            else:
                st.error(f"❌ Usuário ou senha incorretos! (Tentativa {st.session_state.tentativas})")
    
    # Dica para teste
    with st.expander("💡 Credenciais para teste"):
        st.write("**Usuários disponíveis:**")
        st.code("admin / 123456\nusuario / senha123\nconvidado / guest")
    
    # Bloquear após 3 tentativas
    if st.session_state.tentativas >= 3:
        st.warning("⚠️ Você excedeu o número de tentativas. Aguarde um momento.")

else:
    # Tela Principal (após login)
    st.success(f"✅ Logado como: **{st.session_state.usuario}**")
    
    col1, col2 = st.columns([4, 1])
    with col2:
        if st.button("🚪 Sair"):
            fazer_logout()
            st.rerun()
    
    # Área do usuário
    st.subheader("🏠 Área do Usuário")
    st.write("Bem-vindo a sua aplicação.")
    st.write("**Preferências do Usuário:**")
    tema = st.selectbox("Tema:", ["Claro", "Escuro", "Automático"])
    notificacoes = st.checkbox("Receber notificações por email", value=True)
        
    if st.button("Salvar Configurações"):
        st.success("✅ Configurações salvas!")