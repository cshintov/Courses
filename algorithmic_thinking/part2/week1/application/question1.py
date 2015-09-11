"""
answering question1 of the application 2 of algorithmic thinking
"""
from time import time
from matplotlib import pyplot
from random import choice
from gen_rand_clusters import *

def plot(slow, fast):
    """
    Plots a log-log plot
    """
    nodes = range(2,201)
    #pyplot.clf()
    #pyplot.xscale("log")
    #pyplot.yscale("log")
    pyplot.title('running times of closest pair algorithms on desktop python')
    pyplot.xlabel('number_of_clusters')
    pyplot.ylabel('running_time in seconds')
    pyplot.plot(nodes, slow, 'r-', label='slow_closest_pair')
    pyplot.plot(nodes, fast, 'b-', label='fast_closest_pair')
    pyplot.legend()
    #pyplot.ylim(ymin=0)
    #pyplot.xlim(xmin=2)
    pyplot.savefig('running_times.png', bbox_inches='tight')
    pyplot.show()

def timer(func):
    def inner(ugraph):
        start = time()
        result = func(ugraph)
        end = time()
        return end - start
    return inner

time_cp = timer(slow_closest_pair)
time_fast_cp = timer(fast_closest_pair)

def compute_running_times():
    run_time_slow_closest= []
    run_time_fast_closest= []
    for num in range(2,201):
        clusters = gen_random_clusters(num)
        run_time = time_cp(clusters)
        run_time_slow_closest.append(run_time)
        run_time = time_fast_cp(clusters)
        run_time_fast_closest.append(run_time)
    running_time = [run_time_slow_closest, run_time_fast_closest]
    return running_time

def plot_running_times():
    time_slow, time_fast = compute_running_times()
    plot(time_slow, time_fast)

plot_running_times()
