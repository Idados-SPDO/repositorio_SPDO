import streamlit as st
import json

with open("apps.json", "r", encoding="utf-8") as f:
    data = json.load(f)

def team_page(team_name):
    if team_name != 'Selecione a sua área aqui...':
        st.markdown(f'<h1 style="text-align: center; font-size:24px">Aplicações da área de {team_name}</h1>', unsafe_allow_html=True)
        st.markdown("<h1 style='text-align: left; font-size:18px; font-weight:lighter;'>Selecione abaixo o app que deseja utilizar:</h1>", unsafe_allow_html=True)
        for area in data["areas"]:
            if area["name"] == team_name:
                links = area["links"]
                for link in links:
                    link_name = link["name"]
                    sublinks = link["sublinks"]
                    button_expander = st.button(link_name)
                    if button_expander:
                        for sublink in sublinks:
                             st.write(f"<div><a href='{sublink['url']}' style='margin-right: 20px;'>{sublink['name']}</a>&#128209 Tutorial</div>", unsafe_allow_html=True)  # Adiciona o texto "Tutorial" ao lado do link com um espaço de 20px entre o link e o emoji do livro

    else:
        st.markdown("<h1 style='text-align: center; font-size:100px;'>SPDO</h1>", unsafe_allow_html=True)
        st.markdown("<h1 style='text-align: center;'>REPOSITÓRIO DE APLICAÇÕES</h1>", unsafe_allow_html=True)
        st.markdown("<h1 style='text-align: justify; font-size:18px; font-weight:lighter;'>O Repositório de Aplicações da SPDO é uma solução projetada para criar um ambiente centralizado, proporcionando armazenamento e organização de uma ampla gama de soluções tecnológicas. Seu objetivo primordial é simplificar o acesso e o compartilhamento de recursos entre diferentes setores e equipes, impulsionando a colaboração e a eficiência operacional em toda a organização.</h1>", unsafe_allow_html=True)
        st.markdown("<h1 style='font-weight:bold; text-align: center; font-size:14px;'>*** Explore o menu à esquerda, escolha sua área e veja os aplicativos disponíveis para uso ***</h1>", unsafe_allow_html=True)
