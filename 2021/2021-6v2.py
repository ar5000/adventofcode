import numpy as np
import time

np.set_printoptions(threshold=np.inf)

lfs = np.empty([2259978947], dtype=np.int8)
               26285325879
initial = np.fromfile("input6.txt", dtype=np.int8, count=-1, sep=',')

lfs[:initial.size] += initial

days = 80
school = initial.size

begin = time.time()

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
    print(f'Day: {day}\t count: {school}')#\t {lfs[:school]}')
    print(f'Subtract 1: {minusone-start}')
    # print(f'Find Babies: {findmoms-minusone}')
    print(f'Make babies: {findbabies-minusone}')
    print(f'Reset Moms: {appendnewborns-findbabies}')
    print(f'Add babies to lfs: {resetmoms-appendnewborns}')
    print(f'Loop time: {time.time()-start}')
    print(f'Total Elapsed: {time.time()-begin}\n\n\n')

    #26285325879 too low (due to not enough array space being allocated)