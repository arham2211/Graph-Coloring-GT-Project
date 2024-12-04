import random

def generate_graph_file(filename):
    n_nodes = int(input("Enter the number of vertices: "))
    n_edges = int(input("Enter the number of edges: "))
    
    if n_edges > n_nodes * (n_nodes - 1) // 2:
        print("Too many edges for the given number of vertices. Adjusting to maximum possible edges.")
        n_edges = n_nodes * (n_nodes - 1) // 2
    
    edges = set()
    while len(edges) < n_edges:
        v1 = random.randint(0, n_nodes - 1)
        v2 = random.randint(0, n_nodes - 1)
        if v1 != v2:
            edges.add((min(v1, v2), max(v1, v2)))
    
    with open(filename, 'w') as f:
        f.write(f"{n_nodes}\n")
        f.write(f"{n_edges}\n")
        for edge in edges:
            f.write(f"{edge[0]} {edge[1]}\n")

if __name__ == "__main__":
    generate_graph_file("graph_input.txt")
