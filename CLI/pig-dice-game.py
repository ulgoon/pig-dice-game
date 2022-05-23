from random import randint
from time import sleep


scoreboard = [0, 0]
goal_score = 100
is_game_over = False

while True:
    is_turn_on = True
    player_turn_score = 0
    rolled = 0
    while is_turn_on!='h':
        print("==============")
        print("Player's turn!")
        rolled = randint(1,6)
        if rolled==1:
            player_turn_score=0
            print("Oh, you got 1! Ending your turn..")
            break
        else:
            player_turn_score+=rolled
            print(f"You got {rolled}, and You have {player_turn_score}.")
            if scoreboard[0]+player_turn_score>=goal_score:
                is_game_over=True
                break
            is_turn_on = input("Roll(r) or Hold(h)> ").lower()

    if is_game_over==True:
        print(f"Congrats! Player have achieved {goal_score}.")
        break
    scoreboard[0]+=player_turn_score
    print(f'Scoreboard: {scoreboard}')

    com_turn_score = 0
    rolled=0
    while com_turn_score<=30:
        print("================")
        print("Com's Show time!")
        sleep(1)
        rolled = randint(1,6)
        if rolled==1:
            com_turn_score=0
            print("Uh-oh.. Com got 1.. I got nothin' on this turn..")
            break
        else:
            com_turn_score+=rolled
            print(f"I got {rolled}, and I have {com_turn_score}.")
            if scoreboard[1]+com_turn_score>=goal_score:
                is_game_over=True
                break
    if is_game_over==True:
        print(f"Game Over! Computer have achieved {goal_score}")
        break
    scoreboard[1]+=com_turn_score
    print(f'Scoreboard: {scoreboard}')
