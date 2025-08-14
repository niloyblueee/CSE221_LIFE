from collections import deque

def solve():

    n, m, s, d = map(int, input().split())
    u_nodes = list(map(int, input().split()))
    v_nodes = list(map(int, input().split()))

    #IF source and destination are the same
    if s == d:
        print(0)
        print(s)
        return

    # Build the adjacency list
    graph = {i: [] for i in range(1, n + 1)}
    for i in range(m):
        u, v = u_nodes[i], v_nodes[i]
        graph[u].append(v)
        graph[v].append(u)

    # Sort neighbor lists for lexicographical path
    for node in graph:
        graph[node].sort()

    # Initialize BFS data structures
    queue = deque([s])
    visited = {s}
    parent = {s: None}

    path_found = False
    
    while queue:
        current_node = queue.popleft()

        if current_node == d:
            path_found = True
            break
        
        # Iterate through sorted neighbors to find lexicographically smallest path
        for neighbor in graph[current_node]:
            if neighbor not in visited:
                visited.add(neighbor)
                parent[neighbor] = current_node
                queue.append(neighbor)
    
    if path_found:
        path = []
        node = d
        while node is not None:
            path.append(node)
            node = parent.get(node)
        path.reverse()
        
        print(len(path) - 1)
        print(*path)
    else:
        print(-1)

if __name__ == "__main__":
    solve()