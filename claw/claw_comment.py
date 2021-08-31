import json
import requests
import time

API_BASE = 'https://api.bilibili.com/x/v2/reply?jsonp=jsonp&pn=1&type=1&oid={}&sort=0'


def claw_comment(bvid: str):
    dic = json.load(open(f'clawed/{bvid}.json', encoding='utf-8'))
    if 'reply' in dic:
        print('Repeat')
        return

    aid = dic['aid']
    api_url = API_BASE.format(aid)
    api_ret = requests.get(api_url)
    api_text = api_ret.text
    # print(api_text)
    # open('example_comment.json', 'w', encoding='utf-8').write(api_text)
    comment_dict = json.loads(api_text)
    comment_dict = comment_dict['data']['hots']
    comment_list = []

    for comment in comment_dict:
        if len(comment_list) >= 5:
            break
        comment_list.append(comment['content']['message'])

    dic['reply'] = comment_list
    json.dump(dic, open(f'clawed/{bvid}.json', 'w', encoding='utf-8'), ensure_ascii=False)


if __name__ == '__main__':
    # claw_comment('BV1bW411n7fY')
    bv_list = open('clawed_bv').read().splitlines()
    for i, bv in enumerate(bv_list):
        try:
            claw_comment(bv)
            print(f'Clawed comments of {bv}; {i+1} in total')
        except Exception as e:
            print(e)
            print(f'FAILED {bv}')
        time.sleep(0.1)
