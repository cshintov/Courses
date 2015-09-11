"""
Generate a graph using the modified ER generating algorithm
"""

from random import uniform


def generate_digraph(num, prob):
    """
    Generate a graph using the modified ER generating algorithm
    """

    graph = {}

    for node_i in range(num):
        for node_j in range(num):
            prob_a = uniform(0, 1)
            if node_i != node_j and prob_a < prob:
                current_i = graph.setdefault(node_i, set([]))
                current_i.add(node_j)

    return graph

def generate_undigraph(num, prob):
    """
    Generate a graph using the modified ER generating algorithm
    """

    graph = {}

    for node_i in range(num):
        for node_j in range(num):
            prob_a = uniform(0, 1)
            if node_i != node_j and prob_a < prob:
                current_i = graph.setdefault(node_i, set([]))
                current_i.add(node_j)
                current_j = graph.setdefault(node_j, set([]))
                current_j.add(node_i)

    return graph
#g = generate_undigraph(1239,0.003)
#print generate_digraph(5,0.5)
from graphs import *
def edges(graph):
    total = 0
    for node in graph:
        total += len(graph[node])
    print 'edges',total/2
    print 'nodes',len(graph)

print 'network'
edges(NETWORK)
print 'er'
edges(ER)
