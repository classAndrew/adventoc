with open('input.txt') as f:
    a = f.read().split('\n\n')

t = 0
for g in a:
    m = g.split('\n')
    b = set(m[0])
    for k in m[1:]:
        b &= set(k)
    t += len(b)
print(t)
