from sortfuncs import swap
def selection(ltbs:list):           
    n = 0                   #control number, idk how to name this variable
    while n < len(ltbs):
        mini = n            #current minimum value of the list
        for i in range(n, len(ltbs)):
            if ltbs[mini] > ltbs[i]:
                mini = i
        swap(ltbs, n , mini)
        n += 1
    return ltbs
