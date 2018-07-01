###################################################################
# animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}
# animals['d'] = ['donkey']
# animals['d'].append('dog')
# animals['d'].append('dingo')
#
# def how_many(aDict):
#     '''
#     aDict: A dictionary, where all the values are lists.
#
#     returns: int, how many values are in the dictionary.
#     '''
#     # Your Code Here
#     counter = 0
#     for w in aDict:
#         #print(w)
#         for a in aDict[w]:
#             #print(a)
#             counter += 1
#     return counter
#
# print(how_many(animals))

###################################################################




###################################################################
animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}
animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')

# >>> biggest(animals)
# 'd'

def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    # Your Code Here
    for w in aDict:
        biggest = 0
        if len(aDict[w]) > biggest:
            winningKey = w
    return winningKey

print(biggest(animals))
###################################################################
