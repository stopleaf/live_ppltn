from kafka import KafkaProducer
from json import dumps

class Producer:
    def __init__(self):
        self.producer = KafkaProducer(acks=1,
                                      compression_type='gzip',
                                      bootstrap_servers=['localhost:9092'],
                                      value_serializer=lambda x: dumps(x).encode('utf-8'),
                                      )

    def producer_send(self, topic, data):
        self.producer.send('test', value=data)
        self.producer.flush()