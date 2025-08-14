import sys

# Increase the recursion limit for potentially deep trees
sys.setrecursionlimit(2 * 10**5 + 50)

def dfs(node, parent, graph, subtree_size):
    """
    Performs a DFS to pre-compute the size of the subtree for each node.
    
    Args:
        node (int): The current node in the traversal.
        parent (int): The parent of the current node.
        graph (dict): The adjacency list representation of the tree.
        subtree_size (list): A list to store the computed subtree sizes.
    """
    current_size = 1
    
    for neighbor in graph[node]:
        if neighbor != parent:
            current_size += dfs(neighbor, node, graph, subtree_size)
    
    subtree_size[node] = current_size
    return current_size

def solve():
    """
    Main function to handle input, pre-computation, and queries.
    """

    
    n, r = map(int, input().split())
    
    # Build the graph using an adjacency list
    graph = {i: [] for i in range(1, n + 1)}
    for _ in range(n - 1):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    
    # Array to store the size of each subtree
    subtree_size = [0] * (n + 1)
    
    # Perform DFS to pre-compute subtree sizes starting from the root R
    dfs(r, 0, graph, subtree_size)
    
    q = int(input())
    for _ in range(q):
        x = int(input())
        print(subtree_size[x])


if __name__ == "__main__":
    solve()