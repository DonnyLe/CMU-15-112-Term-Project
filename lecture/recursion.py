def listSum(L, result = 0):
    if L == []:
        return result
    else:
        result += L[0]
        return listSum(L[1:], result)

print([1,2,3])
        #listSum([2,3], 1)
            #listSum([3],3)
                #listSum([], 6)