def f(x): 
    return 3 * x - 2

def g(x): 
    return f(x + 3)

def ct1(x):
    print(f(x - 2))
    x -= 2
    print(g(x))
    x %= 4
    return f(g(x) % 6) // 2

print(3 + ct1(4))