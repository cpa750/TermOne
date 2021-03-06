def ask_number(question, low, high, step=1):
    # Asks for a number within a range
    response = None

    while response not in range(low, high, step):
        try:
            response = int(input(question))
        except ValueError:
            print("Integers only!")

    print(response)
    return response

ask_number("What is the number >> ", 0, 10, 2)
