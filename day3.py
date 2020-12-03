k = 10
with open('input.txt') as f:
    inp = f.read().split('\n')
def p1():
    # cnt = 0
    # for i in range(len(inp)):
    #     cnt += inp[i][(i*3)%len(inp[0])] == '#'
    cnt = sum(inp[i][(i*3)%len(inp[0])]=='#' for i in range(len(inp)))
    print(cnt)

def p2():
    cnt = 0
    for i in range(len(inp)//2+1):
        cnt += inp[i*2][(i)%len(inp[0])] == '#'
    print(cnt)
p1()
# 164*93*82*91*43
# 93*164*82*91*44