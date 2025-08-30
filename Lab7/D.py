import sys
import heapq
from collections import defaultdict

input = sys.stdin.readline

def min_cost_path(N, M, S, D, weights, edges):
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)

    dist = [float("inf")] * (N + 1)
    dist[S] = weights[S]

    pq = [(dist[S], S)]  # (cost, node)

    while pq:
        cost, node = heapq.heappop(pq)
        if cost > dist[node]:
            continue
        for nei in graph[node]:
            new_cost = cost + weights[nei]
            if new_cost < dist[nei]:
                dist[nei] = new_cost
                heapq.heappush(pq, (new_cost, nei))

    return -1 if dist[D] == float("inf") else dist[D]


if __name__ == "__main__":
    N, M, S, D = map(int, input().split())
    node_weights = [0] + list(map(int, input().split()))  # 1-indexed
    edges = [tuple(map(int, input().split())) for _ in range(M)]

    print(min_cost_path(N, M, S, D, node_weights, edges))
