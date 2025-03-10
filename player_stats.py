from symtable import Class

class Player_Stats:
    def __init__(self, nombre:str, speed:int, tech:int, intell:int):
        self.nombre = nombre
        self.speed = speed
        self.tech = tech
        self.intell = intell
        
    def __repr__(self):
        return f"{self.nombre}: {self.speed}, {self.tech}, {self.intell}"
    def __eq__(self, other):
        if self.nombre == other.nombre and self.speed == other.speed and self.tech == other.tech and self.intell == other.intell:
            return True
        else:
            return False
        

