class Item():
    def __init__(self, name, shorthand):
        self.name = name
        self.shorthand = shorthand
    def __str__(self):
        f"Item: {self.name}\n"

class Equipment(Item):
    def __init__(self, name, shorthand, slot):
        super().__init__(name, shorthand)
        self.slot = slot
    def __str__(self):
        f"Item: {self.name}\nSlot: {self.slot}\n"

class Armor(Equipment):
    def __init__(self, name, shorthand, slot, defense, strength):
        super().__init__(name, shorthand, slot)
        self.defense = defense
        self.strength = strength
    def __str__(self):
        f"Item: {self.name}\nSlot: {self.slot}\nDefense: {self.defense}\nStrength: {self.strength}\n"

class Weapon(Equipment):
    def __init__(self, name, shorthand, slot, attack, strength):
        super().__init__(name, shorthand, slot)
        self.attack = attack
        self.strength = strength
    def __str__(self):
        f"Item: {self.name}\nSlot: {self.slot}\nAttack: {self.attack}\nStrength: {self.strength}\n"

class Consumable(Item):
    def __init__(self, name, shorthand, effect):
        super().__init__(name, shorthand)
        self.effect = effect
    def __str__(self):
        f"Item: {self.name}\nEffect: {self.effect}\n"

class LoreItem(Item):
    def __init__(self, name, shorthand, description):
        super().__init__(name, shorthand)
        self.description = description
    def __str__(self):
        f"{self.description}. I'm not sure whether it'll be useful later..."

class Book(Item):
    def __init__(self, name, shorthand, description, content = []):
        super().__init__(name, shorthand)
        self.description = description
        self.content = content
    
    def read(self):
        print(self.content[0])
        page = 0
        while True:
            move = input("Press 'n' for next page, 'p' for previous, 'q' to quit.")
            if move == "q":
                break
            elif move == "n":
                if page < len(self.content)-1:
                    page += 1
                    print(self.content[page] + "\n")
                else:
                    print("That looks like the last page of the book...")
            elif move == "p":
                if page > 0:
                    page -= 1
                    print(self.content[page] + "\n")
                else:
                    print("You are on the first page already!\n")
                    continue
            else:
                print("I did not understand that command. Enter 'p', 'n', or 'q'!")
                continue