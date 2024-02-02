ltbs = [11, 6, 3, 24, 46, 22, 7]

def merge(ltbs:list):
    if len(ltbs) > 1:
        mid = int(len(ltbs)/2) + 1
        left = ltbs[:mid]
        rigth = ltbs[mid:]
        print(left)
        print(rigth)
        merge(left)
        merge(rigth)








merge(ltbs)