# ------------------------------
# Depth-First Search (DFS) - Iterative & Recursive Versions
# ------------------------------

def dfs_recursive(graph, start, visited=None):
    """
    Recursive DFS traversal of a graph.
    
    Parameters:
    graph (dict): Adjacency list representation of the graph.
                  Keys are nodes, values are lists of connected neighbors.
    start: Starting node for the DFS.
    visited (set): Keeps track of visited nodes.
    """
    if visited is None:
        visited = set()

    # Mark current node as visited
    visited.add(start)
    print(start, end=" ")  # Process node (can be replaced with other actions)

    # Visit each neighbor if not already visited
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, visited)

    return visited


def dfs_iterative(graph, start):
    """
    Iterative DFS traversal using a stack.
    
    Parameters:
    graph (dict): Adjacency list representation of the graph.
    start: Starting node for the DFS.
    """
    visited = set()      # Keeps track of visited nodes
    stack = [start]      # Stack to control DFS order

    while stack:
        node = stack.pop()  # Pop last element (LIFO)
        if node not in visited:
            visited.add(node)
            print(node, end=" ")  # Process node

            # Add neighbors to stack (reversed for correct order)
            stack.extend(reversed(graph[node]))

    return visited


# ------------------------------
# Example Usage
# ------------------------------
if __name__ == "__main__":
    # Example graph in adjacency list form
    graph = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F'],
        'D': [],
        'E': ['F'],
        'F': []
    }

    print("Recursive DFS starting from A:")
    dfs_recursive(graph, 'A')
    print("\nIterative DFS starting from A:")
    dfs_iterative(graph, 'A')


# ------------------------------
# Time Complexity (Rackstraw Rules Breakdown)
# ------------------------------
# Let:
#   V = number of vertices (nodes)
#   E = number of edges
#
# Steps:
#   1. Each node is visited once → O(V)
#   2. Each edge is explored at most once → O(E)
#
# Overall Time Complexity:
#   O(V + E)
#
# Space Complexity:
#   - Recursive DFS: O(V) due to call stack
#   - Iterative DFS: O(V) for visited + O(V) for stack
