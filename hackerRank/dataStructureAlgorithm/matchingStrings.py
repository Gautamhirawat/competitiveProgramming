def matchingStrings(stringList, queries):
    res = []
    for x in queries:
        p = 0
        for y in stringList:
            if x == y:
                p += 1
            else:
                pass
        res.append(p)
    return res



print(matchingStrings(["aba","baba","aba","xzxb"],["aba","xzxb","ab"]))