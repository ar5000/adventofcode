import os
import numpy as np
from pprint import pprint
from itertools import chain

#print(os.getcwd())
with open('2021\\input-4.txt','r') as f:
	game = [d.rstrip() for d in f.readlines()]

# pprint(game)

draws = [*map(int,game[0].split(','))] # working



# pprint(marked)

boards = list(chain.from_iterable([item.split(' ') for item in game[1:]]))

board_count = int((len(boards)-boards.count(''))/25)

marked = np.zeros((board_count,5,5),dtype=int)
boards = np.array([int(item) for item in boards if item]).reshape(board_count,5,5)

pprint(boards)
pprint(marked)