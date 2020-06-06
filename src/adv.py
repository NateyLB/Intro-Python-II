from room import Room
from player import Player
from item import Item, LightSource



#Declare all items

item = {
"scissors": Item("Scissors", "A pair of rusty old scissors."),
"bandages": Item("Bandages", "A package of small bandages."),
"sword": Item("Sword", "A finely-crafted steel sword."),
"treasure_chest": Item("Treasure Chest", "A treasue chest, although it appears empty."),
"shield": Item("Shield", "A small shield that fits nicely in your off hand."),
"wand": Item("Wand", "An ornamented wand. You can feel it pulsing in your hand."),
"health_potion": Item("Health Potion", "A vial of red liquid, drink to restore health."),
"mana_potion": Item("Mana Potion", "A vial of blue liquid, drink to resstore mana."),
"fire_scroll": Item("Fire Scroll", "Consume to learn fire ball."),
"ice_scroll": Item("Ice Scroll", "Consume to learn ice spike."),
"lightning_scroll": Item("Lightning Scroll", "Consume to learn lightning sparks."),
"earthquake_scroll": Item("Earthquake Scroll", "Consume to learn earthquake."),
"xp_boost": Item("Xp Boost", "Consume to gain xp."),
"lamp": LightSource("Lamp", "A lamp that will light the way."),
}

# Declare all the rooms
room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", [item['bandages'], item['earthquake_scroll']], True),                   

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", [item['scissors'], item['mana_potion'], item['fire_scroll'], item['lamp']], True),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", [item['sword'], item['shield'], item['health_potion']], True),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", [item['mana_potion'], item['lightning_scroll'], item['xp_boost']], False),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", [item['ice_scroll'], item['treasure_chest'], item['wand'], item['health_potion']], False),
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

user_input = ['','']
while user_input[0] != 'q':
    if any(isinstance(item, LightSource) for item in new_player.room.items) or any(isinstance(item, LightSource) for item in new_player.items) or new_player.room.is_light == True:
        print(f"You are at the {new_player.room.name}:\n {new_player.room.description} \n")
        print("The following items are around you:")
        for x in new_player.room.items:
            print(x)
        print("\n")
    else:
        print("It's pitch black!\n")
    user_input = input("""Enter a character to go N, S, E, W. Enter get or take followed by a comma and the item name (get, item) to pick up an item
      Enter i or inventory to view inventory and q to exit: """).split(',')
    if len(user_input) == 1:
        user_input[0]= user_input[0].lower()
        if user_input[0] == "n":
            if hasattr(new_player.room, 'n_to'):
                new_player.room = new_player.room.n_to
            else:
                print("Cannot got North, please enter another direction\n")
        elif user_input[0] == "s":
            if hasattr(new_player.room, 's_to'):
                new_player.room = new_player.room.s_to
            else:
                print("Cannot got South, please enter another direction\n")
        elif user_input[0] == "e":
            if hasattr(new_player.room, 'e_to'):
                new_player.room = new_player.room.e_to
            else:
                print("Cannot got East, please enter another direction\n")
        elif user_input[0] == "w":
            if hasattr(new_player.room, 'w_to'):
                new_player.room = new_player.room.w_to
            else:
                print("Cannot got West, please enter another direction\n")
        elif user_input[0] == "i" or user_input[0] == "inventory":
            print("Inventory:")
            for x in new_player.items:
                print(x)
            print("\n")
        elif user_input[0] == "q":
            pass
        else:
            print("Please enter in a N, S, E, W, or Q")
    else:
        user_input[0] = user_input[0].strip().lower()
        user_input[1] = user_input[1].strip().title()
        if user_input[0] == 'q':
            pass
        elif user_input[0] == 'get' or user_input[0] == 'take':
            if any(isinstance(item, LightSource) for item in new_player.room.items) or any(isinstance(item, LightSource) for item in new_player.items) or new_player.room.is_light == True:
                item_match = [x for x in new_player.room.items if x.name == user_input[1]]
                if len(item_match)>0:
                    new_player.grab_item(item_match[0])
                    new_player.room.items.remove(item_match[0])
                    item_match[0].on_take()
                else:
                    print("There is no item by that name.")
            else:
                print("Good luck finding that in the dark...")

        elif user_input[0] == 'drop':
            if len(new_player.items) == 0:
                print("Player has no items to drop.")
            else:
                item_match = [x for x in new_player.items if x.name == user_input[1]]
                if len(item_match)>0:
                    new_player.drop_item(item_match[0])
                    new_player.room.items.append(item_match[0])
                    item_match[0].on_drop()
                else:
                    print("There is no item by that name")
        else:
            print("Please take, get, or drop an item.")

print(room['outside'])





