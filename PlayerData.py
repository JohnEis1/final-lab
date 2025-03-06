class Player:
    def __init__(self, name, stats):
        #Initialize player with a name and stats dictionary
        self.name = name
        self.stats = stats  # Dictionary storing player statistics

    def display_info(self):
        #Prints player information
        print(f"Player: {self.name}")
        print("Stats:")
        for key, value in self.stats.items():
            print(f"  {key}: {value}")
