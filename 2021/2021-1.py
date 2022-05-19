

with open('/storage/emulated/0/Download/input.txt','r') as f:
	depth = [int(d.rstrip()) for d in f.readlines()]

newDepth = [depth[i-2] + depth[i-1] + depth [i] for i in range(2,len(depth))]

print(depth[0]+depth[1]+depth[2])

count = 0
for n, d in enumerate(newDepth[1:]):
		print(f'line {n} is {d}, prev line {n-1} is {newDepth[n]}')
		if d > newDepth[n]:
			count += 1
			print("+1")
print(newDepth[0:10])
print(count)
