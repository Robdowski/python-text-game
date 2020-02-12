from room import Room
from player import Player
from room_items import outside_items
# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance", 'outside',
                     "North of you, the cave mount beckons", items= outside_items),

    'foyer':    Room("Foyer", 'foyer', """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", 'overlook', """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", 'narrow', """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", 'treasure', """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

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
print("===COMMANDS===\n n: Move North\n s: Move South\n e: Move East\n w: Move West\n q: Quit\n 'i' or 'inventory': Lists Inventory\n room: Current Room Description\n help: Help\n==============\n\n")
while True:
    print(f"\n\n==Current Location: {player.current_room.name}==\n")
    print(f"{player.current_room.description}\n")
    player_move = input("Please enter a command.\n ==>")
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
            else:
                print("\n\nThere isn't a way to go that direction!\n")
        elif player_move == "s":
            if player.current_room.s_to != '':
                player.current_room = player.current_room.s_to
            else:
                print("\n\nThere isn't a way to go that direction!\n")
        elif player_move == "e":
            if player.current_room.e_to != '':
                player.current_room = player.current_room.e_to
            else:
                print("\n\nThere isn't a way to go that direction!\n")
        elif player_move == "w":
            if player.current_room.w_to != '':
                player.current_room = player.current_room.w_to
            else:
                print("\n\nThere isn't a way to go that direction!\n")
        elif player_move == "i" or player_move == "inventory":
            if len(player.inventory) != 0:
                [print(f"{item.name},\n") for item in player.inventory]
            else:
                print("There is nothing in your inventory!\n")

    elif len(player_move.split(' ')) == 2:
        command = player_move.split(' ')[0]
        item = player_move.split(' ')[1]
        if command == 'take' or command == 'get':
            taken = False
            for thing in player.current_room.items:
                if item.upper() == thing.name.upper() or item.upper() == thing.shorthand.upper():
                    player.inventory.append(thing) #add item to inventory
                    player.current_room.items.remove(thing) ## remove it from player[current_room]
                    print(f"You take the {thing.name}.\n")
                    taken = True
            if taken == False:
                print("You search the room for the item you want to pick up... It doesn't look like it's here.\n")
        
        elif command == 'drop':
            dropped = False
            for thing in player.inventory:
                if item.upper() == thing.name.upper() or item.upper() == thing.shorthand.upper():
                    player.current_room.items.append(thing) ## add to room and remove from inventory
                    player.inventory.remove(thing)
                    print(f"You've dropped {thing.name}.\n")
                    dropped = True
            if dropped == False:
                print("You search your inventory for the item you want to drop... but you don't find anything.\n")
