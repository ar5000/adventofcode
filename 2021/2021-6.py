from gettext import find
import numpy as np
import time

lfs = np.fromfile("2021/input6b.txt", dtype=int, count=-1, sep=',')
days = 80

for day in range(1,days+1):
    start = time.time()
    lfs -= 1
    sub1 = time.time()
    inlabor = (lfs == -1)
    findbabies = time.time()
    # babies = np.full((lfs[np.where(lfs == -1)].size),8)
    babies = np.full((lfs[np.where(inlabor)].size),8)
    makebabies = time.time()
    lfs[(lfs == -1)] = 6
    resetmoms = time.time()
    lfs = np.append(lfs,babies)
    add2lfs = time.time()
    print(f'day {day}: {lfs.size}\tNew babies: {babies.size}')#: {lfs}')
    print(f'Subtract 1: {sub1-start}')
    print(f'Find Babies: {findbabies-sub1}')
    print(f'Make babies: {makebabies-findbabies}')
    print(f'Reset Moms: {resetmoms-makebabies}')
    print(f'Add babies to lfs: {add2lfs-resetmoms}\n\n\n')


print(f'Total LF: {lfs.size}')
# print(lfs.size)