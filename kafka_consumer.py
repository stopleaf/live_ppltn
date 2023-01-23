from kafka import KafkaConsumer
from json import loads
import time
import datetime

class Consumer():
    def __init__(self):
        pass


consumer = KafkaConsumer("test",
                        bootstrap_servers=['localhost:9092'],
                        auto_offset_reset="earliest",
                        enable_auto_commit=True,
                        group_id='my-group', # 컨슈머 그룹핑(Fail Over, Offset 관리)
                        value_deserializer=lambda x: loads(x.decode('utf-8')),
                        consumer_timeout_ms=1000
                       )

start = time.time()
print("START= ", start)
for message in consumer:
    topic = message.topic
    partition = message.partition
    offset = message.offset
    value = message.value
    timestamp = message.timestamp
    datetimeobj = datetime.datetime.fromtimestamp(timestamp/1000)
    # print("Topic:{}, partition:{}, offset:{}, value:{}, datetimeobj:{}".format(topic, partition, offset, value, datetimeobj))
    print("Topic:{}, partition:{}, offset:{}, datetimeobj:{}".format(topic, partition, offset, datetimeobj))

print("Elapsed time= ",(time.time()-start))