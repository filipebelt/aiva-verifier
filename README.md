# AIVA – AI Verifier

Sistema de detecção desenvolvido para identificar se imagens ou vídeos foram gerados por Inteligência Artificial ou se são conteúdos reais.

---

### Tecnologias / Status

![Python](https://img.shields.io/badge/Python-3.10-blue)
![Streamlit](https://img.shields.io/badge/Framework-Streamlit-red)
![Cloud Run](https://img.shields.io/badge/Deploy-Google%20Cloud%20Run-green)
![Status](https://img.shields.io/badge/Online-Sim-success)

---

### Acessar Aplicação

[![Acessar Aplicação](https://img.shields.io/badge/ABRIR%20AIVA-1a73e8?style=for-the-badge&logo=google-chrome&logoColor=white)](https://aiva-verifier-999132669974.us-central1.run.app/)

---

## Índice

- [Sobre o Projeto](#sobre-o-projeto)
- [Funcionalidades](#funcionalidades)
- [Tecnologias Utilizadas](#tecnologias-utilizadas)
- [Demonstração](#demonstração)
- [Como Rodar Localmente](#como-rodar-localmente)
- [Docker](#docker)
- [Deploy no Google Cloud](#deploy-no-google-cloud)
- [Status do Projeto](#status-do-projeto)
- [Autor](#autor)

---

## Sobre o Projeto

AIVA (Artificial Intelligence Verification Assistant) é um sistema em Python que analisa imagens ou vídeos para determinar se foram produzidos por modelos de IA ou se são reais.

O projeto utiliza técnicas de visão computacional, análise de padrões sintéticos, detecção de ruído e pré-processamento para gerar uma classificação confiável e interpretável.

---

## Funcionalidades

- Detecção de imagens geradas por IA  
- Análise de vídeos  
- Probabilidade da classificação  
- Interface Web via Streamlit  
- Execução via Docker  
- Deploy escalável no Google Cloud Run  

---

## Tecnologias Utilizadas

- Python 3  
- Streamlit  
- OpenCV  
- NumPy / Pillow  
- TensorFlow / Keras (ou PyTorch)  
- Docker  
- Google Cloud Run  
- Google Cloud Build  
- Google Artifact Registry  

---

## Demonstração

### Interface da Aplicação

![Print 1](docs/Captura%20de%20tela%202025-11-26%20142323.png)

![Print 2](docs/Captura%20de%20tela%202025-11-26%20142402.png)

---

## Como Rodar Localmente

```bash
git clone https://github.com/filipebelt/aiva-verifier
cd aiva-verifier
pip install -r requirements.txt
streamlit run main.py
---

---

## Docker

docker build -t aiva-verifier .
docker run -p 8080:8080 aiva-verifier

---

## Deploy no Google Cloud

Pipeline utilizado:

1. Build com Cloud Build  
2. Imagem armazenada no Artifact Registry  
3. Deploy realizado no Cloud Run  

Comando de deploy (exemplo):

gcloud run deploy aiva-verifier \
  --image=gcr.io/SEU_PROJETO/aiva \
  --region=us-central1 \
  --platform=managed

---

## Status do Projeto

- Projeto online e funcional  
- Versão: 1.0.0  
- Melhorias contínuas em desenvolvimento  

---

## Autor

Filipe Corrêa  
Engenharia de Software • Cloud • Inteligência Artificial  

LinkedIn: https://www.linkedin.com/in/filipebelt/  
GitHub: https://github.com/filipebelt
