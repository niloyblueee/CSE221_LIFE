nodes , edges = map(int, input().split())

u = list(map(int, input().split()))
v = list(map(int, input().split()))

outdegree_adjacency_list = {i: [] for i in range(1, nodes + 1)}

indegree_adjacency_list = {i: [] for i in range(1, nodes + 1)}

for i in range(len(u)):
    outdegree_adjacency_list[u[i]].append(v[i])
    indegree_adjacency_list[v[i]].append(u[i])

for i in range(1, nodes + 1):
    diff = len(indegree_adjacency_list[i]) - len(outdegree_adjacency_list[i])
    print(diff, end=' ')
print()



