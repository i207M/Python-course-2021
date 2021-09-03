import glob
import json
import os

import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "dj.settings")
django.setup()

from video_list.models import Video

bv_list = open('../Python-course-2021-claw/clawed_bv').read().splitlines()

Video.objects.all().delete()

for i, bv in enumerate(bv_list):
    path = f'../Python-course-2021-claw/clawed/{bv}.json'
    if os.path.exists(path):
        dat: dict = json.load(open(path, 'r', encoding='utf-8'))
        dat.pop('up_sign')
        dat.pop('num_up_fan')
        Video.objects.create(**dat)
        if i % 100 == 0:
            print(Video.objects.count())
    else:
        print(f'No json: {bv}')

print('Done')
