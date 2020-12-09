with open('input.txt') as f:
    a = [int(x) for x in f.read().split('\n')]

target = 32321523
def unoptimized():

    i = 0
    for i in range(len(a)):
        for j in range(i+1, len(a)):
            if sum(a[i:j]) == target:
                print(min(a[i:j]), max(a[i:j]))
                break

