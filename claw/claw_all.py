import time

from claw_page import claw

bv_list = open('clawed_bv').read().splitlines()

for i, bv in enumerate(bv_list):
    claw(bv)
    print(f'Clawed {bv}; {i+1} in total')
    time.sleep(0.1)
