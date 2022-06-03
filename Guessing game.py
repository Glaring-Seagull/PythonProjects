# This is a guess the number game.
import random
secretNumber = random.randint(1, 20)
print('I am thinking of a number between 1 and 20.')
guessesTaken = 0
# Ask the player to guess up 6 times. Throw an exption error if input isn't a whole number.
while guessesTaken < 6:
    try:
        print('Take a guess.')
        guess = int(input())
        guessesTaken = guessesTaken + 1
        if guess < secretNumber:
            print('Your guess is too low.')
        elif guess > secretNumber:
            print('Your guess is too high.')
        else: break
    except ValueError: print('Thats not a number!')

    

if guess == secretNumber:
    print('Good job! You guessed my number in ' + str(guessesTaken) + ' guesses!')
else:
    print('Nope. The number I was thinking of was ' + str(secretNumber))
