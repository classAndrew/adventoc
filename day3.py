
with open('input.txt') as f:
    inp = f.read().split('\n')
# def p1():
#     # cnt = 0
#     # for i in range(len(inp)):
#     #     cnt += inp[i][(i*3)%len(inp[0])] == '#'
#     cnt = sum(inp[i][(i*3)%len(inp[0])]=='#' for i in range(len(inp)))
#     return cnt
#     # print(cnt)
# from functools import reduce
# def p2():
#     cnt = reduce(lambda x, y: x*y, [sum(inp[i*y][(i*x)%len(inp[0])]=='#' for i in range(len(inp)//y + len(inp) % y)) for x, y in [(1,1), (3,1),(5, 1), (7, 1), (1,2)]])
#     return cnt

rows = len(inp)
cols = len(inp[0])
def p1_fast(dx, dy):
    bound = rows//dy+rows%dy
    cnt = 0
    pos = 0
    posx = 0
    for j in range(bound):
        cnt += inp[pos][posx] == '#'
        pos += dy 
        posx = (posx+dx)%cols
    return cnt

def p2_fast():
    A = [(1,1), (3,1),(5, 1), (7, 1), (1,2)]
    mul = 1

    for d in A:
        mul *= p1_fast(*d)

    return mul

from timeit import timeit
# print(timeit("p1()", globals=locals()))
# print(p2_fast())
print(timeit("p1_fast(3,1)", globals=globals()))
print(timeit("p2_fast()", globals=globals()))
# 164*93*82*91*43
# 93*164*82*91*44