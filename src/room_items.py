from items import Item, Equipment, Armor, Weapon, Consumable, LoreItem, Book

outside_items = [
    Weapon(name="Rusted Dagger", shorthand="dagger", slot="weapon", attack=1.3, strength=1),
    Weapon(name="Iron Shortsword", shorthand="sword", slot="weapon", attack=2.0, strength=4),
    Item(name="Torch", shorthand="torch"),
    Book(name="Test Book", shorthand="book", description="An old book", content=["Hello", "Page2", "3", "4", "5"])
]

items_list_tier_one = [
    Weapon(name="Iron Shortsword", shorthand="sword", slot="weapon", attack=2.0, strength=4),
    Weapon(name="Iron Axe", shorthand="axe", slot="weapon", attack=1.0, strength=7),
    Armor(name="Iron Circlet", shorthand="circlet", slot="helmet", defense=2.0, strength=1),
    Armor(name="Cloth Tunic", shorthand="tunic", slot="chest", defense=1.2, strength=0),
    Armor(name="Iron Boots", shorthand="boots", slot="feet", defense=1.2, strength=1),
    Armor(name="Wooden Buckler", shorthand="buckler", slot="shield", defense=6, strength=-2),
    Armor(name="Leather Gloves", shorthand="gloves", slot= "hands", defense=1.5, strength=2),
    Armor(name="Bronze Wristguards", shorthand="wristguards", slot="wrists", defense=1, strength=1),
    Consumable(name="Dog Biscuits", shorthand="biscuits", effect="I could give this to a dog at some point. Who knows?"),
    LoreItem(name="Chalice", shorthand="chalice", description="An old chalice, likely used for drinking ale or wine."),
    LoreItem(name="Skull", shorthand="skull", description="A human skull, with an arrowhead still stuck in the side."),
    LoreItem(name="Giant Scale", shorthand="scale", description="An absolutely massive scale. Just touching it sends a wave of warmth through your hand and up your arm, but it doesn't burn. Looks reptilian.")
]

items_list_tier_two = [
    Weapon(name="Iron Shortsword", shorthand="sword", slot="weapon", attack=2.0, strength=4),
    Weapon(name="Iron Axe", shorthand="axe", slot="weapon", attack=1.0, strength=7),
    Armor(name="Iron Circlet", shorthand="circlet", slot="helmet", defense=2.0, strength=1),
    Armor(name="Cloth Tunic", shorthand="tunic", slot="chest", defense=1.2, strength=0),
    Armor(name="Iron Boots", shorthand="boots", slot="feet", defense=1.2, strength=1),
    Armor(name="Wooden Buckler", shorthand="buckler", slot="shield", defense=6, strength=-2),
    Armor(name="Leather Gloves", shorthand="gloves", slot= "hands", defense=1.5, strength=2),
    Armor(name="Bronze Wristguards", shorthand="wristguards", slot="wrists", defense=1, strength=1),
    Consumable(name="Dog Biscuits", shorthand="biscuits", effect="I could give this to a dog at some point. Who knows?"),
    LoreItem(name="Chalice", shorthand="chalice", description="An old chalice, likely used for drinking ale or wine."),
    LoreItem(name="Skull", shorthand="skull", description="A human skull, with an arrowhead still stuck in the side."),
    LoreItem(name="Giant Scale", shorthand="scale", description="An absolutely massive scale. Just touching it sends a wave of warmth through your hand and up your arm, but it doesn't burn. Looks reptilian.")
]

items_list_tier_three = [
    Weapon(name="Iron Shortsword", shorthand="sword", slot="weapon", attack=2.0, strength=4),
    Weapon(name="Iron Axe", shorthand="axe", slot="weapon", attack=1.0, strength=7),
    Armor(name="Iron Circlet", shorthand="circlet", slot="helmet", defense=2.0, strength=1),
    Armor(name="Cloth Tunic", shorthand="tunic", slot="chest", defense=1.2, strength=0),
    Armor(name="Iron Boots", shorthand="boots", slot="feet", defense=1.2, strength=1),
    Armor(name="Wooden Buckler", shorthand="buckler", slot="shield", defense=6, strength=-2),
    Armor(name="Leather Gloves", shorthand="gloves", slot= "hands", defense=1.5, strength=2),
    Armor(name="Bronze Wristguards", shorthand="wristguards", slot="wrists", defense=1, strength=1),
    Consumable(name="Dog Biscuits", shorthand="biscuits", effect="I could give this to a dog at some point. Who knows?"),
    LoreItem(name="Chalice", shorthand="chalice", description="An old chalice, likely used for drinking ale or wine."),
    LoreItem(name="Skull", shorthand="skull", description="A human skull, with an arrowhead still stuck in the side."),
    LoreItem(name="Giant Scale", shorthand="scale", description="An absolutely massive scale. Just touching it sends a wave of warmth through your hand and up your arm, but it doesn't burn. Looks reptilian.")
]