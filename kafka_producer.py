from kafka import KafkaProducer
from json import dumps
import requests
import bs4
import xmltodict

class Data:
    def __init__(self):
        self.open_api_key = '46686d4a4573746f37344553524746'

    def run(self, area_name):
        url = f'http://openapi.seoul.go.kr:8088/{self.open_api_key}/xml/citydata/1/5/{area_name}'
        r = requests.get(url)
        text = r.text
        xml = bs4.BeautifulSoup(text, 'lxml-xml')
        xml_to_dict = xmltodict.parse(str(xml))
        return xml_to_dict

class Producer:
    def __init__(self):
        self.producer = KafkaProducer(acks=1,
                                      compression_type='gzip',
                                      bootstrap_servers=['localhost:9092'],
                                      value_serializer=lambda x: dumps(x).encode('utf-8'),
                                      )

    def run(self, topic, data):
        self.producer.send(topic, value=data)
        self.producer.flush()

def main():
    subway_stations = ['가산디지털단지역', '강남역', '건대입구역', '고속터미널역', '교대역',
                       '구로디지털단지역', '서울역', '선릉역', '신도림역', '신림역',
                       '신촌·이대역', '왕십리역', '역삼역', '연신내역', '용산역']
    topic = 'test'
    data_obj = Data()
    producer_obj = Producer()

    for i in subway_stations:
        data = data_obj.run(i)
        producer_obj.run(topic, data)
        print(f"{i} 전송 완료")

if __name__ == "__main__":
    main()