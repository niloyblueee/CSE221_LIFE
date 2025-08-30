# Kosaraju's Algorithm to find Strongly Connected Components (SCCs) in a directed graph
# -------------------------------------------------------------------
# Steps:
# 1. Do a DFS on the graph, keeping track of the finish times of vertices.
#    (We push nodes into a stack when DFS finishes on them)
# 2. Reverse (transpose) the graph.
# 3. Do DFS again in the order defined by the stack (descending finish time).
#    Each DFS tree gives one SCC.
# -------------------------------------------------------------------

from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.V = vertices                  # Number of vertices
        self.graph = defaultdict(list)     # Adjacency list

    def add_edge(self, u, v):
        """Add a directed edge u -> v"""
        self.graph[u].append(v)

    def dfs(self, v, visited, stack=None, collect=None):
        """
        Standard DFS function.
        - visited: list of visited nodes
        - stack: if provided, nodes are pushed after finishing (for step 1)
        - collect: if provided, collects nodes of the current SCC
        """
        visited[v] = True
        if collect is not None:
            collect.append(v)  # Collect nodes of the current SCC

        for neighbor in self.graph[v]:
            if not visited[neighbor]:
                self.dfs(neighbor, visited, stack, collect)

        if stack is not None:
            stack.append(v)  # Record finish order

    def transpose(self):
        """Reverse (transpose) the graph"""
        g_t = Graph(self.V)
        for u in self.graph:
            for v in self.graph[u]:
                g_t.add_edge(v, u)  # Reverse edge
        return g_t

    def kosaraju(self):
        """Main function to find SCCs using Kosaraju's Algorithm"""
        stack = []
        visited = [False] * self.V

        # Step 1: Fill stack with vertices in order of finishing times
        for i in range(self.V):
            if not visited[i]:
                self.dfs(i, visited, stack)

        # Step 2: Transpose the graph
        gr = self.transpose()

        # Step 3: Do DFS on transposed graph in stack order
        visited = [False] * self.V
        scc_list = []

        while stack:
            v = stack.pop()
            if not visited[v]:
                collect = []
                gr.dfs(v, visited, collect=collect)
                scc_list.append(collect)

        return scc_list


# ---------------- Example Usage ----------------
if __name__ == "__main__":
    g = Graph(5)
    g.add_edge(1, 0)
    g.add_edge(0, 2)
    g.add_edge(2, 1)
    g.add_edge(0, 3)
    g.add_edge(3, 4)

    sccs = g.kosaraju()
    print("Strongly Connected Components (SCCs):")
    for scc in sccs:
        print(scc)
