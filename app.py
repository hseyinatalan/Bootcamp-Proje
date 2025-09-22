import streamlit as st
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model
from PIL import Image
import matplotlib.pyplot as plt

# 1. Modeli yükle
model = load_model("optimized_cnn_model.h5")

# 2. Sınıf isimlerini tanımla (KENDİ sınıflarını yaz buraya!)
class_names = ["buildings", "forest", "glacier", "mountain", "sea", "street"]

st.title("🌍 Görsel Sınıflandırma Uygulaması")
st.write("Bir görsel yükle ve modelin tahminini gör!")

# 3. Görsel yükleme
uploaded_file = st.file_uploader("Bir görsel yükle", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Görseli aç
    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, caption="Yüklenen Görsel", use_column_width=True)

    # Modelin beklediği boyuta göre resize (örneğin 128x128 diyelim)
    img_resized = image.resize((150, 150))  
    img_array = np.array(img_resized) / 255.0  # normalize et
    img_array = np.expand_dims(img_array, axis=0)  # batch dimension ekle

    # Tahmin yap
    predictions = model.predict(img_array)
    confidence = np.max(predictions)
    predicted_class = class_names[np.argmax(predictions)]

    # 4. Sonuçları göster
    st.subheader("📊 Tahmin Sonuçları")
    fig, ax = plt.subplots()
    ax.bar(class_names, predictions[0])
    ax.set_ylabel("Olasılık")
    ax.set_xlabel("Sınıflar")
    plt.xticks(rotation=45)
    st.pyplot(fig)

    # 5. Bilinmeyen sınıf kontrolü
    if confidence < 0.8:
        st.error("❌ Bu görsel modelin bildiği sınıflara benzemiyor (Bilinmeyen sınıf).")
    else:
        st.success(f"✅ Tahmin: **{predicted_class}** (Güven: %{confidence*100:.2f})")