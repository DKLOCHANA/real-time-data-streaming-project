# 📊 Realtime Data Streaming | End-to-End Data Engineering Project

## 🌍 Overview

This project demonstrates a **complete data engineering pipeline** that handles **real-time data ingestion, processing, and storage** — fully containerized for scalability and ease of deployment.
It showcases the integration of modern **data engineering tools** like Apache Airflow, Kafka, Spark, and Cassandra to build a robust, production-ready workflow.

---

## 🛠️ What I Built

* **Real-Time Data Ingestion**: Collects random user data from [randomuser.me API](https://randomuser.me).
* **ETL Orchestration**: Uses Apache Airflow to orchestrate workflows and load raw data into PostgreSQL.
* **Streaming Data Pipeline**: Apache Kafka streams data reliably, coordinated with Zookeeper.
* **Data Processing**: Apache Spark transforms and enriches streaming data across master and worker nodes.
* **Data Storage**: Stores processed data in Cassandra for downstream analytics.
* **Containerized Deployment**: Docker Compose ensures easy setup, scalability, and reproducibility.

---

## ⚙️ System Architecture

```
[RandomUser API] --> [Airflow ETL] --> [PostgreSQL] --> [Kafka + Zookeeper] --> [Spark Streaming] --> [Cassandra]
```

---

## 🧩 Tech Stack

* **Python** – Pipeline scripts & data processing
* **Apache Airflow** – Workflow orchestration
* **Apache Kafka & Zookeeper** – Real-time messaging & coordination
* **Apache Spark** – Streaming data processing
* **PostgreSQL** – Raw data storage
* **Cassandra** – Processed data storage
* **Docker & Docker Compose** – Containerization & local deployment

---

## 🚀 Features

* End-to-end **real-time data pipeline**
* **Fault-tolerant streaming** using Kafka and Zookeeper
* **Parallel data processing** with Spark clusters
* **Persistent storage** of both raw and transformed data
* Fully **containerized setup** for easy deployment

---

## 🟢 Get Started

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/DKLOCHANA/real-time-data-streaming-project
cd real-time-data-streaming-project
```

### 2️⃣ Start All Services

```bash
docker-compose up
```

> This will start all services including PostgreSQL, Kafka, Zookeeper, Spark, Airflow, and Cassandra.

### 3️⃣ Access the Services

* **Airflow UI:** [http://localhost:8080](http://localhost:8080)
* **Kafka:** Default broker running inside Docker
* **Cassandra:** Connect using cqlsh or any Cassandra client
* **Spark:** Accessible via Spark UI on default port 4040

### 4️⃣ Run the Pipeline

* Trigger the Airflow DAG to start real-time ingestion, processing, and storage.
* Monitor logs and data flow in Airflow UI and Spark UI.

---

## 📊 Data Flow Overview

1. **RandomUser API** generates new user records.
2. **Airflow DAG** collects and loads raw data into P
