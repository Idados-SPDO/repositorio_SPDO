import streamlit as st
import json
from pathlib import Path

with open("apps.json", "r", encoding="utf-8") as f:
    data = json.load(f)

def team_page(team_name):
    if team_name == 'Selecione a sua área aqui...':
        st.markdown("<h1 style='text-align: center; font-size:100px;'>SPDO</h1>", unsafe_allow_html=True)
        st.markdown("<h1 style='text-align: center;'>REPOSITÓRIO DE APLICAÇÕES</h1>", unsafe_allow_html=True)
        st.markdown("<h1 style='text-align: justify; font-size:18px; font-weight:lighter;'>O Repositório de Aplicações da SPDO é uma solução projetada para criar um ambiente centralizado, proporcionando armazenamento e organização de uma ampla gama de soluções tecnológicas. Seu objetivo primordial é simplificar o acesso e o compartilhamento de recursos entre diferentes setores e equipes, impulsionando a colaboração e a eficiência operacional em toda a organização.</h1>", unsafe_allow_html=True)
        st.markdown("<h1 style='font-weight:bold; text-align: center; font-size:14px;'>*** Explore o menu à esquerda, escolha sua área e veja os aplicativos disponíveis para uso ***</h1>", unsafe_allow_html=True)

        return

    st.markdown(
        f'<h1 style="text-align:center;font-size:24px">'
        f'Aplicações da área de {team_name}</h1>',
        unsafe_allow_html=True
    )

    for area in data["areas"]:
        if area["name"] != team_name:
            continue

        for link in area["links"]:
            with st.expander(link["name"]):
                # subtítulos e tutoriais em Markdown
                for sub in link["sublinks"]:
                    if "tutorial_url" in sub:
                        st.markdown(
                            f"📁 <a href='{sub['url']}' target='_blank'>{sub['name']}</a> — "
                            f"<a href='{sub['tutorial_url']}' target='_blank'>📄 Tutorial</a>",
                            unsafe_allow_html=True
                        )
                    else:
                        st.markdown(
                            f"📁 <a href='{sub['url']}' target='_blank'>{sub['name']}</a>",
                            unsafe_allow_html=True
                        )

                # seção de vídeos de tutorial
                videos = link.get("videos_tutorial", [])
                if videos:
                    st.markdown("#### 🎬 Vídeos de Tutorial")
                    for vid in videos:
                        # exibe o nome que você colocou
                        st.markdown(f"**{vid['name']}**")
                        src = vid["src"]
                        if src.startswith("http"):
                            # URL pública
                            st.video(src)
                        else:
                            # arquivo local
                            path = Path(src)
                            if path.exists():
                                st.video(path.read_bytes())
                            else:
                                st.error(f"❌ Vídeo não encontrado: {src}")
