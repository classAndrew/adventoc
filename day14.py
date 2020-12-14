with open('input.txt') as f:
    a = f.read().split('\n')
def p1():
    memmap = {}
    i = 0
    while i < len(a):
        if a[i][:4] == 'mask':
            mask = a[i][7:]
            i += 1
            while i < len(a) and a[i][:3]=='mem':
                addr = a[i][a[i].find('[')+1:a[i].find(']')]
                val = int(a[i][a[i].find('=')+2:])
                sval = bin(val)[2:]
                sval = list('0'*(len(mask)-len(sval))+sval)
                for j in range(len(mask)):
                    if mask[j] == 'X':
                        continue
                    sval[j] = mask[j]
                print(sval)
                memmap[addr] = int(''.join(sval), 2)
                i += 1
            i -= 1
        i+=1
    print(memmap)
    print(sum(memmap[k] for k in memmap))

def p2():
    # address combination
    memmap = {}
    i = 0
    while i < len(a):
        if a[i][:4] == 'mask':
            mask = a[i][7:]
            i += 1
            while i < len(a) and a[i][:3]=='mem':
                addr = a[i][a[i].find('[')+1:a[i].find(']')]
                # apply mask on addr
                saddr = bin(int(addr))[2:]
                saddr = list('0'*(len(mask)-len(saddr))+saddr)
                for j in range(len(mask)):
                    if mask[j] == '0': continue
                    saddr[j] = mask[j]
                # print(saddr)
                # need to handle cases like 00 and XX
                xcount = saddr.count('X')
                # apply mask on val
                val = int(a[i][a[i].find('=')+2:])
                sval = bin(val)[2:]
                sval = list('0'*(len(mask)-len(sval))+sval)
                for subset in range(1<<xcount):
                    #print(subset)
                    copy = list(saddr)
                    ssub = '0'*(xcount-len(bin(subset)[2:]))+bin(subset)[2:]
                    ptr = 0 
                    for copyi in range(len(copy)):
                        if copy[copyi] == 'X':
                            copy[copyi] = ssub[ptr]
                            ptr += 1
                    memmap[''.join(copy)] = int(''.join(sval), 2)
                i += 1
            i -= 1
        i+=1
    # print(memmap)
    # X 1 Y 0 1 X -4
    # 0 1 X 0 X X
    #  Y has same effect as X but no sub
    # print(memmap)
    print(sum(memmap[k] for k in memmap))
p2()