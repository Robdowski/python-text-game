from room import Room
from player import Player
# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
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
print("===COMMANDS===\n n: Move North\n s: Move South\n e: Move East\n w: Move West\n q: Quit\n room: Current Room Description\n help: Help\n==============\n\n")
while True:
    print(f"\n\n==Current Location: {player.current_room.name}==\n")
    print(f"{player.current_room.description}\n")
    player_move = input("Please enter a command.\n ==>")
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
            print("There isn't a way to go that direction!\n")
    elif player_move == "s":
        if player.current_room.s_to != '':
            player.current_room = player.current_room.s_to
        else:
            print("There isn't a way to go that direction!\n")
    elif player_move == "e":
        if player.current_room.e_to != '':
            player.current_room = player.current_room.e_to
        else:
            print("There isn't a way to go that direction!\n")
    elif player_move == "w":
        if player.current_room.w_to != '':
            player.current_room = player.current_room.w_to
        else:
            print("There isn't a way to go that direction!\n")
