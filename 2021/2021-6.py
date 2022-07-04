import numpy as np
import time

lfs = np.fromfile("2021/input6b.txt", dtype=int, count=-1, sep=',')
days = 256

for day in range(1,days+1):
    lfs -= 1
    inlabor = (lfs == -1)
    babies = np.full((lfs[np.where(lfs == -1)].size),8)
    lfs[(lfs == -1)] = 6
    lfs = np.append(lfs,babies)
    print(f'day {day}')#: {lfs}')

print(f'Total LF: {lfs.size}')
# print(lfs.size)