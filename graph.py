import networkx as nx
import matplotlib.pyplot as plt

def create_graph():
    G = nx.Graph()
    edges = [
        ('A', 'B', 4), ('A', 'C', 2), ('B', 'C', 5), ('B', 'D', 10),
        ('C', 'E', 3), ('E', 'D', 4), ('D', 'F', 11), ('E', 'F', 5)
    ]
    G.add_weighted_edges_from(edges)
    return G

def create_custom_graph():
    G = nx.Graph()
    while True:
        edge = input("Enter an edge (format: node1 node2 weight) or 'done' to finish (letters only for nodes): ").strip().upper()
        if edge == 'DONE':
            break
        try:
            node1, node2, weight = edge.split()
            weight = float(weight)
            G.add_edge(node1, node2, weight=weight)
        except ValueError:
            print("Invalid input. Please enter the edge in the correct format.")
    return G

def visualize_graph(G, path=None):
    pos = nx.spring_layout(G)  #generate layout for visualization
    nx.draw(G, pos, with_labels=True, node_size=700, node_color='lightblue')  #draw nodes and edges
    labels = nx.get_edge_attributes(G, 'weight')  #get edge weights
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)  #draw edge labels

    if path:
        path_edges = list(zip(path, path[1:]))  #create edge list for the path
        nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='r', width=2)  #highlight path edges

    plt.show()  

def visualize_shortest_path(G, path): # highlight the shortest path
    visualize_graph(G, path=path)  
