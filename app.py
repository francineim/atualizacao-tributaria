import streamlit as st
import streamlit.components.v1 as components
import os

st.set_page_config(
    page_title="Atualização Tributária Diária",
    page_icon="⚖️",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Remove padding padrão do Streamlit para o HTML ocupar a tela toda
st.markdown("""
<style>
    .block-container { padding: 0 !important; max-width: 100% !important; }
    header { display: none !important; }
    footer { display: none !important; }
    #MainMenu { display: none !important; }
</style>
""", unsafe_allow_html=True)

# Caminho do HTML gerado pela tarefa agendada
HTML_FILE = os.path.join(os.path.dirname(__file__), "atualizacao-tributaria.html")

if os.path.exists(HTML_FILE):
    with open(HTML_FILE, "r", encoding="utf-8") as f:
        html_content = f.read()

    # Calcula altura aproximada para não cortar conteúdo
    components.html(html_content, height=1100, scrolling=True)

else:
    st.error(
        "⚠️ Arquivo `atualizacao-tributaria.html` não encontrado.\n\n"
        "Execute a tarefa agendada **atualizao_tributria** no Cowork para gerar o arquivo, "
        "depois faça push para o repositório GitHub."
    )
    st.info(
        "**Estrutura esperada do repositório:**\n"
        "```\n"
        "seu-repo/\n"
        "├── app.py\n"
        "├── requirements.txt\n"
        "└── atualizacao-tributaria.html   ← gerado pela tarefa agendada\n"
        "```"
    )
