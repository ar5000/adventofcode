import math

with open('treemap.txt', 'r', encoding = 'utf-8') as f:
    trees = []
    for line in f:
        trees.append(line.strip('\n'))

print(len(trees))

def extend(stub,width):
    if width == 0:
        width = 1
    return stub*(math.ceil(width/len(stub)))

ouch = 0

slopes = ((1,1),(3,1),(5,1),(7,1),(1,2))
impacts = []

for s in slopes:
    
    print(s)
    ouch = 0
    for i,line in enumerate(trees[::s[1]]):
        terrain = extend(line,(i+1)*s[0])
        # print(terrain, i, i*3, len(terrain))
        
        if terrain[i * s[0]] == '#':
            ouch += 1

    print('ouch', ouch)
    impacts.append(ouch)

print(impacts)
import math
print(math.prod(impacts))