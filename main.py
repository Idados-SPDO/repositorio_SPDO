import streamlit as st
import json
from auth import login
from team_pages import team_page

def main():
    if 'authenticated' not in st.session_state:
        st.session_state.authenticated = False
    
    if not st.session_state.authenticated:
        if login():
            st.session_state.authenticated = True
    
    else:
        st.sidebar.image('fgv.png', use_column_width=True)
        st.sidebar.markdown('---')  # Adicionando uma linha horizontal para separar o título do conteúdo

        # Lista de equipes
        # Carregar o arquivo JSON
        with open("apps.json", "r", encoding="utf-8") as f:
            data = json.load(f)

        # Extrair apenas os nomes das equipes
        teams = ['Selecione a sua área aqui...']
        for area in data["areas"]:
            teams.append(area["name"])

        selected_team = st.sidebar.selectbox('SPDO - Áreas', teams,)
        if selected_team:
            team_page(selected_team)    

if __name__ == "__main__":
    main()
