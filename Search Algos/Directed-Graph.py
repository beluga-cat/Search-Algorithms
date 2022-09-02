import networkx as nx
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

G = nx.Graph()
po = nx.spring_layout(G)
while True:
    print("Enter 1 for input edges and weight: ")
    print("Enter 2 for input vertices: ")
    a = int(input())
    if(a==1):
        edg1 = int(input("Enter edge1: "))
        edg2 = int(input("Enter edge2: "))
        wei = int(input(f"weight for [{edg1}]==>[{edg2}]: "))
        G.add_edge(edg1,edg2,weight=wei)
    elif(a==2):
        nod = int(input("Enter node: "))
        px = int(input("Enter node position at x: "))
        py = int(input("Enter node position at y: "))
        G.add_node(nod,pos=(px,py))
    else:
        break
    
weight = nx.get_edge_attributes(G,'weight')
pos = nx.get_node_attributes(G,'pos')
nx.draw_networkx(G,pos)
nx.draw_networkx_edge_labels(G,pos,edge_labels=weight)
plt.show()
