def merge(ltbs):
    if len(ltbs) > 1:
        mid = len(ltbs)//2
        left = ltbs[:mid]
        rigth = ltbs[mid:]

        merge(left)
        merge(rigth)

        i = j = k = 0

        while i < len(left) and j < len(rigth):
            if left[i] <= rigth[j]:
                ltbs[k] = left[i]
                i+=1
            else:
                ltbs[k] = rigth[j]
                j+=1
            k +=1
        
        while i < len(left):
            ltbs[k] = left[i]
            i += 1
            k += j
        
        while j < len(rigth):
            ltbs[k] = rigth[j]
            j += 1
            k += 1
    
    return ltbs
