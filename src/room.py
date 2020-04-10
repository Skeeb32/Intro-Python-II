# Implement a class to hold room information. This should have name and
# description attributes.
from item import Item

class Room:
    def __init__(self, name, description, n_to=None, s_to=None, e_to=None, w_to=None, items=None):
        self.name = name
        self.description = description
        self.n_to = n_to
        self.s_to = s_to
        self.e_to = e_to
        self.w_to = w_to
        if items is None:
            self.items = []
        else:
            self.items = items

    def __str__(self):
        return f"You are in the {self.name} room. {self.description}"

    def addItem(self, item):
            self.items.append(item)

    def removeItem(self, item):
        if item in item:
            self.items.remove(item)
        else:
            print(f"{item} is not available. ")