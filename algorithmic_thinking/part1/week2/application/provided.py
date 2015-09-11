"""
provided code for application portion of Module 2
"""

# general imports
import urllib2
import random
#import time
import math

# CodeSkulptor import
#import simpleplot
#import codeskulptor
#codeskulptor.set_timeout(60)

# Desktop imports
#import matplotlib.pyplot as plt


############################################
# Provided code

def copy_graph(graph):
    """
    Make a copy of a graph
    """
    new_graph = {}
    for node in graph:
        new_graph[node] = set(graph[node])
    return new_graph

def delete_node(ugraph, node):
    """
    Delete a node from an undirected graph
    """
    neighbors = ugraph[node]
    ugraph.pop(node)
    for neighbor in neighbors:
        ugraph[neighbor].remove(node)
    
def targeted_order(ugraph):
    """
    Compute a targeted attack order consisting
    of nodes of maximal degree
    
    Returns:
    A list of nodes
    """
    # copy the graph
    new_graph = copy_graph(ugraph)
    
    order = []    
    while len(new_graph) > 0:
        max_degree = -1
        for node in new_graph:
            if len(new_graph[node]) > max_degree:
                max_degree = len(new_graph[node])
                max_degree_node = node
        
        neighbors = new_graph[max_degree_node]
        new_graph.pop(max_degree_node)
        for neighbor in neighbors:
            new_graph[neighbor].remove(max_degree_node)

        order.append(max_degree_node)
    return order
    
def fast_targeted_order(ugraph):
    """
    Compute a targeted attack order consisting
    of nodes of maximal degree
    
    Returns:
    A list of nodes
    """
    new_graph = copy_graph(ugraph)
    size = len(new_graph)
    degree_sets = []
    for degree in range(size):
        degree_sets.append(set([]))
    for node in range(size):
        degree = len(new_graph[node])
        degree_sets[degree].add(node)
    attack_order = []
    count = 0
    degrees = range(size-1, -1, -1)
    for degree in degrees:
        while len(degree_sets[degree]) != 0:
            count += 1
            node = degree_sets[degree].pop()
            for neighbor in new_graph[node]:
                nei_deg = len(new_graph[neighbor])
                degree_sets[nei_deg].remove(neighbor)
                degree_sets[nei_deg - 1].add(neighbor)

            attack_order.append(node)
            delete_node(new_graph, node)
    return attack_order
GRAPH1 = {0: set([1, 4, 5]),
             1: set([0, 2, 4]),
             2: set([1, 5]),
             3: set([6]),
             4: set([0, 1]),
             5: set([0, 2]),
             6: set([3])}
"""
from graphs import UPA
from time import time
start = time()
x = targeted_order(UPA)[1]
end = time()
print 'took', end-start, 'seconds'
start = time()
y = fast_targeted_order(UPA)[1]
end = time()

print 'fast took', end-start, 'seconds'
print UPA[x]
print x,y
"""
##########################################################
# Code for loading computer network graph

NETWORK_URL = "http://storage.googleapis.com/codeskulptor-alg/alg_rf7.txt"


def load_graph(graph_url):
    """
    Function that loads a graph given the URL
    for a text representation of the graph
    
    Returns a dictionary that models a graph
    """
    graph_file = urllib2.urlopen(graph_url)
    graph_text = graph_file.read()
    graph_lines = graph_text.split('\n')
    graph_lines = graph_lines[ : -1]
    
    print "Loaded graph with", len(graph_lines), "nodes"
    
    answer_graph = {}
    for line in graph_lines:
        neighbors = line.split(' ')
        node = int(neighbors[0])
        answer_graph[node] = set([])
        for neighbor in neighbors[1 : -1]:
            answer_graph[node].add(int(neighbor))

    return answer_graph

from graphs import *

def compute_outdegree(graph):
    """computes the average degree of the graph"""
    total_degree = 0
    for node in graph:
        total_degree += len(graph[node])
    avg_degree = total_degree / float(len(graph))
    
    return avg_degree

#print compute_outdegree(UPA)
#average outdegree for the computer network is 5
