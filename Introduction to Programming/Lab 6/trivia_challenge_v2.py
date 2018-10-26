import pickle, shelve

import trivia_challenge

questions = trivia_challenge.read_questions()
points = trivia_challenge.main(questions)

with shelve.open("winners", flag='c') as shelf:
    if len(shelf) < 5:
        name = input("君の名前は？")
        shelf[name] = points
    else:
        minimum = 24243523452345
        for key in shelf:
            if shelf[key] < minimum:
                minimum = shelf[key]
                key_to_be_deleted = key
                # Cannot simply del minimum as this deletes the copy that is made, not the actual value.

        if points > minimum:
            name = input("君の名前は？")
            shelf[name] = points
            print("Deleting minimum: ", minimum)
            del shelf[key_to_be_deleted]

    shelf.sync()

    print("Top Scorers:")
    print("Name:\tPoints:\n")

    for key in shelf:
        print(key, shelf[key], sep="\t")
