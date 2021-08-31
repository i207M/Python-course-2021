import requests

r = requests.get('https://www.bilibili.com/video/BV1bW411n7fY')

open('example.html', 'w', encoding='utf-8').write(r.text)
