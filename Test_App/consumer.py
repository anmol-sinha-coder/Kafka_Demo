# consumer.py

from kafka import KafkaConsumer
import json

# Initialize Kafka Consumer
consumer = KafkaConsumer(
    'test_flask',
    bootstrap_servers=['localhost:9092'],
    auto_offset_reset='earliest',
    group_id='my_group',
    enable_auto_commit=True,
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

print("Starting to consume messages...")
for message in consumer:
    print(f"Consumed message: {message.value}")
