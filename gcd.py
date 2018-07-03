def gcd(a, b):
    """
    a, b: two positive integers
    Returns the greatest common divisor of a and b
    """
    #YOUR CODE HERE
    #greatest common divisor of two positive integers
    #one of them is not zero
    if b == 0:
       print(a)
    else:
       return gcd(b, a % b)
