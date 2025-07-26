def is_bipartite_bfs(graph, start_node):
    """
    Detects if a graph is bipartite using Breadth-First Search (BFS).

    A bipartite graph is a graph whose vertices can be divided into two disjoint
    and independent sets U and V such that every edge connects a vertex in U
    to one in V.

    Args:
        graph (dict): An adjacency list representation of the graph.
                      Keys are nodes, and values are lists of adjacent nodes.
                      Example: {'A': ['B', 'C'], 'B': ['A', 'D'], ...}
        start_node: The starting node for the BFS. This function can be called
                    iteratively for all unvisited nodes to handle disconnected graphs.

    Returns:
        bool: True if the graph is bipartite, False otherwise.
    """

    # Initialize colors for all vertices to NIL (None in Python)
    # We'll use 0 and 1 to represent the two colors for bipartition.
    # If a node is None, it means it hasn't been visited yet.
    colors = {node: None for node in graph}

    # Create a queue for BFS. Using a list and pop(0) to simulate a queue.
    # Note: For better performance with large graphs, collections.deque is preferred.
    q = []

    # Set the color of the starting node to 0 (first partition)
    colors[start_node] = 0
    # Enqueue the starting node
    q.append(start_node)

    # While Q is not empty
    while q:
        # Dequeue a vertex u
        u = q.pop(0)

        # For each neighbor v of u
        for v in graph.get(u, []):
            # If v.color is NIL (v is unvisited)
            if colors[v] is None:
                # v.color = 1 - u.color (assign the opposite color)
                colors[v] = 1 - colors[u]
                # Enqueue v
                q.append(v)
            # Else if v.color == u.color (v is visited and has the same color as u)
            elif colors[v] == colors[u]:
                # This means we found an edge connecting two nodes of the same color,
                # which violates the bipartite property.
                return False
    
    # If the BFS completes without finding any conflicts, the component is bipartite.
    return True

# --- Helper function to handle disconnected graphs ---
def check_bipartite_graph(graph):
    """
    Checks if an entire graph (potentially disconnected) is bipartite.

    Args:
        graph (dict): An adjacency list representation of the graph.

    Returns:
        bool: True if the entire graph is bipartite, False otherwise.
    """
    # Keep track of visited nodes across all BFS traversals
    visited = {node: False for node in graph}

    # Iterate through all nodes to handle disconnected components
    for node in graph:
        if not visited[node]:
            # Perform BFS on this component
            # We need to pass a copy of the graph and the start_node for each component
            # The is_bipartite_bfs function will implicitly update 'colors' for the current component
            # We need to ensure that the 'colors' are correctly managed for each call
            # A better approach is to modify is_bipartite_bfs to take and return colors/visited state
            # For simplicity and adherence to the pseudocode, we'll run a fresh BFS for each component
            # and rely on the returned True/False.
            # However, to correctly handle the 'visited' state across components:
            # We need to pass the global 'colors' and 'visited' dictionaries to the BFS function
            # or make the BFS function a helper that modifies these global states.

            # Let's refactor `is_bipartite_bfs` to be more self-contained for a single component,
            # and this wrapper will manage multiple components.
            
            # To correctly check all components, we need a way to track global colors/visited state.
            # Let's pass the 'colors' dictionary to the BFS function and update it.

            # Re-initializing colors for each call to is_bipartite_bfs is incorrect for a multi-component graph.
            # The colors must persist across components.
            # So, the `colors` dictionary should be managed by `check_bipartite_graph`.

            # Let's adjust `is_bipartite_bfs` to work with a pre-initialized `colors` dictionary
            # and only process nodes that are `None`.

            # --- Revised approach for check_bipartite_graph ---
            # The `colors` dictionary should be passed to `is_bipartite_bfs` and updated by it.
            # This way, it acts as a global state for the entire graph.

            # Initialize colors for all vertices to None (unvisited)
            temp_colors = {node: None for node in graph}
            
            # If the current component is not bipartite, the whole graph is not.
            if not _is_bipartite_component_bfs(graph, node, temp_colors):
                return False
            
            # After a component is processed, update the main `colors` dictionary
            # to reflect the visited nodes.
            for n, c in temp_colors.items():
                if c is not None:
                    temp_colors[n] = c # Mark nodes as visited by assigning their color

    return True

# Helper function for internal use by check_bipartite_graph
def _is_bipartite_component_bfs(graph, start_node, colors):
    """
    Internal helper to check if a single connected component is bipartite.
    Modifies the 'colors' dictionary in place.
    """
    q = []

    # Only process if the start_node hasn't been colored by a previous component
    if colors[start_node] is None:
        colors[start_node] = 0
        q.append(start_node)
    else:
        # If it's already colored, it means it's part of a previously checked component.
        # This case should ideally not be hit if `check_bipartite_graph` iterates correctly.
        pass

    while q:
        u = q.pop(0)

        for v in graph.get(u, []):
            if colors[v] is None:
                colors[v] = 1 - colors[u]
                q.append(v)
            elif colors[v] == colors[u]:
                return False # Conflict found

    return True


# --- Example Usage ---
if __name__ == "__main__":
    # Example 1: Bipartite Graph
    graph1 = {
        'A': ['B', 'D'],
        'B': ['A', 'C'],
        'C': ['B', 'E'],
        'D': ['A', 'E'],
        'E': ['C', 'D']
    }
    # Expected: True (e.g., A,C,E in one set; B,D in another)
    print(f"Graph 1 is bipartite: {check_bipartite_graph(graph1)}")

    # Example 2: Non-Bipartite Graph (contains an odd cycle A-B-C-A)
    graph2 = {
        'A': ['B', 'C'],
        'B': ['A', 'C'],
        'C': ['A', 'B']
    }
    # Expected: False
    print(f"Graph 2 is bipartite: {check_bipartite_graph(graph2)}")

    # Example 3: Disconnected Bipartite Graph
    graph3 = {
        '1': ['2'],
        '2': ['1'],
        'X': ['Y'],
        'Y': ['X']
    }
    # Expected: True
    print(f"Graph 3 is bipartite: {check_bipartite_graph(graph3)}")

    # Example 4: Disconnected Non-Bipartite Graph
    graph4 = {
        '1': ['2'],
        '2': ['1'],
        'X': ['Y', 'Z'],
        'Y': ['X', 'Z'],
        'Z': ['X', 'Y']
    }
    # Expected: False (X-Y-Z-X forms an odd cycle)
    print(f"Graph 4 is bipartite: {check_bipartite_graph(graph4)}")

    # Example 5: Single node graph
    graph5 = {'A': []}
    # Expected: True
    print(f"Graph 5 is bipartite: {check_bipartite_graph(graph5)}")

    # Example 6: Empty graph
    graph6 = {}
    # Expected: True
    print(f"Graph 6 is bipartite: {check_bipartite_graph(graph6)}")
