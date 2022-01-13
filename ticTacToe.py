#IMPORTS
import random

#GLOBAL VARIABLES
PLAYERS = ['x', 'o']
CHART_DATA = [1,2,3,4,5,6,7,8,9]

#MAIN FUNCTION
def main():
    """[Function purpose here]
    """
    try:
        global PLAYERS
        global CHART_DATA

        #Picks starting player
        picked_player = random.randint(0, len(PLAYERS)-1)

        #Changes order of list if player 2 goes first
        if picked_player == 1:
            PLAYERS.reverse()

        ###SEQUENCE OF EACH TURN##
        #Repeats until game is over
        while(if_game_finished() == False):
            #Each players turn
            for player in PLAYERS:
                #Checks again if game is done
                if if_game_finished():
                    #End game message
                    display_Chart(CHART_DATA)
                    print("Good game. Thanks for playing!")
                    quit()
                else:
                    #Prints chart to terminal
                    display_Chart(CHART_DATA)

                    #Gets current players choice, -1 to account for 0
                    square_choice = get_choice(player)-1

                    #Checks and reprompts if position is filled
                    while(type(CHART_DATA[square_choice]) != int):
                        print("Position is filled, Please pick another square")
                        square_choice = get_choice(player)-1

                    #Changes chart
                    CHART_DATA = change_chart(square_choice, player, CHART_DATA)
        
        #End game message
        print("Good game. Thanks for playing!")
        quit()
                

    except ValueError as val_err:
         #  This code will be executed if the user enters
        #  an invalid integer for the position in the chart
        print("ERROR: Please enter a valid position")
        print()

#OTHER FUNCTIONS
def display_Chart(cd):
    """Displays a Tic-Tac-Toe Chart in the terminal

    Parameters
        cd: List containing chart dataW
    """
    print(f'{cd[0]}|{cd[1]}|{cd[2]}')
    print('-+-+-')
    print(f'{cd[3]}|{cd[4]}|{cd[5]}')
    print('-+-+-')
    print(f'{cd[6]}|{cd[7]}|{cd[8]}')
    print()

def get_choice(player):
    """Gets a players choice of square

    Parameters
        player: Char representing player

    """
    choice = int(input(f"{player}'s turn to choose a square (1-9): "))
    return choice

def change_chart(square, player, chart):
    """Changes position in list to players name

    Parameters
        square: Int representing position in a list
        player: Char representing player
        chart: List of positions and values on a grid
    Return:
        chart
    """
    chart[square] = player
    return chart

def if_game_finished():
    """Checks if the conditions to end the game have
    been met

    Return:
        chart
    """
    game_finished = False

    #Checks if each position is filled
    num_pos_filled = 0
    for pos in CHART_DATA:
        if type(pos) == str:
            num_pos_filled += 1
    if num_pos_filled >= len(CHART_DATA):
        game_finished = True

    return game_finished

#INITIALIZES MAIN
if __name__ == "__main__":
    main() 
  