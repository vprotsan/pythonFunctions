# bisectional search with reccursion
def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string

    returns: True if char is in aStr; False otherwise
    '''
    # Your code here
    if aStr == '':
        return False

    newStr = aStr
    guess = int(len(aStr) // 2)

    if type(aStr) is str:
        v = aStr.lower()
        y = v.replace(" ", "")
        newStr = sorted(y)

    if newStr[guess] == char:
        return True
    elif len(newStr) == 1:
        return False
    elif newStr[guess] > char:
        return isIn(char, aStr[0:guess])
    elif newStr[guess] < char:
        return isIn(char, aStr[guess:])


isIn('a', '')
isIn('u', 'ff')
isIn('m', 'mq')
isIn('q', 'mmz')
isIn('j', 'afgimmqtuwxz') 
isIn('d', 'addefgkmpprswwxy')
isIn('a', 'cdffijmnopqrttuwxxzz')
isIn('x', 'bginx')
isIn('u', 'jknpruvwwx')
isIn('s', 'efsw')
isIn('u', 'jknpruvwwx')
