import streamlit as st
import pickle
import numpy as np

# Load model
model = pickle.load(open("model.pkl","rb"))

st.title("🏠 House Price Prediction")

area = st.number_input("Enter Area (sq ft)")

if st.button("Predict Price"):
    prediction = model.predict([[area]])
    st.success(f"Estimated Price = ${prediction[0]:,.2f}")