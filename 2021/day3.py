import numpy as np

with open("input.txt") as f:
    data = [[*map(int, x)] for x in f.read().split('\n')]

def p1(data):
    L, data = len(data), zip(*data)
    bstring = ''.join('01'[sum(x)>=L//2+(L&1)] for x in data)
    print(int(bstring,2)*int(bstring.replace('0','t').replace('1','0').replace('t', '1'), 2))

def p2(data):
    data = [*map(tuple, data)]
    L, transpose = len(data), zip(*data)
    cnt, data = [*map(sum, transpose)], set(data)

    i = 0
    while len(data) > 1:
        remove = [x for x in data if x[i] == 0 and cnt[i] >= 1]
        for k in remove: 
            for j in range(len(k)):
                cnt[j] -= k[j] == 1
            data.remove(k)
            
        i += 1

    print(data)
    
p1(data)
p2(data)

# c = len(data[0])*[0]
# d = len(data[0])*[0]
# for x in data:
#     a = list(x)
#     for i in range(len(a)):
#         c[i]+=a[i] == '1'
#         d[i] += a[i] == '0'

# b = ''
# for i in range(len(c)):
#     if c[i] > d[i]:
#         b += '1'
#     else:
#         b += '0'

# a = b.replace('0', 'a').replace('1', '0').replace('a', '1')
# print(a, b)
# L = len(data[0])
# data = set(data)
# i = 0
# while len(data)>1:
#     remove = []
#     if c[i] >= d[i]:
#         remove = [k for k in data if k[i] == '1'] # flip to 0 for other
#     else:
#         remove = [k for k in data if k[i] == '0'] # flip to 1 for other
#     for k in remove:
#         for j in range(len(k)):
#             c[j] -= k[j] == '1'
#             d[j] -= k[j] == '0'
#         data.remove(k)
#     i += 1

# # 011100101100
# # 100011010101
# print(data, i)    