import networkx as nx
import matplotlib.pyplot as plt
import warnings

# warnings.simplefilter('ignore')

# ----Symmetric Networks (undirected)
G_symmetric = nx.Graph()

G_symmetric.add_edge('Steven', 'Laura')
G_symmetric.add_edge('Steven', 'Marc')
G_symmetric.add_edge('Steven', 'John')
G_symmetric.add_edge('Steven', 'Michelle')
G_symmetric.add_edge('Laura', 'Michelle')
G_symmetric.add_edge('Michelle', 'Marc')
G_symmetric.add_edge('George', 'John')
G_symmetric.add_edge('George', 'Steven')

# print(nx.info(G_symmetric))
# plt.figure(figsize=(5,5))
# nx.draw_networkx(G_symmetric)
# plt.show()

# ----Asymmetric networks

G_asymmetric = nx.DiGraph()

G_asymmetric.add_edge('A', 'B')
G_asymmetric.add_edge('A', 'D')
G_asymmetric.add_edge('C', 'A')
G_asymmetric.add_edge('D', 'E')

# nx.spring_layout(G_asymmetric)
# nx.draw_networkx(G_asymmetric)
# plt.show()


# ----Weighted Networks

G_weighted = nx.Graph()

G_weighted.add_edge('Steven',  'Laura',   weight=25)
G_weighted.add_edge('Steven',  'Marc',    weight=8)
G_weighted.add_edge('Steven',  'John',    weight=11)
G_weighted.add_edge('Steven',  'Michelle', weight=1)
G_weighted.add_edge('Laura',   'Michelle', weight=1)
G_weighted.add_edge('Michelle', 'Marc',    weight=1)
G_weighted.add_edge('George',  'John',    weight=8)
G_weighted.add_edge('George',  'Steven',  weight=4)

elarge = [(u, v) for (u, v, d) in G_weighted.edges(data=True) if d['weight'] > 8]
esmall = [(u, v) for (u, v, d) in G_weighted.edges(data=True) if d['weight'] <= 8]

# pos = nx.circular_layout(G_weighted)  # positions for all nodes
#
# nx.draw_networkx_edges(G_weighted, pos, edgelist=elarge,width=6)
# nx.draw_networkx_edges(G_weighted, pos, edgelist=esmall,width=6, alpha=0.5, edge_color='b', style='dashed')
#
# nx.draw_networkx_labels(G_weighted, pos, font_size=20, font_family='sans-serif')

# plt.axis('off')
# plt.show()


# ---- Clustering Coefficient

# print(nx.clustering(G_symmetric,'Michelle'))
# print(nx.clustering(G_symmetric,'Laura'))
# print(nx.average_clustering(G_symmetric))

# ---- Network Distance Measures
# print(nx.degree(G_symmetric, 'Michelle')) # Degree i.e. number of connections
#
# print(nx.shortest_path(G_symmetric, 'Michelle', 'John')) # shortest path
# print(nx.shortest_path_length(G_symmetric, 'Michelle', 'John')) # shortest path length

# S = nx.bfs_tree(G_symmetric, 'Steven')  # breadth first search, reach whole network through single node
# nx.draw_networkx(S)

# M = nx.bfs_tree(G_symmetric, 'Michelle')
# nx.draw_networkx(M)
# plt.show()

# print(nx.eccentricity(G_symmetric, 'Michelle')) # largest distance between A and all other nodes
# print(nx.eccentricity(G_symmetric, 'Steven'))

# ---- Centrality Measures (most important nodes in the network)

# Degree centrality (measure of the number of connections each node has within the network)

# print(nx.degree_centrality(G_symmetric))

# Eigenvector Centrality (how well are the nodes connected to other important nodes)
print(nx.eigenvector_centrality(G_symmetric))

# Closeness Centrality (importance determined by closeness to other nodes)
print(nx.closeness_centrality(G_symmetric))

# Betweenness centrality
#print(nx.betweenness_centrality(G_symmetric))
pos = nx.spring_layout(G_symmetric)
betCent = nx.betweenness_centrality(G_symmetric, normalized=True, endpoints=True)

node_color = [20000.0 * G_symmetric.degree(v) for v in G_symmetric]
node_size = [v * 10000 for v in betCent.values()]
plt.figure(figsize=(10, 10))

nx.draw_networkx(G_symmetric, pos=pos, with_labels=True, node_color=node_color, node_size=node_size)
plt.axis('off')
plt.show()
sorted(betCent, key=betCent.get, reverse=True)[:5]





