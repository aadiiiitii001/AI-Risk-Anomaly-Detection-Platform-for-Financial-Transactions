import os
import joblib
import shap
import numpy as np
from sklearn.ensemble import IsolationForest

MODEL_PATH = os.getenv("MODEL_PATH", "ml/model.joblib")

class AnomalyDetector:
    def __init__(self):
        self.model = None
        self.explainer = None

    def train(self, X):
        self.model = IsolationForest(
            n_estimators=200,
            contamination=0.02,
            random_state=42
        )
        self.model.fit(X)
        self.explainer = shap.TreeExplainer(self.model)

    def predict(self, X):
        if self.model is None:
            raise RuntimeError("Model not loaded or trained")

        scores = self.model.decision_function(X)
        anomalies = self.model.predict(X)
        return scores, anomalies

    def explain(self, X):
        if self.explainer is None:
            self.explainer = shap.TreeExplainer(self.model)
        return self.explainer.shap_values(X)

    def save(self, path: str = MODEL_PATH):
        if self.model is None:
            raise RuntimeError("No model to save")
        joblib.dump(self.model, path)

    def load(self, path: str = MODEL_PATH):
        if not os.path.exists(path):
            raise FileNotFoundError(f"Model file not found at {path}")

        self.model = joblib.load(path)
        self.explainer = shap.TreeExplainer(self.model)
