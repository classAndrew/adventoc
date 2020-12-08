with open('input.txt') as f:
    a = f.read().split('\n')


def cycle():
    i = 0
    visited = set()
    while i < len(a):
        ins = a[i].split(' ')
        opc = ins[0]
        opd = int(ins[1])
        if i in visited:
            return True
        visited.add(i)
        if opc == 'jmp':
            i += opd-1
        i += 1
    return False
i=0
while i < len(a):

    t = a[i].split(' ')

    a[i] = 'jmp '+t[1]
    a[i] = 'nop '+t[1]
    if not cycle():
        print(i)
        break
    a[i] = ' '.join(t)
    i+=1
def acc():
    i = 0
    acc = 0
    while i < len(a):
        ins = a[i].split(' ')
        opc = ins[0]
        opd = int(ins[1])
        if opc == 'jmp':
            i += opd-1
        elif opc == 'acc':
            acc += opd
        i += 1
    return acc
    
print(acc())