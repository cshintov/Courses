"""
Template for testing suite for Solitaire Mancala
"""

import poc_simpletest
from temp import *

def run_suite(puzzle):
    """
    Some informal testing code
    """

    # create a TestSuite object
    suite = poc_simpletest.TestSuite()

    # create a game
    # add tests using suite.run_test(....) here
    suite.run_test(puzzle.solve_row0_tile(2), True, "Test #1")
    print puzzle
    #suite.run_test(str(game), "", "Test #5:if merged")
    # report number of tests and failures
    #suite.report_results()

#puzzle = Puzzle(4, 4, [[4,2,3,12], [5,6,1,7], [8,9,10,11],[0,13,14,15]])
#puzzle = Puzzle(3, 3, [[3, 2, 1], [6, 5, 4], [7, 0, 8]])
#puzzle = Puzzle(4, 5, [[7, 6, 5, 3, 4], [2, 1, 0, 8, 9], [10, 11, 12, 13, 14], [15, 16, 17, 18, 19]])
puzzle = Puzzle(3, 3, [[4, 1, 0], [2, 3, 5], [6, 7, 8]])
print puzzle
run_suite(puzzle)
