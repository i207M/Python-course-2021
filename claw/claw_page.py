import json
import re
import requests

from params import spider_headers


def escape(text: str):
    return text.encode('utf-8').decode('unicode-escape')


def claw(bvid: str):
    url = 'https://www.bilibili.com/video/' + bvid
    html = requests.get(url, headers=spider_headers).text
    open(f'clawed_html/{bvid}.html', 'w', encoding='utf-8').write(html)
    # print(url)
    # print(html)
    dat = re.findall(r'window.__INITIAL_STATE__={[\s\S]*?};', html)[0]
    dat = dat[25:-1]
    # open('example_video.json', 'w', encoding='utf-8').write(dat)
    dat = json.loads(dat)
    # print(dat)

    aid = dat['aid']
    title = dat['videoData']['title']
    desc = dat['videoData']['desc']
    cover = escape(dat['videoData']['pic'])

    num_view = dat['videoData']['stat']['view']
    num_like = dat['videoData']['stat']['like']
    num_coin = dat['videoData']['stat']['coin']
    num_favorite = dat['videoData']['stat']['favorite']

    up_id = dat['videoData']['owner']['mid']
    up_name = dat['videoData']['owner']['name']
    up_face = escape(dat['videoData']['owner']['face'])
    up_sign = dat['upData']['sign']
    num_up_fan = dat['upData']['fans']

    upload_time = re.findall(r'<meta data-vue-meta="true" itemprop="uploadDate" content=".*?">', html)[0]
    upload_time = upload_time[58:-2]

    dic = {
        'aid': aid,
        'bvid': bvid,
        'title': title,
        'desc': desc,
        'cover': cover,
        'num_view': num_view,
        'num_like': num_like,
        'num_coin': num_coin,
        'num_favorite': num_favorite,
        'up_id': up_id,
        'up_name': up_name,
        'up_face': up_face,
        'up_sign': up_sign,
        'num_up_fan': num_up_fan,
        'upload_time': upload_time
    }

    # print(dic)
    # with open(f'clawed/{bv}.json', 'w', encoding='utf-8') as f:
    #     f.write(json.dumps(dic, ensure_ascii=False))
    json.dump(dic, open(f'clawed/{bvid}.json', 'w', encoding='utf-8'), ensure_ascii=False)


if __name__ == '__main__':
    claw('BV1bW411n7fY')  # 改革春风吹满地
    # claw('BV1Sb4y1m7My')  # 合作投稿
    # claw('BV1SJ411e7c9')  # 跳转链接
    # claw('BV1ms411W7tQ')  # 重名
