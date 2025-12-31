from sklearn.ensemble import IsolationForest
import joblib

class AnomalyDetector:
    def __init__(self):
        self.model = IsolationForest(
            n_estimators=200,
            contamination=0.02,
            random_state=42
        )

    def train(self, X):
        self.model.fit(X)

    def predict(self, X):
        scores = self.model.decision_function(X)
        anomalies = self.model.predict(X)
        return scores, anomalies

    def save(self, path="model.joblib"):
        joblib.dump(self.model, path)

    def load(self, path="model.joblib"):
        self.model = joblib.load(path)
