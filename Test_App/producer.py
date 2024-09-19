# producer.py

from kafka import KafkaProducer
import json
import time

# Initialize Kafka Producer
producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    key_serializer=lambda x: json.dumps(x).encode('utf-8'),
    value_serializer=lambda x: json.dumps(x).encode('utf-8')
)

def produce_message(message):
    producer.send('test_flask', value=message)
    producer.flush()
    print(f"Produced message: {message}")

# Example usage
if __name__ == "__main__":
    while True:
        message = {'number': 42}  # Example message
        produce_message(message)
        time.sleep(5)  # Produce a message every 5 seconds
