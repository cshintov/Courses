"""
application question 1: computes the log-log plot of the normalized degree distribution
"""

from matplotlib import pyplot,pylab
from deg_dist import *
from graph import g,GRAPH

def plot(norm_dist,scale='log'):
    """
    Plots a log-log plot
    """
    
    degree = norm_dist.keys()
    dist = norm_dist.values()
    pyplot.clf()
    pyplot.xscale(scale)
    pyplot.yscale(scale)
    pyplot.title('normalised distribution')
    pyplot.xlabel('degree')
    pyplot.ylabel('distribution')
    pyplot.plot(degree, dist, 'ro')
    pyplot.savefig('citation-graph.png', bbox_inches='tight')
    pyplot.show()

def plot_distribution(graph):
    in_deg_dist = in_degree_distribution(graph)
    norm_deg_dist = normalize(in_deg_dist)
    #print g
    #print in_deg_dist
    #print norm_deg_dist
    #print sum(norm_deg_dist.values())
    plot(norm_deg_dist)

if __name__ = '__main__':

    plot_distribution(g)
