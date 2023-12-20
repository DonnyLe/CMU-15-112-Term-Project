def f(x): return x+5
def g(x): return f(x-3)
def h(x): return g(g(x)%f(x))
def bonusCt1(f, g, x):
    if (x > 0):
       return bonusCt1(g, h, -f(x))
    else:
       return f(g(h(x)))
print(bonusCt1(g, f, 4))