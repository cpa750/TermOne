from random import choice, randrange
WORDS = {"python": "Name of a programming language", "jumble": "Name of the game",
         "computer": "Something used to process information", "player": "The one who plays"}

word = choice(list(WORDS.keys()))
correct = word

jumbled_word = ""

guesses = 5
hinted = False

while word:
    position = randrange(len(word))
    jumbled_word += word[position]
    word = word[:position] + word[(position+1):]

print("""Welcome to the word guessing game!\n
         I've chosen a word at random, try your best to guess!\n
         This is the jumble: """, jumbled_word, sep="")

guess = input("What is your guess? (Press enter to quit) >> ")

while guess != correct and guess != "" and guesses > 0:
    if guess != "hint":
        guesses -= 1
        print("Sorry, that's incorrect.\n You have {} guesses remaining.".format(guesses))
        guess = input("What is your guess? >> ")
    else:
        print(WORDS[correct])
        hinted = True
        guess = input("What is your guess? >> ")

if guess == correct and hinted == False:
    print("Congratulations! You guessed without getting a hint!")
elif guess == correct and hinted == True:
    print("You solved it with a hint!")

input("Thanks for playing, press enter to exit.")
