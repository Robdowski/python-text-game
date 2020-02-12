# Write a class to hold player information, e.g. what room they are in
# currently.
class Player():
    def __init__(self, name, current_room, inventory = [], equipment = {}):
        self.name = name
        self.current_room = current_room
        self.inventory = inventory
        self.equipment = equipment
    def __str__(self):
        f"\n===Player===\nName: {self.name}\nLocation: {self.current_room}\nInventory: {self.inventory}\n"

    def equip(self, item):
        if self.equipment[f"{item.slot}"]:
            choice = input(f"You already have a {item.slot} equipped. Do you want to replace it? y / n\n==>")
            if choice == "y":
                self.inventory.append(self.equipment.pop(f"{item.slot}"))
                self.equipment.update(item)
                self.inventory.remove(item)
                print(f"Item {item.name} has been equipped!\n")

            elif choice == "n":
                print("Nothing was equipped.\n")

            else:
                print("I did not understand that command. Valid choices are 'y' / 'n' \n Try equipping again.\n")

        else:
            self.equipment.update(item)
            self.inventory.remove(item)
            print(f"Item {item.name} has been equipped!\n")

