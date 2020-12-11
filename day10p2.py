with open('input.txt') as f:
    a = [int(x) for x in f.read().split('\n')]

a = sorted(a)
exist = set(a)
dp = {}

def paths(n):
    if n in dp:
        return dp[n]
    if n == a[-1]:
        return 1
    c = 0
    for k in exist:
        if 1<= k - n <=3:
            c += paths(k)
    dp[n] = c
    return c

print(paths(0))