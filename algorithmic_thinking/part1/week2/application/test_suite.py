"""
Template for testing suite for Solitaire Mancala
"""

import poc_simpletest

EX_GRAPH0 = {0: set([1, 2]),
             1: set([]),
             2: set([])}

GRAPH1 = {0: set([1, 4, 5]),
             1: set([0, 2, 4]),
             2: set([1, 5]),
             3: set([6]),
             4: set([0, 1]),
             5: set([0, 2]),
             6: set([3])}

EX_GRAPH2 = {0: set([1, 4, 5]),
             1: set([2,6]),
             2: set([3, 7]),
             3: set([7]),
             4: set([1]),
             5: set([2]),
             6: set([]),
             7: set([3]),
             8: set([1, 2]),
             9: set([0, 4, 5, 6, 7, 3])}

GRAPH4 = {"dog": set(["cat"]),
          "cat": set(["dog"]),
          "monkey": set(["banana"]),
          "banana": set([])}

def run_suite(func1):
    """
    Some informal testing code
    """

    # create a TestSuite object
    suite = poc_simpletest.TestSuite()
    #run tests
    suite.run_test(len(func1(28000, 14)),"a undigraph" ,"Test #:gen_digraph")
    # report number of tests and failures
    #suite.report_results()

