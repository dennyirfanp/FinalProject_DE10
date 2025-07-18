from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import os
import pandas as pd
from sqlalchemy import create_engine

# Configuration
CSV_FOLDER = '/opt/airflow/data'
DB_URI = 'postgresql+psycopg2://neondb_owner:npg_xjLsAhE58WGI@ep-dark-frost-a1xm5slv-pooler.ap-southeast-1.aws.neon.tech/neondb?sslmode=require'

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024, 1, 1),
    'retries': 1
}

dag = DAG(
    dag_id='etl_and_analytics_fashion_data',
    default_args=default_args,
    schedule_interval='@daily',
    catchup=False
)

# Task 1: Ingest and clean all CSVs
def ingest_and_clean_csvs():
    engine = create_engine(DB_URI)
    for file in os.listdir(CSV_FOLDER):
        if file.endswith('.csv'):
            file_path = os.path.join(CSV_FOLDER, file)
            df = pd.read_csv(file_path)

            # Clean: drop nulls and duplicates
            df.dropna(inplace=True)
            df.drop_duplicates(inplace=True)

            table_name = file.replace('.csv', '').lower()
            df.to_sql(table_name, con=engine, if_exists='replace', index=False)
            print(f"Ingested and cleaned '{file}' → table '{table_name}'")

etl_task = PythonOperator(
    task_id='clean_and_ingest_all_csvs',
    python_callable=ingest_and_clean_csvs,
    dag=dag
)

# Task 2: Generate analytics table
def create_analytics_table():
    engine = create_engine(DB_URI)

    query = """
    SELECT
        p.product_id,
        p.product_name,
        p.category,
        COUNT(DISTINCT si.sale_id) AS total_sales,
        SUM(si.quantity) AS total_quantity_sold,
        ROUND(SUM(si.item_total)::numeric, 2) AS total_revenue,
        ROUND((SUM(si.item_total)::numeric / NULLIF(SUM(si.quantity), 0)), 2) AS avg_price,
        ROUND((SUM(si.item_total)::numeric / NULLIF(COUNT(DISTINCT si.sale_id), 0)), 2) AS avg_order_value
    FROM dataset_fashion_store_salesitems si
    JOIN dataset_fashion_store_products p ON si.product_id = p.product_id
    GROUP BY p.product_id, p.product_name, p.category
    ORDER BY total_revenue DESC
    """

    df = pd.read_sql_query(query, engine)
    df.to_sql('analytics_product_performance', con=engine, if_exists='replace', index=False)
    print(f"✅ analytics_product_performance created with {len(df)} rows")

analytics_task = PythonOperator(
    task_id='generate_product_performance_table',
    python_callable=create_analytics_table,
    dag=dag
)

# Task sequence
etl_task >> analytics_task
