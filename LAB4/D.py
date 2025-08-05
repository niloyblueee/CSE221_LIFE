nodes, edges = map(int, input().split())

u = list(map(int, input().split()))
v = list(map(int, input().split()))

degree = [0] * (nodes + 1)  

for i in range(edges):
    degree[u[i]] += 1
    degree[v[i]] += 1

odd_count = 0
for i in range(1, nodes + 1):
    if degree[i] % 2 == 1:
        odd_count += 1

if odd_count == 0 or odd_count == 2:
    print("YES")
else:
    print("NO")
