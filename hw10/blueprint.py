def getPairSum(L, target):
    s = set(L)
    for c in s:
        difference = target - c
        if (difference in s and difference is not c):
            return (difference, c)
    return None

print(getPairSum([10, -1, 1, -8, 3, 1, 8, 19, -9, 5], 10))

def friendsOfFriends(friends):
    friendsOfFriends = dict()
    for person, personFriendsSet in friends.items():
        for friend in personFriendsSet:
            for friendOfFriend in friends[friend]:
                print(friendOfFriend)
                if (friendOfFriend != person 
                    and friendOfFriend not in personFriendsSet):
                    if(person in friendsOfFriends):
                        friendsOfFriends[person].add(friendOfFriend)
                    else:
                        friendsOfFriends[person] = {friendOfFriend}
    for person in friends.keys():
        if person not in friendsOfFriends:
            friendsOfFriends[person] = set()

    return friendsOfFriends
d = dict()
d["fred"] = set(["wilma", "betty", "barney", "bam-bam"])
d["wilma"] = set(["fred", "betty", "dino"])
d["betty"] = d["barney"] = d["bam-bam"] = d["dino"] = set()

print(friendsOfFriends(d))