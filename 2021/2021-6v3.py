import numpy as np

initial = np.fromfile("2021/input6b.txt", dtype=np.int8, count=-1, sep=',')

ages = np.array([np.count_nonzero(initial == age) for age in range(9)], dtype=int)

days = 18

for day in range(1,days+1):
    ages = np.roll(ages, shift = -1)
    ages[6] = ages[0]
    print(f"Total LF: {ages.sum()}")

