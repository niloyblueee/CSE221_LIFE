import sys
input = sys.stdin.readline

def solve():
    n, k = map(int, input().split())
    
    parent = list(range(n + 1))
    size = [1] * (n + 1)

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]  # Path compression
            x = parent[x]
        return x

    def union(a, b):
        ra, rb = find(a), find(b)
        if ra != rb:
            if size[ra] < size[rb]:
                ra, rb = rb, ra
            parent[rb] = ra
            size[ra] += size[rb]
        return size[find(ra)]

    out = []
    for _ in range(k):
        a, b = map(int, input().split())
        out.append(str(union(a, b)))

    sys.stdout.write("\n".join(out))

solve()