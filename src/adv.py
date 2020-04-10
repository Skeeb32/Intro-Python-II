from room import Room
from player import Player
from item import Item

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
# Initialize items
#

item = {
'sword': Item("Sword", "You have access to strength." ),
'shield': Item("Sheild", "You have access to defense." ),
'potion': Item("Potion", "You have access to health." )
}

#
# Add item to room
#
room['outside'].addItem(item['sword'])

#
# Main
#
readyPlayerOne = input("What is your name? :: ")
# Make a new player object that is currently in the 'outside' room.
readyPlayerOne = Player(room["outside"])
# Write a loop that:
# while True:
#     print("##################################################################")
# * Prints the current room name
print(f"Current Location: {readyPlayerOne.current_room.name}")
# * Prints the current description (the textwrap module might be useful here).

print(f"Adventure Time! ")

def get_room_access(player):
    print(player.current_room)
    direction_choice = input("Which direction would you like to go? ([n] North, [s] South, [e] East, [w] West or [q] for Quit)      ").lower().strip()
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
    if direction_choice == "n":
        player.go_north()
        get_room_access(player)

    if direction_choice == "s":
        player.go_south()
        get_room_access(player)

    if direction_choice == "e":
        player.go_east()
        get_room_access(player)

    if direction_choice == "w":
        player.go_west()
        get_room_access(player)

    if direction_choice == "q":
        direction_choice = input("It is too bad you quit the game. See you later! ")
# Print an error message if the movement isn't allowed.

print("\n")

get_room_access(readyPlayerOne)