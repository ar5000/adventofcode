import numpy as np

crabs = np.fromfile("2021/input7.txt", dtype=int, sep=',', count=-1)

steps = {crab:0 for crab in range(crabs.max())}

for pos in range(crabs.max()):
    steps[pos] = abs(crabs - pos)

fuel = np.array([sum([sum(range(step+1)) for step in pos]) for pos in steps.values()], dtype=int)

print(f'The least amount of fuel needed is {fuel.min()}')