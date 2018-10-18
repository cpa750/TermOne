from sys import exit
people_dict = {"Cian": "Chris", "Jack": "John", "Alex": "Bill",
               "Chris": "Joe", "John": "George", "Bill": "Fred",
               "Joe": "Peter", "George": "William", "Fred": "Kevin"}

get_father_or_grandfather = input("Get father or grandfather? >> ").lower()

if get_father_or_grandfather == "father":
    user_input = input("Enter name of child >> ").capitalize()
    try:
        print(people_dict[user_input])
    except KeyError:
        print("Child does not exist.")

elif get_father_or_grandfather == "grandfather":
    user_input = input("Enter name of child >> ").capitalize()

    try:
        father = people_dict[user_input]
    except KeyError:
        print("Child does not exist.")
        exit(0)
    
    try:
        print(people_dict[father])
    except KeyError:
        print("There are no records dating that far back.")

else:
    print("Invalid chocie")
