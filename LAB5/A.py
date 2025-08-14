from collections import deque

def bfs_traversal(n, m, edges):
    """
    Performs a Breadth-First Search (BFS) on a graph and prints the traversal order.

    Args:
        n (int): The number of cities (nodes).
        m (int): The number of roads (edges).
        edges (list): A list of tuples representing the edges.
    """
    
    # Build an adjacency list representation of the graph
    graph = {i: [] for i in range(1, n + 1)}
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    
    # Sort the neighbors to ensure a consistent traversal order for the problem statement
    for node in graph:
        graph[node].sort()

    visited = set()
    queue = deque([1])
    visited.add(1)
    
    traversal_order = []

    while queue:
        current_node = queue.popleft()
        traversal_order.append(current_node)
        
        for neighbor in graph[current_node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    
    print(*traversal_order)

if __name__ == "__main__":
    n, m = map(int, input().split())
    edges = []
    for _ in range(m):
        u, v = map(int, input().split())
        edges.append((u, v))
    
    bfs_traversal(n, m, edges)