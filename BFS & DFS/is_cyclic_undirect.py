def is_cyclic_undirected(graph):
    color = {node: "WHITE" for node in graph}

    def dfs(u, parent):
        color[u] = "GRAY"
        for v in graph[u]:
            if color[v] == "WHITE":
                if dfs(v, u):  # explore deeper
                    return True
            elif v != parent:  # back edge → cycle
                return True
        color[u] = "BLACK"
        return False

    for node in graph:
        if color[node] == "WHITE":
            if dfs(node, None):
                return True
    return False
