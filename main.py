# Rock-Paper-Scissors Game

# import the random for computer's 
import random

# set the option for computers selection
moves = ['r', 'p', 's']

def result_statement(player, opponent):
    print('Computer Selected:{}\nAnd the player selected:{}'.format(opponent, player))

# looping the game
while True:
    # Player move
    player_move = input('select from the option: p for paper, s for scissor and r for rock\n')
    player_move.lower()

    # computer select
    computer_move = random.choice(moves)
    
    # Game Logic
 
     # validate the input
    if player_move != 'r' and player_move != 'p' and player_move != 's':
        print("please enter a valid input")
        
       # logic for tie 
    if player_move == computer_move:
        print("Both Players has a Tie with: Player({}): CPU({}) moves".format(player_move, computer_move))
    
    # logic for win or lose
    if player_move == 'r':
        if computer_move == 's':
            result_statement(player_move, computer_move)
            print('Player wins')
        elif computer_move == 'p':
            result_statement(player_move, computer_move)
            print('Computer Wins')
    elif player_move == 'p':
        if computer_move == 'r':
            result_statement(player_move, computer_move)
            print('Player Wins')
        elif computer_move == 's':
            result_statement(player_move, computer_move)
            print('Computer Wins')
    elif player_move == 's':
        if computer_move == 'p':
            result_statement(player_move, computer_move)
            print('Player Wins')
        elif computer_move == 'r':
            result_statement(player_move, computer_move)
            print('Computer Wins')

