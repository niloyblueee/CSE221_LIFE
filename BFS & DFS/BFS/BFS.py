from collections import deque

def bfs(graph, start):
    color = {node: "WHITE" for node in graph}
    queue = deque()

    color[start] = "GRAY"
    queue.append(start)

    while queue:
        node = queue.popleft()
        print(node, end=" ")

        for neighbor in graph[node]:
            if color[neighbor] == "WHITE":  # only undiscovered nodes
                color[neighbor] = "GRAY"
                queue.append(neighbor)

        color[node] = "BLACK"  # done with node
