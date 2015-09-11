""" bfs visited """

from collections import deque
from random import choice
def bfs_visited(ugraph, start_node):
    """ 
    visits the undirected graph in bfs order starting from
    start_node
    """
    que = deque()
    que.append(start_node)
    visited = set([start_node])

    while len(que) != 0:
        node = que.popleft()
        neighbors = ugraph[node]
        for neighbor in neighbors:
            if not neighbor in visited:
                visited.add(neighbor)
                que.append(neighbor)

    return visited

def cc_visited(ugraph):
    """
    takes an undirected graph and returns the list of connected graph-nodes as sets
    """
    connected_components = []
    remaining_nodes = set(ugraph.keys())
    while len(remaining_nodes) != 0:
        node = choice(list(remaining_nodes))
        visited = bfs_visited(ugraph,node)
        connected_components.append(visited)
        remaining_nodes -= visited

    return connected_components

def largest_cc_size(ugraph):
    """
    takes an undirected graph returns the size of the largest connected component
    """
    con_components = cc_visited(ugraph)
    sizes = [len(component) for component in con_components]
    if len(sizes) == 0:
        largest = 0
    else:
        largest = max(sizes)
    return largest

def delete_node(ugraph, del_node):
    """deletes a node from the graph"""
    del ugraph[del_node]
    for node in ugraph:
        ugraph[node] -= set([del_node])

def compute_resilience(ugraph, attack_order):
    """
    takes the undirected graph and list of attack order of nodes , returns the list of largest connected component sizes after removing each node in the given order
    """
    resilience = [largest_cc_size(ugraph)]
    for node in attack_order:
        delete_node(ugraph, node)
        largest = largest_cc_size(ugraph)
        resilience.append(largest)

    return resilience
#import poc_testsuite as test
#test.run_suite(compute_resilience)
