import sys
from collections import deque

input = sys.stdin.readline

def topo_sort_bfs(N, graph, indegree):
    queue = deque([u for u in range(1, N+1) if indegree[u] == 0])
    topo = []

    while queue:
        u = queue.popleft()
        topo.append(u)
        for neighbours in graph[u]:
            indegree[neighbours] -= 1
            if indegree[neighbours] == 0:
                queue.append(neighbours)

    if len(topo) == N:
        print(*topo)
    else:
        print(-1)


if __name__ == "__main__":
    N, M = map(int, input().split())
    graph = [[] for _ in range(N+1)]
    indegree = [0] * (N+1)

    for _ in range(M):
        u, v = map(int, input().split())
        graph[u].append(v)
        indegree[v] += 1

    topo_sort_bfs(N, graph, indegree)
