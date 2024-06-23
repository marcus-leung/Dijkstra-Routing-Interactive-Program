import heapq

def dijkstra(graph, start):
    
    queue = [] #initalize queue
    heapq.heappush(queue, (0, start)) #push start node first
    distances = {node: float('inf') for node in graph.nodes} #initalize distance dict
    distances[start] = 0
    shortest_path_tree = {}
    visited_nodes = set()  #initialize set for visited nodes

    while queue:
        current_distance, current_node = heapq.heappop(queue) #pop shortest distance node from queue

        if current_node in visited_nodes:
            continue

        visited_nodes.add(current_node)

        if current_distance > distances[current_node]: #skip if current distance is > than known shortest distance
            continue

        for neighbor, weight in graph[current_node].items(): #iterate over neighbors of current node
            if neighbor in visited_nodes:
                continue

            distance = current_distance + weight['weight'] #calculate distance

            if distance < distances[neighbor]: #if shorter path found, update 
                distances[neighbor] = distance #update distance 
                shortest_path_tree[neighbor] = current_node #add to shortest path tree
                heapq.heappush(queue, (distance, neighbor)) #push to queue

    return distances, shortest_path_tree

def shortest_path(graph, start, end):
    distances, shortest_path_tree = dijkstra(graph, start)
    path = []
    current_node = end

    while current_node != start:
        path.append(current_node)
        current_node = shortest_path_tree[current_node]
    path.append(start)
    path.reverse()

    return path, distances[end]

def dijkstra_walkthrough(graph, start):
    
    queue = [] #initalize queue
    heapq.heappush(queue, (0, start)) #push start node first
    distances = {node: float('inf') for node in graph.nodes} #initalize distance dict
    distances[start] = 0
    shortest_path_tree = {}
    visited_nodes = set()  #initialize set for visited nodes

    print("Initial state:")
    print(f"Queue: {queue}")
    print(f"Distances: {distances}\n")
    print(f"Visited Nodes: {{}}")

    while queue:
        current_distance, current_node = heapq.heappop(queue) #pop shortest distance node from queue
        print(f"Popped node {current_node} with distance {current_distance} from queue")

        if current_node in visited_nodes:
            print(f"{current_node} is already visited, skipping...")
            continue

        visited_nodes.add(current_node)
        print(f"Marking {current_node} as visited. Visited nodes now: {visited_nodes}")

        if current_distance > distances[current_node]: #skip if current distance is > than known shortest distance
            print(f"Skipping node {current_node} as current distance {current_distance} is greater than known shortest distance {distances[current_node]}")
            continue

        print(f"Now iterating over each neighbor of {current_node}:")
        for neighbor, weight in graph[current_node].items(): #iterate over neighbors of current node
            if neighbor in visited_nodes:
                print(f"{neighbor} is already visited, skipping...")
                continue
            
            distance = current_distance + weight['weight'] #calculate distance

            print(f"Checking neighbor {neighbor} with edge weight {weight['weight']}")
            print(f"Current known distance to {neighbor}: {distances[neighbor]}")

            if distance < distances[neighbor]: #if shorter path found, update 
                distances[neighbor] = distance #update distance 
                shortest_path_tree[neighbor] = current_node #add to shortest path tree
                heapq.heappush(queue, (distance, neighbor)) #push to queue

                print(f"Updated distance for {neighbor} to {distance}")
                print(f"Added {neighbor} to the queue with priority {distance}")
                print(f"Updated distances: {distances}")
                print(f"Current queue: {queue}\n")
            else:
                print(f"No update required for {neighbor}, current shortest distance is {distances[neighbor]}\n")

    print("\nFinal distances: ", distances)
    print("Shortest path tree: ", shortest_path_tree)

    return distances, shortest_path_tree