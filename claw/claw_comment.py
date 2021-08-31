import json
import requests

API_BASE = 'https://api.bilibili.com/x/v2/reply?jsonp=jsonp&pn=1&type=1&oid={}&sort=0'


def claw_comment(aid: int):
    api_url = API_BASE.format(aid)
    api_ret = requests.get(api_url)
    api_text = api_ret.text
    open('example_comment.json', 'w', encoding='utf-8').write(api_text)
    dat = json.loads(api_text)
    print(dat)


if __name__ == '__main__':
    claw_comment(19390801)
