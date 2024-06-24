"""Transform and validate raw CSV into cleaned, feature-engineered dataset."""
import os
import pandas as pd

def validate(df: pd.DataFrame) -> pd.DataFrame:
    # Simple validations: drop duplicates, enforce types, handle missing values
    df = df.drop_duplicates()
    # Example: ensure timestamp column exists and is datetime
    if 'event_ts' in df.columns:
        df['event_ts'] = pd.to_datetime(df['event_ts'], errors='coerce')
    # Fill or drop missing as policy
    df = df.dropna(subset=['user_id', 'amount']) if 'user_id' in df.columns else df.dropna()
    return df

def feature_engineer(df: pd.DataFrame) -> pd.DataFrame:
    # Example derived features
    if 'amount' in df.columns:
        df['amount_log'] = (df['amount'] + 1).apply(lambda x: np.log(x))
    if 'event_ts' in df.columns:
        df['hour'] = df['event_ts'].dt.hour
    return df

if __name__ == '__main__':
    import numpy as np
    raw_path = 'data/raw/transactions_sample.csv'
    out_path = 'data/clean/transactions_clean.csv'
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    df = pd.read_csv(raw_path)
    df = validate(df)
    df = feature_engineer(df)
    df.to_csv(out_path, index=False)
    print('Saved cleaned data to', out_path)
