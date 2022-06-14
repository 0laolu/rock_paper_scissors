# importing the random module
import random

while True:
    def playGame():
        choices = ['R', 'P', 'S']

        CPU = random.choice(choices)
        player = None

        while player not in choices:
            player = input("Select one of 'R' for rock, 'P' for paper, 'S' for scissors: ")

        # if the game is a tie
        if player == CPU:
            print(f'Player ({player}) : CPU ({CPU}). It\'s a TIE!')
        elif player == 'R':
            if CPU == 'P':
                print(f'Player ({player}) : CPU ({CPU}). You LOSE')
            if CPU == 'S':
                print(f'Player ({player}) : CPU ({CPU}). You WIN!')
        elif player == 'S':
            if CPU == 'R':
                print(f'Player ({player}) : CPU ({CPU}). You LOSE')
            if CPU == 'P':
                print(f'Player ({player}) : CPU ({CPU}). You WIN!') 
        elif player == 'P':
            if CPU == 'S':
                print(f'Player ({player}) : CPU ({CPU}). You LOSE')
            if CPU == 'R':
                print(f'Player ({player}) : CPU ({CPU}). You WIN!')

    playGame()
    play_again = input('do you want to play again? (Yes/ NO)\n').lower()
    if play_again != 'yes':
        break

print('Bye!')



