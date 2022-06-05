import os
import numpy as np

#print(os.getcwd())
with open('2021\\input-3.txt','r') as f:
	logs = [d.rstrip() for d in f.readlines()]
# print(logs)

# nlog = np.array([[int(x) for x in logs[i]] for i in range(len(logs))])

# print(nlog)

# mpop = [*map(int, np.around(nlog.sum(axis=0)/len(logs)))]
# lpop = [int(not i) for i in mpop] 

# print(mpop, lpop)

# # mpop_int = int(''.join(map(str,mpop)),2)
# lpop_int = int(''.join(map(str,lpop)),2)

# print(mpop_int, lpop_int)

# print(f'The product is {mpop_int * lpop_int}')

# print(f'mpop: {mpop}')
def sum2pop(logs, pos, upordown):
	# print("Function:")
	# print("Logs:\n", logs, "\nposition: ", pos, "\n1 or 0:  ", upordown)
	# print("np.array(logs.sum(axis=0)/len(logs)):", np.array(logs.sum(axis=0)/len(logs)))
	if upordown:
		newrnd = np.array(logs.sum(axis=0)/len(logs)) >= .5
	elif not upordown:
		newrnd = np.array(logs.sum(axis=0)/len(logs)) < .5
	# print("newround", newrnd)
	# print("newround[pos]: ", newrnd[pos])
	return newrnd[pos]

popl = []

for x in [1,0]:
	nlog = np.array([[int(x) for x in logs[i]] for i in range(len(logs))])
	# print("nlog:\n", nlog)
	for i in range(len(logs[0])):
		xpop = sum2pop(nlog,i,x)
		b = nlog[:,i] == xpop
		nlog = nlog[b]
		if nlog.shape[0] == 1:
			print(f'{i+1} xpop: {xpop}\n {nlog}\n {nlog.shape}')
			popl.append(nlog)
			break
print(int(''.join(item for item in popl[0].astype(str)[0]),2) * int(''.join(item for item in popl[1].astype(str)[0]),2))


