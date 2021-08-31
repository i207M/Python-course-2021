import json
import requests
import time

from params import headers

# 爬取“鬼畜”频道
# URL: https://www.bilibili.com/v/channel/68?tab=featured
BASE_URL = 'https://api.bilibili.com/x/web-interface/web/channel/featured/list?channel_id=68&filter_type=0&offset={}&page_size=30'
INITIAL_OFFSET = '203867418_122051870'

page_cnt = 0
offset = INITIAL_OFFSET
f_json = open('clawed_json', 'w', encoding='utf-8')
f_bv = open('clawed_bv', 'w', encoding='utf-8')
while page_cnt <= 5000:
    api_url = BASE_URL.format(offset)
    api_ret = requests.get(api_url, headers=headers)
    api_text = api_ret.text

    f_json.write(api_text + '\n')
    api_json = json.loads(api_text)
    assert (api_json['code'] == 0 and api_json['message'] == '0')

    offset = api_json['data']['offset']
    video_list = api_json['data']['list']
    for video in video_list:
        f_bv.write(video['bvid'] + '\n')

    cnt = len(video_list)
    page_cnt += cnt
    print(f'Clawed {cnt}; {page_cnt} in total')
    time.sleep(1)

f_json.close()
f_bv.close()
