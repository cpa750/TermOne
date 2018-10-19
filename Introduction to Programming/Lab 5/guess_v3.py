from random import randint

def ask_number(question, low, high, step=1):
    # Asks for a number within a range
    response = None

    while response not in range(low, high, step):
        try:
            response = int(input(question))
        except ValueError:
            print("Integers only!")

    return response

def main():

    choice = randint(1, 101)
    attempts_remaining = 5

    print("A random number between 1 and 100 has been chosen. Try to guess it...")

    question = "What is your guess? >> "

    print(ask_number(question, choice, choice+1))

if __name__ == "__main__":
    main()
