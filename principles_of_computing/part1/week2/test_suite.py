"""
Template for testing suite for Solitaire Mancala
"""

UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4
import poc_simpletest

def run_suite(game_class):
    """
    Some informal testing code
    """

    # create a TestSuite object
    suite = poc_simpletest.TestSuite()

    # create a game
    game = game_class(4,5)
    game.new_tile()
    game.new_tile()
    game.new_tile()
    game.new_tile()
    game.new_tile()
    game.new_tile()
    game.new_tile()
    # add tests using suite.run_test(....) here
    suite.run_test(str(game), "", "Test #5:if merged")
    game.move(RIGHT)
    suite.run_test(str(game), "", "Test #5:if merged")
    # report number of tests and failures
    #suite.report_results()

