import requests

r = requests.get()

open('example.html', 'w', encoding='utf-8').write(r.text)
