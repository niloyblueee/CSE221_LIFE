from collections import deque
import sys
input = sys.stdin.readline

def bfs(start, graph, N):
    dist = [-1] * (N + 1)
    dist[start] = 0
    parent = [-1] * (N + 1)  # to recover path
    queue = deque([start])

    farthest_node = start

    while queue:
        u = queue.popleft()
        for v in graph[u]:
            if dist[v] == -1:
                dist[v] = dist[u] + 1
                parent[v] = u
                queue.append(v)
                if dist[v] > dist[farthest_node]:
                    farthest_node = v
    return farthest_node, dist, parent


if __name__ == "__main__":
    N = int(input())
    graph = [[] for _ in range(N + 1)]

    for _ in range(N - 1):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    # Step 1: BFS from any node (1) to find one end
    A, _, _ = bfs(1, graph, N)

    # Step 2: BFS from A to find the farthest node B
    B, dist, parent = bfs(A, graph, N)

    # The distance between A and B
    length = dist[B]


    print(length)
    print(A, B)
