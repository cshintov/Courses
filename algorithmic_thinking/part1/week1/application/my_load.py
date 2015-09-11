"""loads the given graph"""

def load_graph(filename):
    f = open(filename)
    txt = f.read()
    adj_list = txt.split('\n')[:-1]
    graph = {}
    for lst in adj_list:
        temp = lst.split()
        graph[temp[0]] = set(temp[1:])
    return graph
print load_graph("graph.txt")
