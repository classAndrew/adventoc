with open("input.txt") as f:
    data = f.read().split('\n')

aim = 0
horiz = 0
depth = 0
for x in data:
    a, b = x.split(' ')
    if a == "forward":
        horiz += int(b)
        depth += aim*int(b)
    elif a == "up":
        aim -= int(b)
    else:
        aim += int(b)
    
print(horiz*depth)