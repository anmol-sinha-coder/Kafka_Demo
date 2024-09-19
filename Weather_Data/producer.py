import time
import os
from json import dumps
from kafka import KafkaProducer
import requests, random

class Producer:
    def __init__(self):
        self.producer = KafkaProducer(bootstrap_servers='localhost:9092',
                                      value_serializer=lambda x:dumps(x).encode('utf-8'))

    def produce_weather_data(self,weather_data):
        self.producer.send('weather_data',value=weather_data)

city_list = ['PUNE','KOLHAPUR','SATARA','NASHIK','MUMBAI','NAGPUR','KARAD']
producer = Producer()
WEATHER_API = "http://api.weatherstack.com/current"
API_ACCESS_KEY = "741c50784a839b40e452235b90460a3a"
print(WEATHER_API)
weather_flag = True

def produce_message():
    weather_response = requests.get(f"{WEATHER_API}?access_key={API_ACCESS_KEY}"
                                    f"&query={random.choice(city_list)}")
    weather_data = weather_response.json()
    print(weather_data)
    if 'request' in weather_data:
        #Send weather data into Kafka broker
        producer.produce_weather_data(weather_data)
        return "Message Sent"
    else:
        produce_message()

while weather_flag:
    for i in range(5):
        produce_message()
        time.sleep(10)
    weather_flag = False

