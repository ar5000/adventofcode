import os

#print(os.getcwd())
with open('2021\\input-3.txt','r') as f:
	logs = [d.rstrip() for d in f.readlines()]
#print(len(logs))
mpop = []

for i in range(len(logs[0])):
#	print('i',i,sep='\n')
	
	mpop.append(round(sum(int(n[i]) for n in logs)/len(logs)))
	# print((sum(int(n[i]) for n in logs)/len(logs)))

lpops = ''.join(str(int(not i)) for i in mpop)

mpops = ''.join(str(i) for i in mpop)

logs2 = logs.copy()

print(mpops,lpops)

for i,b in enumerate(mpops):
	for n in logs[:]:
		if n[i] != b:
			# print(f'removing {n} because the {i}th digit isn\'t {b} \t now there are {len(logs)-1} left')
			if len(logs) > 1:
				keepL = n
			logs.remove(n)
			
		# else: print(f'Keeping {n} because the {i}th digit is {int(not b)}')

for i,b in enumerate(lpops):
	for n in logs2[:]:
		if n[i] != b:
			print(f'removing {n} because the {i}th digit isn\'t {b} \t now there are {len(logs2)-1} left')
			if len(logs2) > 1:
				keepS = n
			logs2.remove(n)
			
		else: print(f'Keeping {n} because the {i}th digit is {int(not b)}')



print(logs)
print(mpops,lpops)
print(int(keepL,2) * int(keepS,2))
#  2602692
isinstance()