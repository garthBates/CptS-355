def histo(inputS):
    d = {}
    for c in inputS:
        if c in d.keys():
            d[c] += 1
        else:
            d[c] = 1
    return d


def histo(inputS):
    d= {}
    for c in inputS:
        d[c] = d.get(c,0) + 1
    return sorted(d.items()), key = lambda itme: item[1], reverse = True

import copy
def SumDict(d1, d2):
    myD = copy.deepcopy(d1)
    for key, value in list(d2.items()):
        myD[key] = myD.get(key, 0) + value
    return myD


#def sumSales(data):



    
