import numpy as np

initial = np.fromfile("2021/input6b.txt", dtype=np.int8, count=-1, sep=',')

ages = np.array([np.count_nonzero(initial == age-1) for age in range(8)], dtype=int)
newbies = np.zeros(10, dtype=int) # index 8 = day 7 and  index 9 = day 8

days = 18

print(f"Day: 0  \tTotal LF: {ages.sum()}")

for day in range(days):
    ages = np.roll(ages, shift = -1)
    ages[7] += newbies[8]
    newbies[8] = newbies[9]
    newbies[9] = ages[0]
    print(f"Day: {day+1} Total LF: {ages.sum()}")

"""
Initial state: 3,4,3,1,2        13
After  1 day:  2,3,2,0,1        8
After  2 days: 1,2,1,6,0,8      18
After  3 days: 0,1,0,5,6,7,8
After  4 days: 6,0,6,4,5,6,7,8,8
After  5 days: 5,6,5,3,4,5,6,7,7,8
After  6 days: 4,5,4,2,3,4,5,6,6,7
After  7 days: 3,4,3,1,2,3,4,5,5,6
After  8 days: 2,3,2,0,1,2,3,4,4,5
After  9 days: 1,2,1,6,0,1,2,3,3,4,8
After 10 days: 0,1,0,5,6,0,1,2,2,3,7,8
After 11 days: 6,0,6,4,5,6,0,1,1,2,6,7,8,8,8
After 12 days: 5,6,5,3,4,5,6,0,0,1,5,6,7,7,7,8,8
After 13 days: 4,5,4,2,3,4,5,6,6,0,4,5,6,6,6,7,7,8,8
After 14 days: 3,4,3,1,2,3,4,5,5,6,3,4,5,5,5,6,6,7,7,8
After 15 days: 2,3,2,0,1,2,3,4,4,5,2,3,4,4,4,5,5,6,6,7
After 16 days: 1,2,1,6,0,1,2,3,3,4,1,2,3,3,3,4,4,5,5,6,8
After 17 days: 0,1,0,5,6,0,1,2,2,3,0,1,2,2,2,3,3,4,4,5,7,8
After 18 days: 6,0,6,4,5,6,0,1,1,2,6,0,1,1,1,2,2,3,3,4,6,7,8,8,8,8
"""