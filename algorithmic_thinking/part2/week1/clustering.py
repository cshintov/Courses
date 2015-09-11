"""
Student template code for Project 3
Student will implement five functions:

slow_closest_pair(cluster_list)
fast_closest_pair(cluster_list)
closest_pair_strip(cluster_list, horiz_center, half_width)
hierarchical_clustering(cluster_list, num_clusters)
kmeans_clustering(cluster_list, num_clusters, num_iterations)

where cluster_list is a 2D list of clusters in the plane
"""

import math
import alg_cluster



######################################################
# Code for closest pairs of clusters

def pair_distance(cluster_list, idx1, idx2):
    """
    Helper function that computes Euclidean distance between two clusters in a list

    Input: cluster_list is list of clusters, idx1 and idx2 are integer indices for two clusters
    
    Output: tuple (dist, idx1, idx2) where dist is distance between
    cluster_list[idx1] and cluster_list[idx2]
    """
    return (cluster_list[idx1].distance(cluster_list[idx2]), min(idx1, idx2), max(idx1, idx2))


def slow_closest_pair(cluster_list):
    """
    Compute the distance between the closest pair of clusters in a list (slow)

    Input: cluster_list is the list of clusters
    
    Output: tuple of the form (dist, idx1, idx2) where the centers of the clusters
    cluster_list[idx1] and cluster_list[idx2] have minimum distance dist.       
    """
    result = (float('Inf'), -1, -1)
    for u_idx in range(len(cluster_list)):
        for v_idx in range(len(cluster_list)):
            if(u_idx != v_idx):
                result = min(result, pair_distance(cluster_list, u_idx, v_idx))

    return result



def fast_closest_pair(cluster_list):
    """
    Compute the distance between the closest pair of clusters in a list (fast)

    Input: cluster_list is list of clusters SORTED such that horizontal positions of their
    centers are in ascending order
    
    Output: tuple of the form (dist, idx1, idx2) where the centers of the clusters
    cluster_list[idx1] and cluster_list[idx2] have minimum distance dist.       
    """
    num = len(cluster_list)
    if(num <= 3):
        return slow_closest_pair(cluster_list)

    mid = int(math.floor(num / 2.0))
    left = cluster_list[0:mid]
    right  = cluster_list[mid:]
    left_closest = fast_closest_pair(left)
    right_closest = fast_closest_pair(right)
    result = min(left_closest, (right_closest[0], right_closest[1] + mid, right_closest[2] + mid))
    center = (cluster_list[mid-1].horiz_center() + cluster_list[mid].horiz_center()) / 2.0
    result = min(result, closest_pair_strip(cluster_list, center, result[0]))

    return result

def closest_pair_strip(cluster_list, horiz_center, half_width):
    """
    Helper function to compute the closest pair of clusters in a vertical strip
    
    Input: cluster_list is a list of clusters produced by fast_closest_pair
    horiz_center is the horizontal position of the strip's vertical center line
    half_width is the half the width of the strip (i.e; the maximum horizontal distance
    that a cluster can lie from the center line)

    Output: tuple of the form (dist, idx1, idx2) where the centers of the clusters
    cluster_list[idx1] and cluster_list[idx2] lie in the strip and have minimum distance dist.       
    """
    is_inside = lambda idx: abs(cluster_list[idx].horiz_center() - horiz_center) <= half_width
    strip_indices = [idx for idx in range(len(cluster_list)) if is_inside(idx)]
    strip_indices.sort(key = lambda idx: cluster_list[idx].vert_center())
    size = len(strip_indices)
    result = (float("Inf"), -1, -1)
    for u_idx in range(size-1):
        for v_idx in range(u_idx+1, min(u_idx+3, size-1)+1):
            result = min(result, pair_distance(cluster_list, strip_indices[u_idx], strip_indices[v_idx]))

    return result


######################################################################
# Code for hierarchical clustering


def hierarchical_clustering(cluster_list, num_clusters):
    """
    Compute a hierarchical clustering of a set of clusters
    Note: the function may mutate cluster_list
    
    Input: List of clusters, integer number of clusters
    Output: List of clusters whose length is num_clusters
    """
    while(len(cluster_list) > num_clusters):
        res = fast_closest_pair(cluster_list)
        cluster_list[res[2]].merge_clusters(cluster_list[res[1]])
        cluster_list.pop(res[1])
        cluster_list.sort(key = lambda cluster: cluster.horiz_center())
    return cluster_list


######################################################################
# Code for k-means clustering
def min_idx(cluster, cluster_list):
    """
    Finds the index of the cluster in cluster_list with minimum distance
    from the given cluster
    """
    min_dist = float("Inf")
    m_idx = 0
    for idx, dummy_cluster in enumerate(cluster_list):
        dist = cluster.distance(dummy_cluster)
        if dist < min_dist:
            min_dist = dist
            m_idx = idx
    return m_idx
    
def kmeans_clustering(cluster_list, num_clusters, num_iterations):
    """
    Compute the k-means clustering of a set of clusters
    Note: the function may not mutate cluster_list
    
    Input: List of clusters, integers number of clusters and number of iterations
    Output: List of clusters whose length is num_clusters
    """

    # position initial clusters at the location of clusters with largest populations
    copy_list = [cluster.copy() for cluster in cluster_list]
    old_clusters = sorted(copy_list, key = lambda cluster: cluster.total_population(),reverse = True)[:num_clusters]
    #copy_list = [cluster for cluster in copy_list if cluster not in old_clusters]
    for _ in range(num_iterations):
        new_clusters = [alg_cluster.Cluster(set([]),0,0,0,0.0) for _ in range(num_clusters)]
        for cluster in copy_list:
            closest_idx = min_idx(cluster, old_clusters)
            new_clusters[closest_idx].merge_clusters(cluster)
        old_clusters = new_clusters[:]
    return new_clusters


