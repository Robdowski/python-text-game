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

    def take_item(self, item):
        taken = False
        for thing in self.current_room.items:
            if item.upper() == thing.name.upper() or item.upper() == thing.shorthand.upper():
                self.inventory.append(thing) #add item to inventory
                self.current_room.items.remove(thing) ## remove it from room
                print(f"You take the {thing.name}.\n")
                taken = True
        if taken == False:
            print("You search the room for the item you want to pick up... It doesn't look like it's here.\n")

    def drop_item(self, item):
        dropped = False
        for thing in self.inventory:
            if item.upper() == thing.name.upper() or item.upper() == thing.shorthand.upper():
                self.current_room.items.append(thing) ## add to room
                self.inventory.remove(thing) ## remove from inventory
                print(f"You've dropped {thing.name}.\n")
                dropped = True
        if dropped == False:
            print("You search your inventory for the item you want to drop... but you don't find anything.\n")

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
             

