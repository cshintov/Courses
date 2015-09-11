"""
Template for testing suite for Solitaire Mancala
"""

import poc_simpletest

def run_suite(func):
    """
    Some informal testing code
    """

    # create a TestSuite object
    suite = poc_simpletest.TestSuite()
    # add tests using suite.run_test(....) here
    lst = [1,3,4,5]
    ls = [3,4,5]
    suite.run_test(func(lst,ls), [3,4,5], "Test #1:find 1")
    # report number of tests and failures
    suite.report_results()

