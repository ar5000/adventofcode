import numpy as np
import time

lfs = np.empty([22599789478], dtype=np.int8)

initial = np.fromfile("2021/input6.txt", dtype=np.int8, count=-1, sep=',')

lfs[:initial.size] += initial

days = 256
school = initial.size

for day in range(1, days+1):
    start = time.time()
    lfs[:school] -= 1
    minusone = time.time()
    newborns = lfs[:school][(lfs[:school] == -1)].size
    findbabies = time.time()
    newcount = school + newborns
    lfs[school:newcount] = 8
    appendnewborns = time.time()
    lfs[:school][(lfs[:school] == -1)] = 6
    resetmoms = time.time()
    school = newcount
    print(f'Day: {day}\t count: {newcount}')
    print(f'Subtract 1: {minusone-start}')
    # print(f'Find Babies: {findmoms-minusone}')
    print(f'Make babies: {findbabies-minusone}')
    print(f'Reset Moms: {appendnewborns-findbabies}')
    print(f'Add babies to lfs: {resetmoms-appendnewborns}\n\n\n')