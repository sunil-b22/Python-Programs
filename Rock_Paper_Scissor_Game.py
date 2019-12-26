#Rock, paper, scissor game

import random

#Incrementing player score
def player_inc(player):
    player += 1
    print("Player: {}".format(player))
    return player

#Incrementing compluter score
def comp_inc(comp):
    comp += 1
    print("Computer: {}".format(comp))
    return comp

comp=0
player=0
game=('rock','paper','scissor')

#Game loop
while comp < 3 and player < 3:
    c = random.choice(game)
    u = input("rock, paper, scissor: ")
    print("Computers choice: {}".format(c))
    if  c == "rock":
        if u == "paper":
            player = player_inc(player)
        elif u == "scissor":
            comp = comp_inc(comp)
        else:
            print("Its a draw")
    elif c == "paper":
        if u == "scissor":
            player = player_inc(player)
        elif u == "rock":
            comp = comp_inc(comp)
        else:
            print("Its a draw")
    else:
        if u == "rock":
            player = player_inc(player)
        elif u == "paper":
            comp = comp_inc(comp)
        else:
            print("Its a draw")
if comp == 3:
    print("Computer won the match")
else:
    print("You won the match")
