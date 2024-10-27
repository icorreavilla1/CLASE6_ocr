import streamlit as st
import cv2
import numpy as np
import pytesseract
from PIL import Image

# Configuración del título y descripción
st.title("🔍✨ OCR Mágico en Vivo")
st.markdown("#### Extrae texto de tus fotos en un instante! 📸")
st.write("Solo toma una foto y elige si quieres agregar un toque de magia con un filtro. 🪄")

# Agregar una imagen de bienvenida
st.image("https://images.unsplash.com/photo-1589571894960-20bbe2828b12", use_column_width=True, caption="El poder del OCR al alcance de un clic")

# Configuración de la cámara y carga de imagen
img_file_buffer = st.camera_input("👉 ¡Toma una Foto Aquí!")

# Configuración de la barra lateral
with st.sidebar:
    st.header("🎨 Estilo de la Imagen")
    filtro = st.radio("Selecciona un filtro de magia:", ('✨ Con Filtro', '📸 Sin Filtro'))

# Procesamiento de la imagen si se ha capturado alguna
if img_file_buffer is not None:
    # Leer la imagen capturada usando OpenCV
    bytes_data = img_file_buffer.getvalue()
    cv2_img = cv2.imdecode(np.frombuffer(bytes_data, np.uint8), cv2.IMREAD_COLOR)
    
    # Aplicar filtro según la selección del usuario
    if filtro == '✨ Con Filtro':
        cv2_img = cv2.bitwise_not(cv2_img)  # Filtro tipo 'invertir colores'
    else:
        cv2_img = cv2_img
    
    # Convertir la imagen a RGB para OCR
    img_rgb = cv2.cvtColor(cv2_img, cv2.COLOR_BGR2RGB)
    text = pytesseract.image_to_string(img_rgb)
    
    # Mostrar resultados
    st.subheader("📝 Texto Detectado:")
    st.write(text if text else "¡No se detectó texto! Inténtalo de nuevo.")
    
    # Mostrar imagen procesada
    st.image(img_rgb, caption="📄 Imagen Procesada", use_column_width=True)
else:
    st.info("Espera a tomar una foto para ver el resultado 📸")

# Pie de página
st.markdown("---")
st.markdown("✨ **OCR Mágico en Vivo** - Potenciado por OpenCV, Tesseract y Streamlit")
 
    


    


