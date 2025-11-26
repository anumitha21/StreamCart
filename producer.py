import json
import uuid

from confluent_kafka import Producer

producer_config = {"bootstrap.servers":"localhost:9092"} #bts server -to discover all the nodes avail at this adreess

producer = Producer(producer_config)
#delivery log
def delivery_report(err,msg):
    if err:
        print(f"❌ Delivery fails")
    else:
        print(f"✅ Delivered :  {msg.value().decode("utf-8")}")
        print(f"✅ Delivered to {msg.topic()}:partition{msg.partition()} :at offset {msg.offset()}")

order_id={
    "order_id": str(uuid.uuid4()),
    "user": "venky",
    "item":"loaded animal fries + coke",
    "quantity":4
 }

#this the above which is going to the consumers thro kafka, b4 sending we have to send to kafka readble so comveritng to bytes

value = json.dumps(order_id).encode("utf-8")
#creates the topic for orders
producer.produce(topic="orders",
                 value=value,
                 callback=delivery_report)#for logging the error

producer.flush() #it sends in batch insteadof one by one. if it crashes...the partial whicha re stuck btw are flushed/forced to the kafka..these are called buffer

#docker exec -it kafka kafka-topics --list --bootstrap-server localhost:9092
#it lists allthe topics ...we are using the docker continer to vierinside the prgm
