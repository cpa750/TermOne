from random_word import RandomWords

def asteriskify(char_list, string):
    asterisks = []

    asterisks = list(string)
    asterisks = ["*"]*len(string)
    for char in char_list:
        for i in range(len(string)):
            if string[i] == char:
                asterisks[i] = char

    asterisks = "".join(asterisks)
    return asterisks

RAND_WORD = RandomWords().get_random_word()
char_list = []

word_points = 10*len(RAND_WORD)
points = 0

def main():

    print(
        """
        Welcome to my game. I have chosen a word at random.\n
        It is your job to guess it. You have ten chances to guess letters in the word.\n
        """
    )
    
    for i in range(10):
        guess = input("What is your guess? >> ")
        char_list.append(guess)
        print("The word is: ", asteriskify(char_list, RAND_WORD))

    print("Now you must try and guess the word.")    
    guess = input("What is your guess? >> ").lower()
    guesses = 5
    while guesses > 1 and guess != RAND_WORD:
        guesses -= 1
        print("That is not correct! You have {} guesses remaining.".format(guesses))
        guess = input("What is your guess? >> ")

    if guess == RAND_WORD:
        print("Congratulations! You guessed it!")
        points += 100
        points += word_points
        points -= guesses*2
    else:
        print("Better luck next time!")
        print("The word was {}".format(RAND_WORD))

if __name__ == "__main__":
    play_again = "y"
    while play_again == "y":
        main()
        play_again = input("Play again? (y/n) >> ").lower()
    
    print("Your total points are: ", points)
