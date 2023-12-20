def countVals(L):
    result = dict()
    #count how many times a number appeares in the list L.count(num)
    for num in L:
        freq = L.count(num)
        result[freq] = result.get(freq, set()).union({num})
    return result

def findFactors(s,n):
    res = set()
    for factor in s:
        if n % factor == 0:
            res.add(factor)
    return res

def qualifyingPlayers(s, scoreToBeat):
    board = dict()
    for line in s.splitlines():
        info = line.split()
        name = info[0]
        score = int(info[1])
        if name not in board:
            board[name] = 0
        board[name] += score
    result = set()
    for player in board:
        if board[player] > scoreToBeat:
            result.add(player)

    return result

def makeFriendCounts(d):
    res = dict()
    for person in d:
        for friend in d[person]:
            res[friend] = res.get(friend, 0) + 1

    return res

def mostPopularFriend(d):
    friendCounts = makeFriendCounts(d)
    bestCount = 0
    bestFriend = None

    for (name, count) in friendCounts.items():
        count = friendCounts[name]
        if(bestFriend == None or count > bestCount):
            bestCount = count
            bestFriend = name
    return bestFriend



        

