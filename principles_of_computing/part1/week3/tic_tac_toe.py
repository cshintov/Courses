"""
Monte Carlo Tic-Tac-Toe Player
"""

import random
#import poc_ttt_gui
import poc_ttt_provided as provided

# Constants for Monte Carlo simulator
# You may change the values of these constants as desired, but
# do not change their names.
NTRIALS = 100         # Number of trials to run
SCORE_CURRENT = 5.0 # Score for squares played by the current player
SCORE_OTHER = 3.0   # Score for squares played by the other player

# Add your functions here.

def mc_trial(board, player):
    """
    takes current board and next player to move and play until the game is over.
    """
    empty_sqrs = board.get_empty_squares()
    while len(empty_sqrs) != 0 and board.check_win() is None:
        row, col = random.choice(empty_sqrs)
        empty_sqrs.remove((row, col))
        board.move(row, col, player=player)
        player = provided.switch_player(player)

def mc_update_scores(scores, board, player):
    """
    takes the current score-board, a completed game, which player
    the machine player is ,scores the completed game and updates the scoreboard.
    """
    winner = board.check_win()
    if winner is provided.DRAW:
        return
    if winner is player:
        add = SCORE_CURRENT
        sub = -SCORE_OTHER
    else:
        add = SCORE_OTHER
        sub = -SCORE_CURRENT

    dim = board.get_dim()
    cells = ((row, col) for row in range(dim) for col in range(dim))
    for row, col in cells:
        cell_val = board.square(row, col)
        if cell_val is provided.EMPTY:
            continue
        if cell_val is winner:
            scores[row][col] += add
        else:
            scores[row][col] += sub

def get_best_move(board, scores):
    """
    takes the current board and score-board and returns the best cell to play
    """
    empty_cells = board.get_empty_squares()
    empty_cells = [(row, col, scores[row][col]) for row, col in empty_cells]
    empty_cell_scores = [item[2] for item in empty_cells]
    max_score = max(empty_cell_scores)
    max_score_cells = []
    for row, col, score in empty_cells:
        if score == max_score:
            max_score_cells.append((row, col))
    return random.choice(max_score_cells)

def mc_move(board, player, trials):
    """
    takes the current board, the machine player and number of trials and returns
    the best move possible
    """
    dim = board.get_dim()
    scores = [[0 for dummy_col in range(dim)] for dummy_row in range(dim)]
    for dummytrial in range(trials):
        cln_board = board.clone()
        mc_trial(cln_board, player)
        mc_update_scores(scores, cln_board, player)
        best_move = get_best_move(board, scores)
    print best_move
    return best_move

# Test game with the console or the GUI.  Uncomment whichever
# you prefer.  Both should be commented out when you submit
# for testing to save time.

#provided.play_game(mc_move, NTRIALS, False)
# poc_ttt_gui.run_gui(3, provided.PLAYERX, mc_move, NTRIALS, False)
#import test_suite
#test_suite.run_suite(provided.TTTBoard, mc_move)
