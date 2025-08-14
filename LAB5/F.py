import sys

# It's a good practice to increase the recursion limit for deep graphs
sys.setrecursionlimit(2 * 10**5 + 50)

def is_cyclic_util(node, graph, visited, recursion_stack):
    """
    Recursive utility function to perform DFS and detect cycles.
    """
    visited[node] = True
    recursion_stack[node] = True
    
    # Iterate through all neighbors of the current node
    for neighbor in graph.get(node, []):
        # If the neighbor is in the recursion stack, we found a cycle
        if recursion_stack[neighbor]:
            return True
        # If the neighbor is not visited, recurse on it
        if not visited[neighbor]:
            if is_cyclic_util(neighbor, graph, visited, recursion_stack):
                return True
    
    # Remove the node from the recursion stack before backtracking
    recursion_stack[node] = False
    return False

def solve():
    """
    Main function to handle input and run cycle detection.
    """

    n, m = map(int, input().split())
    # Build the graph using an adjacency list
    graph = {i: [] for i in range(1, n + 1)}
    for _ in range(m):
        u, v = map(int, input().split())
        graph[u].append(v)
    
    # visited array tracks all visited nodes
    visited = [False] * (n + 1)
    
    # recursion_stack tracks nodes in the current DFS path
    recursion_stack = [False] * (n + 1)
    
    # Iterate through all nodes to handle disconnected components
    for i in range(1, n + 1):
        if not visited[i]:
            if is_cyclic_util(i, graph, visited, recursion_stack):
                print("YES")
                return
    
    print("NO")

if __name__ == "__main__":
    solve()