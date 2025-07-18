
# 🛠️ Fashion Product Analytics ETL Pipeline

📦 Proyek ini adalah pipeline **ETL (Extract-Transform-Load)** harian menggunakan **Apache Airflow** untuk memproses data dari toko fashion Eropa. Pipeline ini memuat data CSV, membersihkan, mentransformasi, lalu menyimpannya ke PostgreSQL, dan akhirnya divisualisasikan menggunakan **Metabase**

## 🔗 Arsitektur
    A-->[CSV Files] -->|Daily Ingestion| B[Airflow ETL DAG]
    B --> C[PostgreSQL (NeonDB)]
    C --> D[Analytics Table]
    D --> E[Airflow Analytics Task]
    D --> F[Metabase Dashboard]


## 📁 Dataset

Dataset terdiri dari 7 file CSV utama:

1. `customers.csv`
2. `sales.csv`
3. `sales_items.csv`
4. `products.csv`
5. `stock.csv`
6. `campaigns.csv`
7. `channels.csv`

Dan 1 tabel hasil transformasi:
- `analytics_product_performance` (dibuat otomatis oleh DAG Airflow)

## 🧩 Tools & Teknologi

| Komponen        | Fungsi                                               |
|----------------|------------------------------------------------------|
| **Airflow**     | Orkestrasi dan penjadwalan DAG ETL harian            |
| **Pandas**      | Transformasi data                                    |
| **SQLAlchemy**  | Koneksi Python ↔ PostgreSQL                          |
| **PostgreSQL (NeonDB)** | Penyimpanan data relasional hasil ETL     |
| **Metabase**    | Visualisasi dashboard interaktif (SQL dan GUI)       |
| **Docker**      | Environment konsisten dan terisolasi untuk pipeline  |

## ⚙️ Pipeline Overview

### 1. ETL (airflow DAG `fashion_etl_dag.py`)
- Load 7 CSV
- Hapus duplikat & NULL
- Transformasi kolom, normalisasi string
- Simpan ke PostgreSQL

### 2. Analytics Generation (`generate_product_performance_table`)
- Query agregasi per produk:
  - Total revenue
  - Total orders
  - Quantity sold
- Simpan ke tabel: `analytics_product_performance`

### 3. Visualization (Metabase)
- Query dashboard di Metabase:
  - Top 10 Produk Terlaris
  - Revenue per Kategori
- Bisa juga dipakai di Grafana jika sudah terintegrasi

## 📊 Contoh Visualisasi di Metabase

- 📦 **Top 10 Produk dengan Revenue Tertinggi** (Bar Chart)
- 🥧 **Distribusi Revenue per Kategori Produk** (Pie Chart)
- ⏱️ (Opsional) Revenue per Bulan (Line Chart)

## 🔌 Koneksi Database (PostgreSQL)

```text
postgresql://neondb_owner:npg_xjLsAhE58WGI@ep-dark-frost-a1xm5slv-pooler.ap-southeast-1.aws.neon.tech/neondb?sslmode=require&channel_binding=require
```

## 🐳 Jalankan dengan Docker


### Jalankan dengan docker-compose
```bash
`docker compose --profile airflow up -d`
```

## 📈 Metabase Setup (Opsional)

### Jalankan Metabase:
```bash
docker run -d -p 3001:3000 --name metabase metabase/metabase
```

### Tambahkan PostgreSQL sebagai data source:
- Host: `ep-dark-frost-a1xm5slv-pooler.ap-southeast-1.aws.neon.tech`
- Port: `5432`
- DB: `neondb`
- User: `neondb_owner`
- SSL: ✅ Yes (require)

## 📌 Schedule

- DAG dijalankan **harian**
- Visualisasi diperbarui otomatis berdasarkan tabel analitik terbaru


## 🧠 Keterbatasan

- Dataset statis, belum support incremental load atau streaming
- Tidak semua field (seperti tanggal transaksi) diproses secara time-series
- Belum terhubung ke BI tools lain seperti Looker/Power BI

## ✅ Rencana Pengembangan

- Tambah time dimension untuk analitik per bulan
- Tambah scheduler untuk export PNG otomatis dari Metabase
- Sinkronisasi data dari API eksternal (misal ERP atau eCommerce)
