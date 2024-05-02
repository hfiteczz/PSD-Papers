# 开发时间：2024-05-01_下午 6:24

import matplotlib
import matplotlib.pyplot as plt
import networkx as nx
import transformers


print(f"matplotlib's version: {matplotlib.__version__}")
print(f"networkx's version: {nx.__version__}")
print(f"transformers's version: {transformers.__version__}")


G = nx.Graph()
G.add_nodes_from([4, 3])   #这句话是什么意思？添加什么节点？
edges = [(2,1),(3,2),(4,3),(4,6),(5,3),(6,7),(7,5),(14,5)]
G.add_edges_from(edges)

pos = nx.spring_layout(G, seed=42)
fig, ax = plt.subplots(figsize=(10, 8))

nx.draw(G, pos, with_labels = True, node_size = 3000, font_size = 12, node_color = 'skyblue', font_weight = 'bold',
        alpha = 0.8, linewidths = 0, edge_color = 'gray', ax = ax)
ax.set_title("Draw the Graph")

plt.show()