def read_questions():
    questions = []
    with open("questions2.txt", "r") as f:
        lines = f.readlines()

        for line in lines:
            question, answer, points = line.split("#")
            tup = (question, answer, points)
            
            questions.append(tup)
        return questions

def main(questions):
    points = 0

    input("Welcome to my Python IO trivia game! To start, press enter.")

    for tup in questions:
        print(tup[0])
        guess = input("Answer? >> ")
        if guess == tup[1]:
            print("Correct!")
            points += int(tup[2])
        else:
            print("Sorry, that is not correct.")

    print("You earned a total of {} points.".format(points))
    return points

if __name__ == "__main__":
    main(read_questions())
