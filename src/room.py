# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.n_to = None
        self.s_to = None
        self.w_to = None
        self.e_to = None
        self.players = []
        self.items = []
        
    def __str__(self):
        displayStr = ""
        displayStr += f"\n{self.name}\n"
        displayStr += f"\n{self.description}\n"
        displayStr += f"\n{self.getExitsString()}\n"
        return displayStr
    
    def getRoomInDirections(self, directions):
        if hasattr(self, f"{directions}_to"):
            return getattr(self, f"{directions}_to")
        return None
    
    def getExits(self):
        exits = []
        if self.n_to:
            exits.append("n")
        if self.s_to:
            exits.append("s")
        if self.w_to:
            exits.append("w")
        if self.e_to:
            exits.append("e")
        return exits
    
    def getExitsString(self):
        return f"Exits {', '.join(self.getExits())}"
    
    def getRoomItems(self):
        return f"Items {', '.join(self.items))}"
    
    