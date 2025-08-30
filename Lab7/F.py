import sys
import heapq
from collections import defaultdict

input = sys.stdin.readline

def second_shortest(N, M, S, D, edges):
    graph = defaultdict(list)
    for u, v, w in edges:
        graph[u].append((v, w))
        graph[v].append((u, w))  # bidirectional

    INF = float("inf")
    dist1 = [INF] * (N + 1)
    dist2 = [INF] * (N + 1)

    dist1[S] = 0
    pq = [(0, S)]  # (distance, node)

    while pq:
        d, u = heapq.heappop(pq)

        if d > dist2[u]:
            continue

        for v, w in graph[u]:
            new_cost = d + w

            if new_cost < dist1[v]:
                dist2[v] = dist1[v]
                dist1[v] = new_cost
                heapq.heappush(pq, (new_cost, v))

            elif dist1[v] < new_cost < dist2[v]:
                dist2[v] = new_cost
                heapq.heappush(pq, (new_cost, v))

    return -1 if dist2[D] == INF else dist2[D]


if __name__ == "__main__":
    N, M, S, D = map(int, input().split())
    edges = [tuple(map(int, input().split())) for _ in range(M)]
    print(second_shortest(N, M, S, D, edges))
