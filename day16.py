with open('input.txt') as f:
    a, b, c = f.read().split('\n\n')
    a = a.split('\n')
    b = b.split('\n')[1:]
    c = c.split('\n')[1:]

# parse a data
# [[*range1, *range2]]
a_ranges = []
for ta in a:
    taa, tab = ta[ta.find(':')+2:].split(' or ')
    taa1, taa2 = [int(x) for x in taa.split('-')]
    tab1, tab2 = [int(x) for x in tab.split('-')]
    a_ranges.append([taa1, taa2, tab1, tab2])

my_ticket = [int(x) for x in b[0].split(',')]
def p1():
    bad = 0
    for snumlist in c:
        nums = [int(x) for x in snumlist.split(',')]
        for n in nums:
            invalid = all(not (ran[0] <= n <= ran[1] or ran[2] <= n <= ran[3]) for ran in a_ranges)
            # for ran in a_ranges:
            #     if not (ran[0] <= n <= ran[1] or ran[2] <= n <= ran[3]):
            #         invalid = True
            #         break
            bad += n*invalid
    print(bad)

def satisfied(l, tickets):
    for col in range(len(l)):
        field = l[col]
        restrict = a_ranges[field]
        for r in range(len(tickets)):
            invalid = not (restrict[0] <= tickets[r][col] <= restrict[1] or restrict[2] <= tickets[r][col] <= restrict[3])
            if invalid:
                return False
    return True
from functools import lru_cache
def p2():
    tickets = []
    for snumlist in c:
        nums = [int(x) for x in snumlist.split(',')]
        invalid = False
        for n in nums:
            invalid = all(not (ran[0] <= n <= ran[1] or ran[2] <= n <= ran[3]) for ran in a_ranges)
            if invalid:
                break
        if not invalid:
            tickets.append(nums)
    
    taken = [0]*len(a_ranges)
    order = []
    def backtrack(field, col):
        restrict = a_ranges[field]
        alenrange = len(a_ranges)
        for r in range(len(tickets)):
            invalid = not (restrict[0] <= tickets[r][col] <= restrict[1] or restrict[2] <= tickets[r][col] <= restrict[3])
            if invalid:
                return False
        # print(field, col, invalid)
        if col == alenrange-1:
            return True
        for i in range(len(taken)):
            if not taken[i]:
                taken[i] = 1
                order.append(i)
                res = backtrack(i, col+1)
                if res:
                    return True
                taken[i] = 0
                order.pop()
        return False
    for i in range(len(taken)):
        taken[i] = 1
        order.append(i)
        res = backtrack(i, 0)
        if res:
            print(order)
            break
        taken[i] = 0
        order.pop()
    print(satisfied(order, tickets))
    m = [my_ticket[order.index(i)] for i in range(6)]
    print(m)

def p2_fast():
    tickets = []
    for snumlist in c:
        nums = [int(x) for x in snumlist.split(',')]
        invalid = False
        for n in nums:
            invalid = all(not (ran[0] <= n <= ran[1] or ran[2] <= n <= ran[3]) for ran in a_ranges)
            if invalid:
                break
        if not invalid:
            tickets.append(nums)
    mat = [[1]*len(a_ranges) for i in range(len(a_ranges))]
    for i in range(len(mat)):
        pass

from timeit import timeit
print("Time: {}".format(timeit('p2()', globals=locals(), number=1)))

            

                

