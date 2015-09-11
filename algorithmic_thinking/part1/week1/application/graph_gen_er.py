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

#print generate_undigraph(5,0.5)
