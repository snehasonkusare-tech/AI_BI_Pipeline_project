"""Train a simple IsolationForest anomaly detection model and save it with joblib."""
import os
import pandas as pd
from sklearn.ensemble import IsolationForest
from joblib import dump

def train(input_csv: str, model_out: str):
    df = pd.read_csv(input_csv)
    # Example: pick numeric columns
    X = df.select_dtypes(include='number').fillna(0)
    model = IsolationForest(n_estimators=100, contamination=0.01, random_state=42)
    model.fit(X)
    os.makedirs(os.path.dirname(model_out), exist_ok=True)
    dump(model, model_out)
    print('Saved model to', model_out)

if __name__ == '__main__':
    train('data/clean/transactions_clean.csv', 'model/anomaly_iforest.joblib')
