"""
Template for testing suite for Solitaire Mancala
"""

NTRIALS = 1         # Number of trials to run
SCORE_CURRENT = 1.0 # Score for squares played by the current player
SCORE_OTHER = 2.0   # Score for squares played by the other player
E= 1
X = 2
O = 3 
D= 4
import poc_simpletest

def run_suite(game_class, func):
    """
    Some informal testing code
    """

    # create a TestSuite object
    suite = poc_simpletest.TestSuite()

    # create a game
    board = game_class(3, reverse=False)
    # add tests using suite.run_test(....) here
    row, col = func(board, X, 150) 
    suite.run_test(board.move(row, col,X), "max score empty cell", "Test #2:scores updated")
    print board
    row, col = func(board, O, 150) 
    suite.run_test(board.move(row, col, O), "max score empty cell", "Test #2:scores updated")
    print board
    # report number of tests and failures
    #suite.report_results()

