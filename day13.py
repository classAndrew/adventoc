# junk here doesn't work- use Chinese Remainder Theorem solver
with open('input.txt') as f:
    a = f.read().split('\n')
    t = int(a[0])
    sched = [int(x) if x.isdigit() else x for x in a[1].split(',')]

def p1():
    s = [(x-(t%x), x) for x in sched if x != 'x']
    s = sorted(s)
    print(s[0][1]-s[0][0], s[0][0])
from functools import reduce
def p2():
    pcn = [x for x in sched if x != 'x']
    ccn = [i for i in range(len(sched)) if sched[i] != 'x']
    N = reduce(lambda x, y: x*y, pcn)
    ycn = [N/x for x in pcn]
    zcn = [(ycn[i]) % pcn[i] for i in range(len(ycn))]
    lhs = 0
    rhsvar = 0
    print(''.join(f"{x[0]}\t{x[1]}" for x in zip(pcn, ccn)))
    for i in range(len(ccn)):
        lhs += zcn[i]*ccn[i]*ycn[i]
        rhsvar += zcn[i]*ycn[i]
    print(lhs/rhsvar)
p2()