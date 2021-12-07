with open('input.txt') as f:
    a = f.read().split('.\n')

typecnt = {}
graph = {}

for s in a:
    parts = s.split(" contain ")
    p = ' '.join(parts[0].split(' ')[:-1])
    if not parts[0] in graph:
        graph[p] = []
    info = parts[1].split(', ')
    for u in info:
        if 'no other bags' in u:
            break 
        spl = u.split(' ')
        num = int(spl[0])
        color = ' '.join(spl[1:-1])
        if not color in graph:
            graph[color] = []
        graph[p].append(color)

def p1():
    dp = {}
    def shiny_gold(bag_type):
        if bag_type in dp:
            return dp[bag_type]
        if bag_type == 'shiny gold':
            return 1
        for i in range(len(graph[bag_type])):
            if shiny_gold(graph[bag_type][i]):
                dp[bag_type] = 1
                return 1
        return 0
    c = 0
    for typ in graph:
        if typ != "shiny gold":
            c += shiny_gold(typ)
    return c

from timeit import timeit
print(timeit('p1()', number=200, globals=locals()))