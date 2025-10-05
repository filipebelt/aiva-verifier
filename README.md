# AIVA - Artificial Intelligence Verification Assistant

![Python](https://img.shields.io/badge/Python-3.12-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-1.50-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![PyTorch](https://img.shields.io/badge/PyTorch-2.8-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white)
![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Models-FFD21E?style=for-the-badge)

Um aplicativo web construído em Python e Streamlit para detectar se imagens e vídeos foram gerados por Inteligência Artificial.

![Print da Tela do AIVA](https://i.imgur.com/eaf53e.png) 
*Interface do AIVA em modo escuro, com o design inspirado no Grok.*

---

## 📜 Sobre o Projeto

O **AIVA** (Assistente de Verificação por Inteligência Artificial) é uma ferramenta poderosa e intuitiva para combater a desinformação visual. Em um mundo onde a geração de conteúdo por IA está se tornando cada vez mais realista, o AIVA oferece uma maneira rápida de verificar a autenticidade de mídias visuais, analisando imagens e vídeos em busca de padrões característicos de geração por IA.

Este projeto foi desenvolvido como uma solução completa (end-to-end), desde a criação da interface do usuário até a integração com um modelo de Deep Learning pré-treinado.

---

## ✨ Principais Funcionalidades

* **Análise de Imagens:** Faça o upload de arquivos `JPG`, `JPEG` ou `PNG` para uma análise instantânea.
* **Análise de Vídeos:** Suporte para vídeos (`MP4`, `MOV`, `AVI`) com análise frame a frame e um relatório final.
* **Interface Moderna:** Design responsivo e minimalista inspirado em aplicações modernas de IA, com temas claro e escuro.
* **Modelo de IA:** Utiliza um modelo de classificação de imagens (Vision Transformer) da plataforma Hugging Face.

---

## 🛠️ Tecnologias Utilizadas

* **Linguagem:** Python 3.12
* **Framework Web:** Streamlit
* **Inteligência Artificial:** PyTorch & Transformers (Hugging Face)
* **Processamento de Imagem/Vídeo:** OpenCV & Pillow
* **Outras bibliotecas:** Numpy, Pandas

---

## 🚀 Como Executar o Projeto

Para executar este projeto localmente, siga os passos abaixo:

1.  **Clone o repositório:**
    ```sh
    git clone [https://github.com/SEU-USUARIO/NOME-DO-REPOSITORIO.git](https://github.com/SEU-USUARIO/NOME-DO-REPOSITORIO.git)
    cd NOME-DO-REPOSITORIO
    ```

2.  **Crie e ative um ambiente virtual:**
    ```sh
    python -m venv venv
    venv\Scripts\activate.bat
    ```

3.  **Instale as dependências:**
    ```sh
    pip install -r requirements.txt
    ```

4.  **Execute o aplicativo Streamlit:**
    ```sh
    streamlit run src/ui_streamlit.py
    ```

O aplicativo estará disponível em `http://localhost:8501`.
