from sklearn.ensemble import IsolationForest
import joblib
import shap
import numpy as np

class AnomalyDetector:
    def __init__(self):
        self.model = IsolationForest(
            n_estimators=200,
            contamination=0.02,
            random_state=42
        )
        self.explainer = None

    def train(self, X):
        self.model.fit(X)
        self.explainer = shap.TreeExplainer(self.model)

    def predict(self, X):
        scores = self.model.decision_function(X)
        anomalies = self.model.predict(X)
        return scores, anomalies

    def explain(self, X):
        if self.explainer is None:
            self.explainer = shap.TreeExplainer(self.model)
        shap_values = self.explainer.shap_values(X)
        return shap_values

    def save(self, path="model.joblib"):
        joblib.dump(self.model, path)

    def load(self, path="model.joblib"):
        self.model = joblib.load(path)
        self.explainer = shap.TreeExplainer(self.model)
