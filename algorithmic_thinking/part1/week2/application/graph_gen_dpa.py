"""
Generate a graph using the UPA generating algorithm
"""
from alg_upa_trial import *
from random import uniform, choice
from deg_dist import *
import test_suite as test
def choose_nodes(num,graph):
    """ choose num nodes from graph based on their indegrees """
    
    v_nodes = graph.keys()
    v1_nodes = []
    indegree = compute_in_degrees(graph)
    totindeg = sum(indegree.values())
    while len(v1_nodes) != num:
        node = choice(v_nodes)
        prob = float((indegree[node] + 1)) / (totindeg + len(v_nodes))
        rand = uniform(0,1)
        if rand < prob:
            v1_nodes.append(node)
    return v1_nodes

def generate_digraph(n_nodes, m_nodes):
    """
    Generate a graph using the modified UPA generating algorithm
    """
    dpatrial = UPATrial(m_nodes)

    graph = make_complete_graph(m_nodes)
    for node in range(m_nodes,n_nodes):
        chosen_nodes = dpatrial.run_trial(m_nodes)
        #print chosen_nodes
        graph[node] = set(chosen_nodes)

    return graph

def generate_undigraph(n_nodes, m_nodes):
    """
    Generate an undirected graph using the modified UPA generating algorithm
    """
    upatrial = UPATrial(m_nodes)
    graph = make_complete_graph(m_nodes)
    for node in range(m_nodes,n_nodes):
        chosen_nodes = upatrial.run_trial(m_nodes)
        graph[node] = set(chosen_nodes)
        for nod in chosen_nodes:
            graph[nod].add(node)
    return graph

#test.run_suite(generate_undigraph)
graph = generate_undigraph(50, 4)
total = 0
for node in graph:
    total += len(graph[node])
#print total/2

def compute_outdegree(graph):
    """computes the average degree of the graph"""
    total_degree = 0
    for node in graph:
        total_degree += len(graph[node])
    avg_degree = total_degree / float(len(graph))
    
    return avg_degree
#print "UPA = ",generate_undigraph(1239,3)
from graphs import NETWORK,UPA
def edges(graph):
    total = 0
    for node in graph:
        total += len(graph[node])
    print 'edges',total/2
    print 'nodes',len(graph)

#print 'network'
#edges(NETWORK)
#print 'UPA'
#edges(UPA)
