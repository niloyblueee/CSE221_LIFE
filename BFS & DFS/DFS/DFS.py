def dfs(graph, start, color):
    color[start] = "GRAY"   # discovered
    print(start, end=" ")

    for neighbor in graph[start]:
        if color[neighbor] == "WHITE":   # only go to undiscovered nodes
            dfs(graph, neighbor, color)

    color[start] = "BLACK"  # fully explored


# Example
graph = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['E'],
    'D': [],
    'E': []
}
color = {node: "WHITE" for node in graph}
dfs(graph, 'A', color)
