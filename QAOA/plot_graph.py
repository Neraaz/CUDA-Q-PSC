import networkx as nx
import matplotlib.pyplot as plt

# --- Define graph ---
#nodes = list(range(10))
#edges = [
#    [0, 1], [1, 2], [2, 3], [3, 0],
#    [4, 0], [4, 1], [4, 2], [4, 3],
#    [5, 6], [6, 7], [7, 8], [8, 9],
#    [2, 5], [3, 9]
#]
#nodes: list[int] = [0, 1, 2, 3, 4]
#edges = [[0, 1], [1, 2], [2, 3], [3, 0], [2, 4], [3, 4]]
# Define nodes and edges
nodes = [i for i in range(30)]
edges = [
    [0, 1], [0, 2], [0, 5], [1, 3], [1, 4],
    [2, 6], [2, 7], [3, 8], [3, 9], [4, 10],
    [4, 11], [5, 12], [5, 13], [6, 14], [6, 15],
    [7, 16], [7, 17], [8, 18], [8, 19], [9, 20],
    [9, 21], [10, 22], [10, 23], [11, 24], [11, 25],
    [12, 26], [13, 27], [14, 28], [15, 29],
    # cross connections for complexity
    [5, 10], [7, 9], [13, 17], [18, 23], [19, 25],
    [22, 27], [20, 26], [21, 28], [16, 29], [8, 14]
]
G = nx.Graph()
G.add_nodes_from(nodes)
G.add_edges_from(edges)

# --- MaxCut partition string ---
#partition = "10101"
#partition = "1100110101"
#partition = "1010001001"
#partition = "1010001001"
#partition = "0111001010"
#partition = "1111001010"
#partition = "1100110101"
#partition = "1010101011"
#partition = "1000110101"
#partition = "1000110101"
#partition = "100111111000010000001011111011"
#partition = "011001000111001111110100001100"
#partition = "011001000111001111110100001100"
partition = "100100110011111000111100000001"

# Map partition string to colors
color_map = ["red" if partition[i] == "1" else "blue" for i in nodes]

# --- Identify cut edges (edges crossing partitions) ---
cut_edges = []
same_edges = []
for u, v in edges:
    if partition[u] != partition[v]:
        cut_edges.append((u, v))
    else:
        same_edges.append((u, v))

print(f"Cuts: {len(cut_edges)}\n")
# --- Draw the graph ---
pos = nx.spring_layout(G, seed=42, k=0.5)

plt.figure(figsize=(8, 8))

# Draw nodes
nx.draw_networkx_nodes(
    G, pos,
    node_color=color_map,
    edgecolors="black",
    node_size=1500,
    linewidths=1.5
)

# Draw edges inside partitions (gray)
nx.draw_networkx_edges(G, pos, edgelist=same_edges, width=2, edge_color="gray", alpha=0.5)

# Draw cut edges (highlighted)
nx.draw_networkx_edges(G, pos, edgelist=cut_edges, width=3, edge_color="green", style="dashed")

# Draw labels
nx.draw_networkx_labels(G, pos, font_size=14, font_color="white", font_weight="bold")

plt.title("Max-Cut Partition (red vs blue) with Cut Edges (green dashed)", fontsize=14, fontweight="bold")
plt.axis("off")
plt.savefig("plot.png")
