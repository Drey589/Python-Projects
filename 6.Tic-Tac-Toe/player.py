"""
Tic-Tac-Toe players using inheritance implementation by Kylie YIng
YouTube Kylie Ying: https://www.youtube.com/ycubed 
Twitch KylieYing: https://www.twitch.tv/kylieying 
Twitter @kylieyying: https://twitter.com/kylieyying 
Instagram @kylieyying: https://www.instagram.com/kylieyying/ 
Website: https://www.kylieying.com
Github: https://www.github.com/kying18 
Programmer Beast Mode Spotify playlist: https://open.spotify.com/playlist/4Akns5EUb3gzmlXIdsJkPs?si=qGc4ubKRRYmPHAJAIrCxVQ 
"""

import math
import random


class Player():
# Each player should have an attribute letter(X or O yoke)
# and an ability to move yoke
    def __init__(self, letter):
        self.letter = letter

    def get_move(self, game):
        pass


class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)
# We need (game) parameter(for TicTacToe class) to have acces in its function
# available_moves():
    def get_move(self, game): 
        # Intialize
        valid_square = False
        val = None
        if len(game.available_moves()) == 1:
            square = game.available_moves()[0]
            return square
    #   Getting a move while move given is not valid
        while not valid_square:
        #   Getting the move
            square = input(f'\n{self.letter}\'s turn. Input move (1-9)): ') 
            try:
                val = int(square) -1
        # if val is not in TicTacToe.available_moves() it's invalid raise value error
                if val not in game.available_moves():
                    raise ValueError
            #  Otherwise it's valid
                valid_square = True
            except ValueError:
                print('Invalid square. Try again.')
        
        return val  # get_move() now has val value


class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
# Will randomly select numbers from the list created by game.available_moves()
        square = random.choice(game.available_moves())
        return square

# The SmarComputerPlayer below uses "minimax algorithm" a strategic decision-making algorithm 
# that is commonly used in two-player games, such as tic-tac-toe, chess, and checkers. 

# It works by predicting all possible future scenarios based on the moves of both players 
# and choosing the move that leads to the best outcome for the player.

# The minimax algorithm was developed by John von Neumann and Oskar Morgenstern in the 1940s 
# as a solution to two-player zero-sum games. Zero-sum games are games in which one player's 
# gain is equal to the other player's loss, such as chess, checkers, and tic-tac-toe.

# Von Neumann and Morgenstern's work on the minimax algorithm was part of their 
# broader research on game theory, which is a mathematical framework for studying 
# strategic decision-making in situations where two or more players interact. 
# Their work laid the foundations for the modern field of game theory and has had 
# significant impacts on fields such as economics, political science, and computer science.

# The minimax algorithm has since become a widely used technique for game AI in two-player 
# games and has been applied to a variety of different games, including chess, checkers, 
# tic-tac-toe, and many others. It has also been extended to more complex situations, 
# such as multi-player games and games with imperfect information, 
# through the use of variants such as the minimax-alpha-beta algorithm.

class SmartComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        # If it's our first move we will just pick a random move
        if len(game.available_moves()) == 9:
            square = random.choice(game.available_moves())
        # else we use minmax 
        else:
            square = self.minimax(game, self.letter)['position']
        return square

# For every option we have, we branch a simulation until someone win or there are no boxes left(draw)
# At the top of our branch(our move) we are going to pick the highest posible score
# To do that we have maximizer and minimizer
#                    
#       Maximizer: If we win in a simulation score = num_empty_squares() + 1 * 1 (Score will be positive so we can pick it among the rest)
#       If we lose in a simulation score = num_empty_squares() + 1 * -1 (Score will be negative so we will never pick it )
#       If it reuslts to draw score = 0

# We start at the bottom of the tree
# If it's our turn we assign the branch above the highest value between the branches
# If it's our turn we assign the branch above the lowest value between the branches
# until we reach the last choices where we choose the highest




    def minimax(self, state, player):
        max_player = self.letter  # yourself
        other_player = 'O' if player == 'X' else 'X'
    
        if state.current_winner == other_player:
            return {'position': None, 'score': 1 * (state.num_empty_squares() + 1) if other_player == max_player else -1 * (
                        state.num_empty_squares() + 1)}
        elif not state.empty_squares():
            return {'position': None, 'score': 0}

        if player == max_player:
            best = {'position': None, 'score': -math.inf}  # each score should maximize
        else:
            best = {'position': None, 'score': math.inf}  # each score should minimize
        for possible_move in state.available_moves():
            state.make_move(possible_move, player)
            sim_score = self.minimax(state, other_player)  # simulate a game after making that move

            # undo move
            state.board[possible_move] = ' '
            state.current_winner = None
            sim_score['position'] = possible_move  # this represents the move optimal next move

            if player == max_player:  # X is max player
                if sim_score['score'] > best['score']:
                    best = sim_score
            else:
                if sim_score['score'] < best['score']:
                    best = sim_score
        return best