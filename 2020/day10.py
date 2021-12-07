with open('input.txt') as f:
    a = [int(x) for x in f.read().split('\n')]

a = sorted(a)
jolts = 0
r1 = 0
r2 = 0
b = []
for i in a:
    r1 += abs(jolts-i) == 1
    r2 += abs(jolts-i) == 3
    if abs(jolts-i) == 1:
        b.append(1)
    else:
        b.append(3)
    jolts += abs(jolts-i)
print(a)
print(b)
print(jolts, r1, r2+1, r1*(r2+1))