import streamlit as st
import yaml

def load_credentials():
    with open("credenciais.yaml", "r") as f:
        config = yaml.safe_load(f)
    return config["credenciais"]

credenciais = load_credentials()

def login():
    st.sidebar.image('fgv.png', use_column_width=True)
    st.sidebar.markdown('---')  # Adicionando uma linha horizontal para separar o título do conteúdo
    username = st.sidebar.text_input("Usuário")
    password = st.sidebar.text_input("Senha", type="password")
    st.markdown("<h1 style='text-align: center; font-size:100px;'>SPDO</h1>", unsafe_allow_html=True)
    st.markdown("<h1 style='text-align: center;'>REPOSITÓRIO DE APLICAÇÕES</h1>", unsafe_allow_html=True)
    st.markdown("<h1 style='text-align: justify; font-size:18px; font-weight:lighter;'>O Repositório de Aplicações da SPDO é uma solução projetada para criar um ambiente centralizado, proporcionando armazenamento e organização de uma ampla gama de soluções tecnológicas. Seu objetivo primordial é simplificar o acesso e o compartilhamento de recursos entre diferentes setores e equipes, impulsionando a colaboração e a eficiência operacional em toda a organização.</h1>", unsafe_allow_html=True)
    st.markdown("<h1 style='font-weight:bold; text-align: center; font-size:14px;'>*** Explore o menu à esquerda, escolha sua área e veja os aplicativos disponíveis para uso ***</h1>", unsafe_allow_html=True)


    if st.sidebar.button("Login"):
        if username in credenciais and credenciais[username] == password:
            st.sidebar.success("Login efetuado com sucesso!")
            return True
            
        else:
            st.sidebar.error("Usuário ou senha incorretos.")
            return False
