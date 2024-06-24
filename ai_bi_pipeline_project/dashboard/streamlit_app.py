"""Simple Streamlit dashboard that loads the trained model and shows anomaly scores."""
import streamlit as st
import pandas as pd
from joblib import load

st.title('AI-driven BI — Anomaly Detection Dashboard')
st.markdown('Upload cleaned CSV (same features used for training) to score anomalies.')

uploaded = st.file_uploader('Upload CSV', type=['csv'])
model = None
try:
    model = load('model/anomaly_iforest.joblib')
except Exception as e:
    st.warning('Model not found. Please train and place model/anomaly_iforest.joblib')

if uploaded is not None and model is not None:
    df = pd.read_csv(uploaded)
    X = df.select_dtypes(include='number').fillna(0)
    scores = model.decision_function(X)
    preds = model.predict(X)
    df['anomaly_score'] = scores
    df['anomaly_flag'] = preds == -1
    st.dataframe(df.head(200))
    st.metric('Anomalies detected', int(df['anomaly_flag'].sum()))
