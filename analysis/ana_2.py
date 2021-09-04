import glob
import json

import matplotlib.pyplot as plt
import numpy as np

num_upload = np.zeros((24, ))
num_view = np.zeros((24, ))
all_num = 0
all_view = 0
for file in glob.glob('clawed/*.json'):
    dat = json.load(open(file, 'r', encoding='utf-8'))
    date = dat['upload_time']  # 2021-05-30 11:48:06
    hour = int(date[11:13])
    num_upload[hour] += 1
    num_view[hour] += dat['num_view']
    all_num += 1
    all_view += dat['num_view']
    # print(date, date[11:13])
    # break
print('Data Loaded')

print(all_view / all_num)
print(num_view / num_upload)
plt.bar(range(24), num_view / num_upload)
plt.show()
