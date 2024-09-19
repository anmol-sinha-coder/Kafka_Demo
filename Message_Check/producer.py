from flask import Flask, request, jsonify
from kafka import KafkaProducer
import json

app = Flask(__name__)

@app.route('/send', methods=['POST'])
def send_message():
    data = request.json
    message = data.get('message')
    topic = data.get('topic')
    print(message,topic)
    
    # Kafka producer configuration
    producer = KafkaProducer(
        bootstrap_servers='localhost:9092',
        key_serializer=lambda x: json.dumps(x).encode('utf-8'),
        value_serializer=lambda v: json.dumps(v).encode('utf-8')
    )

    # Send message to Kafka
    producer.send(topic, value={'message': message})
    producer.flush()  # Ensure all messages are sent

    return jsonify({'status': 'Message sent successfully!'})

if __name__ == '__main__':
    app.run(debug=True, port=4109)
