"""Example Airflow DAG that runs the ingestion, transform, load, and model training tasks."""
from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

with DAG(
    dag_id='ai_bi_pipeline',
    default_args=default_args,
    start_date=datetime(2024, 1, 1),
    schedule_interval='@daily',
    catchup=False,
    max_active_runs=1,
) as dag:

    ingest = BashOperator(
        task_id='ingest_sql',
        bash_command='python /opt/airflow/scripts/ingest_sql.py'
    )

    transform = BashOperator(
        task_id='transform_validate',
        bash_command='python /opt/airflow/scripts/transform_validate.py'
    )

    load = BashOperator(
        task_id='load_snowflake',
        bash_command='python /opt/airflow/scripts/load_snowflake.py'
    )

    train_model = BashOperator(
        task_id='train_anomaly_model',
        bash_command='python /opt/airflow/scripts/anomaly_model.py'
    )

    ingest >> transform >> load >> train_model
