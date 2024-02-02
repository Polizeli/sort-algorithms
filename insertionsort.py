def insertion(ltbs:list):
    for i in range(0, len(ltbs)-1):
        n = i + 1
        if ltbs[i] > ltbs[n]:
            for j in range(i, -1, -1):
                if ltbs[n] < ltbs[j]:
                    tempIND = j         #temp index of the number to be change
                else:
                    break
            tempVALUE = ltbs[n]         #place holder of the number to be change
            ltbs.pop(n)
            ltbs.insert(tempIND, tempVALUE)
    return ltbs
