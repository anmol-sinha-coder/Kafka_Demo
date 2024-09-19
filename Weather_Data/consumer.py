from flask import Flask, render_template
from json import loads
from kafka import KafkaConsumer


class Consumer:
    def __init__(self):
        nums_list = []
        self.consumer = KafkaConsumer('weather_data',
                                      value_deserializer=lambda x: loads(x),
                                      group_id='my_weather_group',
                                      auto_offset_reset='latest')

    def consume_data(self):
        for message in self.consumer:
            print(f"Received message :{message.value}")
            return message.value

app = Flask(__name__,template_folder='templates')
consumer = Consumer()

@app.route("/")
def get_weather_data():
    #Get data from Kafka broker
    try:
        weather_data = consumer.consume_data()
        print(type(weather_data),type(weather_data))
        return render_template('index.html', weather=weather_data)
    except ValueError:
        return render_template('index.html', error="Error")

if __name__ == "__main__":
    app.run(debug=True, port=4109)
