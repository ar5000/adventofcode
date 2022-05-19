

with open('/storage/emulated/0/Download/input2.txt','r') as f:
	hds = [d.rstrip() for d in f.readlines()]

print(hds[:10])

f = 0
d =0
aim = 0

for t in hds:
	if t[0] == 'd':
		aim += int(t[-1])
		
	elif t[0] == 'u':
		aim -= int(t[-1])
	
	elif t[0] == 'f':
		f += int(t[-1])
		d += aim * int(t[-1])
		
		
print(f,d,f*d)