📊 Realtime Data Streaming | End-to-End Data Engineering Project
In this project, I built a complete data engineering pipeline that handles everything from real-time data ingestion to processing and storage — fully containerized for scalability and ease of deployment.

🛠️ What I Built
Developed a real-time data ingestion pipeline using the randomuser.me API as a data source

Orchestrated ETL workflows with Apache Airflow, storing raw data in PostgreSQL

Streamed data seamlessly through Apache Kafka and managed coordination with Zookeeper

Processed streaming data using Apache Spark (with master and worker nodes)

Stored the processed and transformed data in a Cassandra database

Containerized the entire system with Docker Compose for easy local setup and scalability


System Architechture

⚙️ Tech Stack
Python

Apache Airflow

Apache Kafka

Apache Zookeeper

Apache Spark

Cassandra

PostgreSQL

Docker

🚀 How to Run
Clone the repository:

bash
Copy
Edit
git clone https://github.com/DKLOCHANA/real-time-data-streaming-project
Start all services:

bash
Copy
Edit
docker-compose up
🧩 System Overview
Data Source: randomuser.me API generates random user data

Airflow: Orchestrates data collection and loads raw data into PostgreSQL

Kafka & Zookeeper: Streams data reliably to Spark for real-time processing

Spark: Transforms and enriches the data

Cassandra: Stores final processed data for analysis and downstream use

