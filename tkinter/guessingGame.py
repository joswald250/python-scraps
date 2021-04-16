#guess the number game
import random
import getpass

def guessingGame():
    username = getpass.getuser()
    randomNum = random.randint(1,100)
    print('{}, I am thinking of a number, guess away! (you have 5 guesses)'.format(username))

    for guessNum in range(5):
        try:
            guess = int(input("Whaddaya think?"))
        except ValueError:
            print('Please enter a number value, not text.')

        try:
            if guess == randomNum:
                break
            elif guess > randomNum:
                print('Too high!')
            else:
                print('Too low!')
        except NameError:
            print('Name Error.')

    if int(guessNum) > 4 and guess != randomNum:
        print(f'{username}, it took you {guessNum + 1} guesses to get it right.')
    else:
        print(f'{username}, you took: {guessNum + 1} guesses. I was thinking of {randomNum}.')
