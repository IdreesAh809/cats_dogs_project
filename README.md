# 🐶🐱 Cat vs Dog Classifier

A web application built with **Streamlit** that uses a trained deep learning model (**MobileNetV2**) to classify uploaded images as either a **Cat** or a **Dog**.

The model was trained on Kaggle’s Cat vs Dog dataset in **Google Colab**, using MobileNetV2 with input size `160x160`.  
Achieved **~98% validation accuracy**.

## Features

- Detects Cat / Dog in uploaded images.
- Shows prediction confidence percentage.
- Easy-to-use web interface via Streamlit.
- Pre-trained MobileNetV2 model for instant predictions.

## Project Structure
```
cat-dog-project/
├── model/
│   └── cats_vs_dogs_mobil...
├── notebooks/
│   └── cats_vs_dogs_mobil...
├── venv/
├── .gitignore
├── requirements.txt
└── streamlit_app.py
```




## Installation

1. **Clone the repository and navigate into it:**

```bash
https://github.com/IdreesAh809/cats_dogs_project
cd cat_dog_project
```

2. **Create and activate a virtual environment:**
```
python -m venv venv
.\venv\Scripts\activate   # Windows
source venv/bin/activate  # Mac/Linux

```
4. **Install dependencies and run the app:**
```
pip install -r requirements.txt
streamlit run streamlit_app.py
```
## Usage

 **Upload an image of a cat or dog.**

**The app will predict whether the image is a cat or a dog.**

## License
**This project is open-source and free to use**
