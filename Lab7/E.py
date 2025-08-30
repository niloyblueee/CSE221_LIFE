import sys
import heapq
from collections import defaultdict

input = sys.stdin.readline

def shortest_path_parity(N, M, u, v, w):
    graph = defaultdict(list)
    for i in range(M):
        graph[u[i]].append((v[i], w[i]))

    INF = float("inf")
    dist = [[INF, INF] for _ in range(N + 1)]
    # From node 1, no parity restriction initially
    pq = [(0, 1, -1)]  # (cost, node, last_parity)

    while pq:
        cost, node, last_parity = heapq.heappop(pq)

        if last_parity != -1 and cost > dist[node][last_parity]:
            continue

        for nei, wt in graph[node]:
            p = wt % 2
            if last_parity == -1 or p != last_parity:
                new_cost = cost + wt
                if new_cost < dist[nei][p]:
                    dist[nei][p] = new_cost
                    heapq.heappush(pq, (new_cost, nei, p))

    ans = min(dist[N][0], dist[N][1])
    return -1 if ans == INF else ans


if __name__ == "__main__":
    N, M = map(int, input().split())
    u = list(map(int, input().split()))
    v = list(map(int, input().split()))
    w = list(map(int, input().split()))
    print(shortest_path_parity(N, M, u, v, w))
