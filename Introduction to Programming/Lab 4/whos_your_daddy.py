people_dict = {"Cian": "Chris", "Jack": "John", "Alex": "Bill"}

user_input = input("Name of son >> ").capitalize()

try:
    print(people_dict[user_input])
except:
    print("Child does not")
