import glob
import json
import os
import requests

bv_list = open('clawed_bv').read().splitlines()

mxlen = 0

for bv in bv_list:
    path = f'clawed/{bv}.json'
    if os.path.exists(path):
        dat = json.load(open(path, 'r', encoding='utf-8'))
        mxlen = max(len(dat['title']), mxlen)
    else:
        print(f'No json: {bv}')

print(mxlen)
