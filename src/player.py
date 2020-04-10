# Write a class to hold player information, e.g. what room they are in
# currently.
from room import Room

class Player:
    def __init__(self, current_room, inventory=None):
        self.current_room = current_room
        if inventory is None:
            self.inventory = []
        else:
            self.inventory = inventory
    
    def takeItem(self, item):
        self.inventory.append(item)
    
    def dropItem(self, item):
        self.inventory.remove(item)

    def go_north(self):
        if self.current_room.n_to != None:
            self.current_room = self.current_room.n_to
        else:
            print("You shall not pass north. Please enter another direction. ")

    def go_south(self):
        if self.current_room.s_to != None:
            self.current_room = self.current_room.s_to
        else:
            print("You shall not pass south. Please enter another direction. ")

    def go_east(self):
        if self.current_room.e_to != None:
            self.current_room = self.current_room.e_to
        else:
            print("You shall not pass east. Please enter another direction. ")

    def go_west(self):
        if self.current_room.w_to != None:
            self.current_room = self.current_room.w_to
        else:
            print("You shall not pass west. Please enter another direction. ")