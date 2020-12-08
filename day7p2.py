with open('input.txt') as f:
    a = f.read().split('.\n')

typecnt = {}
graph = {}

class node:
    def __init__(self, col, cnt):
        self.col = col
        self.cnt = cnt

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
        graph[p].append(node(color, num))

def nest(bag_type):
    if len(graph[bag_type]) == 0: return 1
    bags = 1
    for bagnode in graph[bag_type]:
        bags += bagnode.cnt * nest(bagnode.col)
    return bags
c = nest('shiny gold')-1
print(c)