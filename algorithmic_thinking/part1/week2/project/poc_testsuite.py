"""
Test suite for func in "Yahtzee"
"""

import poc_simpletest
from alg_module1_graphs import *
def run_suite(func):
    """
    Some informal testing code for func
    """
    print 'testing ',func.__name__
    # create a TestSuite object
    suite = poc_simpletest.TestSuite()
    
    # test func on various inputs
    
    #suite.run_test(func(GRAPH0, 1), , "Test #1:")
    #suite.run_test(func(GRAPH0), [set([0,1,2,3]),set([4,5]),set([6])], "Test #2:")
    suite.run_test(func(GRAPH0, [1,2]), [4, 2, 1], "Test #2:")

    suite.report_results()
