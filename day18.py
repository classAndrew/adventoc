
# WHY DID THIS WORK LOL. Cheesed it with dunder override
class N:
    def __init__(self, num):
        self.num = num
    def __sub__(self, other):
        return N(self.num*other.num)
    def __add__(self, other):
        return N(self.num+other.num)
class M:
    def __init__(self, num):
        self.num = num
    def __add__(self, other):
        return M(self.num*other.num)
    def __mul__(self, other):
        return M(self.num+other.num)

with open('input.txt') as f:
    inp = f.read().split('\n')
def p1():
    vals = 0
    for expr in inp:
        tokens = []
        i = 0
        while i < len(expr):
            if expr[i].isdigit():
                buf = []
                while i < len(expr) and expr[i].isdigit():
                    buf.append(expr[i])
                    i += 1
                tokens.append('N('+''.join(buf)+')')
                continue
            tokens.append(expr[i])
            i += 1
        expr = ''.join(tokens)
        expr = expr.replace('*','-')
        # print(expr)
        vals += eval(expr).num
    print(vals)

def p2():
    vals = 0
    for expr in inp:

        expr = expr.replace('*', 'p')
        expr = expr.replace('+', '*')
        expr = expr.replace('p', '+')
        tokens = []
        i = 0
        while i < len(expr):
            if expr[i].isdigit():
                buf = []
                while i < len(expr) and expr[i].isdigit():
                    buf.append(expr[i])
                    i += 1
                tokens.append('M('+''.join(buf)+')')
                continue
            tokens.append(expr[i])
            i += 1

        expr = ''.join(tokens)
        # expr = expr.replace('*','-')

        vals += eval(expr).num
    print(vals)
p2()
p1()