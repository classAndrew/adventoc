with open('input.txt') as f:
    a = [int(x) for x in f.read().split('\n')]

i = 25
while i < len(a):
    good = False
    for j in range(i-25, i):
        for k in range(j+1, i):
            if a[i] == a[j]+a[k]:
                good = True
        if good:
            break
    if not good:
        print(a[i])

    i += 1