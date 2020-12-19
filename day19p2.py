# CODE DOESN'T WORK FIX LATER
with open('input.txt') as f:
    a, b = f.read().split('\n\n')
    a = a.split('\n')
    b = b.split('\n')

graph = {}
for i in range(len(a)):
    colonsplit = a[i].split(': ')
    node = int(colonsplit[0])
    orsplit = colonsplit[1].split(' | ' )
    neighbors1 = [int(x) for x in orsplit[0].split(' ')] if not '"' in orsplit[0] else orsplit[0][1]
    neighbors2 = []
    if len(orsplit) > 1:
        neighbors2 = [int(x) for x in orsplit[1].split(' ')]
    graph[node] = (neighbors1, neighbors2)


# returns length. length = 0 means something went wrong (invalid)
def valid(s, rule, pos):
    if type(rule) != int:
        return s[pos] == rule
    length = 0
    for i in range(len(graph[rule][0])):
        res = valid(s, graph[rule][0][i], pos+length)
        length += res
        if not res:
            length = 0
            break
    if length:
        return length
    for i in range(len(graph[rule][1])):
        res = valid(s, graph[rule][1][i], pos+length)
        length += res
        if not res:
            return 0
    if len(graph[rule][1]) > 0:
        return length
    return 0
bad =0
for s in b:
    bad += valid(s,0,0) == len(s)
print(bad)


        