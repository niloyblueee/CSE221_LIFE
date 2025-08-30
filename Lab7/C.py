import sys
import heapq
from collections import defaultdict

input = sys.stdin.readline

def min_danger_path(N, M, edges):
    graph = defaultdict(list)
    for u, v, w in edges:
        graph[u].append((v, w))
        graph[v].append((u, w))  # bi-directional

    # Distance array: min danger to each node
    dist = [float("inf")] * (N + 1)
    dist[1] = 0

    pq = [(0, 1)]  # (danger, node)

    while pq:
        danger, node = heapq.heappop(pq)
        if danger > dist[node]:
            continue

        for nei, w in graph[node]:
            new_danger = max(danger, w)
            if new_danger < dist[nei]:
                dist[nei] = new_danger
                heapq.heappush(pq, (new_danger, nei))

    # Replace inf with -1
    result = [dist[i] if dist[i] != float("inf") else -1 for i in range(1, N + 1)]
    return result


if __name__ == "__main__":
    N, M = map(int, input().split())
    edges = []
    for _ in range(M):
        edges.append(tuple(map(int, input().split())))
    ans = min_danger_path(N, M, edges)
    print(" ".join(map(str, ans)))
