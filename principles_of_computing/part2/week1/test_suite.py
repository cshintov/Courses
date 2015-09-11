"""
Template for testing suite for Solitaire Mancala
"""

import poc_simpletest

EMPTY = 0 
FULL = 1
FOUR_WAY = 0
EIGHT_WAY = 1
OBSTACLE = 5
HUMAN = 6
ZOMBIE = 7
def run_suite(game_class):
    """
    Some informal testing code
    """

    # create a TestSuite object
    suite = poc_simpletest.TestSuite()

    # create a game
    game = game_class(4,6,[],[(1,5),(3,2)],[(3,4)])
    print "the apocalypse initially\n"
    print game
    # add tests using suite.run_test(....) here
    suite.run_test(game.compute_distance_field(ZOMBIE), "", "Test #1:compute distance\n")
    # report number of tests and failures
    #suite.report_results()
