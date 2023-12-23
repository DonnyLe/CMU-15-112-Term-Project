def ct2(m):
    x = 1
    while x < 5:
        x += 2
        print('x = ', x)
    for y in range(m, m+2):
        print('y = ', y)
        x += y
    return x

print(3+ct2(2))