import glob
import json
from collections import defaultdict

import matplotlib.pyplot as plt
import numpy as np

dic = defaultdict(int)
for file in glob.glob('clawed/*.json'):
    dat = json.load(open(file, 'r', encoding='utf-8'))
    dic[dat['up_id']] += 1
print('Data Loaded')

x = np.array(list(dic.values()))
# x = np.array(list(filter(lambda x: x > 2, dic.values())))
# x = np.random.normal(100, 20, 100)
print(x)
print(np.max(x))
n, bins, patches = plt.hist(x, 50)
print(n)
print(bins)
plt.show()
