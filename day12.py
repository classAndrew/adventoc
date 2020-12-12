from math import cos, sin, pi, atan2
with open('input.txt') as f:
    a = f.read().split('\n')

vecs = [[1, 0], [0,1], [-1,0],[0,-1]]
def p1_vec():
    x = 0
    y = 0
    d = 0
    for s in a:
        cmd = s[0]
        mag = int(s[1:])
        m = {'L' : 1, 'R': -1}
        if cmd in m:
            d = (d+m[cmd]*(mag//90))%4
            if d < 0:
                d += 4
            continue
        m = {'F': d, 'E': 0, 'N': 1, 'W': 2, 'S': 3}
        x+=vecs[m[cmd]][0]*mag
        y+=vecs[m[cmd]][1]*mag
    return abs(x)+abs(y)


def p2():
    x = 0
    y = 0
    wayx = 10
    wayy = 1
    for s in a:
        cmd = s[0]
        mag = int(s[1:])
        m = {'L' : 1, 'R': -1}
        if cmd in m:
            r = (wayx**2+wayy**2)**.5
            ang = atan2(wayy, wayx)+m[cmd]*pi/2*(mag//90)
            wayx = r*cos(ang)
            wayy = r*sin(ang)
            continue
        m = {'E': 0, 'N': 1, 'W': 2, 'S': 3}
        if cmd in m:
            wayx+=vecs[m[cmd]][0]*mag
            wayy+=vecs[m[cmd]][1]*mag
            continue
        x+=mag*wayx
        y+=mag*wayy
    return abs(x)+abs(y)
    
print(p2())
    