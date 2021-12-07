from collections import Counter

with open('input.txt') as f:
    a = f.read().split('\n')

def p1():
    valid = 0
    for s in a:
        pos = s.find(":")
        char = s[pos-1]
        b1, b2 = s[:pos-2].split("-")
        b1 = int(b1)
        b2 = int(b2)
        cnt = Counter(s[pos+2:])
        valid += b1 <= cnt[char] <= b2
    print(valid)

def p2():
    valid = 0
    for s in a:
        pos = s.find(":")
        char = s[pos-1]
        b1, b2 = s[:pos-2].split("-")
        b1 = int(b1)
        b2 = int(b2)
        s = s[pos+2:]
        valid += (s[b1-1] == char) ^ (s[b2-1] == char)
    print(valid)

p1()
p2()
