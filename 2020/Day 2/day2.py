'''  password inspector
1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc
Each line gives the password policy and then the password. The password policy indicates the lowest and highest number of times a given letter must appear for the password to be valid. For example, 1-3 a means that the password must contain a at least 1 time and at most 3 times.

In the above example, 2 passwords are valid. The middle password, cdefg, is not; it contains no instances of b, but needs at least 1. The first and third passwords are valid: they contain one a or nine c, both within the limits of their respective policies.

How many passwords are valid according to their policies?
'''
from operator import xor

passwords = []

def parseline(entry):
    line = entry.replace('-',' ').split()
    minocc = int(line[0])
    maxocc = int(line[1])
    letter = line[2].strip(':')
    pw = line[3]
    return [minocc, maxocc, letter, pw]

with open('passwords.txt', 'r', encoding='utf-8') as f:
    for line in f:
        passwords.append(line.strip('\n'))

print(f'Number of passwords {len(passwords)}')

passed = 0

for line in passwords:
    # print(parseline(line))
    
    parsedline = parseline(line)
    letter = parsedline[2]
    pos1 = parsedline[0]
    pos2 = parsedline[1]
    pwd = parsedline[3]

    pos1a = pos1 - 1
    pos2a = pos2 - pos1 - 1
    print(f'\n{line}\n{pwd} shall contain the letter "{letter}" in either position {pos1} or {pos2}')
    print(' ' * pos1a, letter, ' ' * pos2a, letter, sep='')
    try: 
        if xor(bool(letter in pwd[pos1-1]), bool(letter in pwd[pos2-1])):
            print(f'passed: {pwd.count(letter)}\n')
            passed += 1
        else:
            print(f'failed: pos1 = {pwd[pos1-1]} and pos2 = {pwd[pos2-1]}\n')
    except:
        print(f'failed: not long enough: {len(pwd)}\t pwd[pos1+1] = {pwd[pos1-1]} \t pwd[pos2-1] = {pwd[pos2-1]} \n')

print(f'Number of compliant passwords: {passed}')

#not 575, 197