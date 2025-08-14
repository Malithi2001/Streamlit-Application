import streamlit as st
import pandas as pd
import numpy as np
import pickle
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
st.write("📂 Base directory:", BASE_DIR)
st.write("📄 Files in BASE_DIR:", os.listdir(BASE_DIR))

model_path = os.path.join(BASE_DIR, "model.pkl")
scaler_path = os.path.join(BASE_DIR, "scaler.pkl")

def load_pickle_safe(path):
    #"""Safely load pickle files with clear error messages."""
    try:
        with open(path, "rb") as f:
            return pickle.load(f)
    except ModuleNotFoundError as e:
        st.error(f"❌ Missing Python module: `{e.name}`. "
                 f"Add it to `requirements.txt` and redeploy.")
        st.stop()
    except Exception as e:
        st.error(f"❌ Error loading {os.path.basename(path)}: {e}")
        st.stop()

# Check file existence
if not os.path.exists(model_path):
    st.error(f"❌ model.pkl not found at: {model_path}")
    st.stop()
if not os.path.exists(scaler_path):
    st.error(f"❌ scaler.pkl not found at: {scaler_path}")
    st.stop()

# Load model and scaler
model = load_pickle_safe(model_path)
scaler = load_pickle_safe(scaler_path)
st.success("✅ Model and Scaler loaded successfully!")

# Prediction function
def predict_quality(features):
    try:
        scaled = scaler.transform([features])
        prediction = model.predict(scaled)
        return "Good" if prediction[0] == 1 else "Bad"
    except Exception as e:
        st.error(f"❌ Prediction failed: {e}")
        return None

# Sidebar menu
st.sidebar.title("Wine Quality App")
option = st.sidebar.radio(
    "Select Page",
    ["Data Exploration", "Visualization", "Prediction", "Model Performance"]
)

# Example Prediction Page
if option == "Prediction":
    st.header("Wine Quality Prediction")
    feature_inputs = []
    feature_names = X.columns if 'X' in globals() else [
        "fixed acidity", "volatile acidity", "citric acid", "residual sugar",
        "chlorides", "free sulfur dioxide", "total sulfur dioxide", "density",
        "pH", "sulphates", "alcohol"
    ]
    
    for feature in feature_names:
        val = st.number_input(f"{feature}", value=0.0)
        feature_inputs.append(val)

    if st.button("Predict"):

        r
