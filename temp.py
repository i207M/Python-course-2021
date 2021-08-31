import requests

r = requests.get('https://blog.i207m.top/')

open('example_blog.html', 'w', encoding='utf-8').write(r.text)
