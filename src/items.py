class Item():
    def __init__(self, name):
        self.name = name
    def __str__(self):
        f"Item: {self.name}\n"

class Equipment(Item):
    def __init__(self, name, slot):
        super().__init__(self, name)
        self.slot = slot
    def __str__(self):
        f"Item: {self.name}\nSlot: {self.slot}\n"

class Armor(Equipment):
    def __init__(self, name, slot, defense, strength):
        super().__init__(self, name, slot)
        self.defense = defense
        self.strength = strength
    def __str__(self):
        f"Item: {self.name}\nSlot: {self.slot}\nDefense: {self.defense}\nStrength: {self.strength}\n"

class Weapon(Equipment):
    def __init__(self, name, slot, attack, strength):
        super().__init__(self, name, slot)
        self.attack = attack
        self.strength = strength
    def __str__(self):
        f"Item: {self.name}\nSlot: {self.slot}\nAttack: {self.attack}\nStrength: {self.strength}\n"

class Consumable(Item):
    def __init__(self, name, effect):
        super().__init__(self, name)
        self.effect = effect
    def __str__(self):
        f"Item: {self.name}\nEffect: {self.effect}\n"
        