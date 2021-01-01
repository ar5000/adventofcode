with open('bpasses.txt','r',encoding='utf-8') as f:
    binseats = []
    for line in f:
       binseats.append(line)


seatIDs = []
# print(seats)

for line in binseats:
    binrow = line.replace('F','0').replace('B','1').replace('L','0').replace('R','1')
    row = int(binrow[:7],2)
    seat = int(binrow[7:],2)
    sID = row * 8 + seat
    # print(row,seat, sID)
    seatIDs.append(sID)

seatIDs.sort()
# print(max(seatIDs))
# print(seatIDs)

for i,line in enumerate(seatIDs):
    if i+100 != int(line):
        print(line)

'''
line = 'FBFBBFFRLR'
binrow = line.replace('F','0').replace('B','1').replace('L','0').replace('R','1')
row = int(binrow[:7],2)
seat = int(binrow[7:],2)
sID = row * 8 + seat
print(row,seat, sID)
'''