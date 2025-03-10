class Player:
    #player class that will be called throughout the code.
    def __init__(self, name:str, position:str):
        self.name = name
        self.position = position

    def set_name(self, name):
        self.name = name
    def set_position(self, position):
        self.position = position


    def __repr__(self):
        return f"{self.name}, {self.position}"
    def __str__(self):
        return f"{self.name}, {self.position}"

    def __eq__(self, other):
        if self.name == other.name and self.position == other.position:
            return True
        else:
            return False