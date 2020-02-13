from random import choice
from room_items import items_list_tier_one, items_list_tier_two, items_list_tier_three
class Monster():
    def __init__(self, name, description, health, attack, defense, tier):
        self.name = name
        self.description = description
        self.health = health
        self.attack = attack
        self.defense = defense
        self.tier = tier

    def attack_player(self, player):
        attack_damage = self.attack - player.get_defense()

        if attack_damage < 0:
            attack_damage = 0

        player.health -= attack_damage

        print(f"The {self.name} did {attack_damage} damage to your health!")

        return player.health
    
    def on_death(self, player):
        if self.tier == 1:
            item_drop = choice(items_list_tier_one)
            player.current_room.items.append(item_drop)
            print(f"The {self.name} dropped {item_drop}!")

        if self.tier == 2:
            item_drop = choice(items_list_tier_two)
            player.current_room.items.append(item_drop)
            print(f"The {self.name} dropped {item_drop}!")

        if self.tier == 3:
            item_drop = choice(items_list_tier_three)
            player.current_room.items.append(item_drop)
            print(f"The {self.name} dropped {item_drop}!")
