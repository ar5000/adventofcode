import os
import numpy as np


#print(os.getcwd())
with open('2021\\input-3.txt','r') as f:
	logs = [d.rstrip() for d in f.readlines()]
# print(logs)

nlog = np.array([[int(x) for x in logs[i]] for i in range(len(logs))])

print(nlog)

mpop = [*map(int, list(np.around(nlog.sum(axis=0)/len(logs))))]
lpop = [int(not i) for i in mpop] 

mpop_int = int(''.join(map(str,mpop)),2)
lpop_int = int(''.join(map(str,lpop)),2)

print(mpop_int, lpop_int)

print(f'The product is {mpop_int * lpop_int}')