from sortfuncs import masterlist
from time import time
from bubblesort import bubble
from onebyone import onebyone

tsf = 0
tbf = 0
tof = 0

for i in range(10):
    testlist:list = masterlist(10000)

    si = time()
    sortlist:list = testlist
    sortlist.sort()
    sf = time() - si

    bi = time()
    bubblelist:list = testlist
    bubblelist = bubble(bubblelist)
    bf = time() - bi

    oi = time()
    onebyonelist:list = testlist
    onebyonelist = onebyone(onebyonelist)
    of = time() - oi
    tsf += sf
    tbf += bf
    tof += of

print(tsf)
print(tbf)
print(tof)