def groupByAge(L):
    ages = dict()
    for i in range(0,len(L),2 ):
        name = L[i]
        age = L[i+1]
        if age in ages:
            ages[age].add(name)
        else:
            ages[age] = set([name])

    return ages

def only112(L):
    if L == []:
        return []

    else:
        item = L[0]
        if type(item) == int and has112(item):
            return [item] + only112(L[1:])
        else:
            return only112(L[1:])
    

def only112(n):
    if(n)==0:
        return False
    else:
        partofn = n % 1000
        if n == partofn:
            return True 
        return only112(n % 1000)
