# AIVA – AI Verifier  
**Detecte se uma imagem ou vídeo foi gerado por Inteligência Artificial ou é real.**

AIVA (Artificial Intelligence Verification Assistant) é um sistema desenvolvido em **Python** que identifica se um conteúdo visual (imagem ou vídeo) foi criado por IA ou capturado do mundo real.  
O projeto utiliza modelos de visão computacional, pré-processamento avançado e um pipeline otimizado para deploy em nuvem.

---

## 🚀 Tecnologias Utilizadas
- **Python 3**
- **Streamlit** (UI)
- **OpenCV** (processamento de imagens e vídeos)
- **TensorFlow/Keras** (modelo de classificação)
- **NumPy / Pillow**
- **Docker** (containerização)
- **Google Cloud Run** (deploy serverless)
- **Google Cloud Build & Artifact Registry**

---

## 🌐 Aplicação Online
Acesse a versão ativa do projeto:  
👉 **https://aiva-verifier-999132669974.us-central1.run.app/**

---

## 🧠 Como Funciona
1. O usuário faz upload de uma imagem ou vídeo.  
2. O pipeline de pré-processamento converte o conteúdo para o formato ideal.  
3. O modelo neural analisa texturas, padrões de geração, ruído estatístico e marcas comuns de conteúdo sintético.  
4. O sistema retorna:  
   - **IA Gerada**  
   - **Imagem/Video Real**  
   - Probabilidade  
   - Explicação técnica simplificada  

---

## 🛠 Como Rodar Localmente
```bash
git clone https://github.com/filipebelt/aiva-verifier
cd aiva-verifier
pip install -r requirements.txt
streamlit run main.py
