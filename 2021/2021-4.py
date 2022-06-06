import os
import numpy as np
from pprint import pprint

#print(os.getcwd())
with open('2021\\input-4b.txt','r') as f:
	game = [d.rstrip() for d in f.readlines()]

pprint(game)

draws = [*map(int,game[0].split(','))] # working

