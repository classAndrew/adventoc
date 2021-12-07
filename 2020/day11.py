with open('input.txt') as f:
    a = [list(l) for l in f.read().split('\n')]


def neighbors(i, j):
    vecs = [[-1,-1],[-1,0],[-1,1],[0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
    c = 0
    for v in vecs:
        if i+v[0] >= 0 and j + v[1] >= 0 and i +v[0] < len(a) and j+v[1] < len(a[0]):
            c += a[i+v[0]][j+v[1]] == '#'
    return c

while True:
    copy = [list(l) for l in a]
    for i in range(len(a)):
        for j in range(len(a[0])):
            if a[i][j] == '.': continue
            if not neighbors(i, j):
                copy[i][j] = '#'
            if neighbors(i, j) >= 4:
                copy[i][j] = 'L'
    if a == copy:
        break
    a = copy
cnt = 0
for s in a:
    cnt += s.count('#')
print(cnt)
    

