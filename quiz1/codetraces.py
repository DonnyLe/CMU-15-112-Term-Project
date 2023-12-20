def a(x):
    print("a1", x)
    y=2
    x=x*y
    y=3
    print("a2", x, y) 
    return x + y
def b(x):
    print("b1", x)
    return x * 3
x=5
print("main", a(b(2))) 
print("main", x)
