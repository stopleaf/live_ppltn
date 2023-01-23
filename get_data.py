import requests
import bs4
import xmltodict

class GetData:
    def __init__(self):
        self.open_api_key = '46686d4a4573746f37344553524746'

    def get_data(self, area_name):
        url = f'http://openapi.seoul.go.kr:8088/{self.open_api_key}/xml/citydata/1/5/{area_name}'
        r = requests.get(url)
        text = r.text
        xml = bs4.BeautifulSoup(text, 'lxml-xml')
        xml_to_dict = xmltodict.parse(str(xml))
        return xml_to_dict