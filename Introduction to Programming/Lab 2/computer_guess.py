from random import randint

print("Pick and remember a digit between 1 and 100.")

print("I will now attempt to guess it")

person_input = None

guesses_remaining = 20

low = 1
high = 101

while guesses_remaining != 0:
    guess = randint(low, high)
    print("My guess is {}".format(guess))

    person_input = input("Am I correct, or is my guess lower, or higher? ")
    person_input = person_input.lower()

    if person_input == "correct":
        print("I guessed it!")
        quit()
    
    elif person_input == "lower":
        low = guess
        guesses_remaining -= 1
    
    elif person_input == "higher":
        high = guess
        guesses_remaining -= 1

    else:
        print("Check your spelling")

print("I give up.")
