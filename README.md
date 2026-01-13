<h1 align="center">📦 Kafka Orders Shop – Event-Driven Order Processing</h1>

<p align="center">
  <em>"Real-time order streaming using Apache Kafka and Python"</em> ⚡📨
</p>

<p align="center">
  A lightweight, event-driven system that demonstrates <strong>Kafka producers and consumers</strong>
  using <strong>Docker</strong> and <strong>Python</strong> to stream and process orders in real time.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Kafka-Apache-black?style=for-the-badge&logo=apachekafka" />
  <img src="https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python" />
  <img src="https://img.shields.io/badge/Docker-Containerized-2496ED?style=for-the-badge&logo=docker" />
</p>

---

## 🎯 Project Overview

This project demonstrates a **real-world Kafka workflow** where:

- A **Producer** publishes order events to Kafka
- A **Consumer** subscribes to the topic and processes incoming orders
- Kafka runs in **KRaft mode (without Zookeeper)** using Docker

The goal is to understand **event-driven architecture**, **message streaming**, and **producer–consumer communication**.

---

## ✨ Key Features

- 📤 **Kafka Producer**: Publishes structured order events
- 📥 **Kafka Consumer**: Subscribes and processes orders in real time
- 🐳 **Dockerized Kafka**: Easy setup using Docker Compose
- ⚡ **Event-Driven Flow**: Asynchronous message streaming
- 🧩 **JSON Messaging**: Clean, structured event payloads
- 🔄 **Persistent Topics**: Kafka data survives container restarts

---

## 🏗️ Architecture

```mermaid
graph TD
    A[Python Producer] -->|Publish Order| B[Kafka Topic: orders]
    B -->|Consume Order| C[Python Consumer]
    D[Docker Compose] --> B
🛠️ Tech Stack
Layer	Technology	Purpose
Messaging	Apache Kafka	Distributed event streaming
Runtime	Python	Producer & Consumer logic
Serialization	JSON	Message format
Containerization	Docker	Kafka deployment
Orchestration	Docker Compose	Service management

📁 Project Structure
bash
Copy code
kafka-orders-shop/
├── docker-compose.yaml   # Kafka (KRaft mode)
├── producer.py           # Kafka producer (order publisher)
├── tracker.py            # Kafka consumer (order processor)
├── .gitignore
├── requirements.txt
└── README.md
📦 Order Event Format
json
Copy code
{
  "order_id": "uuid",
  "user": "chris",
  "item": "chicken pizza",
  "quantity": 2
}
🚀 Quick Start
1️⃣ Start Kafka (Docker)
bash
Copy code
docker compose up -d
Verify Kafka is running:

bash
Copy code
docker ps
2️⃣ Create Topic (if not exists)
bash
Copy code
docker exec -it kafka kafka-topics \
  --create \
  --topic orders \
  --bootstrap-server localhost:9092 \
  --partitions 1 \
  --replication-factor 1
3️⃣ Install Python Dependencies
bash
Copy code
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
4️⃣ Run Consumer
bash
Copy code
python tracker.py
Output:

text
Copy code
Consumer is running and subscribed to orders topic
5️⃣ Run Producer
bash
Copy code
python producer.py
Output:

text
Copy code
Delivered {"order_id":"...","item":"chicken pizza","quantity":2}
Consumer receives:

text
Copy code
Received order: 2 x chicken pizza from chris
📊 What This Project Demonstrates
How Kafka decouples producers and consumers

How messages flow through a Kafka topic

How to use confluent-kafka Python client

How Docker simplifies Kafka setup

How event-driven systems work in practice

🧠 Learning Outcomes
Understanding Kafka fundamentals

Working with event streams

Designing producer–consumer systems

Debugging Kafka CLI and clients

Managing Kafka with Docker

🔮 Possible Extensions
Add multiple consumers (consumer groups)

Introduce partitions

Add message keys

Persist orders to a database

Build a REST API on top of Kafka

Add retries & dead-letter topics

👨‍💻 Author
Chris Robert Yeslin

📧 Email: robertchemist2006@gmail.com

🐙 GitHub: https://github.com/chris-robert-yeslin2006

📜 License
This project is licensed under the MIT License.

<p align="center"> <strong>⚡ Built to understand event-driven systems using Apache Kafka 🚀</strong> </p> ```
