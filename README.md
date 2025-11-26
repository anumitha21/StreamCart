# 📦 StreamCart – Kafka Demo

This project demonstrates a simple event-driven architecture using Apache Kafka, Docker, and Python.

## Features

* Runs Kafka in KRaft mode (no Zookeeper needed)
* Uses Docker Compose to create Kafka broker + volume
* Python producer to send order messages
* Python consumer that reads messages continuously
* Kafka data stays safe using Docker volumes

## Tech Stack

* Apache Kafka (KRaft mode)
* Docker & Docker Compose
* Python (confluent-kafka library)

## Project Structure

```
StreamCart/
│── docker-compose.yaml
│── producer.py
│── consumer.py
│── README.md
```

## Steps to Run

1. Start Kafka:

```bash
docker compose up -d
```

2. Run Producer (send messages):

```bash
python producer.py
```

3. Run Consumer (receive messages):

```bash
python consumer.py
```

## Files

* `docker-compose.yaml` → Runs Kafka in KRaft mode
* `producer.py` → Sends order messages to Kafka
* `consumer.py` → Reads messages from Kafka

## Kafka Connection

Both producer and consumer connect to:

```
localhost:9092
```

## Stopping Kafka

```bash
docker compose down
```

Data is safe because of the volume.

## Conclusion

This project demonstrates how to set up a lightweight, event-driven architecture using Kafka in KRaft mode with Python and Docker. It’s a simple, hands-on way to learn message streaming, producer-consumer workflows, and containerized applications.

With this foundation, you can extend StreamCart to handle real-time order processing, notifications, or analytics, making it a great starting point for learning microservices and event-driven systems.
You can extend StreamCart to handle real-time order processing, notifications, or analytics, making it a great starting point for learning microservices and event-driven systems.