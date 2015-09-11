"""
answering question1 of the application 2 of principles of computing
"""

from matplotlib import pyplot
from graphs import NETWORK, UPA, ER
from random import choice
from bfs import *
from provided import targeted_order
def random_order(ugraph):
    """
    computes a random order for attack
    """
    nodes = ugraph.keys()
    attack_order = []
    for dummy_idx in range(len(nodes)):
        attacked = choice(nodes)
        attack_order.append(attacked)
        nodes.remove(attacked)

    return attack_order

def plot(resilience_er, resilience_upa, resilience_ntwk):
    """
    Plots a log-log plot
    """
    
    #pyplot.clf()
    #pyplot.xscale(scale)
    #pyplot.yscale(scale)
    pyplot.title('graph_resilience_under_connectivity_attack')
    pyplot.xlabel('removed_nodes')
    pyplot.ylabel('size_of_largest_connected_component')
    removed, size = zip(*(resilience_er))
    pyplot.plot(removed, size, 'r-', label='er_resilience p=0.003')
    removed, size = zip(*(resilience_upa))
    pyplot.plot(removed, size, 'b-', label='upa_resilience m=3')
    removed, size = zip(*(resilience_ntwk))
    pyplot.plot(removed, size, 'y-', label='network_resilience')
    pyplot.legend()
    pyplot.ylim(ymin=0)
    pyplot.savefig('graph_resilience_connectivity.png', bbox_inches='tight')
    pyplot.show()

def compute_plot(graph):
    attack_order = targeted_order(graph)
    removed = range(len(graph) + 1)
    resilience = compute_resilience(graph, attack_order)
    resilience = zip(removed, resilience)
    return resilience

def plot_resilience(graph1, graph2, graph3):
    resilience_er = compute_plot(graph1)
    resilience_upa = compute_plot(graph2)
    resilience_ntwk = compute_plot(graph3)
    plot(resilience_er, resilience_upa, resilience_ntwk)

plot_resilience(ER, UPA, NETWORK)
