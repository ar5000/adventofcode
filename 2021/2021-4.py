import os
import numpy as np
from pprint import pprint
from itertools import chain

#print(os.getcwd())
with open('2021\\input-4.txt','r') as f:
	game = [d.rstrip() for d in f.readlines()]

draws = [*map(int,game[0].split(','))] # working

boards = list(chain.from_iterable([item.split(' ') for item in game[1:]]))

board_count = int((len(boards)-boards.count(''))/25)

marked = np.zeros((board_count,5,5),dtype=int)
boards = np.array([int(item) for item in boards if item]).reshape(board_count,5,5)

# pprint(boards)

# print(draws)

winner_order = []

for num in draws[:]:
	i = np.where(boards == num)
	# print(f'num= {num}')
	# pprint(i)

	marked[i] = 1
	leave = 0

	for b,value in np.ndenumerate(marked):
		if b[0] not in winner_order:
			if marked[b[0:2]].sum() == 5 or marked[b[0],:,b[2]].sum() == 5:  # might want to check for columns here too
				print(f"Bingo! Board #{b[0]} won")
				winner = b
				winner_order.append(b[0])
				
				leave = 1
				# boards = np.delete(boards, winner[0])
				# marked = np.delete(marked, winner[0])
				# break



	if len(boards) == len(winner_order):
		last_num = num
		break
	
print("Marked locations: ")
pprint(marked)
pprint(boards[winner[0]])
sumboard = marked[winner[0]] == 0
sumboard = boards[winner[0]][sumboard]
print(sumboard.sum() * last_num)
# print(f'Winner Order: {boards[winner_order[-1]]}')
#76704
#p2= 8649- too low