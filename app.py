# app.py

import streamlit as st
import numpy as np
import joblib

# Load the saved model
model = joblib.load('sales_forecasting_model.pkl')

# Streamlit App
st.set_page_config(page_title="Sales Forecasting App", layout="centered")
st.title("📈 Sales Forecasting App")
st.write("Predict sales based on Quantity Ordered, Price Each, Month, Year, and Quarter.")

# User Inputs
quantity = st.number_input("Enter Quantity Ordered:", min_value=0, step=1)
price = st.number_input("Enter Price Each ($):", min_value=0.0, format="%.2f")
month = st.selectbox("Select Month:", list(range(1, 13)))
year = st.selectbox("Select Year:", [2003, 2004, 2005])
quarter = st.selectbox("Select Quarter:", [1, 2, 3, 4])

# Prediction
if st.button("Predict Sales"):
    features = np.array([[quantity, price, month, year, quarter]])
    prediction = model.predict(features)[0]
    st.success(f"💰 Predicted Sales: **${prediction:,.2f}**")
