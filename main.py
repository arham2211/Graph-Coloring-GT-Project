import networkx as nx
import matplotlib.pyplot as plt
import itertools
import time

def is_valid_coloring(graph, coloring):
    for u, v in graph.edges():
        if coloring[u] == coloring[v]:
            return False
    return True

def greedy_coloring(graph):
    coloring = {}
    for node in graph.nodes():
        adjacent_colors = {coloring.get(neighbor) for neighbor in graph.neighbors(node)}
        coloring[node] = next(color for color in itertools.count() if color not in adjacent_colors)
    return coloring

def read_graph_file(filename):
    with open(filename, 'r') as f:
        n_nodes = int(f.readline().strip())
        n_edges = int(f.readline().strip())
        edges = [tuple(map(int, line.strip().split())) for line in f.readlines()]
    return n_nodes, n_edges, edges

# Measure the start time
start_time = time.time()

# Read graph from file
n_nodes, n_edges, edges = read_graph_file("graph_input.txt")

# Create graph
G = nx.Graph()
G.add_nodes_from(range(n_nodes))
G.add_edges_from(edges)

# Generate layout for the graph
pos = nx.spring_layout(G)

# Plot the original graph
plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
nx.draw(G, pos, with_labels=True, font_weight='bold', node_size=500)
plt.title("Original Graph")

# Color the graph
coloring_result = greedy_coloring(G)
print("\nColoring:", coloring_result)
print("Valid:", is_valid_coloring(G, coloring_result))
print("Number of colors used:", len(set(coloring_result.values())))

# Plot the colored graph
color_map = [coloring_result[node] for node in G.nodes()]

plt.subplot(1, 2, 2)
nx.draw(G, pos, with_labels=True, node_color=color_map, font_weight='bold', node_size=500, cmap=plt.cm.rainbow)
plt.title("Colored Graph")

# Measure the end time
end_time = time.time()

# Calculate and print the total time taken
total_time = end_time - start_time
print(f"\nTotal time taken: {total_time:.4f} seconds")

# Show the plots
plt.show()
