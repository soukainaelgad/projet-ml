import streamlit as st
import joblib

# Load model
model = joblib.load("model.pkl")

st.title("My Machine Learning App 🚀")

st.write("Enter your data:")

# Inputs (change according to your model)
feature1 = st.number_input("Feature 1")
feature2 = st.number_input("Feature 2")
feature3 = st.number_input("Feature 3")

if st.button("Predict"):
    input_data = [[feature1, feature2, feature3]]
    prediction = log_model.predict(input_data)

    st.success(f"Prediction: {prediction[0]}")
