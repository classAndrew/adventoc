
start = [15,5,1,4,7,0]
cache =  {start[i]:i+1 for i in range(len(start))}

num = 0
i = 6
b = 0
while i < 2021:
    b = num
    if num in cache:
        diff = i-cache[num]
        cache[num] = i
        num = diff
    else:
        cache[num] = i
        num = 0
    i += 1
print(b)