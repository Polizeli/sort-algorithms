from random import randint

def swap(slist:list, m:int, n:int):
    slist[m], slist[n] = slist[n], slist[m]

def mandM(mMlist:list):
    mnv = mMlist[0]
    mxv = mMlist[0]
    mnvindex = 0
    mxvindex = 0

    for j in range(len(mMlist)):
        n = mMlist[j]
        if n <= mnv:
            mnv = n
            mnvindex = j
        elif n >= mxv:
            mxv = n
            mxvindex = j

    infolist = [mnv, mxv, mnvindex, mxvindex]

    return infolist

def masterlist(n):
    biglist = []
    for i in range(0, n):
        a = randint(-1000, 1000)
        biglist.append(a)
    return biglist

def posmasterlist(n):
    biglist = []
    for i in range(0, n):
        a = randint(0, 1000)
        biglist.append(a)
    return biglist