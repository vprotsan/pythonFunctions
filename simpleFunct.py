##################################################################
#count number of vowels
count = 0
for x in s:
    if x == 'a' or x == 'e' or x == 'i' or x == 'o' or x == 'u':
        count += 1

print("Number of vowels: " + str(count))
##################################################################



##################################################################
# Find number of occurances
import re
strToFind = 'bob'
s = 'azcbobobegghakl'
count = len(re.findall(r'(?=bob)', s))
print(count)
print("Number of times " + str(strToFind)+ " occurs is: " + str(count))
##################################################################



##################################################################
s = 'azcbobobegghakl'
count = 0
substring = ''
while count < len(s):
    if count == 0:
        substring = s[0]
    else:

    count +=1
newArray = s.split('')
print(newArray)
##################################################################



##################################################################
long = ""
max = ""

for i in range(len(s) - 1):
    if(s[i] <= s[i + 1] ):
       long = long + s[i]
       if(i == len(s) - 2):
           long = long + s[i + 1]
    else:
        long += s[i]
        if(len(long) > len(max)):
            max = long
        long = ""

if(len(s) == 1):
    long = s

if(len(long) > len(max)):
    print("Longest substring in alphabetical order is: " + long)
else:
    print("Longest substring in alphabetical order is: " + max)
##################################################################


##################################################################
x = 23
epsilon = 0.01
step = 0.1
guess = 0.0

while abs(guess**2-x) >= epsilon:
    if guess <= x:
        guess += step
    else:
        break

if abs(guess**2 - x) >= epsilon:
    print('failed')
else:
    print('succeeded: ' + str(guess))
##################################################################
