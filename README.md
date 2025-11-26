# AIVA – AI Verifier

Sistema de detecção que identifica se imagens ou vídeos foram gerados por Inteligência Artificial ou se são reais.

---

### Badges

![Python](https://img.shields.io/badge/Python-3.10-blue)
![Streamlit](https://img.shields.io/badge/Framework-Streamlit-red)
![Cloud Run](https://img.shields.io/badge/Deploy-Google%20Cloud%20Run-brightgreen)
![Status](https://img.shields.io/badge/Online-Yes-success)

---

### Testar Aplicação

[![Acessar AIVA](https://img.shields.io/badge/Acessar%20Aplicação-1a73e8?style=for-the-badge&logo=google-chrome&logoColor=white)](https://aiva-verifier-999132669974.us-central1.run.app/)

---

## Índice
- [Sobre o Projeto](#sobre-o-projeto)
- [Funcionalidades](#funcionalidades)
- [Tecnologias Utilizadas](#tecnologias-utilizadas)
- [Demonstração](#demonstração)
- [Como Rodar Localmente](#como-rodar-localmente)
- [Rodando com Docker](#rodando-com-docker)
- [Deploy no Google Cloud](#deploy-no-google-cloud)
- [Status do Projeto](#status-do-projeto)
- [Autor](#autor)

---

## Sobre o Projeto

AIVA (Artificial Intelligence Verification Assistant) é um sistema desenvolvido em Python capaz de identificar se uma **imagem ou vídeo** foi gerado por ferramentas de IA ou se é um conteúdo real.

O sistema utiliza modelos de visão computacional, análise de padrões sintéticos, ruído e técnicas de pré-processamento para entregar uma classificação confiável.

---

## Funcionalidades

- Detecção de imagens reais vs. geradas por IA  
- Análise de vídeos  
- Probabilidade e explicação simplificada  
- Interface Web via Streamlit  
- Execução em Docker  
- Deploy automatizado e escalável no Google Cloud Run  

---

## Tecnologias Utilizadas

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

## Rodando com Docker

docker build -t aiva-verifier .
docker run -p 8080:8080 aiva-verifier

---

## Deploy no Google Cloud

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

## Status do Projeto

- Online e funcional  
- Versão: 1.0.0  
- Recebendo melhorias contínuas  

---

## Autor

**Filipe Corrêa**  
Estudante de Engenharia de Software — Cloud — IA  

🔗 LinkedIn: https://www.linkedin.com/in/filipebelt/  
🔗 GitHub: https://github.com/filipebelt

