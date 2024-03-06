import streamlit as st

areas = {
    "Cadastramento e Governança BP": {"Calculadora Digital": "https://calculadora-ehmlxleg8k28ehpsa4ox77.streamlit.app/", 
                                      "Globo.com": "https://www.globo.com/", 
                                      "Busca de informantes": "https://www.globo.com/"},
    "Coleta Tradicional": {"Globo.com": "https://www.globo.com/", 
                           "Busca de insumos informados": "https://www.globo.com/"},
    "Coleta Não Tradicional": {"Link 1": "https://www.globo.com/"},
    "Inteligência de Dados": {},
    "Pessoas e Qualidade": {},
    "Processos e Projetos": {},
    "Relacionamento": {},
    "Setorial": {},
    "Sondagem": {},
    "Vertical": {}
}

def team_page(team_name):
    if team_name != 'Selecione a sua área aqui...':
        st.markdown(f'<h1 style="text-align: center; font-size:24px">Aplicações da área de {team_name}</h1>', unsafe_allow_html=True)
        st.markdown("<h1 style='text-align: left; font-size:18px; font-weight:lighter;'>Selecione abaixo o app que deseja utilizar:</h1>", unsafe_allow_html=True)
        links = areas[team_name]
        for link_name, link_url in links.items():
            st.write(f"[{link_name}]({link_url})")
        # Adicione aqui as funcionalidades específicas para cada equipe

    else:
        st.markdown("<h1 style='text-align: center; font-size:100px;'>SPDO</h1>", unsafe_allow_html=True)
        st.markdown("<h1 style='text-align: center;'>REPOSITÓRIO DE APLICAÇÕES</h1>", unsafe_allow_html=True)
        st.markdown("<h1 style='text-align: justify; font-size:18px; font-weight:lighter;'>O Repositório de Aplicações da SPDO é uma solução projetada para criar um ambiente centralizado, proporcionando armazenamento e organização de uma ampla gama de soluções tecnológicas. Seu objetivo primordial é simplificar o acesso e o compartilhamento de recursos entre diferentes setores e equipes, impulsionando a colaboração e a eficiência operacional em toda a organização.</h1>", unsafe_allow_html=True)
        st.markdown("<h1 style='font-weight:bold; text-align: center; font-size:14px;'>*** Explore o menu à esquerda, escolha sua área e veja os aplicativos disponíveis para uso ***</h1>", unsafe_allow_html=True)

def main():
    st.sidebar.image('fgv.png', use_column_width=True)
    st.sidebar.markdown('---')  # Adicionando uma linha horizontal para separar o título do conteúdo

    # Lista de equipes
    teams = ['Selecione a sua área aqui...',
            'Cadastramento e Governança BP', 
            'Coleta Tradicional', 
            'Coleta Não Tradicional', 
            'Inteligência de Dados', 
            'Pessoas e Qualidade', 
            'Processos e Projetos', 
            'Relacionamento', 
            'Setorial', 
            'Sondagem', 
            'Vertical']

    selected_team = st.sidebar.selectbox('SPDO - Áreas', teams,)
    if selected_team:
        team_page(selected_team)    

if __name__ == "__main__":
    main()
