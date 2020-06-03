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
new_player = Player("Nathan", room["outside"])

print(new_player.room.n_to)

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

user_input = ''
while user_input != 'q':
    print(f"{new_player.room.name}: {new_player.room.description} \n")
    user_input = input("Enter a direction to go; N, S, E, W: ")
    user_input.lower()
    if user_input == "n":
        if hasattr(new_player.room, 'n_to'):
            new_player.room = new_player.room.n_to
        else:
            print("Cannot got North, please enter another direction\n")
    elif user_input == "s":
        if hasattr(new_player.room, 's_to'):
            new_player.room = new_player.room.s_to
        else:
            print("Cannot got South, please enter another direction\n")
    elif user_input == "e":
        if hasattr(new_player.room, 'e_to'):
            new_player.room = new_player.room.e_to
        else:
            print("Cannot got East, please enter another direction \n")
    elif user_input == "w":
        if hasattr(new_player.room, 'w_to'):
            new_player.room = new_player.room.w_to
        else:
            print("Cannot got West, please enter another direction\n")
    elif user_input == "q":
        pass
    else:
        print("Please enter in a N, S, E, W, or Q")





