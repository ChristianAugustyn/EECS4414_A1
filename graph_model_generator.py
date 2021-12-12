############################################
# EECS 4414 Infomation Networks
# York University Fall 2021
# Assignment 1
# October 25, 2021
# Hong Chen, hjc@my.yorku.ca
# Christian Augustyn, chrisaug@my.yorku.ca
############################################

import networkx as nx
import matplotlib.pyplot as plt
from networkx.classes.function import neighbors
from tabulate import tabulate as tb

n = 1000

#############
# Section A -----------------------------------------------------------------------------------------------
#############

# Erdös-Rényi random graph
er1 = nx.erdos_renyi_graph(n, 0.02002)
er2 = nx.erdos_renyi_graph(n, 0.02002)
er3 = nx.erdos_renyi_graph(n, 0.02002)

# Watts–Strogatz small-world graph
ws1 = nx.watts_strogatz_graph(n, 20, 0.5)
ws2 = nx.watts_strogatz_graph(n, 20, 0.5)
ws3 = nx.watts_strogatz_graph(n, 20, 0.5)

# Barabási–Albert preferential attachment model
ba1 = nx.barabasi_albert_graph(n, 10)
ba2 = nx.barabasi_albert_graph(n, 10)
ba3 = nx.barabasi_albert_graph(n, 10)

graphs = {
    "er1": er1,
    "er2": er2,
    "er3": er3,
    "ws1": ws1,
    "ws2": ws2,
    "ws3": ws3,
    "ba1": ba1,
    "ba2": ba2,
    "ba3": ba3,
}
# graph_names = [
#     "Erdös-Rényi Random Graph 1",
#     "Erdös-Rényi Random Graph 2",
#     "Erdös-Rényi Random Graph 3",
#     "Watts–Strogatz Small-World Graph 1",
#     "Watts–Strogatz Small-World Graph 2",
#     "Watts–Strogatz Small-World Graph 3",
#     "Barabási–Albert Preferential Attachment Model 1",
#     "Barabási–Albert Preferential Attachment Model 2",
#     "Barabási–Albert Preferential Attachment Model 3",
# ]
table = [["Graph", "# Of Nodes", "# Of Edges"]]
gcc_arr = []
for name, g in graphs.items():
    # finds all connected components of the graph
    g_cc = sorted(nx.connected_components(g), key=len, reverse=True)
    # retrieves the largest connected component
    gc = g.subgraph(g_cc[0])
    gcc_arr.append(gc)
    node_count = gc.number_of_nodes()
    edge_count = gc.number_of_edges()

    table.append([name, node_count, edge_count])

print(tb(table, headers="firstrow"))

#############
# Section B -----------------------------------------------------------------------------------------------
#############

#######
# b.i #
#######


def get_degree_distribution(name, G):
    node_degree_dist = [x[1] for x in G.degree()]

    plt.hist(node_degree_dist)
    plt.title(f"[b.i] {name}: Distribution of Node Degrees")
    plt.xlabel("Node Degree")
    plt.ylabel("Count")
    plt.show()


for name, g in zip(graphs.keys(), gcc_arr):
    get_degree_distribution(name, g)


########
# b.ii #
########

def get_local_clusteirng_distribution(name, G):
    clustering_coeff = list(nx.clustering(G).values())
    plt.hist(clustering_coeff)
    plt.title(f"[b.ii] {name}: Distribution of Local Clustering Coefficients")
    plt.xlabel("Clustering Coefficient")
    plt.ylabel("Count")
    plt.show()


for name, g in zip(graphs.keys(), gcc_arr):
    get_local_clusteirng_distribution(name, g)


#########
# b.iii #
#########

for name, g in zip(graphs.keys(), gcc_arr):
    print()
    print(name)
    print(
        f"[b.iii]\tGlobal Clustering Coefficient: {nx.average_clustering(g)}")


###################
# b.iv, b.v, b.vi #
###################

def get_shortest_path_stats(name, G):
    path_length_dict = dict(nx.all_pairs_shortest_path_length(G))
    path_length_per_origin = [list(node.values())
                              for node in path_length_dict.values()]
    path_lengths = [
        length
        for origin_length_list in path_length_per_origin
        for length in origin_length_list
    ]
    # paths of length 0 are ignored
    path_lengths_without_zeros = list(filter(lambda x: x != 0, path_lengths))

    plt.hist(path_lengths)
    plt.title(f"[b.iv] {name}: Distribution of Shortest Path Lengths")
    plt.xlabel("Shortest Path Length")
    plt.ylabel("Count")
    plt.show()

    print()
    print(name)
    print(
        f"[b.v]\tAverage Shortest Path Length: {sum(path_lengths_without_zeros) / len(path_lengths_without_zeros)}"
    )
    print(f"[b.vi]\tDiameter: {max(path_lengths_without_zeros)}")


for name, g in zip(graphs.keys(), gcc_arr):
    get_shortest_path_stats(name, g)
