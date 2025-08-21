import streamlit as st
from tensorflow.keras.models import load_model
import numpy as np
from PIL import Image

# --- Page configuration ---
st.set_page_config(
    page_title="Cats vs Dogs Classifier",
    page_icon="🐱🐶",
    layout="centered"
)

# --- Custom CSS Styling ---
st.markdown(
    """
    <style>
    body {
        background-color: #f5f5f5;
        color: #333333;
        font-family: 'Segoe UI', sans-serif;
    }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        font-size: 16px;
        padding: 10px 20px;
        border-radius: 8px;
    }
    .stImage>img {
        border-radius: 15px;
        box-shadow: 3px 3px 15px rgba(0,0,0,0.3);
    }
    </style>
    """,
    unsafe_allow_html=True
)

# --- Title & Description ---
st.title("🐱🐶 Cats vs Dogs Classifier")
st.write("Upload an image of a Cat or Dog and get the prediction instantly!")

# --- Load model ---
model = load_model("model/cats_vs_dogs_mobilenetv2.h5")
class_names = ['Cat', 'Dog']

# --- File uploader ---
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])
if uploaded_file is not None:
    img = Image.open(uploaded_file).convert('RGB')
    st.image(img, caption='Uploaded Image', use_container_width=True)

    img = img.resize((160, 160))
    img_array = np.array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    pred = model.predict(img_array)
    class_index = int(pred > 0.5)
    st.success(f"Prediction: **{class_names[class_index]}**")
else:
    st.info("Please upload an image to see the prediction.")
