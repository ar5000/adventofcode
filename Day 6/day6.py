with open('customs.txt', 'r', encoding='utf-8') as f:
    data = f.read()

    
answers = []
count = []
pax = []
# print(data)

data = data.split('\n\n')
# print(data)
for line in data:
    pax.append(line.count('\n')+1)
    answers.append(line.replace('\n',''))


# print(answers)
letters = []

for i,line in enumerate(answers):
    print(f'Group: {i}\tNumber of pax: {pax[i]}\tanswers: {line}\t ')
    used = []
    for o in line:
        print(o)
        if line.count(o) == pax[i] and o not in used:
            used.append(o)
    print(used)
    count.append(len(used))

    print()
  

print(f'# of Groups: {len(answers)}')
print(sum(count))




'''
    for o in line:
        if line.count(o) == pax[i]:
            allused.append(o)
    if len(allused) > 0:
        letters.extend(set(allused))
    print(set(allused))
    count += len(set(allused))
'''
print(count)
print(sum(count))
# #3196 (too low)