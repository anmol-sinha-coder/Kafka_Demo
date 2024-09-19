# Kafka_Demo
Tools and testing for Apache Kafka

Download link: https://kafka.apache.org/downloads

Essential requirements for Python package libraries:
```
pip install  kafka-python  --upgrade jinja2  flask  requests
```
<hr/>

Start ZooKeeper: &emsp; bin/zookeeper-server-start.sh config/zookeeper.properties
 
Start Kafka: &emsp; bin/kafka-server-start.sh config/server.properties
 
Create Topic: &emsp; bin/kafka-topics.sh --create --topic new_test --bootstrap-server localhost:9092
 
Update Topic: &emsp; bin/kafka-topics.sh --alter --topic new_test --bootstrap-server localhost:9092 --partitions 16
 
Show Topics: &emsp; bin/kafka-topics.sh --bootstrap-server=localhost:9092 --list
 
Describe Topic: &emsp; bin/kafka-topics.sh --describe --topic new_test --bootstrap-server localhost:9092
 
Show Groups: &emsp; bin/kafka-consumer-groups.sh  --list --bootstrap-server localhost:9092
 
Describe Group: &emsp; bin/kafka-consumer-groups.sh --describe --group test_group --bootstrap-server localhost:9092

Start console-based Input Producer: &emsp; bin/kafka-console-producer.sh --broker-list localhost:9092 --topic new_test
 
Start console-based Output Consumer: &emsp; bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic new_test --group test_group --from-beginning
 
Login to ZooKeeper Terminal: &emsp; bin/zookeeper-shell.sh localhost:2181
