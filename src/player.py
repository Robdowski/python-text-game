# Write a class to hold player information, e.g. what room they are in
# currently.
class Player():
    def __init__(self, name, current_room, health=100, inventory = [], equipment = {}, entered_new_room=True):
        self.name = name
        self.current_room = current_room
        self.health = health
        self.inventory = inventory
        self.equipment = equipment
        self.entered_new_room = entered_new_room

    def movement(self, command):
        new_room = self.current_room.__getattribute__(f"{command}"+"_to")
        if new_room:
            self.current_room = new_room
            self.entered_new_room = True
        else:
            print("You cannot go that way! Are you blind?")

    def equip(self, item):
        for thing in self.inventory:
            if item in [thing.shorthand, thing.name]:
                if hasattr(self.equipment, thing.slot):
                    choice = input(f"You already have a {thing.slot} equipped. Do you want to replace it? y / n\n==>")
                    if choice == "y":
                        self.inventory.append(self.equipment.pop(f"{thing.slot}"))
                        self.equipment[thing.name] = thing
                        self.inventory.remove(thing)
                        print(f"Item {thing.name} has been equipped!\n")

                    elif choice == "n":
                        print("Nothing was equipped.\n")

                    else:
                        print("I did not understand that command. Valid choices are 'y' / 'n' \n Try equipping again.\n")

                else:
                    self.equipment[thing.name] = thing
                    self.inventory.remove(thing)
                    print(f"Item {thing.name} has been equipped!\n")

    def inspect_self(self):
       print(f"""Name: {self.name}
Health: {self.health}
Location: {self.current_room.name}
       """)
             

