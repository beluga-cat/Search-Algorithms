from graphviz import Graph
import matplotlib.pyplot as plt
import networkx as nx


Graph1 = nx.DiGraph()

Graph1.add_edges_from([(1, 2), (1, 4), (2, 5), (2, 3), (3, 1), (3, 5), (4, 5), (4, 6), (5, 6)])
plt.figure(figsize =(9, 9))
nx.draw_networkx(Graph1,with_labels=True, node_color ='grey', edge_color ='black', node_size =1000)
plt.show()