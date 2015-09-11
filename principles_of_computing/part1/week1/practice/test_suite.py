"""
Template for testing suite for Solitaire Mancala
"""

import poc_simpletest

def run_suite(game_class):
    """
    Some informal testing code
    """

    # create a TestSuite object
    suite = poc_simpletest.TestSuite()

    # create a game
    game = game_class()

    # add tests using suite.run_test(....) here

    # report number of tests and failures
    suite.report_results()

