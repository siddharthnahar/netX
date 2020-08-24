import networkx as nx
import math
import matplotlib.pyplot as plt

G = nx.Graph()
G.add_edge(1, 2)
G.add_edge(2, 3, weight=0.9)
plt.subplot(121)
nx.draw(G)
plt.show()

