def is_cyclic_directed(graph):
    color = {node: "WHITE" for node in graph}

    def dfs(u):
        color[u] = "GRAY"
        for v in graph[u]:
            if color[v] == "WHITE":
                if dfs(v):
                    return True
            elif color[v] == "GRAY":  # back edge → cycle
                return True
        color[u] = "BLACK"
        return False

    for node in graph:
        if color[node] == "WHITE":
            if dfs(node):
                return True
    return False
