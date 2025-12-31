import streamlit as st
import requests

st.title("Financial Transaction Risk Monitor")

amount = st.number_input("Transaction Amount")
user_id = st.number_input("User ID")
timestamp = st.text_input("Timestamp (YYYY-MM-DD HH:MM:SS)")

if st.button("Check Risk"):
    payload = {
        "user_id": user_id,
        "amount": amount,
        "timestamp": timestamp
    }
    res = requests.post("http://localhost:8000/predict", json=payload)
    st.json(res.json())
