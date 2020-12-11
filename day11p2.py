with open('input.txt') as f:
    a = [list(l) for l in f.read().split('\n')]


def neighbors(i, j):
    vecs = [[-1,-1],[-1,0],[-1,1],[0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
    c = 0
    for v in vecs:
        if i+v[0] >= 0 and j + v[1] >= 0 and i +v[0] < len(a) and j+v[1] < len(a[0]):
            c += a[i+v[0]][j+v[1]] == '#'
    return c

def visible(i, j):
    ci = i
    cj = j
    vis = 0
    #up
    ci = i-1
    while ci >= 0:
        if a[ci][cj] == 'L': 
            break
        if a[ci][cj] == '#':
            vis += 1
            break
        ci -= 1
    #down
    ci = i+1
    while ci < len(a):
        if a[ci][cj] == 'L': 
            break
        if a[ci][cj] == '#':
            vis += 1
            break
        ci += 1
    #ne
    ci = i-1
    cj = j+1
    while ci >= 0 and cj < len(a[0]):
        if a[ci][cj] == 'L':
            break
        if a[ci][cj] == '#':
            vis += 1
            break
        ci -= 1
        cj += 1
    
    ci = i-1
    cj = j-1
    #nw
    while ci >= 0 and cj >= 0:
        if a[ci][cj] == 'L': 
            break
        if a[ci][cj] == '#':
            vis += 1
            break
        ci -= 1
        cj -= 1
    
    #right
    ci = i
    cj = j+1
    while cj < len(a[0]):
        if a[ci][cj] == 'L': 
            break
        if a[ci][cj] == '#':
            vis += 1
            break
        cj += 1
    
    #left
    ci = i
    cj = j-1
    while cj >= 0:
        if a[ci][cj] == 'L':
            break
        if a[ci][cj] == '#':
            vis += 1
            break
        cj -= 1

    #sw
    ci = i +1
    cj = j-1
    while ci < len(a) and cj >= 0:
        if a[ci][cj] == 'L': 
            break
        if a[ci][cj] == '#':
            vis += 1
            break
        cj -= 1
        ci += 1
    # se
    ci = i+1
    cj = j+1
    while ci <len(a) and cj < len(a[0]):
        if a[ci][cj] == 'L': 
            break
        if a[ci][cj] == '#':
            vis += 1
            break
        ci += 1
        cj += 1
    return vis
    
while True:
    copy = [list(l) for l in a]
    for i in range(len(a)):
        for j in range(len(a[0])):
            if a[i][j] == '.': continue
            if not visible(i, j):
                copy[i][j] = '#'
            if visible(i, j) >= 5:
                copy[i][j] = 'L'
    if a == copy:
        break
    a = copy
cnt = 0
for s in a:
    cnt += s.count('#')

print(cnt)
# print('\n'.join(''.join(x) for x in a))

    

