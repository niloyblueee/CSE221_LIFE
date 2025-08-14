import sys
from collections import deque

def bfs(graph, start, end):
    """
    Performs BFS to find the shortest path and its length from start to end.
    Returns (path, length) or (None, -1) if no path exists.
    """
    queue = deque([start])
    visited = {start}
    parent = {start: None}
    
    path_found = False
    
    while queue:
        current_node = queue.popleft()
        
        if current_node == end:
            path_found = True
            break
            
        for neighbor in graph.get(current_node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                parent[neighbor] = current_node
                queue.append(neighbor)
    
    if not path_found:
        return None, -1
        
    path = []
    node = end
    while node is not None:
        path.append(node)
        node = parent.get(node)
    path.reverse()
    
    return path, len(path) - 1

def solve():

    n, m, s, d, k = map(int, input().split())
    
    graph = {i: [] for i in range(1, n + 1)}
    for _ in range(m):
        u, v = map(int, input().split())
        graph[u].append(v)
            

        
    # Find shortest path from S to K
    path_sk, len_sk = bfs(graph, s, k)
    
    # Find shortest path from K to D
    path_kd, len_kd = bfs(graph, k, d)
    
    # Check if both paths exist
    if path_sk and path_kd:
        # Combine the paths and remove the duplicate 'k'
        combined_path = path_sk + path_kd[1:]
        total_length = len_sk + len_kd
        
        print(total_length)
        print(*combined_path)
    else:
        print(-1)

if __name__ == "__main__":
    solve()