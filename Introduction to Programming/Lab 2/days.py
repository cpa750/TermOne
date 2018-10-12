days = {"monday": "Shopping day", "tuesday": "Lecture for data analysis", "wednesday": "Programming lab",
        "thursday": "Essential skills lecture", "friday": "Data analysis lab", "saturday": "Laundry day",
        "sunday": "Free all day"}

user_input = input("Day: ").lower()

while user_input != "holiday":
    if user_input in days:
        print(user_input.capitalize(), days[user_input], sep=": ")

    else:
        print("Check your spelling.")

    user_input = input("Day: ").lower()

print("Hooray!")
