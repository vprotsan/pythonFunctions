def uniqueValues(aDict):
    '''
    aDict: a dictionary
    '''
    uniqVal = []
    for key,val in aDict.items():
        allVal = list(aDict.values())
        if allVal.count(val) == 1:
                 uniqVal.append(key)
    print(sorted(uniqVal))
    return sorted(uniqVal)



#uniqueValues({1: 1, 2: 2, 3: 3}) #[1, 2, 3]
#uniqueValues({1: 1, 2: 1, 3: 1}) #[]
#uniqueValues({1: 1}) #[1]
#uniqueValues({1: 1, 2: 1, 3: 3}) #[3]
uniqueValues({2: 0, 3: 3, 6: 1}) #[2, 3, 6]
uniqueValues({1: 1, 3: 2, 6: 0, 7: 0, 8: 4, 10: 0}) #[1, 3, 8]
