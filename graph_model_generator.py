import networkx as nx
import matplotlib.pyplot as plt
from networkx.classes.function import neighbors
from tabulate import tabulate as tb

n = 1000

#Section A

#Erdős-Rényi random graph
er1 = nx.erdos_renyi_graph(n, 0.001)
er2 = nx.erdos_renyi_graph(n, 0.5)
er3 = nx.erdos_renyi_graph(n, 0.1)

#Watts–Strogatz small-world graph
ws1 = nx.watts_strogatz_graph(n, 2, 0.5)
ws2 = nx.watts_strogatz_graph(n, 5, 0.5)
ws3 = nx.watts_strogatz_graph(n, 10, 0.5)

#Barabási–Albert preferential attachment model
ba1 = nx.barabasi_albert_graph(n, 2)
ba2 = nx.barabasi_albert_graph(n, 5)
ba3 = nx.barabasi_albert_graph(n, 10)

graphs = {"er1":er1,"er2":er2, "er3":er3, "ws1":ws1, "ws2":ws2, "ws3":ws3, "ba1":ba1, "ba2":ba2, "ba3":ba3}
table = [["Graph", "# Of Nodes", "# Of Edges"]]
gcc_arr = []
for name, g in graphs.items():
    #finds all connected components of the graph
    g_cc = sorted(nx.connected_components(g), key=len, reverse=True)
    #retrieves the largest connected component
    gc = g.subgraph(g_cc[0])
    gcc_arr.append(gc)
    node_count = gc.number_of_nodes()
    edge_count = gc.number_of_edges()

    table.append([name, node_count, edge_count])

print(tb(table, headers='firstrow'))

#Section B

#b.i
# def get_degree_distribution(G):
#     d = []
#     for n in G.nodes():
#         d.append(G.degree(n))
    
#     plt.hist(d)
#     plt.show()

# for g in gcc_arr:
#     get_degree_distribution(g)

#b.ii
def get_local_clusteirng_distribution(G):
    coefficients = []
    n = 1
    for n in G.nodes():
        links = 0
        #get the nodes neighbors
        neighbors = []
        for neighbor in nx.neighbors(G, n):
            neighbors.append(neighbor)

        if len(neighbors) > 1:
            for n1 in neighbors:
                for n2 in neighbors:
                    if G.has_edge(n1, n2):
                        links += 1
 
            links /= 2
            coefficient = links / (len(neighbors) * (len(neighbors) - 1))
            coefficients.append(coefficient)

        print(n)
        n += 1

    return coefficients

for g in gcc_arr:
    c = get_local_clusteirng_distribution(g)
    plt.hist(c)
    plt.show()