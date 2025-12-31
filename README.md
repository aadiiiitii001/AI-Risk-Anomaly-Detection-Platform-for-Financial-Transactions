# AI Risk & Anomaly Detection Platform for Financial Transactions

An **enterprise-grade, real-time AI platform** for detecting anomalous and high-risk financial transactions using **Machine Learning, Explainable AI (SHAP), Kafka streaming, FastAPI, PostgreSQL, Docker, and CI/CD**.

This project is inspired by real systems used in **banks, fintechs, payment gateways, and AML compliance teams**.

---

## 🚀 Key Highlights

- 🔍 **Unsupervised Anomaly Detection** (Isolation Forest)
- ⚡ **Real-time Streaming** with Apache Kafka
- 🧠 **Explainable AI (SHAP)** for regulatory transparency
- 🌐 **FastAPI** for real-time inference
- 🗄️ **PostgreSQL** for audit & compliance storage
- 📊 **Streamlit Dashboard** for analysts
- 🐳 **Dockerized Microservices**
- ✅ **Automated Tests + GitHub Actions CI**

---

## 🏗️ System Architecture
```bash
Kafka Producer
↓
Kafka Topic (financial-transactions)
↓
Kafka Consumer
↓
ML + SHAP Inference
↓
PostgreSQL (Audit Store)
↓
FastAPI API
↓
Dashboard / Clients
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
## ⚡ Kafka Real-Time Streaming
- Producer simulates live financial transactions
- Consumer:
     - Consumes Kafka messages
     - Runs ML + SHAP
     - Stores results in PostgreSQL

## Kafka Topic:
``` bash
financial-transactions
```

## 🐳 Dockerized Deployment
- Run Entire System
- docker-compose up --build

## Services included:
- FastAPI
- PostgreSQL
- Kafka
- Zookeeper
- ML Consumer

## FastAPI Docs:
``` bash
http://localhost:8000/docs
```

🧪 Testing & CI/CD
Tests

Feature engineering tests

ML model tests

API integration tests

Run locally:

pytest -v

GitHub Actions CI

Runs on every push & PR

Automatically installs dependencies

Executes all tests

✔ Ensures reliability
✔ Prevents breaking changes

📊 Use Cases

Fraud Detection

AML (Anti-Money Laundering)

Transaction Risk Scoring

Financial Compliance & Auditing

🛠️ Tech Stack
Layer	Technology
Backend	FastAPI
ML	Scikit-learn
Explainability	SHAP
Streaming	Apache Kafka
Database	PostgreSQL
Dashboard	Streamlit
DevOps	Docker, GitHub Actions
Testing	Pytest

## 🧩 Future Enhancements
- Risk rules engine (ML + business rules)
- Model versioning & monitoring
- Cloud deployment (AWS / Azure / GCP)
- Role-based access control
- Advanced analytics queries

👩‍💻 Author
---
Aditi Nayak
AI / ML | Backend | FinTech Systems
---
