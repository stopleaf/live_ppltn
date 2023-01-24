from kafka import KafkaConsumer
from json import loads
import datetime
import pymongo

class Mongodb():
    def __init__(self):
        self.client = pymongo.MongoClient('mongodb://localhost:27017/')
        self.db = self.client['seoulrtd_citydata']
        self.collection = self.db['raw_data']

    def insert(self, message):
        self.collection.insert_one(message)

class Consumer():
    def __init__(self):
        self.consumer = KafkaConsumer('test',
                                 bootstrap_servers=['localhost:9092'],
                                 auto_offset_reset="earliest",
                                 enable_auto_commit=False,
                                 group_id='my-group', # 컨슈머 그룹핑(Fail Over, Offset 관리)
                                 value_deserializer=lambda x: loads(x.decode('utf-8')),
                                 consumer_timeout_ms=1000)

    def print_message(self, message):
        topic = message.topic
        partition = message.partition
        offset = message.offset
        timestamp = message.timestamp
        datetimeobj = datetime.datetime.fromtimestamp(timestamp / 1000)
        print("Topic:{}, partition:{}, offset:{}, datetimeobj:{}"
              .format(topic, partition, offset, datetimeobj))

    def run(self, mongodb_obj):
        while True:
            for message in self.consumer:
                self.print_message(message)
                mongodb_obj.insert(message.value)
                self.consumer.commit()

def main():
    Consumer().run(Mongodb())

if __name__ == "__main__":
    main()