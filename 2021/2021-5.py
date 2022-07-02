import numpy as np
import time

start = time.time()

fname = '2021/input-5.txt'
# dtype1 = np.dtype([('x1', 'i'), ('y1', 'i'), ('x2','i'), ('y2','i')]) # names elements
# for some reason, this made the data harder to call with np functions ^^

def reformat(coords): # generator that removes , and ->
    for line in coords:
        line = line.replace(',',' ')
        line = line.replace(' ->','')
        newline = line.strip().split(' ')
        newline = list(map(int, newline))
        # ordering the coordinates from low to high
        if newline[0] == newline[2] or newline[1] == newline[3]:
            newline = [min([newline[0],newline[2]]),
                    min([newline[1], newline[3]]),
                    max([newline[0],newline[2]]),
                    max([newline[1],newline[3]])]
        newline = list(map(str, newline))
        yield ' '.join(newline)

with open(fname) as coords:
    vents = np.loadtxt(reformat(coords), dtype='int_')

# data formated like this= vents[z][x1, y1, x2, y2]
x1 = 0
y1 = 1
x2 = 2
y2 = 3

# Create an array of appropriate size with all zeros
ocean = np.zeros([int(max([vents[:,x1].max(),vents[:,x2].max()]))+1, int(max([vents[:,y1].max(),vents[:,y2].max()])) +1], dtype='int_')

# print(vents)

for vent in vents:
    
    if vent[x1] == vent[x2]:
        # print("x1 = x2")
        ocean[vent[y1]:vent[y2]+1,vent[x2]] += 1
    elif vent[y1] == vent[y2]:
        # print("y1 = y2")
        ocean[vent[y1],vent[x1]:vent[x2]+1] += 1
    # print(f'x1: {vent[x1]}\t x2: {vent[x2]}\t y1: {vent[y1]}\t y2: {vent[y2]}')
    else:# vent[x1] not vent[x2] or vent[y1] not vent[y2]:
        # print(f'diagonal: {vent}')
        diags = []
        for step in range(abs(vent[x2]-vent[x1])+1):
            if vent[x1] > vent[x2] and vent[y1] > vent[y2]: # subtract x and y
                diags.append([vent[x1]-step,vent[y1]-step])
            elif vent[x1] < vent[x2] and vent[y1] > vent[y2]: # add x, subtract y
                diags.append([vent[x1]+step,vent[y1]-step])
            elif vent[x1] > vent[x2] and vent[y1] < vent[y2]: # subtract x, add y
                diags.append([vent[x1]-step,vent[y1]+step])
            elif vent[x1] < vent[x2] and vent[y1] < vent[y2]: # add x and y
                diags.append([vent[x1]+step,vent[y1]+step])
        for item in diags:
            ocean[item[1],item[0]] += 1
        
# print(ocean)

overlap = ocean > 1

print(f'Overlaps: {len(ocean[overlap])}')
end = time.time()
print(f'Time: {end-start}')

#21488 too high