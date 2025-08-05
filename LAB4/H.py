import sys
from math import gcd

def solve():
    """
    Solves the Coprime Graph problem by constructing the graph and then
    answering queries efficiently.
    """
    try:
        # Use fast I/O for large inputs
        input = sys.stdin.readline
        n_str, q_str = input().split()
        n, q = int(n_str), int(q_str)
    except (IOError, ValueError):
        # Handle case of empty or malformed input line
        return

    # Adjacency list to store the graph.
    # adj[i] will store the list of nodes connected to node i.
    # We use n+1 size to make indexing 1-based, matching the problem statement.
    adj = [[] for _ in range(n + 1)]

    # 1. Graph Construction:
    # Build the undirected graph by iterating through all pairs of nodes (i, j).
    # An edge exists if gcd(i, j) == 1.
    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):
            if gcd(i, j) == 1:
                # Add edge (i, j)
                adj[i].append(j)
                adj[j].append(i)

    # 2. Pre-computation for Queries:
    # Sort the neighbors of each node. This makes finding the K-th smallest
    # neighbor a simple O(1) lookup during the query phase.
    for i in range(1, n + 1):
        adj[i].sort()

    # 3. Query Processing:
    # Process each of the Q queries.
    for _ in range(q):
        try:
            x_str, k_str = input().split()
            x, k = int(x_str), int(k_str)

            # Check if there are at least K neighbors.
            if k <= len(adj[x]):
                # The K-th smallest neighbor is at index k-1 due to 0-based indexing.
                print(adj[x][k - 1])
            else:
                # If there are fewer than K neighbors, print -1.
                print(-1)
        except (IOError, ValueError):
            # Break if we hit an empty or malformed line during queries
            break

if __name__ == "__main__":
    solve()