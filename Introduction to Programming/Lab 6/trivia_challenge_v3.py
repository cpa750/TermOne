import pickle, shelve

import trivia_challenge

questions = trivia_challenge.read_questions()
points = trivia_challenge.main(questions)

with open("winners_text.txt", "r+") as file:
    if file.read() != "":
        winners = {}
        for line in file:
            if line != "":
                key = line.split()[0]
                winners[key] = line.split("#")[1]

        minimum = 12341234234 # TODO: Change this to a non-arbritrary value
        for key in winners:
            if winners[key] < minimum:
                minimum = winners[key]
                key_to_be_deleted = key
        
        if points > minimum:
            del winners[key_to_be_deleted]
            name = input("君の名前は？")
            winners[name] = points

        for key in winners:
            file.write("{}#{}".format(key, winners[key]))

        print("Top Scorers:")
        print("Name:\tPoints:\n")

        for key in winners:
            print(key, winners[key], sep="\t")
