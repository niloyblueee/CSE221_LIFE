import heapq
from collections import defaultdict

def dijkstra(start, n, graph):
    dist = [float("inf")] * (n + 1)
    dist[start] = 0
    pq = [(0, start)]

    while pq:
        distance, node = heapq.heappop(pq)
        if distance > dist[node]:
            continue
        for neighbour, weight in graph[node]:
            if distance + weight < dist[neighbour]:
                dist[neighbour] = distance + weight
                heapq.heappush(pq, (dist[neighbour], neighbour))
    return dist

if __name__ == "__main__":
    N, M, S, T = map(int, input().split())
    graph = defaultdict(list)

    for _ in range(M):
        u, v, w = map(int, input().split())
        graph[u].append((v, w))

    distA = dijkstra(S, N, graph)
    distB = dijkstra(T, N, graph)

    best_time = float("inf")
    best_node = -1

    for i in range(1, N + 1):
        if distA[i] != float("inf") and distB[i] != float("inf"):
            time = max(distA[i], distB[i])  # since one can wait
            if time < best_time or (time == best_time and i < best_node):
                best_time = time
                best_node = i

    if best_node == -1:
        print(-1)
    else:
        print(best_time, best_node)
