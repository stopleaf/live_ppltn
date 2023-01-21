from get_live_ppltn import GetData
from kafka_producer import Producer

subway_stations = ['가산디지털단지역', '강남역', '건대입구역', '고속터미널역', '교대역',
                  '구로디지털단지역', '서울역', '선릉역', '신도림역', '신림역',
                  '신촌·이대역', '왕십리역', '역삼역', '연신내역', '용산역']
topic = 'test'
get_data_cls = GetData()
producer_cls = Producer()

for i in subway_stations:
    data = get_data_cls.get_data(i)
    producer_cls.producer_send(topic, data)
    print(f"{i} 전송 완료")

