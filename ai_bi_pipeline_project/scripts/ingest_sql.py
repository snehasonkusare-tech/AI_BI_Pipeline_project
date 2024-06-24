"""Example: ingest data from a SQL database and write to CSV.
Replace DATABASE_URI with your DB connection string (SQLAlchemy format).
"""
import os
import pandas as pd
from sqlalchemy import create_engine

DATABASE_URI = "postgresql://user:password@host:5432/database"  # <-- REPLACE

def ingest(query: str, out_path: str):
    engine = create_engine(DATABASE_URI)
    with engine.connect() as conn:
        df = pd.read_sql(query, conn)
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    df.to_csv(out_path, index=False)
    print(f"Wrote {len(df)} rows to {out_path}")

if __name__ == '__main__':
    sample_query = "SELECT * FROM transactions LIMIT 10000;"
    ingest(sample_query, "data/raw/transactions_sample.csv")
