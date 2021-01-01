#find the two elements in the list whos sum is 2020, then multiply them

expense = []
with open('expense.txt', 'r', encoding='utf-8') as f:
    for line in f:
        expense.append(int(line.strip('\n')))

#print(expense)

for i in expense:
    for o in expense:
        for t in expense:
            if i + o + t == 2020:
                print(f'The answer you seek is {i*o*t}')
                print(f'i = {i} and o = {o} and t = {t}')
