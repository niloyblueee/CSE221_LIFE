# import collections # Removed as per your request

def bfs(graph, start_node):
    """
    Performs a Breadth-First Search (BFS) on a graph.

    Args:
        graph (dict): An adjacency list representation of the graph.
                      Keys are nodes, and values are lists of adjacent nodes.
                      Example: {'A': ['B', 'C'], 'B': ['D'], 'C': ['E'], 'D': [], 'E': []}
        start_node: The starting node for the BFS.

    Returns:
        tuple: A tuple containing two dictionaries:
               - distances (dict): Stores the shortest distance from the start_node to each node.
               - predecessors (dict): Stores the predecessor of each node in the BFS path.
    """

    # Initialize vertices:
    # 'color' tracks the state of the node (WHITE: unvisited, GREY: visited but neighbors not explored, BLACK: visited and neighbors explored)
    # 'd' stores the distance from the start_node
    # 'p' stores the predecessor node in the BFS path
    colors = {node: 'WHITE' for node in graph}
    distances = {node: float('inf') for node in graph}
    predecessors = {node: None for node in graph}

    # Initialize Q (Queue) with the start_node
    # Using a standard list as a queue. Note: list.pop(0) is less efficient than collections.deque.popleft()
    q = [] 

    # Set initial properties for the start_node
    colors[start_node] = 'GREY'
    distances[start_node] = 0
    q.append(start_node)

    # While Q is not empty
    while q:
        # u = RemoveTop(Q) - Get the node from the front of the queue
        u = q.pop(0) # Using pop(0) for list to simulate deque.popleft()

        # For each v in u->adj (for each neighbor of u)
        for v in graph.get(u, []):  # .get(u, []) handles cases where a node might not have neighbors
            if colors[v] == 'WHITE':
                # v->color = GREY - Mark neighbor as visited
                colors[v] = 'GREY'
                # v->d = u->d + 1 - Update distance
                distances[v] = distances[u] + 1
                # v->p = u - Set predecessor
                predecessors[v] = u
                # Enqueue(Q, v) - Add neighbor to the queue
                q.append(v)
        
        # u->color = BLACK - Mark u as fully explored
        colors[u] = 'BLACK'

    return distances, predecessors

# --- Example Usage ---
if __name__ == "__main__":
    # Define a sample graph using an adjacency list
    sample_graph = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F'],
        'D': [],
        'E': ['F'],
        'F': []
    }

    start_node = 'A'
    print(f"Performing BFS starting from node: {start_node}")
    
    # Run BFS
    dist, pred = bfs(sample_graph, start_node)

    print("\nDistances from start node:")
    for node, distance in dist.items():
        print(f"  {node}: {distance}")

    print("\nPredecessors in BFS path:")
    for node, predecessor in pred.items():
        print(f"  {node}: {predecessor}")

    # Another example with a disconnected graph or different start
    print("\n--- Another Example (starting from 'C') ---")
    start_node_2 = 'C'
    dist2, pred2 = bfs(sample_graph, start_node_2)
    print(f"Performing BFS starting from node: {start_node_2}")
    print("\nDistances from start node:")
    for node, distance in dist2.items():
        print(f"  {node}: {distance}")

    print("\nPredecessors in BFS path:")
    for node, predecessor in pred2.items():
        print(f"  {node}: {predecessor}")
