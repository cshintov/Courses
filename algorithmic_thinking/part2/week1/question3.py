"""
answering question1 of the application 2 of algorithmic thinking
"""
from time import time
from matplotlib import pyplot
from random import choice
from bfs import *
from provided import *
def plot(slow, fast):
    """
    Plots a log-log plot
    """
    nodes = range(10,1000,10)
    #pyplot.clf()
    pyplot.xscale("log")
    pyplot.yscale("log")
    pyplot.title('running times of targeted orders on desktop python')
    pyplot.xlabel('number_of_nodes')
    pyplot.ylabel('running_time')
    pyplot.plot(nodes, slow, 'r-', label='target_order')
    pyplot.plot(nodes, fast, 'b-', label='fast_target_order')
    pyplot.legend()
    #pyplot.ylim(ymin=0)
    pyplot.savefig('running_times_log.png', bbox_inches='tight')
    pyplot.show()

def timer(func):
    def inner(ugraph):
        start = time()
        result = func(ugraph)
        end = time()
        return end - start
    return inner
time_to = timer(targeted_order)
time_fast_to= timer(fast_targeted_order)
from graph_gen_dpa import generate_undigraph
def compute_running_times():
    run_time_targ_order = []
    run_time_fast_to = []
    for n_nodes in range(10,1000,10):
        ugraph = generate_undigraph(n_nodes, 5)
        run_time = time_to(ugraph)
        run_time_targ_order.append(run_time)
        run_time = time_fast_to(ugraph)
        run_time_fast_to.append(run_time)
    running_time = [run_time_targ_order, run_time_fast_to]
    return running_time

def plot_running_times():
    time_slow, time_fast = compute_running_times()
    plot(time_slow, time_fast)

plot_running_times()
