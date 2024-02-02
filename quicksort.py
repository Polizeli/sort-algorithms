def quick(ltbs:list, inicio=0, fim=None):
    if fim==None:
        fim = len(ltbs)-1
    if inicio < fim:
        p = partion(ltbs, inicio, fim)
        quick(ltbs, inicio, p-1)
        quick(ltbs, p+1, fim)

def partion(slist:list, inicio, fim):
    pivot = slist[fim]
    i = inicio
    for j in range(inicio, fim):
        if slist[j] <=pivot:
            slist[j], slist[i] = slist[i], slist[j]
            i+=1
    slist[i], slist[fim] = slist[fim], slist[i]
    return i
