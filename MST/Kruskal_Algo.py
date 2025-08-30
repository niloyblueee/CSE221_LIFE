# Kruskal's Algorithm to find the Minimum Spanning Tree (MST) of a graph
# -------------------------------------------------------------
# Kruskal’s Algorithm works by:
# 1. Sorting all edges by their weights (smallest to largest).
# 2. Picking the smallest edge that doesn’t form a cycle (using Union-Find/Disjoint Set).
# 3. Repeating until we have V-1 edges in the MST (where V = number of vertices).
# -------------------------------------------------------------

class DisjointSet:
    """
    Disjoint Set (Union-Find) Data Structure
    - Used to efficiently check if two vertices belong to the same connected component.
    """
    def __init__(self, n):
        # Initialize parent and rank for path compression + union by rank
        self.parent = [i for i in range(n)]
        self.rank = [0] * n

    def find(self, x):
        """
        Find the root (representative) of a set containing x
        with path compression optimization.
        """
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # Path compression
        return self.parent[x]

    def union(self, x, y):
        """
        Union two sets by rank.
        Returns True if union was successful (i.e., they were in different sets),
        False if x and y were already connected (cycle would form).
        """
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x == root_y:
            return False  # Cycle detected, no union performed

        # Union by rank heuristic
        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        elif self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        else:
            self.parent[root_y] = root_x
            self.rank[root_x] += 1

        return True


def kruskal(n, edges):
    """
    Kruskal’s Algorithm to find MST.
    
    Parameters:
    - n: Number of vertices (assumed labeled 0 to n-1)
    - edges: List of tuples (weight, u, v)
    
    Returns:
    - mst: List of edges in the MST
    - total_weight: Sum of weights in the MST
    """
    # Step 1: Sort edges by weight
    edges.sort()

    ds = DisjointSet(n)
    mst = []
    total_weight = 0

    # Step 2: Process edges in increasing order
    for weight, u, v in edges:
        if ds.union(u, v):  # If u and v are not already connected
            mst.append((u, v, weight))
            total_weight += weight

            # Stop if we already have (n-1) edges in the MST
            if len(mst) == n - 1:
                break

    return mst, total_weight


# ---------------- Example Usage ----------------
if __name__ == "__main__":
    # Example graph with 5 vertices and 7 edges
    # Format: (weight, node1, node2)
    edges = [
        (1, 0, 1),
        (3, 0, 2),
        (3, 1, 2),
        (6, 1, 3),
        (4, 2, 3),
        (2, 2, 4),
        (5, 3, 4)
    ]
    n = 5  # Number of vertices

    mst, total_weight = kruskal(n, edges)

    print("Edges in MST:")
    for u, v, w in mst:
        print(f"{u} -- {v} (weight {w})")

    print("Total weight of MST:", total_weight)
