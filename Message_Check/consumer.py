from flask import Flask, jsonify, request
from kafka import KafkaConsumer
import json

app = Flask(__name__)

@app.route('/consume', methods=['GET'])
def consume_message():

    query=request.args

    # Kafka consumer configuration
    consumer = KafkaConsumer(
        query.get('topic'),  # Topic to consume from
        bootstrap_servers='localhost:9092',
        auto_offset_reset='earliest',  # Read messages from the beginning if no offset is available
        enable_auto_commit=True,
        group_id=query.get('group'),
        key_deserializer=lambda x: json.loads(x.decode('utf-8')),
        value_deserializer=lambda x: json.loads(x.decode('utf-8'))
    )

    # Poll for messages with a timeout of 10 second, fetch up to 5 messages
    messages = consumer.poll(timeout_ms=10000, max_records=5)

    # Prepare a list to hold the consumed messages
    message_list = []

    # Process the messages received
    for topic_partition, records in messages.items():
        for record in records:
            message_list.append(record.value)

    if len(message_list) == 0:
        return jsonify({'messages': 'No new messages'}), 204  # Return 'No Content' if no messages are found
    else:
        return jsonify({'messages': message_list}), 200  # Return the messages as JSON

if __name__ == '__main__':
    app.run(debug=True, port=14109)
