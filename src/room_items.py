from items import Item, Equipment, Armor, Weapon, Consumable, LoreItem, Uncarriable

outside_items = [
    Weapon(name="Rusted Dagger", shorthand="dagger", slot="Weapon", attack=1.2, strength=1),
    Item(name="Torch", shorthand="torch")
]

items_list_tier_one = [
    Weapon(name="Iron Shortsword", shorthand="sword", slot="Weapon", attack=2.0, strength=4),
    Weapon(name="Iron Axe", shorthand="axe", slot="Weapon", attack=1.0, strength=7),
    Armor(name="Iron Circlet", shorthand="circlet", slot="Helmet", defense=2.0, strength=1),
    Armor(name="Cloth Tunic", shorthand="tunic", slot="Chest", defense=1.2, strength=0),
    Armor(name="Iron Boots", shorthand="boots", slot="Feet", defense=1.2, strength=1),
    Armor(name="Wooden Buckler", shorthand="buckler", slot="Shield", defense=6, strength=-2),
    Armor(name="Leather Gloves", shorthand="gloves", slot= "Hands", defense=1.5, strength=2),
    Armor(name="Bronze Wristguards", shorthand="wristguards", slot="Wrists", defense=1, strength=1),
    Consumable(name="Dog Biscuits", shorthand="biscuits", effect="I could give this to a dog at some point. Who knows?"),
    LoreItem(name="Chalice", shorthand="chalice", description="An old chalice, likely used for drinking ale or wine."),
    LoreItem(name="Skull", shorthand="skull", description="A human skull, with an arrowhead still stuck in the side."),
    Uncarriable(name="Giant Scale", shorthand="scale", description="An absolutely massive scale. Just touching it sends a wave of warmth through your hand and up your arm, but it doesn't burn. Looks reptilian.")
]

items_list_tier_two = [
    
]

items_list_tier_three = [
    
]