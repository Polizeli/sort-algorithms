from sortfuncs import posmasterlist, mandM, swap

sortlist:list = posmasterlist(5)
mandMlist:list = mandM(sortlist)
mnv = mandMlist[0]
mxv = mandMlist[1]
mnvindex = mandMlist[2]
mxvindex = mandMlist[3]
print(mnv ,sortlist, mxv)
swap(sortlist, 0, mnvindex)
swap(sortlist, -1, mxvindex)
print(mnv ,sortlist, mxv)



for i in range(1, len(sortlist)-1):
    if (sortlist[i] - mnv) < (mxv - sortlist[i]):
        for j in range(len(sortlist)-1):
            if (sortlist[i] <= sortlist[j]) and (i != j):
                swap(sortlist, i, j)
                break
    else:
        for k in range(len(sortlist)-1, 0, -1):
            if (sortlist[i] >= sortlist[k]) and (i != k):
                swap(sortlist, i, k)
                break


