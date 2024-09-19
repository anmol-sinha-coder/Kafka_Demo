# Kafka_Demo
Tools and testing for Apache Kafka

Download link: https://kafka.apache.org/downloads

Essential requirements for Python package libraries:
```
pip install  kafka-python  --upgrade jinja2  flask  requests
```
<hr/>

<style>
table, th, td {
  border: 1px solid black;
}
</style>

<table style="background-color:LightBlue;border: 1px solid black;">
<tr style="background-color:Yellow;border: 1px solid black;"><th>Objective</th><th>Shell Command</th></tr>
<tr><td>Start ZooKeeper: &emsp; </td><td> bin/zookeeper-server-start.sh config/zookeeper.properties </td> </tr>
<tr><td>Start Kafka: &emsp; </td><td> bin/kafka-server-start.sh config/server.properties </td> </tr>
<tr><td>Create Topic: &emsp; </td><td> bin/kafka-topics.sh --create --topic new_test --bootstrap-server localhost:9092 </td> </tr>
<tr><td>Update Topic: &emsp; </td><td> bin/kafka-topics.sh --alter --topic new_test --bootstrap-server localhost:9092 --partitions 16 </td> </tr>
<tr><td>Show Topics: &emsp; </td><td> bin/kafka-topics.sh --bootstrap-server=localhost:9092 --list </td> </tr>
<tr><td>Describe Topic: &emsp; </td><td> bin/kafka-topics.sh --describe --topic new_test --bootstrap-server localhost:9092 </td> </tr>
<tr><td>Show Groups: &emsp; </td><td> bin/kafka-consumer-groups.sh  --list --bootstrap-server localhost:9092 </td> </tr>
<tr><td>Describe Group: &emsp; </td><td> bin/kafka-consumer-groups.sh --describe --group test_group --bootstrap-server localhost:9092 </td> </tr>
<tr><td>Start console-based Input Producer: &emsp; </td><td> bin/kafka-console-producer.sh --broker-list localhost:9092 --topic new_test </td> </tr>
<tr><td>Start console-based Output Consumer: &emsp; </td><td> bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic new_test --group test_group --from-beginning </td> </tr>
<tr><td>Login to ZooKeeper Terminal: &emsp; </td><td> bin/zookeeper-shell.sh localhost:2181 </td> </tr>
</table>
