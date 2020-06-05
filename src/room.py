# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description, items, is_light ):
        self.name = name
        self.description = description
        self.items = items
        self.is_light = is_light
    def __str__(self):
        return f"{self.name}: {self.description} \n items: {[x.__str__() for x in self.items]}"