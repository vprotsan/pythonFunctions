def closest_power(base, num):
    '''
    base: base of the exponential, integer > 1
    num: number you want to be closest to, integer > 0
    Find the integer exponent such that base**exponent is closest to num.
    Note that the base**exponent may be either greater or smaller than num.
    In case of a tie, return the smaller value.
    Returns the exponent.
    '''
    res = 0
    if base > num:
        res = 0
    elif base == num:
        res = 1
    else:
        for i in range(1, int(num)):
            if abs(base**i - num) <= abs(base**(i + 1) - num):
                print(abs(base**i - num))
                print(abs(base**(i + 1) - num))
                res = i
                break
    return res



closest_power(3,12) #returns 2
closest_power(4,12) #returns 2
closest_power(4,1) #returns 0
