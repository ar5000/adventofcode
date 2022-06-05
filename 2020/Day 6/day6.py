
with open('customs.txt', 'r', encoding='utf-8') as f:
    data = f.read()

    
answers = []
count = 0
pax = []
# print(data)

data = data.split('\n\n')

# print(data)
for line in data:
    answers.append(line.split('\n'))
    pax.append(line.count('\n')+1)
    # answers.append(line.replace('\n',''))

# print(pax)
# print(answers)
letters = {}

class Alpha:
    def __init__(self):
        self.letters = {}
        for i in range(97,97+26):
            self.letters[chr(i)] = 0
        # print(self.letters)

# print(answers[0])

for i,group in enumerate(answers):
    chars = Alpha()
    print(i, group)
    for person in group:
        # print(person)
        for letter in person:
            chars.letters[letter] += 1
    for i in chars.letters:
        if len(group) == chars.letters[i]:
            count += 1
        
        # print(chars.letters[i])
        # print(len(group),chars.letters)

print(count)
# #3196 (too low)
