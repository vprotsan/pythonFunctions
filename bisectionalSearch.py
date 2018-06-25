# bisectional search

print("Please think of a number between 0 and 100!")
guessNum = 83
epsilon = 1
low = 0
high = 100
guess = (high + low) // 2

while guessNum:
    print("Is your secret number " + str(guess) + "?")
    userInput = raw_input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")
    if userInput == 'h':
        high = guess
    elif userInput == 'l':
        low = guess
    elif userInput == 'c':
        break
    else:
        print("Sorry, I did not understand your input.")
    guess = int((high + low) // 2)

print('Game over. Your secret number was: ' + str(guess))
