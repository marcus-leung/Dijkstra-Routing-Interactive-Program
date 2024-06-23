from graph import create_graph, visualize_graph, create_custom_graph, visualize_shortest_path
from dijkstra import shortest_path, dijkstra, dijkstra_walkthrough

def main_menu():
    print("\n" + "========================================")
    print("LEARN ABOUT NETWORK ROUTING")
    print("1. What is Network Routing?")
    print("2. Explore various routing algorithms and their applications.")
    print("3. Fun facts")
    print("4. Learn Dijkstra's Algorithm")
    print("Q. Quit")
    print("========================================" + "\n")

def dijkstra_menu():
    print("\n" + "========================================")
    print("LEARN DIJKSTRRA'S ALGORITHM")
    print("1. What is Dijkstra’s algorithm and how does it work?")
    print("2. Make your own graph")
    print("3. Premade graph")
    print("Q. Quit")
    print("========================================" + "\n")

def graph_operations_menu():
    print("\n" + "========================================")
    print("GRAPH OPERATIONS")
    print("1. Display the network graph and its connections")
    print("2. Find the shortest path between two nodes")
    print("3. Routing table of a node")
    print("4. Visualize the shortest path between two nodes")
    print("5. Show Dijkstra's algorithm walkthrough for a node")
    print("Q. Quit")
    print("========================================" + "\n")

def network_routing_q():
    print("### Network Routing ###\n")

    print("Network routing is a fundamental concept in computer networks, ensuring the efficient transmission of data across interconnected devices.")
    print("At its core, routing involves selecting the optimal path for data packets to travel from a source to a destination within a network.")
    print("This process is crucial for maintaining network performance, reliability, and scalability.\n")

    print("In routing, intermediary devices such as routers play a critical role.")
    print("They receive data packets, examine their destination IP addresses, and determine the best path using routing tables.")
    print("These tables can be populated through static routes, where paths are manually set, or dynamic routing protocols,")
    print("which automatically adjust routes based on current network conditions.\n")

    print("Dynamic routing protocols, such as OSPF (Open Shortest Path First) and BGP (Border Gateway Protocol),")
    print("enable routers to discover remote networks, maintain up-to-date routing information, and choose the best paths based on various metrics like bandwidth or hop count.")
    print("This adaptability allows networks to be self-healing, automatically finding new paths when current ones fail.\n")

    print("Understanding network routing is essential for anyone studying computer networks,")
    print("as it underpins the ability to design, manage, and troubleshoot complex network infrastructures.")
    print("This knowledge ensures that data can be efficiently and reliably transmitted across the globe, connecting billions of devices and enabling the internet as we know it.\n")


def explore_q():
    print("### Explore Various Routing Algorithms and Their Applications ###\n")

    print("As part of our interactive network routing Python program, let's dive into the fascinating world of routing algorithms and their real-world applications.")
    print("Routing algorithms are essential for determining the best paths for data packets to travel across a network.")
    print("By understanding these algorithms, we can appreciate how data seamlessly moves from one place to another, even across vast and complex networks like the internet.\n")

    print("#### Dijkstra's Algorithm ####\n")
    print("Dijkstra's algorithm is one of the most well-known routing algorithms. It calculates the shortest path between nodes in a graph, which represents the network.")
    print("This algorithm is widely used in OSPF (Open Shortest Path First) routing protocol, which is common in large enterprise networks.")
    print("By finding the shortest path, OSPF ensures that data travels the quickest route, reducing latency and improving network performance.\n")
    print("#### Bellman-Ford Algorithm ####\n")
    print("The Bellman-Ford algorithm is another important routing algorithm, particularly known for its use in the RIP (Routing Information Protocol).")
    print("Unlike Dijkstra's algorithm, Bellman-Ford can handle negative weights, making it versatile but slower.")
    print("RIP uses hop count as a metric, with each hop representing a step from one router to the next.")
    print("Although RIP is simpler and less efficient than OSPF, it's still used in smaller, simpler networks where ease of configuration is a priority.\n")
    print("#### BGP (Border Gateway Protocol) ####\n")
    print("BGP is a path vector protocol essential for routing between large networks, like those managed by internet service providers (ISPs).")
    print("Unlike OSPF and RIP, which are used within individual networks, BGP manages how packets are routed between autonomous systems (AS),")
    print("which are large collections of IP networks under a single administrative domain.")
    print("BGP considers various attributes, such as path length, policy constraints, and rule-based routing decisions, to ensure data is efficiently routed across the global internet.\n")
    print("#### Applications in Real-World Networks ####\n")
    print("Each routing algorithm has its specific applications based on the network size, complexity, and requirements:\n")
    print("  - OSPF (using Dijkstra's algorithm): Ideal for large enterprise networks due to its fast convergence and scalability.")
    print("  - RIP (using Bellman-Ford algorithm): Suitable for smaller networks where simplicity is preferred over efficiency.")
    print("  - BGP: Essential for routing between large networks, particularly in ISP and global internet backbones.")

def facts_q():
    print("#### Fun Facts ####\n")
    print("1. The concept of packet switching, which is fundamental to modern network routing, was developed by Paul Baran and Donald Davies in the 1960s.")
    print("   Packet switching allows data to be broken into smaller packets and sent independently across the network, increasing efficiency and reliability.\n")
    print("2. Dijkstra's algorithm is not only used in computer networks but also in various applications like Google Maps and GPS systems to find the shortest routes.\n")
    print("3. The algorithm was originally designed to find the shortest path between two cities in the Netherlands. Dijkstra's inspiration came while drinking coffee at a café!\n")
    print("4. The Border Gateway Protocol (BGP) is often referred to as the backbone of the internet. It manages how packets are routed across different autonomous systems,")
    print("   ensuring that data can travel across vast distances and different network infrastructures.\n")
    print("5. In 1983, the ARPANET adopted the TCP/IP protocol suite, which included the use of packet switching. This transition was a pivotal moment that marked the beginning of the modern Internet.\n")
    print("6. In 1997, the internet experienced a major outage caused by a BGP misconfiguration at an ISP, highlighting the critical role of proper routing configurations and the interdependence of global networks.\n")
    print("7. The Open Shortest Path First (OSPF) protocol, developed in the late 1980s, became the standard for internal routing within large enterprise networks due to its efficiency and ability to quickly adapt to changes in network topology.\n")
    print("8. In 1990, Tim Berners-Lee invented the World Wide Web, which relies heavily on routing protocols like HTTP (built on TCP/IP) to transfer data between web servers and browsers.\n")
    print("9. The Internet Assigned Numbers Authority (IANA) is responsible for the global coordination of the DNS Root, IP addressing, and other Internet protocol resources, ensuring consistent and accurate routing of data.\n")
    print("10. In 2008, the undersea fiber optic cables that connect continents experienced multiple cuts due to an earthquake, demonstrating the resilience and adaptability of global routing protocols in rerouting traffic through alternative paths.\n")
   
def dijkstra_q():
    print("\n### What is Dijkstra's Algorithm and How Does It Work? ###\n")
    print("Dijkstra's Algorithm is a fundamental algorithm in computer science used to find the shortest paths between nodes in a graph.")
    print("Named after its creator, Edsger Dijkstra, the algorithm was first described in 1959 and has since become an essential tool in network routing and pathfinding applications.\n")
    print("Time Complexity:")
    print("    - The time complexity of Dijkstra's algorithm is O(V^2) with a simple array-based implementation.")
    print("    - With a priority queue (min-heap), as implemented in our code, the time complexity is improved to O((V + E) log V), where V is the number of vertices and E is the number of edges.")
    print("\n")
    print("### How Dijkstra's Algorithm Works ###\n")
    print("Dijkstra's Algorithm is a fundamental algorithm used in networking to find the shortest path between nodes in a graph. Here's how it works in our code:\n")

    print("1. Initialization:")
    print("    - We initialize a priority queue to manage the nodes to be explored.")
    print("    - We push the start node into the queue with a distance of 0.")
    print("    - We create a distances dictionary to store the shortest known distance to each node, initialized to infinity for all nodes except the start node, which is set to 0.")
    print("    - We create an empty dictionary shortest_path_tree to keep track of the shortest path tree.\n")
    print("2. Processing Nodes:")
    print("    - We enter a loop that continues until the priority queue is empty.")
    print("    - In each iteration, we pop the node with the smallest distance from the queue.")
    print("    - We skip this node if the current distance is greater than the known shortest distance for this node.\n")

    print("3. Updating Distances:")
    print("    - For each neighbor of the current node, we calculate the distance from the start node to this neighbor through the current node.")
    print("    - If this distance is shorter than the known shortest distance to the neighbor, we update the shortest distance and add the current node to the shortest path tree.")
    print("    - We push the neighbor into the priority queue with the updated distance.\n")

    print("4. Constructing the Shortest Path:")
    print("    - Once we have the shortest distances and the shortest path tree, we construct the shortest path from the start node to the end node.")
    print("    - We start from the end node and trace back through the shortest path tree to the start node, adding each node to the path.")
    print("    - Finally, we reverse the path to get the correct order from start to end.\n")

def main():
    graph = None

    while True:
        main_menu()
        choice = input("Select an option: ").strip().upper()

        if choice == '1':
            network_routing_q()
        elif choice == '2':
            explore_q()
        elif choice == '3':
            facts_q()
        elif choice == '4':
            while True:
                dijkstra_menu()
                dijkstra_choice = input("Select an option: ").strip().upper()

                if dijkstra_choice == '1':
                    dijkstra_q()
                elif dijkstra_choice == '2':
                    graph = create_custom_graph()
                    while True:
                        graph_operations_menu()
                        graph_operations_choice = input("Select an option: ").strip().upper()

                        if graph_operations_choice == '1':
                            visualize_graph(graph)
                        elif graph_operations_choice == '2':
                            start = input("Enter the start node (letter): ").strip().upper()
                            end = input("Enter the end node (letter): ").strip().upper()
                            path, distance = shortest_path(graph, start, end)
                            print(f"Shortest path from {start} to {end}: {' -> '.join(path)} with distance {distance}")
                        elif graph_operations_choice == '3':
                            node = input("Enter a node to display its routing table (letter): ").strip().upper()
                            distances, _ = dijkstra(graph, node)
                            print(f"Routing table for {node}:")
                            for destination, distance in distances.items():
                                print(f"To {destination}: {distance}")
                        elif graph_operations_choice == '4':
                            start = input("Enter the start node (letter): ").strip().upper()
                            end = input("Enter the end node (letter): ").strip().upper()
                            path, distance = shortest_path(graph, start, end)
                            visualize_shortest_path(graph, path)
                            print(f"Visualized shortest path from {start} to {end} with distance {distance}")
                        elif graph_operations_choice == '5':
                            start = input("Enter the start node (letter): ").strip().upper()
                            distances, shortest_path_tree = dijkstra_walkthrough(graph, start)
                        elif graph_operations_choice == 'Q':
                            break
                        else:
                            print("Invalid option, please try again.")
                elif dijkstra_choice == '3':
                    graph = create_graph()
                    while True:
                        graph_operations_menu()
                        graph_operations_choice = input("Select an option: ").strip().upper()

                        if graph_operations_choice == '1':
                            visualize_graph(graph)
                        elif graph_operations_choice == '2':
                            start = input("Enter the start node (letter): ").strip().upper()
                            end = input("Enter the end node (letter): ").strip().upper()
                            path, distance = shortest_path(graph, start, end)
                            print(f"Shortest path from {start} to {end}: {' -> '.join(path)} with distance {distance}")
                        elif graph_operations_choice == '3':
                            node = input("Enter a node to display its routing table (letter): ").strip().upper()
                            distances, _ = dijkstra(graph, node)
                            print(f"Routing table for {node}:")
                            for destination, distance in distances.items():
                                print(f"To {destination}: {distance}")
                        elif graph_operations_choice == '4':
                            start = input("Enter the start node (letter): ").strip().upper()
                            end = input("Enter the end node (letter): ").strip().upper()
                            path, distance = shortest_path(graph, start, end)
                            visualize_shortest_path(graph, path)
                            print(f"Visualized shortest path from {start} to {end} with distance {distance}")
                        elif graph_operations_choice == '5':
                            start = input("Enter the start node (letter): ").strip().upper()
                            distances, shortest_path_tree = dijkstra_walkthrough(graph, start)
                        elif graph_operations_choice == 'Q':
                            break
                        else:
                            print("Invalid option, please try again.")
                elif dijkstra_choice == 'Q':
                    break
                else:
                    print("Invalid option, please try again.")
        elif choice == 'Q':
            break
        else:
            print("Invalid option, please try again.")

if __name__ == "__main__":
    main()
