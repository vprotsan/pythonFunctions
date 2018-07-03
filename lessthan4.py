def lessThan4(aList):
    '''
    aList: a list of strings
    '''
    newList = []
    for i in aList:
        if len(i) < 4:
            newList.append(i)
    return newList



aList = ["apple", "cat", "dog", "banana"]
#lessThan4(aList)
lessThan4(['vu', 'EskT', 'L', '', 'AnAzxNTVKW', 'ocUulxHGmj'])
lessThan4(['i', 'HmoJ', 'we', 'bSzwDr', 'hniB', 'V', 'StpArvb', 'dTeR'])
