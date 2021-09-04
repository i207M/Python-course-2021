import datetime
import glob
import json

import matplotlib.pyplot as plt
import numpy as np

x = []
y = []
for file in glob.glob('clawed/*.json'):
    dat = json.load(open(file, 'r', encoding='utf-8'))
    date = dat['upload_time']  # 2021-05-30 11:48:06
    tt = datetime.datetime.strptime(date[:10], "%Y-%m-%d").timestamp()
    x.append(tt)
    y.append(dat['num_like'] / dat['num_view'])
print('Data Loaded')

x = np.array(x)
y = np.array(y)
print(x)
print(y)
plt.title('num_like / num_view')
plt.scatter(x, y)
plt.show()
