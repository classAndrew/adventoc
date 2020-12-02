with open("input.txt") as f:
    a = [int(x) for x in f]

def ncubed():
    for i in range(len(a)):
        for j in range(i+1, len(a)):
            for k in range(j+1, len(a)):
                if a[i] + a[j] + a[k] == 2020:
                    return a[i]*a[j]*a[k]
                    

# a = next(x*y*z for x in a for y in a for z in a if x+y+z==2020)
def nsquared():
    memes = set(a)
    for i in range(len(a)):
        for j in range(i+1, len(a)):
            y = 2020-a[i]-a[j]
            if y in memes:
                return a[i]*a[j]*y
            
from timeit import timeit
print(nsquared())
print(timeit("nsquared()", globals=locals(), number=10))