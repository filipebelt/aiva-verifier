<h1 align="center">🤖 AIVA – AI Verifier</h1>

<p align="center">
  <strong>Detecte se uma imagem ou vídeo foi gerado por Inteligência Artificial ou é real.</strong>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10-blue" />
  <img src="https://img.shields.io/badge/Framework-Streamlit-red" />
  <img src="https://img.shields.io/badge/Deploy-Google%20Cloud%20Run-brightgreen" />
  <img src="https://img.shields.io/badge/Status-Online-success" />
</p>

<br>

<p align="center">
  <a href="https://aiva-verifier-999132669974.us-central1.run.app/">
    <img src="https://img.shields.io/badge/🌐 Testar%20Aplicação-AIVA-blue?style=for-the-badge" />
  </a>
</p>

---

## 📌 **Índice**
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


## 🧠 **Sobre o Projeto**
AIVA (Artificial Intelligence Verification Assistant) é uma ferramenta criada para identificar se **imagens ou vídeos** foram gerados por IA (como Midjourney, DALL·E, Runway, etc.) ou se são conteúdos **reais**.

O sistema utiliza modelos de visão computacional e técnicas de análise estatística de ruído e padrões artificiais presentes em conteúdo sintético.

---

## ⚙️ **Funcionalidades**
- 📸 **Detecção de imagens artificiais ou reais**
- 🎥 **Análise de vídeos**
- 🔍 **Probabilidade e explicação da classificação**
- 🌐 **Interface fácil de usar via Streamlit**
- 🚀 **Deploy automático e escalável no Google Cloud Run**
- 🐳 **Container Docker pronto para rodar em qualquer ambiente**

---

## 🚀 **Tecnologias Utilizadas**
- **Python 3**
- **Streamlit**
- **OpenCV**
- **NumPy / Pillow**
- **TensorFlow/Keras** (ou PyTorch, dependendo da versão final)
- **Docker**
- **Google Cloud Run**
- **Google Cloud Artifact Registry**
- **Google Cloud Build**

---

## 🖼️ **Demonstração**
> *Adicione aqui futuramente prints ou GIF de demonstração da interface.*

---

## 🛠 **Como Rodar Localmente**
```bash
git clone https://github.com/filipebelt/aiva-verifier
cd aiva-verifier
pip install -r requirements.txt
streamlit run main.py


