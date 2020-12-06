with open('input.txt') as f:
    a = f.read().split('\n')

s = []
for i in a:
    b = i[-3:].replace('L','0').replace('R','1')
    i = i[:-3]
    n = int(i.replace('F', '0').replace('B', '1'),2)
    s.append(n*8+int(b,2))
s = sorted(s)
for i in range(len(s)):
    if (s[i]-s[i-1] > 1):
        print(i)
        print(s[i], s[i-1])
