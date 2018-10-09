from random import randint

choice = randint(1, 101)
attempts_remaining = 5

print("A random number between 1 and 100 has been chosen. Try to guess it...")

while attempts_remaining != 0:
    guess = int(input("What is your guess? "))

    if guess == choice:
        print("Correct!")
        attempts_remaining = 0

    else:
        attempts_remaining -= 1
        print("Guesses remaining: {}".format(attempts_remaining))
