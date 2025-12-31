import shap
import matplotlib.pyplot as plt
import pandas as pd

def plot_shap(explanation):
    df = pd.DataFrame({
        "feature": explanation.keys(),
        "shap_value": explanation.values()
    })

    shap.bar_plot(df["shap_value"].values, feature_names=df["feature"])
    plt.show()
