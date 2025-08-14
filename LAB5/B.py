import sys

# It's good practice to increase recursion limit for deep graphs
sys.setrecursionlimit(2 * 10**5 + 50)

def dfs_traversal(n, m, u_nodes, v_nodes):

    # Build the adjacency list representation of the graph
    graph = {i: [] for i in range(1, n + 1)}
    
    for i in range(m):
        u, v = u_nodes[i], v_nodes[i]
        graph[u].append(v)
        graph[v].append(u)


        
    # Sort the neighbors to ensure a consistent traversal order as per the problem statement
    for node in graph:
        graph[node].sort()

    visited = set()
    traversal_order = []

    def dfs(node):
        visited.add(node)
        traversal_order.append(node)
        
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs(neighbor)

    dfs(1)
    
    # Print the result as a space-separated list
    print(*traversal_order)

if __name__ == "__main__":
    n, m = map(int, input().split())
    edges = []
    u = list(map(int, input().split()))
    v = list(map(int, input().split()))

    dfs_traversal(n, m, u, v)