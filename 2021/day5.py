import numpy as np

with open("input.txt") as f:
    data = f.read().split('\n')
    # rise, run, p1
    lines = []
    for x in data:
        a, b = x.split(' -> ')
        p1, p2 = [*map(int, a.split(','))], [*map(int, b.split(','))]
        lines.append([np.array(p1), np.array(p2)])

def intersect(p1, p2, p3, p4):
    if p2[1] != p1[1] and p2[0] != p1[0]: return -1
    if p4[1] != p3[1] and p4[0] != p3[0]: return -1
    rhs = p3-p1
    lhs = np.array([(p2-p1),-(p4-p3)]).T
    try:
        t1, t2 = np.linalg.solve(lhs, rhs)
        print("good", p1, p2, p3, p4, t1)
        return t1
    except:
        print("singular", p1, p2, p3, p4)
        return -1

cnt = 0
for i in range(len(lines)):
    for j in range(i+1, len(lines)):
        cnt += 0 <= intersect(*lines[i], *lines[j]) <= 1

# intersect(np.array([1,1]), np.array([2.72,2.29]), np.array([1.05, 2.13]), np.array([2.718, 1.77]))
print(cnt)