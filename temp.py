import glob
import os
import requests

bv_list = open('clawed_bv').read().splitlines()
print(len(bv_list))
s = set()
cnt_a = 0
cnt_b = 0
for bv in bv_list:
    if not os.path.exists(f'clawed/{bv}.json'):
        print(bv)
        cnt_a += 1
    else:
        s.add(bv)
        cnt_b += 1
print(cnt_a, cnt_b)
print(len(s))

s2 = set()
cnt = 0
for file in glob.glob('clawed/*.json'):
    # print(file)
    s2.add(file.split('\\')[1][:-5])
    cnt += 1
print(cnt)
print(s - s2)
