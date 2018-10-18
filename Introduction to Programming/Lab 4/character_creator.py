class Character():
    # TODO: add getters and setters for self.attributes

    def __init__(self):
        self.points = 50
        self.attributes = {"Strength": 0, "Perception": 0, "Endurance": 0, "Charisma": 0,
                           "Intelligence": 0, "Agility": 0, "Luck": 0}
        self.name = None
    
    def set_name(self, new_name):
        self.name = new_name
        self.__name__ = self.name

    def add_points(self, attribute, amount):
        self.attributes[attribute] += amount
        self.points -= amount

    def remove_points(self, attribute, amount):
        self.attributes[attribute] -= amount
        self.points += amount

    def display(self):
        print("Character name:\t\t{}".format(self.name))
        for attribute in self.attributes:
            if attribute != "Luck":
                print(attribute, self.attributes[attribute], sep=":\t\t")
            else:
                print(attribute, self.attributes[attribute], sep=":\t\t\t")

        print("\nRemaining points: {}".format(self.points))


def show_help():
    print("""
          List of commands:\n
          help: Shows this message
          add: Walkthrough adding points to an attribute
          remove: Walkthrough removing points from an attribute
          rename: Rename your character
          character: Displays information about your character
          exit: Exits the tool

          Character attributes are:
          Strength, Perception, Endurance, Charisma, Intelligence,
          Agility, and Luck
          """)

def get_attribute_to_modify(character, user_input):
    if user_input.capitalize() in character.attributes.keys():
        return user_input.capitalize()
    else:
        return None

def main():
    character = Character()

    print("""Welcome to the character creator!\n
          To see a list of commands, type 'help'.""")

    print("""
          First we will set a name for the character.\n
          This can always be done using the 'rename' command.
          """)
    
    character.set_name(input("What would you like the name of your Character to be? >> "))\

    next_action = "help"
    while next_action != "exit":
        if next_action == "help":
            show_help()
        elif next_action == "add":
            user_input = input("Which attribute would you like to add points to? >> ").lower()
            attribute_to_modify = get_attribute_to_modify(character, user_input)

            if attribute_to_modify is not None:
                try:
                    points_to_add = int(input("How many points would you like to add? >> "))
                except:
                    print("Integers only!")
                    points_to_add = 0

                if character.points - points_to_add >= 0:
                    character.add_points(attribute_to_modify, points_to_add)
                else:
                    print("Not enough points!")
            else:
                print("Not a valid attribute!")
        
        elif next_action == "remove":
            user_input = input("Which attribute would you like to remove points from? >> ")
            attribute_to_modify = get_attribute_to_modify(character, user_input)

            if attribute_to_modify is not None:
                try:
                    points_to_remove = int(input("How many points would you like to remove? >> "))
                except:
                    print("Integers only!")
                    points_to_remove = 0

                if character.attributes[attribute_to_modify] - points_to_remove >= 0:
                    character.remove_points(attribute_to_modify, points_to_remove)
                else:
                    print("Attribute does not have enough points!")
            else:
                print("Not a valid attribute!")
        
        elif next_action == "rename":
            new_name = input("What would you like the new name to be? >> ").capitalize()
            character.set_name(new_name)

        elif next_action == "character":
            character.display()

        else:
            print("Not a valid command!")

        next_action = input("What is your next action? >> ").lower()


if __name__ == "__main__":
    main()
