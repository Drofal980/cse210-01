#IMPORTS
import random

#GLOBAL VARIABLES
PLAYERS = ['x', 'o']
CHART_DATA = [1,2,3,4,5,6,7,8,9]

#MAIN FUNCTION
def main():
    """Calls the functions needed to play a game of 
    Tic-Tac-Toe
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
                    return 0
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
        return 0
        
    except Exception as excep:
        #  This code will be executed if some
        #  other type of exception occurs.
        print("ERROR: Run the program again")
    
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
        Bool game_finished
    """
    game_finished = False

    #Checks for each player
    for player in PLAYERS:
        #Checks 
        # row 1
        if CHART_DATA[0] == player and CHART_DATA[1] == player and CHART_DATA[2] == player:
            game_finished = True
        # row 2
        if CHART_DATA[3] == player and CHART_DATA[4] == player and CHART_DATA[5] == player:
            game_finished = True
        # row 3
        if CHART_DATA[6] == player and CHART_DATA[7] == player and CHART_DATA[8] == player:
            game_finished = True

        # column 1
        if CHART_DATA[0] == player and CHART_DATA[3] == player and CHART_DATA[6] == player:
            game_finished = True
        # column 2
        if CHART_DATA[1] == player and CHART_DATA[4] == player and CHART_DATA[7] == player:
            game_finished = True
        # column 3
        if CHART_DATA[2] == player and CHART_DATA[5] == player and CHART_DATA[8] == player:
            game_finished = True
        
        # diagonal 1
        if CHART_DATA[0] == player and CHART_DATA[4] == player and CHART_DATA[8] == player:
            game_finished = True
        # diagonal 2
        if CHART_DATA[2] == player and CHART_DATA[4] == player and CHART_DATA[6] == player:
            game_finished = True
    #Checks if each position is filled
    #counter
    num_pos_filled = 0
    #For ever square
    for pos in CHART_DATA:
        #If data was entered
        if type(pos) == str:
            num_pos_filled += 1
    #if count was equal or higher than spots avaliable
    if num_pos_filled >= len(CHART_DATA):
        game_finished = True

    return game_finished

#INITIALIZES MAIN
if __name__ == "__main__":
    main() 
  