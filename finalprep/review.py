def largestCheeTank(L):
    rows, cols = len(L), len(L[0])
    currBestArea = 0

    for startR in range(rows):
        for startC in range(cols):

            for endR in range(startR + 1, rows +1):
                for endC in range(startC + 1, cols +1):
                    if isCheeTank(L, startR, startC, endR, endC):
                        area = (endR - startR)*(endC - startC)
                        if area > currBestArea:
                            currBestArea = area 

def isCheeTank(L, startR, startC, endR, endC):
    for r in range(startR,endR):
        for c in range(startC, endC):
            if not (L[r][c] == "o" or L[r][c] == ">>(owo)<<"):
                return False
    return True 