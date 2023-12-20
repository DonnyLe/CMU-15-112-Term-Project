def shuffleCols(L,n):
    # 1. find new cols
    netShift = n% len(L[0])
    newColList = []
    for colIcx in range(len(L[0])):
        newCol = (colIcx + netShift) % len(L[0])
        newColList.append(newCol)

    # 3. move elems from old position to new position 
    result = [[0] * len(L[0]) for row in L]
    for colIdx in range(len(L[0])):
        for rowIdx in range(len(L)):
            newColIdx = newColList[colIdx]
            result[rowIdx][newColIdx] = L[rowIdx][colIdx]
    

def findExcludedStudents(names, numbers):
    res = set()
    d = dict()
    for i in range(len(names)):
        if numbers[i] not in d:
            d[numbers[i]] = {names[i]}
        else:
            d[numbers[i]].add(names[i])
    
    for i in range(len(names)):
        findGroup = False
        for j in range(len(names)):
            if i == j:
                continue
            diff = 10 - numbers[i] - numbers[j]
            if diff in d:
                repeat = 0
                if names[i] in d[diff]: repeat +=1
                if names[j] in diff: repeat += 1
                if len(d[diff])>repeat:
                    findGroup = True
        if not findGroup:
            res.add(names[i])
    return res
                
            