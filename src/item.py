
class Item:
    def __init__(self,name, description):
        self.name = name
        self.description = description
    def __str__(self):
        return f"{self.name}: {self.description}"
    def on_take(self):
        print(f"You have picked up {self.name}\n")
    def on_drop(self):
        print(f"You have dropped {self.name}\n")

class LightSource(Item):
    def __init__(self, name, description):
        super().__init__(name, description)
        self.name = name
        self.description = description
    def on_drop(self):
        print(f"It's not wise to drop your light!")
