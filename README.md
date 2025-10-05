# AIVA - Artificial Intelligence Verification Assistant

![Python](https://img.shields.io/badge/Python-3.12-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-1.50-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![PyTorch](https://img.shields.io/badge/PyTorch-2.8-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white)
![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Models-FFD21E?style=for-the-badge)

A web application built with Python and Streamlit to detect whether images and videos are AI-generated.

![AIVA Screenshot](https://i.imgur.com/eaf53e.png) 
*The AIVA interface in its Grok-inspired dark mode design.*

---

## 📜 About The Project

**AIVA** (Artificial Intelligence Verification Assistant) is a powerful and intuitive tool designed to combat visual misinformation. In a world where AI-generated content is becoming increasingly realistic, AIVA provides a quick way to verify the authenticity of visual media by analyzing images and videos for patterns characteristic of AI generation.

This project was developed as a complete end-to-end solution, from creating the user interface to integrating a pre-trained Deep Learning model.

---

## ✨ Key Features

* **Image Analysis:** Upload `JPG`, `JPEG`, or `PNG` files for instant analysis.
* **Video Analysis:** Supports `MP4`, `MOV`, and `AVI` files with frame-by-frame analysis and a final report.
* **Modern Interface:** A responsive and minimalist design inspired by modern AI applications.
* **AI Model:** Utilizes an image classification model (Vision Transformer) from the Hugging Face platform.

---

## 🛠️ Tech Stack

* **Language:** Python 3.12
* **Web Framework:** Streamlit
* **Artificial Intelligence:** PyTorch & Transformers (Hugging Face)
* **Image/Video Processing:** OpenCV & Pillow
* **Other Libraries:** Numpy, Pandas

---

## 🚀 How To Run

To run this project locally, follow these steps:

1.  **Clone the repository:**
    ```sh
    git clone [https://github.com/filipebelt/aiva.git](https://github.com/filipebelt/aiva.git)
    cd aiva
    ```

2.  **Create and activate a virtual environment:**
    ```sh
    python -m venv venv
    venv\Scripts\activate.bat
    ```

3.  **Install the dependencies:**
    ```sh
    pip install -r requirements.txt
    ```

4.  **Run the Streamlit app:**
    ```sh
    streamlit run src/ui_streamlit.py
    ```

The application will be available at `http://localhost:8501`.