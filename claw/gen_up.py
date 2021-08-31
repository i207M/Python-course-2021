from glob import glob
import json

up_dict = {}
for file in glob('clawed/*.json'):
    dat = json.load(open(file, 'r', encoding='utf-8'))
    dic = {
        'id': dat['up_id'],
        'name': dat['up_name'],
        'face': dat['up_face'],
        'sign': dat['up_sign'],
        'num_fan': dat['num_up_fan']
    }
    up_dict[dat['up_id']] = dic

print('Read')

for up in up_dict.values():
    json.dump(up, open(f'clawed_up/{up["id"]}.json', 'w', encoding='utf-8'), ensure_ascii=False)

print('Done')
