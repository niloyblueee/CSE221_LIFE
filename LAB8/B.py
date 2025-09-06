import sys
input = sys.stdin.readline

def solve():
    n, m = map(int, input().split())
    edges = []
    for _ in range(m):
        u, v, w = map(int, input().split())
        edges.append((w, u, v))

    # Sort edges by weight
    edges.sort()

    parent = list(range(n+1))
    size = [1] * (n+1)

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(a, b):
        ra, rb = find(a), find(b)
        if ra != rb:
            if size[ra] < size[rb]:
                ra, rb = rb, ra
            parent[rb] = ra
            size[ra] += size[rb]
            return True
        return False

    total_cost = 0
    for w, u, v in edges:
        if union(u, v):  # add edge if it connects different components
            total_cost += w

    print(total_cost)
solve()