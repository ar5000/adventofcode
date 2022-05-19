

with open('./input-3.txt','r') as f:
	logs = [d.rstrip() for d in f.readlines()]

#print(len(logs))
mpop = []

for i in range(len(logs[0])):
#	print('i',i,sep='\n')
	
	mpop.append(round(sum(int(n[i]) for n in logs)/len(logs)))

lpops = ''.join(str(int(not i)) for i in mpop)

mpops = ''.join(str(i) for i in mpop)

print(mpops,lpops)

print(int(mpops,2)*int(lpops,2))