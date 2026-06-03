
# Save this part as app.py
import streamlit as st
import numpy as np
import joblib

# Load model
model = joblib.load("fraud_detection_model.pkl")

st.title("\U0001F4B3 Fraud Detection System")

amount = st.number_input("Enter transaction amount (\u20B9):", value=100.0)
hour = st.slider("Select transaction hour (0-23):", 0, 23)
high_amount = 1 if amount > 200 else 0

features = np.array([[amount, hour, high_amount]])

if st.button("Check Transaction"):
    prediction = model.predict(features)
    if prediction[0] == 1:
        st.error("\U0001F6A8 Fraud Detected!")
    else:
        st.success("\u2705 Legitimate Transaction")