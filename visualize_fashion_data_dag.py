from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt
import os
from sqlalchemy import create_engine

# PostgreSQL URI
DB_URI = 'postgresql+psycopg2://neondb_owner:npg_xjLsAhE58WGI@ep-dark-frost-a1xm5slv-pooler.ap-southeast-1.aws.neon.tech/neondb?sslmode=require'

# Path to save visualizations
VIS_DIR = '/opt/airflow/visualization'
os.makedirs(VIS_DIR, exist_ok=True)

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024, 1, 1),
    'retries': 1
}

dag = DAG(
    dag_id='visualize_fashion_data',
    default_args=default_args,
    schedule_interval='@daily',
    catchup=False
)

def generate_charts():
    engine = create_engine(DB_URI)
    df = pd.read_sql("SELECT * FROM analytics_product_performance", engine)

    # --- Plot 1: Top 10 products by revenue ---
    top10 = df.sort_values(by='total_revenue', ascending=False).head(10)
    plt.figure(figsize=(10, 6))
    plt.barh(top10['product_name'], top10['total_revenue'], color='skyblue')
    plt.xlabel('Revenue')
    plt.ylabel('Product')
    plt.title('Top 10 Products by Revenue')
    plt.gca().invert_yaxis()
    plt.tight_layout()
    plt.savefig(f"{VIS_DIR}/top10_products_revenue.png")
    plt.close()

    # --- Plot 2: Revenue share by category ---
    category = df.groupby('category')['total_revenue'].sum().sort_values(ascending=False)
    plt.figure(figsize=(8, 8))
    category.plot.pie(autopct='%1.1f%%', startangle=90)
    plt.title('Revenue Share by Product Category')
    plt.ylabel('')
    plt.tight_layout()
    plt.savefig(f"{VIS_DIR}/revenue_share_by_category.png")
    plt.close()

    print("✅ Visualizations saved to:", VIS_DIR)

visualize_task = PythonOperator(
    task_id='generate_visual_reports',
    python_callable=generate_charts,
    dag=dag
)
