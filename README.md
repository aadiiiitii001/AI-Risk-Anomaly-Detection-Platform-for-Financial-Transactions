# AI Risk & Anomaly Detection Platform for Financial Transactions

## 📌 Overview
An enterprise-grade AI platform to detect anomalous and high-risk financial transactions in real time using machine learning and rule-based risk scoring.

## 🚀 Features
- Unsupervised anomaly detection (Isolation Forest)
- Real-time FastAPI inference
- Risk scoring engine
- PostgreSQL transaction storage
- Analyst dashboard

## 🏗️ Architecture
- ML: Scikit-learn
- Backend: FastAPI
- Database: PostgreSQL
- Dashboard: Streamlit

## 🧠 Use Cases
- Fraud detection
- AML compliance
- Financial risk monitoring

## ▶️ Run Locally
```bash
- pip install -r requirements.txt
- uvicorn api.main:app --reload
- streamlit run dashboard/app.py
```
## 📈 Future Enhancements
- Kafka streaming
- SHAP explainability
- Docker & cloud deployment
