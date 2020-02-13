from room import Room
from player import Player
from rooms_list import room

# Make a new player object that is currently in the 'outside' room.
player = Player(name = input("Please enter a name for your character..."), current_room = room['outside'])

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
print(f"\n==={player.name}, your adventure awaits! Go forth, and conquer!===\n")
print("===COMMANDS===\n n: Move North\n s: Move South\n e: Move East\n w: Move West\n q: Quit\n 'i' or 'inventory': Lists Inventory\n room: Current Room Description\n inspect: Lists items in room\n help: Help\n==============\n\n")
while True:

    if len(player.current_room.enemies) == 1:
       player.fight(player.current_room.enemies[0])
    if len(player.current_room.enemies) > 1:
        print(f"There are {len(player.current_room.enemies)} here! You're going to have to fight them all in a row!")
        for enemy in player.current_room.enemies:
            player.fight(enemy)
    
    if player.health == 0:
        print("""You've taken so much damage... everything is fading
...
...
You awaken, it seems like hours have passed, and you're back outside.
Strangely, you feel great, and you didn't lose any equipment!\n""")
        player.current_room = room['outside']
        player.health = 100

    if player.entered_new_room == True: ##Print room info when player enters new room
        print(f"\n\n==Current Location: {player.current_room.name}==\n")
        print(f"{player.current_room.description}\n")
        player.entered_new_room = False ## Stop from reprinting unless new room entered
    player_move = input("\nPlease enter a command.\n ==>")
    if len(player_move.split(' ')) == 1:

        if player_move.lower() == "q":
            break

        elif player_move.lower() == "help":
            print("Move commands: n, s, e, w. Type 'room' to get a description of your current position. Type 'inspect' to look around. Type 'q' to quit")

        elif player_move.lower() == "room":
            print(player.current_room.description)

        elif player_move.lower() in ["n", "s", "e", "w"]:
            player.movement(player_move)

        elif player_move.lower() in ["i", "inv", "inventory", "bag", "backpack"]:
            if len(player.inventory) != 0:
                [print(f"{item.name},\n") for item in player.inventory]
            else:
                print("There is nothing in your inventory!\n")

        elif player_move.lower() in ["inspect", "search", "look", "investigate"]:
            player.current_room.inspect()
        
        elif player_move.lower() in ["me", "self", "person", "myself"]:
            player.inspect_self()

    elif len(player_move.split(' ')) == 2:

        command = player_move.split(' ')[0]
        item = player_move.split(' ')[1]

        if command == 'take' or command == 'get':
            player.take_item(item)
            
        elif command == 'drop':
            player.drop_item(item)
        
        elif command in ["equip", "wear", "weild"]:
            player.equip(item)
        
        elif command in ["read", "r"]:
            read = False
            for thing in player.current_room.items:
                if item.lower() == thing.name.lower() or item.lower() == thing.shorthand.lower():
                    if hasattr(thing, "read"):
                        thing.read()
                        read = True
            for thing in player.inventory:
                if item.lower() == thing.name.lower() or item.lower() == thing.shorthand.lower():
                    if hasattr(thing, "read"):
                        thing.read()
                        read = True
            if read == False:
                print("You look for the item you want to read... it's not here!\n")
        
        elif command in ["inspect", "look", "investigate", "search"]:
            examined = False
            for thing in player.current_room.items:
                if item.lower() == thing.name.lower() or item.lower() == thing.shorthand.lower():
                    print(f"You get closer to the item. {thing.description}")
                    examined=True
            for thing in player.inventory.items:
                if item.lower() == thing.name.lower() or item.lower() == thing.shorthand.lower():
                    print(f"You get closer to the item. {thing.description}")
                    examined=True
            if examined == False:
                print("You look around for the item you want to examine... you can't find it.")
