with open("input.txt") as f:
    a = f.read().split("\n\n")

reqs = ['byr','iyr','eyr','hgt','hcl','ecl','pid']
valid = 0
for e in a:
    try:
        d = {k.split(':')[0]:k.split(':')[1] for k in e.replace('\n', ',').replace(' ', ',').split(',')}
        c0 = 1920 <= int(d['byr']) <= 2002
        c1 = 2010 <= int(d['iyr']) <= 2020
        c2 = 2020 <= int(d['eyr']) <= 2030
        c3 = 0
        if d['hgt'][-2:] == 'cm':
            c3 = 150 <= int(d['hgt'][:-2]) <= 193
        elif d['hgt'][-2:] == 'in':
            c3 = 59 <= int(d['hgt'][:-2]) <= 76
        int(d['hcl'][1:], 16)
        c4 = d['hcl'][0] == '#' and len(d['hcl'])==7
        c5 = d['ecl'] in {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'}
        int(d['pid'])
        c6 = len(d['pid']) == 9
        for m in range(6):
            if not [c0,c1,c2,c3,c4,c5,c6][m]:
                print(d,m) 
                break
        valid += c0 and c1 and c2 and c3 and c4 and c5 and c6
    except Exception as e:
        # print(e)
        pass
print(valid)