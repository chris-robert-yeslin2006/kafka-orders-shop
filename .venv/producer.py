import json
import uuid

from confluent_kafka import Producer

producer=Producer({'bootstrap.servers':'localhost:9092'})

def delivery_report(err,msg):
    if err:
        print(f" delivery failed:{err}")
    else:
        print(f"Delivered {msg.value().decode("utf-8")}")

order={
    "order_id":str(uuid.uuid4()),
    "user":"chris",
    "item":"chicken pizza",
    "quantity":2,

}

value=json.dumps(order).encode("utf-8")
producer.produce(
    topic="orders",
    value=value,
    callback=delivery_report)

producer.flush()