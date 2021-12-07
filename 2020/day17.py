with open('input.txt') as f:
    a = [list(x) for x in f.read().split('\n')]

from itertools import product
def p1():
    max_cycles = 15
    width = (max_cycles-1)*2+len(a)
    space = [[list('.'*(width)) for i in range(width)] for i in range(width)]

    # initialize middle slice

    mid_ind = (width)//2
    offset = max_cycles-1
    print(mid_ind, offset)
    for i in range(len(a)):
        for j in range(len(a[0])):
            space[mid_ind][offset+i][offset+j] = a[i][j]
    #print('\n'.join(str(x) for x in space[mid_ind]))
    cycle = 0
    vec = [*product([0,1,-1], repeat=3)]
    vec.remove((0,0,0))
    # print(vec)

    while cycle < 6:
        copy = [[list(y) for y in x] for x in space]
        for i in range(len(space)):
            for j in range(len(space)):
                for k in range(len(space)):
                    neighbors = 0
                    for d in vec:
                        if i+d[0] < len(space) and i+d[0] >= 0 and j + d[1] < len(space[0]) and j +d[1] >= 0 and k + d[2] < len(space[0][0]) and k + d[2] >= 0:
                            neighbors += space[i+d[0]][j+d[1]][k+d[2]] == '#'
                    if space[i][j][k] == '#':
                        if neighbors != 2 and neighbors != 3:
                            copy[i][j][k] = '.'
                    elif space[i][j][k] == '.':
                        if neighbors == 3:
                            copy[i][j][k] = '#'
                    #print(neighbors)
        space = copy
                    
        cycle += 1
    # print()
    print('\n'.join(str(x) for x in space[mid_ind-1]))
    active = 0
    for i in range(len(space)):
        for j in range(len(space[0])):
            for k in range(len(space[0][0])):
                active += space[i][j][k] == '#'
    print(active)
def p2(n):
    max_cycles = n
    width = (max_cycles-1)*2+len(a)
    space = [[[list('.'*(width)) for i in range(width)] for i in range(width)] for k in range(width)]

    # initialize middle slice

    mid_ind = (width)//2
    offset = max_cycles-1
    # print(mid_ind, offset)
    # look at this if no work
    for i in range(len(a)):
        for j in range(len(a[0])):
            space[mid_ind][mid_ind][offset+i][offset+j] = a[i][j]
    #print('\n'.join(str(x) for x in space[mid_ind]))
    cycle = 0
    vec = [*product([0,1,-1], repeat=4)]
    vec.remove((0,0,0,0))
    # print(vec)

    while cycle < 6:
        copy = [[[list(y) for y in x] for x in l] for l in space]
        for i in range(len(space)):
            for j in range(len(space)):
                for k in range(len(space)):
                    for l in range(len(space)):
                        neighbors = 0
                        for d in vec:
                            if i+d[0] < len(space) and i+d[0] >= 0 and j + d[1] < len(space[0]) and j +d[1] >= 0 and k + d[2] < len(space[0][0]) and k + d[2] >= 0 and l+d[3] >= 0 and l + d[3] < len(space):
                                neighbors += space[i+d[0]][j+d[1]][k+d[2]][l+d[3]] == '#'
                        if space[i][j][k][l] == '#':
                            if neighbors != 2 and neighbors != 3:
                                copy[i][j][k][l] = '.'
                        elif space[i][j][k][l] == '.':
                            if neighbors == 3:
                                copy[i][j][k][l] = '#'
                    #print(neighbors)
        space = copy
                    
        cycle += 1
    # print()
    # print('\n'.join(str(x) for x in space[mid_ind-1]))
    active = 0
    for i in range(len(space)):
        for j in range(len(space[0])):
            for k in range(len(space[0][0])):
                for l in range(len(space)):
                    active += space[i][j][k][l] == '#'
    print(active)
def p2_fast(a):
    pts = {(0,0,i,j): a[i][j]=='#' for i in range(len(a)) for j in range(len(a))}
    vecs = {*product([-1,0,1], repeat=4)}-{(0,0,0,0)}
    cycle = 0
    while cycle < 7:
        copy = {}
        for k in pts:
            neighbors = 0
            for d in vecs:
                # cand = tuple(sum(x) for x in zip(d, k))
                cand = (k[0]+d[0], k[1]+d[1], k[2]+d[2],k[3]+d[3])
                if not cand in pts:
                    copy[cand] = 0
                else:
                    neighbors += pts[cand]
            copy[k] = pts[k]
            if cycle != 0:
                copy[k] = neighbors==2 or neighbors == 3 if pts[k] else neighbors == 3
        pts = copy
        cycle += 1
    print(sum(pts.values()))

from timeit import timeit

print(timeit('p2_fast(a)', number=1, globals=locals()))