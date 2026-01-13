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

This project demonstrates a real-world Kafka workflow where:

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
