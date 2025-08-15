import heapq  # For priority queue implementation

# ------------------------------
# Dijkstra's Algorithm for Directed Positive-Weighted Graphs
# ------------------------------

def dijkstra(graph, start):
    """
    Finds the shortest paths from the start node to all other nodes in a directed, 
    positively weighted graph using Dijkstra's algorithm.
    
    Parameters:
    graph (dict): Adjacency list representation of the graph where:
                  - Keys are nodes
                  - Values are lists of tuples (neighbor, weight)
    start: The starting node
    
    Returns:
    dict: Shortest distance from start to each node
    """
    
    # Step 1: Initialize distances
    # Distance to every node is set to infinity initially, except the start node (set to 0)
    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    # Step 2: Create a priority queue to pick the smallest distance node first
    # Each element in the queue: (distance_so_far, node)
    priority_queue = [(0, start)]  # Start with the source node having distance 0

    # Step 3: Keep track of visited nodes to avoid reprocessing
    visited = set()

    while priority_queue:
        # Step 4: Extract node with smallest known distance
        current_distance, current_node = heapq.heappop(priority_queue)

        # Step 5: If we already visited this node, skip
        if current_node in visited:
            continue
        visited.add(current_node)

        # Step 6: Update distances to neighbors
        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight

            # If we found a shorter path to neighbor, update
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances


# ------------------------------
# Example Usage
# ------------------------------
if __name__ == "__main__":
    # Example directed graph (positive weights only)
    # Format: graph[node] = [(neighbor, weight), ...]
    graph = {
        'A': [('B', 2), ('C', 5)],
        'B': [('C', 1), ('D', 4)],
        'C': [('D', 1)],
        'D': []
    }

    start_node = 'A'
    shortest_paths = dijkstra(graph, start_node)

    print(f"Shortest distances from node {start_node}:")
    for node, dist in shortest_paths.items():
        print(f"{node}: {dist}")


# ------------------------------
# Time Complexity (Rackstraw Rules Breakdown)
# ------------------------------
# Let:
#   V = number of vertices (nodes)
#   E = number of edges
#
# Steps:
#   1. Initializing distances → O(V)
#   2. Each vertex is pushed & popped from the priority queue at most once → O(V log V)
#   3. Each edge is examined once; each relaxation may push into queue → O(E log V)
#
# Overall Time Complexity:
#   O((V + E) log V) using a binary heap priority queue
#
# Space Complexity:
#   O(V) for distances + O(V) for visited + O(E) for adjacency list storage
