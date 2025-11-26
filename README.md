# 🤖 AIVA – AI Verifier

**Detecte se uma imagem ou vídeo foi gerado por Inteligência Artificial ou é real.**

---

### 🏷️ Badges

![Python](https://img.shields.io/badge/Python-3.10-blue)
![Streamlit](https://img.shields.io/badge/Framework-Streamlit-red)
![Deploy](https://img.shields.io/badge/Deploy-Google%20Cloud%20Run-brightgreen)
![Status](https://img.shields.io/badge/Status-Online-success)

---

### 🌐 Testar Aplicação

[![Testar AIVA](https://img.shields.io/badge/🌐%20TESTAR%20AIVA-0000FF?style=for-the-badge)](https://aiva-verifier-999132669974.us-central1.run.app/)

---

## 📌 Índice

- [Sobre o Projeto](#-sobre-o-projeto)
- [Funcionalidades](#-funcionalidades)
- [Tecnologias Utilizadas](#-tecnologias-utilizadas)
- [Demonstração](#-demonstração)
- [Como Rodar Localmente](#-como-rodar-localmente)
- [Rodando com Docker](#-rodando-com-docker)
- [Deploy no Google Cloud](#-deploy-no-google-cloud)
- [Status do Projeto](#-status-do-projeto)
- [Autor](#-autor)

---

## 🧠 Sobre o Projeto

AIVA (Artificial Intelligence Verification Assistant) é um sistema desenvolvido em Python que identifica se **imagens ou vídeos** foram gerados por Inteligência Artificial ou são reais.

Ele utiliza modelos de visão computacional, análise de ruído, padrões sintéticos e técnicas de pré-processamento para classificar o conteúdo com alta precisão.

---

## ⚙️ Funcionalidades

- 📸 Detecção de imagens reais vs. IA  
- 🎥 Análise de vídeos  
- 🔍 Probabilidade e explicação simplificada  
- 🌐 Interface com Streamlit  
- 🐳 Docker para rodar em qualquer ambiente  
- ☁️ Deploy automatizado no Google Cloud Run  

---

## 🚀 Tecnologias Utilizadas

- Python 3
- Streamlit
- OpenCV
- NumPy / Pillow
- TensorFlow / Keras (ou PyTorch)
- Docker
- Google Cloud Run
- Google Cloud Artifact Registry
- Google Cloud Build

---

## 🖼️ Demonstração

### 📸 Interface da Aplicação

![Print 1](docs/Captura%20de%20tela%202025-11-26%20142323.png)

![Print 2](docs/Captura%20de%20tela%202025-11-26%20142402.png)

---

## 🛠 Como Rodar Localmente

```bash
git clone https://github.com/filipebelt/aiva-verifier
cd aiva-verifier
pip install -r requirements.txt
streamlit run main.py
---

## 🐳 Rodando com Docker

docker build -t aiva-verifier .
docker run -p 8080:8080 aiva-verifier

---

## ☁️ Deploy no Google Cloud

Pipeline utilizado:

1. Build via Cloud Build  
2. Armazenamento da imagem no Artifact Registry  
3. Deploy no Cloud Run  

Comando usado:

gcloud run deploy aiva-verifier \
  --image=gcr.io/SEU_PROJETO/aiva \
  --region=us-central1 \
  --platform=managed

---
