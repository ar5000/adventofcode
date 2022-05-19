import os

#print(os.getcwd())
with open('2021\\input-3a.txt','r') as f:
	logs = [d.rstrip() for d in f.readlines()]
#print(len(logs))
mpop = []

for i in range(len(logs[0])):
#	print('i',i,sep='\n')
	
	mpop.append(round(sum(int(n[i]) for n in logs)/len(logs)))
	# print((sum(int(n[i]) for n in logs)/len(logs)))

lpops = ''.join(str(int(not i)) for i in mpop)

mpops = ''.join(str(i) for i in mpop)



print(mpops,lpops)

for i,b in enumerate(mpops):
	for n in logs[:]:
		if n[i] != b:
			print(f'removing {n} because the {i}th digit isn\'t {b} \t now there are {len(logs)-1} left')
			logs.remove(n)
			
		else: print(f'Keeping {n} because the {i}th digit is {int(not b)}')

print(logs)