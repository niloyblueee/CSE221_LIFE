def topo_sort_dfs(graph):
    visited = set()
    stack = []

    def dfs(u):
        visited.add(u)
        for v in graph[u]:
            if v not in visited:
                dfs(v)
        stack.append(u)  # push after exploring

    for node in graph:
        if node not in visited:
            dfs(node)

    return stack[::-1]  # reverse

#khans Algo

from collections import deque

def topo_sort_bfs(graph):
    indegree = {u: 0 for u in graph}
    for u in graph:
        for v in graph[u]:
            indegree[v] += 1

    queue = deque([u for u in graph if indegree[u] == 0])
    topo = []

    while queue:
        u = queue.popleft()
        topo.append(u)
        for v in graph[u]:
            indegree[v] -= 1
            if indegree[v] == 0:
                queue.append(v)

    return topo

if __name__ == "__main__":
    N, M = map(int, input().split())
    graph = [[] for _ in range(N+1)]
    indegree = [0] * (N+1)

    for _ in range(M):
        u, v = map(int, input().split())
        graph[u].append(v)
        indegree[v] += 1

    topo_sort_bfs(N, graph, indegree)
#https://youtu.be/cIBFEhD77b4?si=n981wTBvrsiCEsNZ