import numpy as np
import time

initial = np.fromfile("2021/input6.txt", dtype=np.int8, count=-1, sep=',')

lfs = {i:np.count_nonzero(initial == i) for i in range(9)}

days = 256

start = time.time()

for day in range(days+1):
    print(f'Day: {day}\t Count: {sum(lfs.values())}')
    babies = lfs[0]
    lfs[0] = lfs[1]
    lfs[1] = lfs[2]
    lfs[2] = lfs[3]
    lfs[3] = lfs[4]
    lfs[4] = lfs[5]
    lfs[5] = lfs[6]
    lfs[6] = lfs[7] + babies
    lfs[7] = lfs[8]
    lfs[8] = babies

print(f'Elapsed time: {time.time()-start}')