"""
Computes the degree distribution of a directed graph
"""

import test_suite as test

EX_GRAPH0 = {0: set([1, 2]),
             1: set([]),
             2: set([])}

EX_GRAPH1 = {0: set([1, 4, 5]),
             1: set([2, 6]),
             2: set([3]),
             3: set([0]),
             4: set([1]),
             5: set([2]),
             6: set([])}

EX_GRAPH2 = {0: set([1, 4, 5]),
             1: set([2, 6]),
             2: set([3, 7]),
             3: set([7]),
             4: set([1]),
             5: set([2]),
             6: set([]),
             7: set([3]),
             8: set([1, 2]),
             9: set([0, 4, 5, 6, 7, 3])}


def make_complete_graph(num):
    """
    Makes a complete graph with num nodes
    """
    graph = {}

    if num <= 0:
        return graph

    for node in range(num):
        heads = [head for head in range(num) if head != node]
        graph[node] = set(heads)

    return graph


def compute_in_degrees(digraph):
    """
    computes the in-degrees of all the nodes in the digraph
    """

    in_degrees = {}

    for node in digraph:
        in_degrees.setdefault(node, 0)
        for head in digraph[node]:
            in_degrees[head] = in_degrees.get(head, 0) + 1

    return in_degrees


def in_degree_distribution(digraph):
    """
    Computes the unnormalised degree distribution of the digraph
    """

    in_degrees = compute_in_degrees(digraph)
    degree_dist = {}

    for degree in in_degrees.values():
        degree_dist[degree] = degree_dist.get(degree, 0) + 1

    return degree_dist


def normalize(degree_dist):
    """
    normalizes the degree distribution
    """
    num_nodes = sum(degree_dist.values())
    norm_deg_dist = {}
    
    for degree in degree_dist:
        norm_deg_dist[degree] = degree_dist[degree] / float(num_nodes)
    
    return norm_deg_dist

#test.run_suite(compute_in_degrees,in_degree_distribution,normalize)
