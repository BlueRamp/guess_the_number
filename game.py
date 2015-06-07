__author__ = 'oleg'

import random

guessesNumber = 0

print('Hi! What is your name?')
name = input()

number = random.randint(1, 20)
print('Okay, I am thinking about a number, ' + name + '. What is that number?')

while guessesNumber < 6:
    print('Make a guess')
    guess = input()
    guess = int(guess)

    guessesNumber = guessesNumber + 1

    if guess > number:
        print('It is too high')
    if guess < number:
        print('It is too low')
    if guess == number:
        print('You get it! This is ' + str(number))
        break

if guess == number:
    print('You won the game')
else:
    print('You lose')

if guessesNumber == 1:
    print("You made " + str(guessesNumber) + " attempt")
else:
    print("You made " + str(guessesNumber) + " attempts")
