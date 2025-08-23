import heapq

def dijkstra(graph, start):
    color = {node: "WHITE" for node in graph}
    dist = {node: float("inf") for node in graph}
    dist[start] = 0

    pq = [(0, start)]  # (distance, node)
    color[start] = "GRAY"

    while pq:
        d, node = heapq.heappop(pq)
        if color[node] == "BLACK":
            continue

        color[node] = "BLACK"

        for neighbor, weight in graph[node]:
            if dist[node] + weight < dist[neighbor]:
                dist[neighbor] = dist[node] + weight
                heapq.heappush(pq, (dist[neighbor], neighbor))
                color[neighbor] = "GRAY"

    return dist
