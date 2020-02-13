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

    def attack(self, target):
        attack_power = 0
        strength = 0
        for item in self.equipment.items():
            if item[0] == "attack":
                attack_power += item[1]
            if item[0] == "strength":
                strength += item[1]
        total_power = attack_power + (strength * 0.9)

        target.health - (total_power - target.defense)

        return target.health

    def get_defense(self):
        defense = 0
        for item in self.equipment.items():
            if item[0] == "defense":
                defense += item[1]
        return defense

    def fight(self, monster):
        print("There's a monster here, no running away now!\n")
        while True:
            if self.health == 0:
                break
            if monster.health == 0:
                monster.on_death()
                break
            
            print(f"Player Health: {self.health}\nMonster Health: {monster.health}")
            move = input("Press 'a' to attack. Press 'c' to use consumable." )

            if move.lower() == 'a':
                monster_health_start = monster.health
                self.attack(monster)
                damage = monster_health_start - monster.health
                print(f"You attack the {monster.name}. The attack did {damage} damage! It has {monster.health} left.\n")

                input("The monster looks like it's going to attack, press 'any key' to defend!")
      
                monster.attack_player(self)

             

