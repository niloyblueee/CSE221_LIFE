from collections import deque
import sys
input = sys.stdin.readline

def multi_source_bfs(N, graph, sources):
    dist = [-1] * (N + 1)
    queue = deque()
    
    # Initialize sources
    for s in sources:
        dist[s] = 0
        queue.append(s)
    
    # Standard BFS
    while queue:
        u = queue.popleft()
        for v in graph[u]:
            if dist[v] == -1:  # Not visited yet
                dist[v] = dist[u] + 1
                queue.append(v)
    
    return dist

# Read input
N, M, S, Q = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

sources = list(map(int, input().split()))
destinations = list(map(int, input().split()))

# Run multi-source BFS
distances = multi_source_bfs(N, graph, sources)

# Print distances to each destination
print(' '.join(str(distances[d]) for d in destinations))
