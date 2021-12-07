# with open("input.txt") as f:
#     data = f.read().split('\n')

# cnt = 0
# for i in range(1, len(data)):
#     cnt += int(data[i]) > int(data[i-1])

# print(cnt)

with open("input.txt") as f:
    data = [*map(int, f.read().split('\n'))]

data2 = []
for i in range(len(data)-2):
    data2.append(sum(data[i:i+3]))

print(data2, len(data))

cnt = 0
for i in range(1, len(data2)):
    cnt += data2[i] > data2[i-1]

print(cnt)