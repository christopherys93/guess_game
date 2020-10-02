import random

print('Hello, what is your name?')
name = input()
randomNumber = random.randint(1, 10)
print('Hello, ' + name + ', I am thinking of a number between 1-10. Can you guess?')

for guessesTaken in range(1, 4):
    print('Take a guess.')
    guess = int(input())
    if guess < randomNumber:
        print('Your guess is too low.')
    elif guess > randomNumber:
        print('Your guess is too high.')
    else:
        break

if guess == randomNumber:
    print('Good job, ' + name + ', you guessed the number in ' + str(guessesTaken) + ' guesses.')
else:
    print('Nope, the number was ' + str(randomNumber) + '.')
    print('You took ' + str(guessesTaken) + ' guesses.')

