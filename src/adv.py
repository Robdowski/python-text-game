from room import Room
from player import Player
from rooms_list import room
# Declare all the rooms



# Link rooms together


#
# Main
#

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
print(f"\n\n==Current Location: {player.current_room.name}==\n")
print(f"{player.current_room.description}\n")
description_needed = False # initially set to false
while True:
    if description_needed == True:
        print(f"\n\n==Current Location: {player.current_room.name}==\n")
        print(f"{player.current_room.description}\n")
        description_needed = False ## Room will not keep reprinting until another room is entered and this is turned back true
    player_move = input("\nPlease enter a command.\n ==>")
    if len(player_move.split(' ')) == 1:
        if player_move == "q":
            break
        elif player_move == "help":
            print("Move commands: n, s, e, w. Type 'room' to get a description of your current position. Type 'q' to quit")
        elif player_move == "room":
            print(player.current_room.description)
        elif player_move == "n":
            if player.current_room.n_to != '':
                player.current_room = player.current_room.n_to
                description_needed = True # Set to true so that the description will print upon entering room
            else:
                print("\n\nThere isn't a way to go that direction!\n")
        elif player_move == "s":
            if player.current_room.s_to != '':
                player.current_room = player.current_room.s_to
                description_needed = True # Set to true so that the description will print upon entering room
            else:
                print("\n\nThere isn't a way to go that direction!\n")
        elif player_move == "e":
            if player.current_room.e_to != '':
                player.current_room = player.current_room.e_to
                description_needed = True # Set to true so that the description will print upon entering room
            else:
                print("\n\nThere isn't a way to go that direction!\n")
        elif player_move == "w":
            if player.current_room.w_to != '':
                player.current_room = player.current_room.w_to
                description_needed = True # Set to true so that the description will print upon entering room
            else:
                print("\n\nThere isn't a way to go that direction!\n")
        elif player_move == "i" or player_move == "inventory":
            if len(player.inventory) != 0:
                [print(f"{item.name},\n") for item in player.inventory]
            else:
                print("There is nothing in your inventory!\n")
        elif player_move == "inspect":
            player.current_room.inspect()
            if player.current_room.items:
                for item in player.current_room.items:
                    print(item.name)

    elif len(player_move.split(' ')) == 2:
        command = player_move.split(' ')[0]
        item = player_move.split(' ')[1]
        if command == 'take' or command == 'get':
            taken = False
            for thing in player.current_room.items:
                if item.upper() == thing.name.upper() or item.upper() == thing.shorthand.upper():
                    player.inventory.append(thing) #add item to inventory
                    player.current_room.items.remove(thing) ## remove it from room
                    print(f"You take the {thing.name}.\n")
                    taken = True
            if taken == False:
                print("You search the room for the item you want to pick up... It doesn't look like it's here.\n")
        
        elif command == 'drop':
            dropped = False
            for thing in player.inventory:
                if item.upper() == thing.name.upper() or item.upper() == thing.shorthand.upper():
                    player.current_room.items.append(thing) ## add to room
                    player.inventory.remove(thing) ## remove from inventory
                    print(f"You've dropped {thing.name}.\n")
                    dropped = True
            if dropped == False:
                print("You search your inventory for the item you want to drop... but you don't find anything.\n")
