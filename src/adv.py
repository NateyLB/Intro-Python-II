from room import Room
from player import Player
from item import Item


#Declare all items

scissors = Item("Scissors", "A pair of rusty old scissors.")
bandages = Item("Bandages", "A package of small bandages.")
sword = Item("Sword", "A finely-crafted steel sword.")
treasure_chest = Item("Treasure Chest", "A treasue chest, although it appears empty.")
shield = Item("Shield", "A small shield that fits nicely in your off hand.")
wand = Item("Wand", "An ornamented wand. You can feel it pulsing in your hand.")
health_potion = Item("Health Potion", "A vial of red liquid, drink to restore health.")
mana_potion = Item("Mana Potion", "A vial of blue liquid, drink to resstore mana.")
fire_scroll = Item("Fire Scroll", "Consume to learn fire ball.")
ice_scroll = Item("Ice Scroll", "Consume to learn ice spike.")
lightning_scroll = Item("Lightning Scroll", "Consume to learn lightning sparks.")
earthquake_scroll = Item("Earthwuake Scroll", "Consume to learn earthquake.")
xp_boost = Item("Xp Boost", "Consume to gain xp")


# Declare all the rooms
room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", [bandages, earthquake_scroll]),
                     

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", [scissors, mana_potion, fire_scroll]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", [sword, shield, health_potion]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", [mana_potion, lightning_scroll, xp_boost]),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", [ice_scroll, treasure_chest, wand, health_potion]),
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
    print("The following items are around you:")
    for x in new_player.room.items:
        print(x)
    print("\n")
    user_input = input("Enter a character to go N, S, E, W. Press q to exit: ")
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





