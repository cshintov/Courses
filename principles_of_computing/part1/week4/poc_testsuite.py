"""
Test suite for func in "Yahtzee"
"""

import poc_simpletest

def run_suite(func):
    """
    Some informal testing code for func
    """
    print 'testing ',func.__name__
    # create a TestSuite object
    suite = poc_simpletest.TestSuite()
    
    # test func on various inputs
    hand = tuple([])
    suite.run_test(func(hand, 6, 1), 5,"Test #1:")
