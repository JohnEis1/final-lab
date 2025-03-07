# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
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
        return f"{self.name}: {self.position}"
    def __str__(self):
        return f"{self.name}: {self.position}"

    def __eq__(self, other):
        if self.name == other.name and self.position == other.position:
            return True
        else:
            return False


lads = ['juan', 'john', 'jod']
positions = ['10', '9', '8']
#prototype list, that could be called to check if player is real

textfile_data = ["TBD"]
# fill this in later /\

team_composition = {
    "Arsenel" : [Player("John", "10")]
}
#dictonary that stores  a teams info, which is a list of inctances of the class Player and stated beofre




def position_maker():
    name = input("player name ")
    position = input("what position do you want your player to play ")
    model_player = (name, position)
    return model_player
#This function makes an instance of the class

person1 = (position_maker())
print(person1)

def player_checker(p1: person1.position) -> bool:
    if p1 in positions:
        return True
    else:
        return False and print("not a player")
#This function tests if the player is an actual player and the user isn't just trolling

def position_checker(p1: person1.name) -> bool:
    if p1 in lads:
        return True
    else:
        return False and print("not a position")
#This function tests if the position is an actual position and the user isn't just trolling

def position_comparison(guy: Player, team:str) -> str:
#This functions determines if a player should be swapped
    current_players = team_composition[team]
    potential_swaps = []
    for dude in current_players:
        if dude.position == guy.position:
            potential_swaps.append(dude)
#this segment determines if a player is eligble for swapping

    returnstr = "\n"
    # empty except for a line break

    for dude in potential_swaps:
        if dude.speed > guy.speed:
            returnstr = returnstr + f"DON'T SWAP! {dude.speed} >>> {guy.speed}"
# prototype for suggesting(or in this case not suggesting) a player for swap



    # comopare person1, stats found in dictonary with stats in .txt
    # file to print list of compatibility





    # except ValueError:
    #     print('not a player')





# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
