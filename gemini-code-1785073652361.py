import streamlit as st

# 1. Configuração da Página (deve ser a primeira linha)
st.set_page_config(
    page_title="O Cofre das Camisolas ⚽",
    page_icon="👕",
    layout="wide"
)

# 2. CSS Personalizado para um look mais clean
st.markdown("""
    <style>
    /* Esconder o menu default do Streamlit para ficar mais profissional */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    
    /* Estilizar os títulos */
    h1 {
        text-align: center;
        font-weight: 700;
        margin-bottom: 2rem;
    }
    
    /* Dar um aspeto de "cartão" às métricas e textos */
    div[data-testid="stVerticalBlock"] {
        gap: 1.5rem;
    }
    </style>
""", unsafe_allow_html=True)

# 3. Base de Dados Fictícia (Substitui pelos dados reais)
# Podes usar URLs de imagens alojadas online ou caminhos locais (ex: 'imagens/benfica2010.jpg')
colecao = [
    {"clube": "SL Benfica", "ano": "2009/10", "tipo": "Principal", "img": "https://placehold.co/400x500/eaeaea/a8a8a8?text=Benfica+09/10"},
    {"clube": "Real Madrid", "ano": "2016/17", "tipo": "Alternativa", "img": "https://placehold.co/400x500/eaeaea/a8a8a8?text=Real+Madrid+16/17"},
    {"clube": "AC Milan", "ano": "2006/07", "tipo": "Principal", "img": "https://placehold.co/400x500/eaeaea/a8a8a8?text=AC+Milan+06/07"},
    {"clube": "Boca Juniors", "ano": "2020/21", "tipo": "Edição Especial", "img": "https://placehold.co/400x500/eaeaea/a8a8a8?text=Boca+20/21"}
]

wishlist = [
    {"clube": "Arsenal", "ano": "2005/06", "motivo": "A mítica camisola cor de vinho de Highbury", "img": "https://placehold.co/400x500/4a0010/ffffff?text=Arsenal+05/06"},
    {"clube": "Seleção de Portugal", "ano": "2004", "motivo": "Euro 2004, clássico intemporal", "img": "https://placehold.co/400x500/8b0000/ffffff?text=Portugal+04"}
]

# 4. Navegação na Barra Lateral
st.sidebar.title("Navegação 🧭")
st.sidebar.markdown("---")
pagina = st.sidebar.radio("Ir para:", ["A Coleção", "Wishlist"])

# 5. Lógica da Página: A Coleção
if pagina == "A Coleção":
    st.title("👕 Coleção Atual")
    st.markdown("<p style='text-align: center; color: gray;'>As peças de arte que já estão no roupeiro.</p>", unsafe_allow_html=True)
    st.markdown("---")
    
    # Criar uma grelha de 3 a 3
    col1, col2, col3 = st.columns(3)
    
    for i, camisola in enumerate(colecao):
        # Distribuir as camisolas pelas colunas usando o resto da divisão
        with [col1, col2, col3][i % 3]:
            st.image(camisola["img"], use_column_width=True)
            st.subheader(camisola["clube"])
            st.caption(f"**Época:** {camisola['ano']} | **Tipo:** {camisola['tipo']}")
            st.markdown("---") # Linha separadora para manter organizado

# 6. Lógica da Página: Wishlist
elif pagina == "Wishlist":
    st.title("🎯 O Santo Graal (Wishlist)")
    st.markdown("<p style='text-align: center; color: gray;'>Aquelas que ainda faltam para a coleção ficar perfeita.</p>", unsafe_allow_html=True)
    st.markdown("---")
    
    col1, col2 = st.columns(2) # Na wishlist usamos 2 colunas para focar mais na imagem
    
    for i, camisola in enumerate(wishlist):
        with [col1, col2][i % 2]:
            st.image(camisola["img"], use_column_width=True)
            st.subheader(f"✨ {camisola['clube']} ({camisola['ano']})")
            st.info(f"**Porquê?** {camisola['motivo']}")