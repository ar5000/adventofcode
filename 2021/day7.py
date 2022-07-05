import numpy as np

crabs = np.fromfile("2021/input7.txt", dtype=int, sep=',', count=-1)

fuel = {crab:0 for crab in range(crabs.max())}

for crab in range(crabs.max()):
    fuel[crab] = sum(abs(crabs - crab))

print(f'The least amount of fuel needed is {sorted(fuel.values())[0]}')