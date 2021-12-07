import matplotlib.pyplot as plt
from functools import lru_cache

with open("input.txt") as f:
    fish_g = [int(x) for x in f.read().split(',')]

def simu(days):
    global fish_g
    fish_cnt = [0]*9
    for x in fish_g:
        fish_cnt[x+1] += 1

    while days:
        tmp = [0]*9
        
        tmp[8] += fish_cnt[0]
        tmp[6] += fish_cnt[0]
        
        for i in range(1, 9):
            tmp[i-1] += fish_cnt[i]

        fish_cnt = tmp
        days -= 1

    return sum(fish_cnt)

print(simu(257))