# src/ui_streamlit.py (Versão 1.0 - Design Final)

import streamlit as st
from PIL import Image
from detector import analyze_image, analyze_video
import tempfile
import os

def load_css():
    st.markdown("""
        <style>
            .main .block-container {
                padding-top: 2rem; padding-bottom: 2rem; padding-left: 1rem; padding-right: 1rem;
                max-width: 800px; margin: auto;
            }
            .center-text { text-align: center; }
            .grok-title {
                font-size: 8rem; font-weight: 800; color: #FFFFFF;
                text-shadow: 0 0 15px #8A2BE2, 0 0 35px #8A2BE2;
                letter-spacing: 0.15em; margin-bottom: 0.5rem;
            }
            .subtitle {
                color: #A0A0B0; margin-bottom: 3rem; font-size: 1.1em;
            }
            section[data-testid="stFileUploadDropzone"] {
                border: 1px solid #4A4A5E; background-color: #1E1E2E;
                border-radius: 40px; padding: 1rem 1.5rem; transition: all 0.3s ease;
            }
            section[data-testid="stFileUploadDropzone"]:hover {
                border-color: #8A2BE2; box-shadow: 0 0 15px rgba(138, 43, 226, 0.5);
            }
            div[data-testid="stFileUploader"] { border: none; background: none; padding: 0; }
            div[data-testid="stFileUploader"] button {
                 background-color: #33334A; border: none; border-radius: 20px; padding: 8px 20px;
            }
            div[data-testid="stFileUploaderFileList"] { width: 100%; }
            div[data-testid="stFileUploader"] li { color: #A0A0B0; }
            .stButton>button {
                border: 2px solid #8A2BE2; background-color: transparent; color: white;
                border-radius: 12px; padding: 12px 28px; font-weight: bold;
                transition: all 0.3s ease; margin: 1rem auto; display: block;
            }
            .stButton>button:hover {
                background-color: #8A2BE2; box-shadow: 0 0 20px #8A2BE2; transform: scale(1.05);
            }
            img, video { border-radius: 12px; }
            div[data-testid="stTab"] button[aria-selected="true"] {
                border-bottom: 3px solid #8A2BE2;
            }
        </style>
    """, unsafe_allow_html=True)

# --- Início do App ---
load_css()

st.markdown("<div class='center-text grok-title'>AIVA</div>", unsafe_allow_html=True)
st.markdown("<div class='center-text subtitle'>Artificial Intelligence Verification Assistant by Filipe Correa</div>", unsafe_allow_html=True)

tab1, tab2 = st.tabs(["Análise de Imagem", "Análise de Vídeo"])

with tab1:
    uploaded_image = st.file_uploader("Carregue uma imagem", type=["jpg", "jpeg", "png"], key="image_uploader", label_visibility="collapsed")
    
    if uploaded_image:
        image = Image.open(uploaded_image)
        st.image(image, caption="Imagem Carregada", use_container_width=True)
        if st.button("Analisar Imagem"):
            with st.spinner('Analisando...'):
                result, confidence = analyze_image(image)
            st.subheader("Resultado da Análise:")
            col1, col2 = st.columns(2)
            with col1:
                # --- MUDANÇA AQUI: Usando st.success e st.error ---
                if result == "Provavelmente Humano":
                    st.success("Resultado: Humano")
                else:
                    st.error("Resultado: Gerado por IA")
            with col2:
                st.metric(label="Nível de Confiança", value=f"{confidence:.1%}")

with tab2:
    uploaded_video = st.file_uploader("Carregue um vídeo", type=["mp4", "mov", "avi"], key="video_uploader", label_visibility="collapsed")

    if uploaded_video:
        st.video(uploaded_video)
        if st.button("Analisar Vídeo"):
            with tempfile.NamedTemporaryFile(delete=False, suffix='.mp4') as tfile:
                tfile.write(uploaded_video.read())
                video_path = tfile.name
            
            progress_bar = st.progress(0, text="Analisando frames...")
            with st.spinner('Processando vídeo...'):
                human_frames, ai_frames = analyze_video(video_path, progress_bar)
            
            progress_bar.empty()
            os.remove(video_path)
            
            total_frames = human_frames + ai_frames
            ai_percentage = (ai_frames / total_frames) * 100 if total_frames > 0 else 0
            
            st.subheader("Resultado da Análise do Vídeo:")

            col1, col2 = st.columns(2)
            with col1:
                # --- MUDANÇA AQUI: Unificando o texto ---
                if ai_percentage > 50:
                    st.error("Resultado: Gerado por IA")
                    confidence_video = ai_percentage
                else:
                    st.success("Resultado: Humano")
                    confidence_video = 100 - ai_percentage
            with col2:
                st.metric(label="Nível de Confiança", value=f"{confidence_video:.1f}%")

            st.caption(f"Detalhes: {total_frames} frames analisados | {ai_frames} frames de IA | {human_frames} frames Humanos")