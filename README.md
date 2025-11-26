<h1 align="center">🧠 AIVA – Assistente de Autenticação Visual por IA</h1>
<p align="center">
  <em>Sistema avançado que detecta se imagens ou vídeos foram gerados por Inteligência Artificial ou capturados por câmeras reais.</em>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Status-Online-brightgreen?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/Google%20Cloud-Cloud%20Run-4285F4?style=for-the-badge&logo=googlecloud&logoColor=white"/>
  <img src="https://img.shields.io/badge/HuggingFace-Transformers-FFD21E?style=for-the-badge&logo=huggingface&logoColor=black"/>
</p>

---

## 🚀 Demonstração ao Vivo

<p align="center">
  <a href="https://aiva-verifier-999132669974.us-central1.run.app" target="_blank">
    <img src="https://img.shields.io/badge/🔗%20ABRIR%20AIVA%20AGORA-8A2BE2?style=for-the-badge&logo=data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjQiIGhlaWdodD0iMjQiIHZpZXdCb3g9IjAgMCAyNCAyNCIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48cGF0aCBkPSJNMTIgMjFDMTcuNTIyMSAyMSAyMSAxNy41MjIxIDIxIDEyQzIxIDYuNDc3NzkgMTcuNTIyMSAzIDEyIDNDNi40Nzc3OSAzIDMgNi40Nzc3OSAzIDEyQzMgMTcuNTIyMSA2LjQ3Nzc5IDIxIDEyIDIxWk0xMiAyMUM2LjQ3Nzc5IDIxIDMgMTcuNTIyMSAzIDEyQzMgNi40Nzc3OSA2LjQ3Nzc5IDMgMTIgM0MxNy41MjIxIDMgMjEgNi40Nzc3OSAyMSAxMkMyMSAxNy41MjIxIDE3LjUyMjEgMjEgMTIgMjFaIiBmaWxsPSJ3aGl0ZSIvPjwvc3ZnPg==" />
  </a>
</p>

Faça upload de qualquer **imagem** ou **vídeo** e receba a classificação imediatamente.

<p align="center">
  <img src="docs/print1.png" width="80%" />
</p>

<p align="center">
  <img src="docs/print2.png" width="80%" />
</p>

---

## 📌 Visão Geral

A **AIVA** (Artificial Intelligence Visual Authentication) é uma solução completa que identifica padrões característicos de conteúdo gerado por IA.

Ela detecta se um conteúdo é:

- ✔️ **Gerado por Inteligência Artificial**, ou  
- ✔️ **Capturado por um dispositivo real**

O sistema combina:

- **Visão computacional**  
- **Modelos de Deep Learning (HuggingFace)**  
- **Infraestrutura serverless do Google Cloud**

---

## 🧠 Como funciona

### 🔥 Modelo HuggingFace
- Detector de mídia gerada por IA  
- Extração de features  
- Análise de embeddings  
- Probabilidade final **IA vs Humano**

### ⚡ Interface Streamlit
- Design limpo e moderno  
- Suporte a vídeos e imagens  
- Respostas em tempo real  

### ☁️ Arquitetura Google Cloud
- Cloud Run (serverless & escalável)  
- Cloud Storage (armazenamento temporário)  
- IAM seguro  
- Baixa latência e alta disponibilidade  

---

## 🛠️ Tecnologias Utilizadas

### **Inteligência Artificial**
- PyTorch  
- Transformers (HuggingFace)  
- Vision Transformer Models  

### **Backend**
- Python  
- Streamlit  
- Processamento de vídeo  
- Sistema de caching inteligente  

### **Cloud & DevOps**
- Docker  
- Google Cloud Run  
- Cloud Storage  
- CI/CD (GitHub Actions Ready)  

---

## ✨ Funcionalidades

- 🖼️ **Análise de Imagens** (PNG, JPG, JPEG)  
- 🎥 **Análise de Vídeos** (MP4, MOV, AVI)  
- ⚡ Resultados rápidos e precisos  
- 📊 Probabilidade clara (ex.: 62% IA)  
- 🖥️ Interface moderna  

---

## 📂 Estrutura do Projeto

