"""
Template for testing suite for Solitaire Mancala
"""

import poc_simpletest
from alignment import *

def run_suite(fun1,fun2):
    """
    Some informal testing code
    """

    # create a TestSuite object
    suite = poc_simpletest.TestSuite()

    # create a game
    scoring_matrix = build_scoring_matrix(set(['A','C','T','G']), 10, 4, 2)

    # add tests using suite.run_test(....) here
    print "local"
    alignment_matrixl = compute_alignment_matrix('AA','TAAT', scoring_matrix, False)
    print alignment_matrixl
    suite.run_test(fun1('AA','TAAT', scoring_matrix, alignment_matrixl), "", "")
    print "global"
    alignment_matrixg = compute_alignment_matrix('AA','TAAT', scoring_matrix, True)
    print alignment_matrixg
    suite.run_test(fun2('AA','TAAT', scoring_matrix, alignment_matrixg), "", "")
    # report number of tests and failures
    #suite.report_results()

run_suite(compute_local_alignment, compute_global_alignment)
