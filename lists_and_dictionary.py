from Player_class import *
from player_stats import *


team_composition = {
    "Lakers" : [Player("Bowie", '1'), Player("Andrew", '2'),Player("Bob", '3'),
                 Player("Sam", '4'), Player("Kobe", '5')],
    "Warriors" : [Player('Curry','1'),Player('Jimmy','2'),Player('Garry','3'),
                  Player('Leborn','4'),Player('Clay','5')]
}

player_stats = [Player_Stats('John',9,8,7), Player_Stats('Bowie',5,2,7),
                Player_Stats('Bob',6,5,4), Player_Stats('Sam',5,3,6),
                Player_Stats('Kobe',10,10,10), Player_Stats('Max',8,8,8),
                Player_Stats('Andrew',3,5,5), Player_Stats('Curry',9,9,9),
                Player_Stats('Jimmy',5,5,5),Player_Stats('Garry',3,5,5),
                Player_Stats('Leborn',10,10,10), Player_Stats('Clay',7,6,5)]

#all the lists are for checking purposes
lads = ['John', 'Max']
positions = ['1', '2', '3','4','5']
teams = ['Lakers', 'Warriors']