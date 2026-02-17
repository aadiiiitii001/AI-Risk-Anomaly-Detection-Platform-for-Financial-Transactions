# AI Risk & Anomaly Detection Platform

An end-to-end machine learning system for detecting anomalous financial transactions using unsupervised learning, real-time ingestion simulation, explainable AI, and a production-style FastAPI inference layer.

This project demonstrates how ML models can be integrated into backend systems for risk scoring and audit storage.

---

## 🚀 Overview

This system simulates real-time financial transactions and evaluates them using an Isolation Forest model to detect anomalies. Each prediction includes a SHAP-based explanation for feature-level interpretability.

**Key goals demonstrated:**
- ML model training and inference integration
- API-driven risk scoring
- Kafka-based streaming simulation
- Database-backed audit logging
- Explainable AI using SHAP

---

## 🏗️ System Architecture

```bash
Kafka Producer
↓
Kafka Topic (financial-transactions)
↓
Kafka Consumer
↓
Feature Engineering
↓
Isolation Forest Inference
↓
SHAP Explanation
↓
Database (SQLAlchemy)
↓
FastAPI API
↓
Swagger UI / Clients
```
## 📁 Project Structure
```bash
AI-Risk-Anomaly-Detection-Platform/
│
├── api/ # FastAPI inference service
├── ml/ # Feature engineering & ML models
├── kafka/ # Kafka producer & consumer
├── db/ # Database models & config
├── dashboard/ # Streamlit analyst dashboard
├── data/
│ ├── raw/
│ └── processed/
├── tests/ # Unit & integration tests
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md
```

---

## 🧠 Machine Learning

### Model
- Isolation Forest (Scikit-learn)
- Unsupervised anomaly detection
- Contamination rate: **2%**

### Engineered Features
- `amount_log` – Log-transformed transaction amount  
- `transaction_hour` – Extracted from timestamp  
- `velocity` – Transaction frequency per user  

### Explainability
- SHAP (TreeExplainer)
- Per-feature contribution scores for each prediction

---

## 🌐 API Layer

FastAPI is used to expose real-time prediction endpoints.

### Main Endpoint

**POST `/predict`**

#### Request
```json
{
  "user_id": 101,
  "amount": 98000,
  "merchant": "CryptoX",
  "country": "SG",
  "timestamp": "2024-11-21T10:16:30"
}
```
### Response
```
{
  "transaction_id": 12,
  "risk_score": -0.42,
  "anomaly": true,
  "explanation": {
    "amount_log": 0.31,
    "transaction_hour": -0.04,
    "velocity": 0.22
  }
}
```
## ⚡ Real-Time Streaming (Simulation)
```
- Kafka Producer simulates live financial transactions
- Kafka processes transactions and performs ML inference
- Results are stored in the database for audit tracking
```
## Kafka Topic
```
financial-transactions
```
## 🗄️ Database
```
SQLAlchemy ORM
SQLite (default) or PostgreSQL via environment variable
Stored data includes:
- Transaction metadata
- Risk score
- Anomaly flag
```
## 🐳 Running the Project
## Start API
```
uvicorn api.main:app --reload
```

## Swagger UI:
```
http://localhost:8000/docs
```

## Train Model
```
python ml/train_model.py
```
## Kafka Simulation

## Start producer:
```
python kafka/producer.py
```

## Start consumer:
```
python kafka/consumer.py
```
## 🧪 Testing
```
pytest -v
```

## 💡 Use Cases
```
- Fraud detection
- AML risk scoring
- Transaction monitoring
- Financial anomaly analysis
- Explainable AI for compliance workflows
```

## 🛠️ Tech Stack
```
- Backend: FastAPI
- ML: Scikit-learn
- Explainability: SHAP
- Streaming: Apache Kafka
- Database: SQLAlchemy (SQLite / PostgreSQL)
- Dashboard: Streamlit
- Containerization: Docker
```
### Screenshot
<img width="1920" height="1080" alt="Screenshot (43)" src="https://github.com/user-attachments/assets/e6358621-464b-4b70-8716-c07716053143" />

## 👩‍💻 Author
```
Aditi Nayak
AI / ML & Backend system
Focused on secure, explainable AI for enterprise finance
```
