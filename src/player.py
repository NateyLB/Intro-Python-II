# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    items = []
    def __init__(self, name, room):
        self.name= name
        self.room = room
    def __str__(self):
        return f"Player(name={self.name} room={self.room}"
    def grab_item(self, item):
        self.items.append(item)
    def drop_item(self, item):
        self.items.remove(item)