# note: probably don't need data of insides. just need edges
with open('input.txt') as f:
    a = f.read().split('\n\n')
    tiles = {}
    for e in a:
        tmp = e.split('\n')
        tiles[int(tmp[0][tmp[0].find(' ')+1:-1])] = tmp[1:]
# edge to id
edges = {}
# id to edge
edge_dat = {k:[]}
for t in tiles:
    data = tiles[t]
    if not data[0] in edges:
        edges[data[0]] = []

    if not data[-1] in edges:
        edges[data[-1]] = []
    left = ''.join(data[i][0] for i in range(10))
    if not left in edges:
        edges[left] = []
    right = ''.join(data[i][-1] for i in range(10))
    if not right in edges:
        edges[right] = []
    edges[data[0]].append(t)
    edges[data[-1]].append(t)
    edges[left].append(t)
    edges[right].append(t)
# print(edges)
graph = {k:[0,0,0,0] for k in tiles}
def solve(tile_id):
    for k in tiles:
        for orient in range(4):
            if graph[tile_id][orient]:
                continue


