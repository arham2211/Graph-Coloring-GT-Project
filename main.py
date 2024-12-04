import networkx as nx
import matplotlib.pyplot as plt
import itertools

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

# Get number of vertices from user
n_nodes = int(input("Enter the number of vertices: "))

# Create graph
G = nx.Graph()
G.add_nodes_from(range(n_nodes))

# Get number of edges from user
n_edges = int(input("Enter the number of edges: "))

# Get edges from user
print("\nEnter edges (vertex pairs, 0-based indexing):")
for i in range(n_edges):
    while True:
        try:
            v1, v2 = map(int, input(f"Edge {i+1} (format: vertex1 vertex2): ").split())
            if 0 <= v1 < n_nodes and 0 <= v2 < n_nodes and v1 != v2:
                G.add_edge(v1, v2)
                break
            else:
                print(f"Invalid vertices! Vertices should be between 0 and {n_nodes-1} and should be different")
        except ValueError:
            print("Invalid input! Please enter two numbers separated by space")

# Color the graph
coloring_result = greedy_coloring(G)
print("\nColoring:", coloring_result)
print("Valid:", is_valid_coloring(G, coloring_result))
print("Number of colors used:", len(set(coloring_result.values())))

# Visualize the graph
color_map = [coloring_result[node] for node in G.nodes()]
nx.draw(G, with_labels=True, node_color=color_map, font_weight='bold', node_size=500)
plt.show()