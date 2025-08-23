import sys
from collections import deque

input = sys.stdin.readline

def max_group_size(N, graph):
    visited = [0] * (N + 1)  # 0 = unvisited, 1 or -1 = group
    answer = 0

    for start in range(1, N + 1):
        if visited[start] == 0:
            queue = deque([start])
            visited[start] = 1
            count1, count2 = 1, 0

            while queue:
                u = queue.popleft()
                for neighbours in graph[u]:
                    if visited[neighbours] == 0:
                        visited[neighbours] = -visited[u]  # opposite group
                        if visited[neighbours] == 1:
                            count1 += 1
                        else:
                            count2 += 1
                        queue.append(neighbours)
                    # If visited[neighbours] == visited[u], it’s an odd cycle (not bipartite).
                    # But problem guarantees tackles follow the Robot/Human rule, so graph is bipartite.

            answer += max(count1, count2)

    return answer


if __name__ == "__main__":
    N, M = map(int, input().split())
    graph = {i: [] for i in range(1, N + 1)}

    for _ in range(M):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)  # tackling is mutual for bipartition

    print(max_group_size(N, graph))
