def gcdRecur(a, b):
    '''
    a, b: positive integers

    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Your code here
    if b == 0:
       print(a)
    else:
       return gcdRecur(b, a % b)


gcdRecur(1071,462)
gcdRecur(84, 144)
gcdRecur(380, 456)
gcdRecur(120, 36)
gcdRecur(276, 180)
gcdRecur(24, 50)
gcdRecur(20, 36)
gcdRecur(396, 72)
gcdRecur(77, 84)
