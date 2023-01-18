'''
ver 0.0.1
stopleaf
'''

import requests
import bs4
import pandas as pd

def get_row(open_api_key, target, cols_list):
    url = f'http://openapi.seoul.go.kr:8088/{open_api_key}/xml/citydata/1/5/{target}'
    r = requests.get(url)
    text = r.text
    soup = bs4.BeautifulSoup(text, 'lxml-xml')
    tags = [soup.findAll(i)[0] for i in cols_list]
    row = [tags[i].text for i in range(0, len(tags))]
    return row

cols_list = ['PPLTN_TIME', 'AREA_NM', 'LIVE_PPLTN_STTS', 'AREA_CONGEST_LVL', 'AREA_CONGEST_MSG',
             'AREA_PPLTN_MIN', 'AREA_PPLTN_MAX', 'MALE_PPLTN_RATE', 'FEMALE_PPLTN_RATE', 'PPLTN_RATE_0',
             'PPLTN_RATE_10', 'PPLTN_RATE_20', 'PPLTN_RATE_30', 'PPLTN_RATE_40', 'PPLTN_RATE_50',
             'PPLTN_RATE_60', 'PPLTN_RATE_70', 'RESNT_PPLTN_RATE', 'NON_RESNT_PPLTN_RATE']

subway_station = ['가산디지털단지역', '강남역', '건대입구역', '고속터미널역', '교대역',
                  '구로디지털단지역', '서울역', '선릉역', '신도림역', '신림역',
                  '신촌·이대역', '왕십리역', '역삼역', '연신내역', '용산역']

open_api_key = '46686d4a4573746f37344553524746'

rows = [get_row(open_api_key, i, cols_list) for i in subway_station]
df = pd.DataFrame(rows, columns=cols_list)
print(df)