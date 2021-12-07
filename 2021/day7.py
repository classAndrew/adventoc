import statistics
with open("input.txt") as f:
    data = [int(x) for x in f.read().split(',')]

def p1(data):
    data = list(data)
    m = statistics.median(data)
    return sum(abs(x-m) for x in data)

def p2(data):
    data = list(data)
    m = sum(data)//len(data)
    # bruteforce
    # return min(range(min(data), max(data)+1), key=lambda m: sum(abs(x-m)*(abs(x-m)+1)/2 for x in data))
    return sum(abs(x-m)*(abs(x-m)+1)/2 for x in data)

print(p1(data))
print(p2(data))