import glob
import json
import os
import requests

bv_list = open('clawed_bv').read().splitlines()

for bv in bv_list:
    path = f'clawed/{bv}.json'
    if os.path.exists(path):
        dat = json.load(open(path, 'r', encoding='utf-8'))
        if 'reply' not in dat:
            print(f'No reply: {bv}')
    else:
        print(f'No json: {bv}')
