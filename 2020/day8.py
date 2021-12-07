with open('input.txt') as f:
    a = f.read().split('\n')

visited = set()
i = 0
acc = 0
changed = False
while i < len(a):
    opcode, operan = a[i].split(' ')
    operan = int(operan)
    if i in visited:
        print(a[i])
    visited.add(i)
    if opcode == 'acc':
        acc += operan
    if opcode == 'jmp':
        if not i+operan-1 in visited:
            i += operan-1
        else:
            a[i] = 'nop '+ str(operan)
    elif opcode == 'nop' and operan > 1:
        nxt = a[i+operan-1].split(' ')
        if i+1 in visited and a[i+int(nxt[1])-1]:
            a[i] = 'jmp '+str(operan)
            i += operan-1
    i += 1

print(acc)