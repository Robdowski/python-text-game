from items import Item, Equipment, Armor, Weapon, Consumable, LoreItem, Book

### STARTER ITEMS
dagger = Weapon(name="Rusted Dagger", shorthand="dagger", slot="weapon", attack=10, strength=1, description="An old, rusty dagger.")
torch = Item(name="Torch", shorthand="torch", description="It's a torch. It looks like it hasn't been used for a while, but there's still oil on it.")
book = Book(name="Test Book", shorthand="book", description="An old, dusty book.", content=["Hello", "Page2", "3", "4", "5"])

outside_items = [dagger, book, torch]


## TIER ONE ITEMS (EASY TO GET)
sword = Weapon(name="Iron Shortsword", shorthand="sword", slot="weapon", attack=2.0, strength=4, description="An iron shortsword.")
axe = Weapon(name="Iron Axe", shorthand="axe", slot="weapon", attack=1.0, strength=7)
circlet = Armor(name="Iron Circlet", shorthand="circlet", slot="helmet", defense=2.0, strength=1)
tunic = Armor(name="Cloth Tunic", shorthand="tunic", slot="chest", defense=1.2, strength=0)
boots = Armor(name="Iron Boots", shorthand="boots", slot="feet", defense=1.2, strength=1)
buckler = Armor(name="Wooden Buckler", shorthand="buckler", slot="shield", defense=6, strength=-2)
gloves = Armor(name="Leather Gloves", shorthand="gloves", slot= "hands", defense=1.5, strength=2)
wristguards = Armor(name="Bronze Wristguards", shorthand="wristguards", slot="wrists", defense=1, strength=1)
biscuits = Consumable(name="Dog Biscuits", shorthand="biscuits", effect="I could give this to a dog at some point. Who knows?")
chalice = LoreItem(name="Chalice", shorthand="chalice", description="An old chalice, likely used for drinking ale or wine.")
skull = LoreItem(name="Skull", shorthand="skull", description="A human skull, with an arrowhead still stuck in the side.")
scale = LoreItem(name="Giant Scale", shorthand="scale", description="An absolutely massive scale. Just touching it sends a wave of warmth through your hand and up your arm, but it doesn't burn. Looks reptilian.")

items_list_tier_one = [sword, axe, circlet, tunic, boots, buckler, gloves, wristguards, biscuits, chalice, skull, scale]
items_list_tier_two = []
items_list_tier_three = []