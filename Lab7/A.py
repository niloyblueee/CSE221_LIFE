import heapq

def dijkstra(graph, start, dest, n):
    dist = [float("inf")] * (n + 1)
    parent = [-1] * (n + 1)
    dist[start] = 0

    pq = [(0, start)]  # (distance, node)

    while pq:
        distance, node = heapq.heappop(pq)

        if distance > dist[node]:
            continue  # already found a better path

        for neighbor, weight in graph[node]:
            if dist[node] + weight < dist[neighbor]:
                dist[neighbor] = dist[node] + weight
                parent[neighbor] = node
                heapq.heappush(pq, (dist[neighbor], neighbor))

    # If destination is unreachable
    if dist[dest] == float("inf"):
        return -1, []

    # Reconstruct path
    path = []
    cur = dest
    while cur != -1:
        path.append(cur)
        cur = parent[cur]
    path.reverse()

    return dist[dest], path


if __name__ == "__main__":
    N, M, S, D = map(int, input().split())
    u = list(map(int, input().split()))
    v = list(map(int, input().split()))
    w = list(map(int, input().split()))

    graph = {i: [] for i in range(1, N + 1)}
    for i in range(M):
        graph[u[i]].append((v[i], w[i]))

    distance, path = dijkstra(graph, S, D, N)

    if distance == -1:
        print(-1)
    else:
        print(distance)
        print(*path)
