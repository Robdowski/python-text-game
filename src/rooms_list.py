from room_items import outside_items, items_list_tier_one
from room import Room
from random import choices
from enemy_list import bat

room = {
    'outside':  Room(
                    name="Outside Cave Entrance",
                    shorthand= 'outside',
                    description="\nNorth of you, the cave mount beckons",
                    inspect_message_items="""\nYou take a look around.
It looks like the only way to go is north, into the cave.
As you look into the maw of blackness, 
you realize that you'll need some source of light.
You see a torch laying next to the entrance,
as well as a satchel.
Upon further inspection, the satchel contains a rusty, old dagger.\n""",
                    inspect_message_looted="""\nYou've taken everything you can from here. 
You step closer to the cave. 
As you come closer to the entrance, your neck hair stands straight on its ends. 
Something isn't quite right here, but you aren't sure what...\n""",
                    items= outside_items
                    ),

    'foyer':    Room(
                    name="Foyer",
                    shorthand= 'foyer',
                    description= """\nDim light filters in from the south.
Dusty passages run north and east.""",
                    inspect_message_items="""\nThe room is so dark that even with the torch,
you can barely make anything out.  
After rifling through a pile of dusty books,
you do manage to find some things,""",
                    inspect_message_looted="""\nAfter clearing the room of anything useful,
you now realize this place has not
been inhabited for some time. Still yet,
you can't shake the feeling you're being watched.""",
                    items = choices(items_list_tier_one, k=2)
                    ),

    'overlook': Room(
                    name="Grand Overlook",
                    shorthand= 'overlook',
                    description= """\nA steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.\n""",
                    inspect_message_items="""\ns""",
                    inspect_message_looted="""\ns""",
                    items= []
                    ),

    'narrow':   Room(
                    name="Narrow Passage",
                    shorthand= 'narrow',
                    description= """The narrow passage bends here from west
to north. The smell of gold permeates the air.""",
                    inspect_message_items= """asd""",
                    inspect_message_looted= """asd""",
                    items = []
                    ),

    'treasure': Room(
                    name="Treasure Chamber",
                    shorthand= 'treasure',
                    description= """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""",
                    inspect_message_items= """asd""",
                    inspect_message_looted= """asd""",
                    items=[],
                    enemies=[bat]
                    ),
}

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']