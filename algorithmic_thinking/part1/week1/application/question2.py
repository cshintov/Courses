"""
application question 1: computes the log-log plot of the normalized degree distribution
"""

from matplotlib import pyplot
from deg_dist import *
from graph import g,GRAPH
from graph_gen_er import *

def plot(dist1, dist2, scale='log'):
    """
    Plots a log-log plot
    """
    
    degree1, dist1 = zip(*(dist1.items()))
    degree2, dist2 = zip(*(dist2.items()))
    #dist = norm_dist.values()
    #pyplot.clf()
    pyplot.xscale(scale)
    pyplot.yscale(scale)
    pyplot.title('normalised distribution')
    pyplot.xlabel('degree')
    pyplot.ylabel('distribution')
    pyplot.plot(degree1, dist1, 'ro',label='er_graph')
    pyplot.plot(degree2, dist2, 'bo',label='citation_graph')
    pyplot.legend()
    pyplot.savefig('er_comparison.png', bbox_inches='tight')
    pyplot.show()

def plot_distribution(graph1,graph2):
    in_deg_dist1 = in_degree_distribution(graph1)
    #print in_deg_dist1 
    norm_deg_dist1 = normalize(in_deg_dist1)
    in_deg_dist2 = in_degree_distribution(graph2)
    norm_deg_dist2 = normalize(in_deg_dist2)
    plot(norm_deg_dist1,norm_deg_dist2)

if __name__ == '__main__':
    
    graph = generate_undigraph(1000,0.2)
    plot_distribution(graph, GRAPH)
    graph = generate_digraph(1000,0.2)
    plot_distribution(graph, GRAPH)
