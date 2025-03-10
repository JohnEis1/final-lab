from Player_class import *
from player_stats import *
from lists_and_dictionary import *


print('Players: John, Max')
print('Teams: Lakers, Warriors')
print('Positions: 1, 2, 3, 4, 5')
#These print statements display to the user there options for the program
#Max

team = input("what team do you want them on ")
# This sets the team that you would like to put your selected player on

def position_maker():
    name = input("player name ")
    position = input("what position do you want your player to play ")
    model_player = Player(name, position)
    return model_player
#This function makes an instance of the class Player class, so you can compare positions
#The point is for to things
#1) select what position you want your player to play on
#2) create a place to store both name and data which you can call on
#John

person1 = position_maker()
print(person1)
#This actually calls the previous function

def player_checker(p1) -> bool:
    if p1 in lads:
        return True
    else:
        print('not a real player')
        return False
#This function tests if the player is an actual player and the user isn't just trolling
#John

def position_checker(p1) -> bool:
    if p1 in positions:
        return True
    else:
        print('not a real position')
        return False
#This function tests if the position is an actual position and the user isn't just trolling
#John

def team_checker(team1) -> bool:
    try:
        if team1 in teams:
            return True
        else:
            print('not a real team')
            return False
    except KeyError:
        return False
#This function tests if the position is an actual team and the user isn't just trolling
#John

print(player_checker(person1.name),position_checker(person1.position),team_checker(team))
# This calls the checker functions, not exactly needed because these functions are called later, but nice when testing to see whats happening

def position_comparison_id(guy: Player, team1:str) -> list:
    if team_checker(team1) == True:
        current_players = team_composition[team1]
        potential_swaps = []
        for dude in current_players:
            if dude.position == guy.position:
                potential_swaps.append(dude.name)
        return potential_swaps
    else:
        return []
#This functions determines if a player should be swapped, and makes a list of players to be swapped
#As you can see, the team checker function is being called
#John

def swaps(guy1: Player, team2:str) -> int:
    if position_comparison_id(guy1, team2) == []:
        return False
    if player_checker(person1.name) == False:
        return False
    if position_checker(person1.position) == False:
        return False
    #Phase one of Swaps checks to see if everything is in order, calling previous functions to see there results
    else:
        str_name = person1.name
        current_name = ''
        for i in player_stats:
            if str_name == i.nombre:
                current_name = i
                #This section converts a str into a object of player_stats class, so the stats form each player
                #can actually be called
        ps = position_comparison_id(guy1, team2)
        counter = 0
        for bro in ps:
            for y in player_stats:
                ynam = y.nombre
                if bro == ynam:
                    player_object_bro = y
                    #John

                    if current_name.speed > player_object_bro.speed:
                        counter += 1
                    if current_name.speed > player_object_bro.tech:
                        counter += 1
                    if current_name.speed > player_object_bro.intell:
                        counter += 1
        if counter >= 2:
            #The counter tallies the stats of selected player that are better than the player
            #on selected team in selected position
            print('swapping is a good choice')
            return counter
        else:
            print("don't swap")
            #Max


print(swaps(person1, team))
#calls swaps


