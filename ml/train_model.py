import pandas as pd
from ml.anomaly_model import AnomalyDetector
from ml.feature_engineering import create_features, FEATURES
import os

# ------------------------------------------------------------------
# Load training data
# ------------------------------------------------------------------
DATA_PATH = "data/processed/transactions.csv"

if not os.path.exists(DATA_PATH):
    raise FileNotFoundError(f"Training data not found at {DATA_PATH}")

df = pd.read_csv(DATA_PATH)

# ------------------------------------------------------------------
# Feature engineering
# ------------------------------------------------------------------
df = create_features(df)
X = df[FEATURES]

# ------------------------------------------------------------------
# Train model
# ------------------------------------------------------------------
model = AnomalyDetector()
model.train(X)

# ------------------------------------------------------------------
# Save model explicitly inside ml/
# ------------------------------------------------------------------
MODEL_PATH = "ml/model.joblib"
model.save(MODEL_PATH)

print(f"✅ Model trained and saved at {MODEL_PATH}")
