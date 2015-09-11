""" generate random clusters(points in -1,1 square) """

import math
import random

def gen_random_clusters(num_clusters):
    """ generate a list of random points in the -1,1 square """
    point = lambda: (random.uniform(-1, 1), random.uniform(-1, 1))
    return [point() for _ in range(num_clusters)]

def distance(pnt1, pnt2):
    """
    Compute the Euclidean distance between two clusters
    """
    vert_dist = pnt1[1] - pnt2[1]
    horiz_dist = pnt1[0] - pnt2[0]
    return math.sqrt(vert_dist ** 2 + horiz_dist ** 2)


def pair_distance(cluster_list, idx1, idx2):
    return (distance(cluster_list[idx1],cluster_list[idx2]), min(idx1, idx2), max(idx1, idx2))

def slow_closest_pair(cluster_list):
    """
    """
    result = (float('Inf'), -1, -1)
    for u_idx in range(len(cluster_list)):
        for v_idx in range(len(cluster_list)):
            if(u_idx != v_idx):
                result = min(result, pair_distance(cluster_list, u_idx, v_idx))

    return result


def fast_closest_pair(cluster_list):
    """
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
    center = (cluster_list[mid-1][0] + cluster_list[mid][0]) / 2.0
    result = min(result, closest_pair_strip(cluster_list, center, result[0]))

    return result

def closest_pair_strip(cluster_list, horiz_center, half_width):
    is_inside = lambda idx: abs(cluster_list[idx][0] - horiz_center) <= half_width
    strip_indices = [idx for idx in range(len(cluster_list)) if is_inside(idx)]
    strip_indices.sort(key = lambda idx: cluster_list[idx][1])
    size = len(strip_indices)
    result = (float("Inf"), -1, -1)
    for u_idx in range(size-1):
        for v_idx in range(u_idx+1, min(u_idx+3, size-1)+1):
            result = min(result, pair_distance(cluster_list, strip_indices[u_idx], strip_indices[v_idx]))

    return result

if __name__ == "__main__":
    clusters = gen_random_clusters(10)
    print slow_closest_pair(clusters)
    print fast_closest_pair(clusters)
