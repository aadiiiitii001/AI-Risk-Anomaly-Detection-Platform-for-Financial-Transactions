from sklearn.ensemble import IsolationForest
import shap

class AnomalyDetector:
    def __init__(self):
        self.model = IsolationForest(
            n_estimators=100,
            contamination=0.05,
            random_state=42
        )
        self.explainer = shap.TreeExplainer(self.model)
        self.is_trained = False

    def train(self, X):
        self.model.fit(X)
        self.explainer = shap.TreeExplainer(self.model)
        self.is_trained = True

    def predict(self, X):
        if not self.is_trained:
            # Fit on first batch (cold start)
            self.train(X)
        scores = self.model.decision_function(X)
        anomalies = self.model.predict(X)
        return scores, anomalies

    def explain(self, X):
        if not self.is_trained:
            self.train(X)
        return self.explainer.shap_values(X)
