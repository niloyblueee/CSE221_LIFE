nodes, edges = map(int, input().split())

matrix = [[0 for _ in range(nodes)] for _ in range(nodes)]


for _ in range(edges):
    u, v, w = map(int,  input().split())
    matrix[u - 1 ][v - 1] = w

for row in matrix:
    for element in row:
        print(element, end=(" "))
    print(end=("\n"))