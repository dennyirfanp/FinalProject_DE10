# eCommerce Data Engineering Pipeline

## 📊 Project Overview

This project implements a comprehensive data engineering pipeline for analyzing eCommerce transaction data from a Pakistan-based online store. The pipeline processes transaction data from January 2025 to June 2025, focusing on unique and all-occasion gifts retail business.

## 🎯 Objectives

- Build a scalable data pipeline for eCommerce transaction processing
- Implement real-time and batch data processing capabilities
- Create data warehouse for analytics and reporting
- Develop automated data quality checks and monitoring
- Enable business intelligence 

## 📋 Dataset Description

**Source**: Pakistan-based eCommerce store specializing in unique, all-occasion gifts
**Period**: January 2025 - June 2025 (First two quarters)
**Data Type**: Transaction records from retail customers
**Format**: CSV

### Key Attributes
- Transaction date
- SKU (Stock Keeping Unit)
- Product details
- Quantity
- Customer information
- Purchase transaction records

## 🏗️ Architecture

```
Raw Data (CSV) → Data Ingestion → Data Processing → Data Warehouse → Analytics/ML
     ↓               ↓               ↓              ↓              ↓
  Source Files → Apache Kafka → Apache Spark → PostgreSQL → Tableau
```

## 🛠️ Technology Stack

### Data Ingestion
- **Apache Kafka**: Real-time data streaming
- **Apache Airflow**: Workflow orchestration
- **Python**: Data extraction scripts

### Data Processing
- **Apache Spark**: Distributed data processing
- **Python (PySpark)**: Data transformation
- **Pandas**: Data manipulation

### Data Storage
- **PostgreSQL**: Primary data warehouse
- **Apache Parquet**: Columnar storage format
- **Redis**: Caching layer

### Analytics & Visualization
- **Tableau**: Business intelligence dashboards
- **Jupyter Notebooks**: Data analysis
- **scikit-learn**: Machine learning models

### Infrastructure
- **Docker**: Containerization
- **Docker Compose**: Multi-container orchestration
- **Apache Airflow**: Pipeline scheduling

## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- Docker and Docker Compose
- PostgreSQL
- Apache Spark
- Git

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/ecommerce-data-pipeline.git
   cd ecommerce-data-pipeline
   ```

2. **Set up environment variables**
   ```bash
   cp .env.example .env
   # Edit .env with your configuration
   ```

3. **Start the infrastructure**
   ```bash
   docker-compose up -d
   ```

4. **Install Python dependencies**
   ```bash
   pip install -r requirements.txt
   ```

5. **Initialize the database**
   ```bash
   python scripts/init_db.py
   ```

## 📁 Project Structure

```
ecommerce-data-pipeline/
├── data/
│   ├── raw/                    # Raw CSV files
│   ├── processed/              # Processed data
│   └── models/                 # ML model outputs
├── src/
│   ├── ingestion/              # Data ingestion modules
│   ├── processing/             # Data processing logic
│   ├── models/                 # Data models and schemas
│   └── utils/                  # Utility functions
├── config/
│   ├── airflow/                # Airflow DAGs
│   ├── spark/                  # Spark configurations
│   └── database/               # Database schemas
├── notebooks/
│   ├── exploratory_analysis.ipynb
│   ├── data_quality_check.ipynb
│   └── ml_modeling.ipynb
├── tests/
│   ├── unit/                   # Unit tests
│   └── integration/            # Integration tests
├── docker-compose.yml
├── requirements.txt
├── .env.example
└── README.md
```

## 🔄 Pipeline Workflow

### 1. Data Ingestion
- **Batch Processing**: Daily ingestion of CSV transaction files
- **Real-time Processing**: Stream processing for live transactions
- **Data Validation**: Schema validation and data quality checks

### 2. Data Processing
- **Data Cleaning**: Handle missing values, duplicates, and inconsistencies
- **Data Transformation**: 
  - Date parsing and formatting
  - SKU standardization
  - Product categorization
  - Customer segmentation
- **Feature Engineering**: Create derived metrics for analytics

### 3. Data Storage
- **Raw Data**: Store original CSV files
- **Processed Data**: Clean and transformed data in Parquet format
- **Data Warehouse**: Structured data in PostgreSQL with optimized schemas

### 4. Analytics & ML Applications
- **Time Series Analysis**: Sales trends and seasonality
- **Customer Segmentation**: Clustering analysis
- **Product Recommendation**: Collaborative filtering
- **Classification**: Anomaly detection for fraud prevention

## 📊 Use Cases

### Business Intelligence
- Sales performance dashboard
- Customer behavior analysis
- Product performance metrics
- Inventory optimization insights

## 🔧 Configuration

### Environment Variables
```bash
# Database Configuration
DB_HOST=localhost
DB_PORT=5432
DB_NAME=ecommerce_dw
DB_USER=postgres
DB_PASSWORD=your_password

# Kafka Configuration
KAFKA_BOOTSTRAP_SERVERS=localhost:9092
KAFKA_TOPIC=ecommerce_transactions

# Spark Configuration
SPARK_MASTER=local[*]
SPARK_APP_NAME=ecommerce_pipeline
```

## 🧪 Testing

Run the test suite:
```bash
# Unit tests
pytest tests/unit/

# Integration tests
pytest tests/integration/

# All tests
pytest tests/
```

## 📈 Monitoring & Logging

- **Airflow UI**: Monitor pipeline execution
- **Spark UI**: Monitor Spark job performance
- **Database Monitoring**: Query performance and resource usage
  
## 🚀 Deployment

### Local Development
```bash
docker-compose up -d
python src/main.py
```

### Production Deployment
- Use Kubernetes for container orchestration
- Implement CI/CD pipeline with GitHub Actions
- Configure auto-scaling for Spark clusters
- Set up monitoring and alerting

## 🙏 Acknowledgments

- Dataset provided by M. Fayyaz
- Pakistan-based eCommerce store for data partnership
- Open-source community for tools and libraries used

---

**Note**: This project is for educational purposes as part of a Data Engineering final project. All data has been anonymized and used with proper permissions.
