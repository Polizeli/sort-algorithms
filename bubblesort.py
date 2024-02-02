from sortfuncs import swap

def bubble(slist:list):
    for i in range(len(slist)-1, 0, -1):
        for j in range(i):
            if slist[j] > slist[j+1]:
                swap(slist, j, j+1)
    return slist
