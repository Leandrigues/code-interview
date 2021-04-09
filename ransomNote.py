# HackerRank
def checkMagazine(magazine, note):
    mDict = createDict(magazine)
    nDict = createDict(note)

    for key, value in nDict.items():
        if key not in mDict:
            print("No")
            return
        elif nDict[key] > mDict[key]:
            print("No")
            return
        else:
            mDict[key] -= nDict[key]

    print("Yes")
    return