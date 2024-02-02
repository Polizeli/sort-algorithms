def onebyone(listofnumbers:list):
    sortedlist = []  
    for i in listofnumbers:
        for j in range(0, len(listofnumbers)):
            if len(sortedlist) == 0:
                sortedlist.append(i)
                break

            else:
                if i <= sortedlist[j]:
                    sortedlist.insert(j, i)
                    break

                if i > sortedlist[-1]:
                    sortedlist.append(i)
                    break
          
    return sortedlist
