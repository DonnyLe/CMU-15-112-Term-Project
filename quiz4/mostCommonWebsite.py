def mostCommonWebsite(L):
    d = dict()
    for site in L:
        d[site] = d.get(site, 0) + 1

    s = set()
    max = 0
    maxname = ''
    for name, num in d.items():
        if num >= max:
            s.add(name)
            max = num 
            maxname = name 

    if not s:
        return maxname
    return s

L = ["cs.cmu.edu/~112", "agar.io", "cs.cmu.edu/~112", "google.com", "agar.io"]
print(mostCommonWebsite(L))

def findTriplets(L):

    res = set()
    L = set(L)
    
    for num1 in L:
        for num2 in L:
            difference = 0 - num1 - num2
            if (difference in L 
                and difference != num1
                and difference != num2
                ):
                res.add(tuple(sorted((num1, num2, difference))))
    return res


print(findTriplets([-1, 0, -3, 2, 1]))
        
        