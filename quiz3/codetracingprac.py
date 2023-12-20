def ct2(s, L):
    i=0
    M=[]
    while (i < len(L)):
        if (not L[i].isalpha()):
                i += 1
        else:
            u, t, s = L.pop(i), s[0], s[1:] 
            if (u == t):
                M.append(i)
    return M

L = ['a', '2', 'bc', '#', 'd', '4']
s = 'abde'
print(ct2(s, L))
print('-'.join(L))
