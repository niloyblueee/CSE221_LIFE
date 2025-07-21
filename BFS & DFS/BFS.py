def bfs(graph, start_node):
    """
    Performs a Breadth-First Search (BFS) on a graph without using collections.deque.

    Args:
        graph (dict): An adjacency list representation of the graph.
        start_node: The node from which to start the BFS.

    Returns:
        list: A list representing the order in which nodes were visited.
    """
    visited = set()
    queue = [] # Using a standard Python list as a queue
    traversal_order = []

    # Enqueue the start node and mark as visited
    queue.append(start_node)
    visited.add(start_node)

    while queue:
        # Dequeue the current node from the front of the list
        # WARNING: list.pop(0) is O(n) operation, making this less efficient for large graphs.
        current_node = queue.pop(0)
        traversal_order.append(current_node)

        # Explore neighbors
        for neighbor in graph.get(current_node, []): 
            """"The dict.get() method in Python is a safe way to 
            access dictionary values. When you call graph.get(current_node, []):
            
            > If current_node exists as a key in graph: The method returns the list of 
            neighbors associated with that current_node. For example,
            if graph = {'A': ['B', 'C']} and current_node is 'A', it will return ['B', 'C'].

            > If current_node does NOT exist as a key in graph: 
            Instead of raising a KeyError (which graph[current_node] would do),
              get() returns the specified default value, which in this case is an empty list []."""

            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor) # Enqueue neighbor to the back of the list
    
    return traversal_order

# --- Example Usage ---
if __name__ == "__main__":
    graph = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F'],
        'D': [],
        'E': ['F'],
        'F': []
    }
    
    print(f"BFS traversal (no deque) starting from 'A': {bfs(graph, 'A')}") # Expected: ['A', 'B', 'C', 'D', 'E', 'F']

    graph_cycled = {
        '0': ['1', '2'],
        '1': ['2'],
        '2': ['0', '3'],
        '3': ['3']
    }
    print(f"BFS traversal (no deque) starting from '2': {bfs(graph_cycled, '2')}") # Expected: ['2', '0', '3', '1']