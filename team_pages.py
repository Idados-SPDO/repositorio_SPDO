import streamlit as st

areas = {
    "Cadastramento e Governança BP": {"Calculadora Digital":{"teste1": "https://calculadora-ehmlxleg8k28ehpsa4ox77.streamlit.app/"}, 
                                      "Globo.com": {"Tratar Lote": "https://www.globo.com/", 
                                                    "Ensaio": "https://www.globo.com/"},
                                      "Busca de informantes":{"teste": "https://www.globo.com/"}},
    "Coleta Tradicional": {},
    "Coleta Não Tradicional": {},
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
        for link_name, sublinks in links.items():
            if sublinks:
                button_expander = st.button(link_name)
                if button_expander:
                    for sublink_name, sublink_url in sublinks.items():
                        st.write(f"[{sublink_name}]({sublink_url})")
            else:
                st.write(f"[{link_name}]")
        # Adicione aqui as funcionalidades específicas para cada equipe

    else:
        st.markdown("<h1 style='text-align: center; font-size:100px;'>SPDO</h1>", unsafe_allow_html=True)
        st.markdown("<h1 style='text-align: center;'>REPOSITÓRIO DE APLICAÇÕES</h1>", unsafe_allow_html=True)
        st.markdown("<h1 style='text-align: justify; font-size:18px; font-weight:lighter;'>O Repositório de Aplicações da SPDO é uma solução projetada para criar um ambiente centralizado, proporcionando armazenamento e organização de uma ampla gama de soluções tecnológicas. Seu objetivo primordial é simplificar o acesso e o compartilhamento de recursos entre diferentes setores e equipes, impulsionando a colaboração e a eficiência operacional em toda a organização.</h1>", unsafe_allow_html=True)
        st.markdown("<h1 style='font-weight:bold; text-align: center; font-size:14px;'>*** Explore o menu à esquerda, escolha sua área e veja os aplicativos disponíveis para uso ***</h1>", unsafe_allow_html=True)
