
import streamlit as st
import pandas as pd
import joblib

st.set_page_config(page_title="CLV Predictor", page_icon="📊")

st.title("📊 Customer Lifetime Value Predictor")
st.write("Predict customer lifetime value for the next 90 days.")

model = joblib.load("models/customer_lifetime_value_model.pkl")
columns = joblib.load("models/customer_lifetime_value_columns.pkl")

values = {}

for col in columns:
    values[col] = st.number_input(col, min_value=0.0, value=1.0)

if st.button("Predict CLV"):
    data = pd.DataFrame([values], columns=columns)
    prediction = model.predict(data)[0]

    st.success(f"{max(0, prediction):,.2f}")
