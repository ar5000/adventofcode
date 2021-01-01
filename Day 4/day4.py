


with open('passports.txt', 'r', encoding= 'utf-8') as f:
    
    passports = f.read().replace('\n\n','%').replace('\n', ' ').split('%')
    
# for line in passports[:5]:
#     print(line)

class Passport:
    def __init__(self, byr=False, iyr=False, eyr=False, hgt=False, hcl=False, ecl=False, pid=False, cid=False):
        self.byr = byr
        self.iyr = iyr
        self.eyr = eyr
        self.hgt = hgt
        self.hcl = hcl
        self.ecl = ecl
        self.pid = pid
        self.cid = cid
    
    def validbyr(self):
        if len(self.byr) == 4 and 1920 <= int(self.byr) <= 2002:
            return True
        else:
            # print(f'byr failed: {self.byr}\t ', end='')
            return False

    def validiyr(self):
        if len(self.iyr) == 4 and 2010 <= int(self.iyr) <= 2020:
            return True
        else:
            # print(f'iyr failed: {self.iyr}\t ', end='')
            return False
    
    def  valideyr(self):
        if len(self.eyr) == 4 and 2020 <= int(self.eyr) <= 2030:
            return True
        else:
            # print(f'eyr failed: {self.eyr}\t ', end='')
            return False

    def validhgt(self):
        # print(self.hgt)
        units = self.hgt[-2:]
        height = self.hgt.strip('incm')
        # print(height,units)
        if height.isnumeric() and ('in' in units or 'cm' in units):
            if units == 'in' and 59 <= int(height) <= 76:
                return True
            elif units == 'cm' and 150 <= int(height) <= 193:
                return True
            else:
                return False
            
            # print(f'hgt passed: {self.hgt}\t ', end='')
            return True
        else:
            # print(f'hgt failed: {self.hgt}\t ', end='')
            return False

    def validhcl(self):
        # print(self.hcl)
        import re
        charRe = re.compile(r'[^a-f0-9.]')
        subset = charRe.search(self.hcl)
        if self.hcl[0] == '#' and len(self.hcl) == 7 and bool(subset):
            # print(f'hcl passed: {self.hcl}\t ', end='')
            return True
        else:
            # print(f'hcl failed: {self.hcl}\t ', end='')
            return False 

    def validecl(self):
        if self.ecl in ['amb','blu','brn','gry','grn','hzl','oth'] and len(self.ecl) == 3:
            # print(f'ecl passed: {self.ecl}\t ', end='')
            return True
        else:
            # print(f'ecl failed: {self.ecl}\t ', end='')
            return False

    def validpid(self):
        if len(self.pid) == 9:
            # print(f'pid passed: {self.pid}\t ', end='')
            return True
        else:
            # print(f'pid failed: {self.pid}\t ', end='')
            return False

    def valid(self):
        if self.validbyr() and self.validiyr() and self.valideyr() and self.validhgt() and self.validhcl() and self.validecl() and self.validpid():
            # print()
            return True
        else:
            # print()
            return False



valid1 = []

for i, line in enumerate(passports):
    byr = False
    iyr = False
    eyr = False
    hgt = False
    hcl = False
    ecl = False
    pid = False

    brokenline = line.split()
    for bline in brokenline:
        parsedline = bline.split(':')
        # print(parsedline[0],parsedline[1])
        if parsedline[0] == 'byr':
            byr = parsedline[1].strip()

        if parsedline[0] == 'iyr':
            iyr = parsedline[1].strip()        
        
        if parsedline[0] == 'eyr':
            eyr = parsedline[1].strip()

        if parsedline[0] == 'hgt':
            hgt = parsedline[1].strip()
        
        if parsedline[0] == 'hcl':
            hcl = parsedline[1].strip()
        
        if parsedline[0] == 'ecl':
            ecl = parsedline[1].strip()

        if parsedline[0] == 'pid':
            pid = parsedline[1].strip()


    if 'byr' not in locals():
        byr = False

    if 'iyr' not in locals():
        iyr = False

    if 'eyr' not in locals():
        eyr = False        

    if 'hgt' not in locals():
        hgt = False

    if 'hcl' not in locals():
        hcl = False

    if 'ecl' not in locals():
        ecl = False

    if 'pid' not in locals():
        pid = False


    # print(f'{i+1}: byr= {byr}\tiyr= {iyr}\teyr= {eyr}\thgt= {hgt}\thcl= {hcl}\tecl= {ecl} pid= {pid}')
    
    if byr and iyr and eyr and hgt and hcl and ecl and pid:
        valid1.append(Passport(byr,iyr,eyr,hgt,hcl,ecl,pid))
    
    
print(len(valid1))
valid = 0
for i in valid1:
    if i.valid():
        valid += 1
    # print(i.valid())

print(valid)

#part 1: 295
#part 2: 190,
'''

    if (
        len(byr) == 4 and 1920 >= byr <= 2002 and
        len(iyr) == 4 and 2010 >= iyr <= 2020 and
        len(byr) == 4 and 2020 >= byr <= 2030 and
        ('cm' in hgt or 'in' in hgt)
        
        and iyr and eyr and hgt and hcl and ecl and pid:
        valid += 1
'''