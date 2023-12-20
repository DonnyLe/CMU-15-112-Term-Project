




def p(a, b):
    return (abs(a - b) + abs(b - a)) if (a != b) else a*b

def q(a, b, c):
    if (a > b):
        return p(a, b+c)
    a += b
    if (a > c):
        return p(a+b, c)
    else:
        c %= b
        return p(a+c, b)

def ct2(a, b, c):
    print(q(a, b, c))
    print(q(b, c, a))
    print(q(c, a, b))

ct2(3, 5, 2) # hint: prints 3 total lines