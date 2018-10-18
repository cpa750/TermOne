from random_word import RandomWords

rand_word = RandomWords()

wordlist = []

for i in range(10):
    word = rand_word.get_random_word()
    wordlist.append(word)

for element in wordlist:
    print(element)

