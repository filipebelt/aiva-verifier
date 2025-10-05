# src/detector.py (Com a correção final do NameError)

import streamlit as st
from PIL import Image
from transformers import AutoProcessor, AutoModelForImageClassification
import torch
import cv2
import numpy as np

@st.cache_resource
def load_model():
    # Modelo original e funcional
    model_name = "umm-maybe/AI-image-detector"
    
    print(f"Carregando o modelo original: {model_name}...")
    
    processor = AutoProcessor.from_pretrained(model_name)
    model = AutoModelForImageClassification.from_pretrained(model_name)
    
    print("Modelo original carregado com sucesso!")
    
    return processor, model

def analyze_image(image: Image.Image):
    processor, model = load_model()
    image = image.convert("RGB")
    
    inputs = processor(images=image, return_tensors="pt")
    
    with torch.no_grad():
        outputs = model(**inputs)
        logits = outputs.logits

    probabilities = torch.nn.functional.softmax(logits, dim=1)
    predicted_class_idx = probabilities.argmax(-1).item()
    result_label = model.config.id2label[predicted_class_idx]
    confidence = probabilities[0][predicted_class_idx].item()

    if result_label == 'human':
        final_result = "Provavelmente Humano"
    else: # result_label == 'ai'
        final_result = "Provavelmente Gerado por IA"

    return final_result, confidence

def analyze_video(video_file, progress_bar):
    cap = cv2.VideoCapture(video_file)
    
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    frames_to_process = min(total_frames, 90)
    
    ai_count = 0
    human_count = 0
    
    for i in range(frames_to_process):
        success, frame = cap.read()
        if not success: break
            
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        pil_image = Image.fromarray(rgb_frame)
        
        result, _ = analyze_image(pil_image)
        
        if result == "Provavelmente Gerado por IA":
            ai_count += 1
        else:
            human_count += 1
            
        progress_bar.progress((i + 1) / frames_to_process)
        
    cap.release()
    
    # --- LINHA CORRIGIDA AQUI ---
    return human_count, ai_count # Trocamos 'ai_frames' por 'ai_count'