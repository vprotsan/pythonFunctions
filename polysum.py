import math

def polysum(n,s):
    '''
    n: integer, number of sides
    s: length of one side

    returns: sum of area of polygon and square of the perimeter rounded to 4 decimal places
    '''
    area = (0.25* n * s**2) / math.tan(math.pi / n)
    perimeter = (n * s)**2
    sum = round(area + perimeter, 4)
    return sum
