"""
Test suite for func in "Yahtzee"
"""

SIM_TIME = 10000000000.0
import poc_simpletest
from poc_clicker_provided import *
def run_suite(func,arg):
    """
    Some informal testing code for func
    """
    # create a TestSuite object
    suite = poc_simpletest.TestSuite()
    build_info = BuildInfo()
    # test func on various inputs
    #state = func(buildinfo,15,arg)
    #suite.run_test(func(buildinfo,15,arg),"state after 10 cookies" ,"Test #1:simulator")
    state = func(build_info,SIM_TIME,arg)
    #state = func(build_info,125,arg)
    print state
    #print state.history
    #suite.run_test(func(buildinfo,15,arg),"state after 10 cookies" ,"Test #1:simulator")
