"""
Tic Tac Toe class + game play implementation by Kylie Ying
YouTube Kylie Ying: https://www.youtube.com/ycubed 
Twitch KylieYing: https://www.twitch.tv/kylieying 
Twitter @kylieyying: https://twitter.com/kylieyying 
Instagram @kylieyying: https://www.instagram.com/kylieyying/ 
Website: https://www.kylieying.com
Github: https://www.github.com/kying18 
Programmer Beast Mode Spotify playlist: https://open.spotify.com/playlist/4Akns5EUb3gzmlXIdsJkPs?si=qGc4ubKRRYmPHAJAIrCxVQ 
"""

import math
import time
from player import HumanPlayer, RandomComputerPlayer, SmartComputerPlayer
import random

class TicTacToe():
    def __init__(self):
    # Board is 9 blanks representing 9 spots in the TicTacToe
        self.board = [' ' for _ in range(9)] 
    # The self.board above is basically like this [' ', ' ', ' ', ' ', ' ',]
        self.current_winner = None

# For the function print_board() below
# Every time we want to print self.board ex( [' ', 'X', ' ', 'X', 'O', ' ', ' '] )
# We slice it first into 3 rows then concantenate it with '|'
# to look something like this:
#                           
#                           | X | O | X | <-- Print First row
#                           | O | O | X | <-- Print Second row 
#                           | O | X | O | <-- Print Third row
# 
# But we don't save it, we just print it this way if we want to
# Our board is still just a list of 9 items

    def print_board(self):
        print("")  
        #          [[0,1,2],[3,4,5], [6,7,8]] every list called row
        for row in [self.board[i*3:(i+1) * 3] for i in range(3)]:# slice list into three rows 0,1,2
            print('| ' + ' | '.join(row) + ' |')


    @staticmethod
# The print_board_nums() below
# prints numbered boared as guide at the start of the program 
# like this: 
#           | 1 | 2 | 3 |
#           | 4 | 5 | 6 |
#           | 7 | 8 | 9 |

    def print_board_nums():
        number_board = [[str(i+1) for i in range(j*3, (j+1)*3)] for j in range(3)] # creates sublist for every j or range 0-2
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')

# This processes the moves of letter X or O
    def make_move(self, square, letter):
    # If the letter moves in a blank space ' '
        if self.board[square] == ' ':
    # We update the board likes this [' ', ' ', ' ', 'X', ' ',]
    # The position base on the index given by square and the current letter X or O
            self.board[square] = letter
        #   We check if it wins or not
            if self.winner(square, letter):
            # If it wins the current letter will be the winner
                self.current_winner = letter
            return True
        return False
#    The function below is used to check if the current letter wins
    def winner(self, square, letter):
        # checking if the latest move results to win by 
        # checking every angle of it (row, column, diagonal)

        # Find out what row it is then, check if the whole row is similar
        # Get the items in the row it belongs to, check if the whole row is similar
        row_ind = square//3
        # we get the row items we needed by indexing 
        row = self.board[row_ind*3:(row_ind+1)*3]
        if all([item == letter for item in row]):
            return True

        # Get the items of column it belongs to , check if the whole row is similar
        col_ind = square % 3
        # We get the column items we needed by adding the remainder to the row
        column = [self.board[col_ind+i*3] for i in range(3)]
        # print('col', column)
        if all([s == letter for s in column]):
            return True
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]]
            # print('diag1', diagonal1)
            if all([s == letter for s in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]]
            # print('diag2', diagonal2)
            if all([s == letter for s in diagonal2]):
                return True
        return False
#
    def empty_squares(self):
        return ' ' in self.board

    def num_empty_squares(self):
        return self.board.count(' ')
        
#   Retuns a list of index for every " " in the list
    def available_moves(self):

        return [i for i, x in enumerate(self.board) if x == " "]

# The function below play() inherits the Class: TictacToe and Two Subclasses of player
# to have acces in their abilities or functions
def play(game, x_player, o_player):
    print('')
# Prints the number board
    game.print_board_nums()

    letter = 'X' # first turn
# random.choice(['X','O'])
# The code runs while there's an empty squares
    while game.empty_squares():
        if letter == 'O':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)

        # TicTacToe.make_move() below returns true if it get's the move
        # It also updates our board and checks if there's a current winner
        # The indented code below the if statement will be executed 
        # if the make_move() function returns a truthy value, 
        # and it will not be executed if the function returns a falsy value. 
        if game.make_move(square, letter):
            
            print(f'{letter} makes a move to square {square+1}')
            game.print_board()
            print('')

            if game.current_winner:
                print(letter + ' wins!')
                return letter  # ends the loop and exits the game
            letter = 'O' if letter == 'X' else 'X'  # switches player

        # time.sleep(.9) # Tiny pause to the loop

    
    print('It\'s a tie!')

def get_valid_response():
    while True:
        response = input("\nDo you want to play again? (Y/N): ")
        if response.upper() in ["Y", "N"]:
            return response
        else:
            print("Please enter Y/N !")


choice = '''
    Choices:
            H - Human player
            E - Easy Computer
            S - Smart Computer
'''
x = {
    'H' : HumanPlayer('X'),
    'E' : RandomComputerPlayer('X'),
    'S' : SmartComputerPlayer('X')
}
y = {
    'H' : HumanPlayer('O'),
    'E' : RandomComputerPlayer('O'),
    'S' : SmartComputerPlayer('O')
}
if __name__ == '__main__':
    print("\nWelcome to the TicTacToe game!")
    while True:
        print("\nPick the players to start the game")
        print(choice)
        while True:
            try:
                x_player = x[input("Input X player: ").upper()]
            except(KeyError):
                print("\nPlease input from the choices!\n")
            else:
                break
        while True:
            try:
                o_player = y[input("Input O player: ").upper()]
            except(KeyError):
                print("\nPlease input from the choices!\n")
            else:
                break

        t = TicTacToe()
        play(t, x_player, o_player)
        ans = get_valid_response().upper()
        if ans == 'Y':
            continue
        if ans == 'N':
            print("Understandable have a nice day!")
            break