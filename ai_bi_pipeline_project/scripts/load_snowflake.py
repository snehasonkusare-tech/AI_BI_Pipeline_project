"""Template to load CSV into Snowflake using snowflake-connector-python.
Fill SNOWFLAKE_* variables or use environment variables / secrets manager.
"""
import os
import snowflake.connector

# Replace these placeholders
SNOWFLAKE_USER = os.getenv('SNOWFLAKE_USER', 'USER')
SNOWFLAKE_PASSWORD = os.getenv('SNOWFLAKE_PASSWORD', 'PASSWORD')
SNOWFLAKE_ACCOUNT = os.getenv('SNOWFLAKE_ACCOUNT', 'ACCOUNT')
SNOWFLAKE_DATABASE = os.getenv('SNOWFLAKE_DATABASE', 'DB')
SNOWFLAKE_SCHEMA = os.getenv('SNOWFLAKE_SCHEMA', 'PUBLIC')
SNOWFLAKE_WAREHOUSE = os.getenv('SNOWFLAKE_WAREHOUSE', 'COMPUTE_WH')

def load_csv(local_path: str, table_name: str):
    ctx = snowflake.connector.connect(
        user=SNOWFLAKE_USER,
        password=SNOWFLAKE_PASSWORD,
        account=SNOWFLAKE_ACCOUNT,
        warehouse=SNOWFLAKE_WAREHOUSE,
        database=SNOWFLAKE_DATABASE,
        schema=SNOWFLAKE_SCHEMA
    )
    cs = ctx.cursor()
    try:
        # Create table - in practice use proper DDL to match schema
        # Stage the file and copy into table. This example assumes small CSV and uses PUT/COPY.
        print("Please upload file to an internal/external stage and run COPY INTO from that stage.")
    finally:
        cs.close()
        ctx.close()

if __name__ == '__main__':
    load_csv('data/clean/transactions_clean.csv', 'transactions_clean')
