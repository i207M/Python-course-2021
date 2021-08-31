import time

from claw_page import claw

bv_list = open('clawed_bv').read().splitlines()
f = open('fail.txt', 'a', encoding='utf-8')
for i, bv in enumerate(bv_list):
    try:
        claw(bv)
        print(f'Clawed {bv}; {i+1} in total')
    except Exception as e:
        print(e)
        print(f'FAILED {bv}')
        f.write(bv + '\n')
    time.sleep(0.1)

f.close()
