import sys
from collections import deque
input = sys.stdin.readline

def solve():
    n, m = map(int, input().split())
    edges = []
    for i in range(m):
        u, v, w = map(int, input().split())
        edges.append((w, u-1, v-1, i))  # (weight, u, v, original index)

    # Kruskal to build one MST and mark used edges by index
    edges.sort()
    parent = list(range(n))
    sz = [1]*n
    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    def union(a,b):
        ra, rb = find(a), find(b)
        if ra == rb: return False
        if sz[ra] < sz[rb]:
            ra, rb = rb, ra
        parent[rb] = ra
        sz[ra] += sz[rb]
        return True

    used = [False]*m
    mst_edges = []
    best_cost = 0
    for w,u,v,idx in edges:
        if union(u,v):
            used[idx] = True
            mst_edges.append((u,v,w))
            best_cost += w

    if len(mst_edges) != n-1:
        print(-1)
        return

    # Build adjacency list of MST
    adj = [[] for _ in range(n)]
    for u,v,w in mst_edges:
        adj[u].append((v,w))
        adj[v].append((u,w))

    # Binary lifting parameters
    LOG = max(1, (n).bit_length())  # enough levels
    up = [[-1]*LOG for _ in range(n)]
    # For each jump store top-two values (max1, max2) where max2 < max1 or -1 if none
    max1 = [[-1]*LOG for _ in range(n)]
    max2 = [[-1]*LOG for _ in range(n)]
    depth = [-1]*n

    # BFS to set depth and up[*][0], max1[*][0]
    root = 0
    dq = deque([root])
    depth[root] = 0
    up[root][0] = -1
    max1[root][0] = -1
    max2[root][0] = -1
    while dq:
        u = dq.popleft()
        for v,w in adj[u]:
            if depth[v] == -1:
                depth[v] = depth[u] + 1
                up[v][0] = u
                max1[v][0] = w
                max2[v][0] = -1
                dq.append(v)

    # helper to combine two (max1,max2) pairs -> top1 and top2 (< top1 or -1)
    def combine(a1, a2, b1, b2):
        # a1 >=? a2, b1 >=? b2 (we maintain that)
        # find top1 = max(a1,b1)
        # find top2 = max among values < top1 (i.e., candidates: the other values and duplicates less than top1)
        # sentinel -1 means "no value"
        vals = []
        if a1 != -1: vals.append(a1)
        if a2 != -1: vals.append(a2)
        if b1 != -1: vals.append(b1)
        if b2 != -1: vals.append(b2)
        if not vals:
            return -1, -1
        # find top1
        top1 = max(vals)
        # find top2 strictly less than top1
        top2 = -1
        for x in vals:
            if x < top1 and x > top2:
                top2 = x
        return top1, top2

    # Build binary lifting tables
    for j in range(1, LOG):
        for i in range(n):
            pj = up[i][j-1]
            if pj != -1:
                up[i][j] = up[pj][j-1]
                # combine (max1[i][j-1], max2[i][j-1]) with (max1[pj][j-1], max2[pj][j-1])
                t1, t2 = combine(max1[i][j-1], max2[i][j-1], max1[pj][j-1], max2[pj][j-1])
                max1[i][j] = t1
                max2[i][j] = t2
            else:
                up[i][j] = -1
                max1[i][j] = max1[i][j-1]
                max2[i][j] = max2[i][j-1]

    # Query function: returns (top1, top2) on path u-v in MST
    def query_top2(u, v):
        if depth[u] < depth[v]:
            u, v = v, u
        cur1, cur2 = -1, -1
        diff = depth[u] - depth[v]
        # lift u
        for j in range(LOG-1, -1, -1):
            if diff & (1 << j):
                # combine current with max on jump u->up[u][j]
                cur1, cur2 = combine(cur1, cur2, max1[u][j], max2[u][j])
                u = up[u][j]
        if u == v:
            return cur1, cur2
        for j in range(LOG-1, -1, -1):
            if up[u][j] != -1 and up[u][j] != up[v][j]:
                cur1, cur2 = combine(cur1, cur2, max1[u][j], max2[u][j])
                cur1, cur2 = combine(cur1, cur2, max1[v][j], max2[v][j])
                u = up[u][j]
                v = up[v][j]
        # finally include edges to their parent
        cur1, cur2 = combine(cur1, cur2, max1[u][0], max2[u][0])
        cur1, cur2 = combine(cur1, cur2, max1[v][0], max2[v][0])
        return cur1, cur2

    # Try all non-MST edges as candidates
    second_best = float('inf')
    for w,u,v,idx in edges:
        if used[idx]:
            continue
        p1, p2 = query_top2(u, v)  # p1 = max edge weight on path, p2 = second largest < p1 or -1
        if p1 == -1:
            continue
        # case 1: replace p1
        if w > p1:
            cand = best_cost + w - p1
            if cand > best_cost and cand < second_best:
                second_best = cand
        elif w == p1:
            # removing p1 gives same best_cost -> invalid. try removing second max if exists.
            if p2 != -1:
                cand = best_cost + w - p2
                if cand > best_cost and cand < second_best:
                    second_best = cand
        else:  # w < p1 -> new_cost = best + w - p1 < best (shouldn't happen), ignore
            # but for safety check and only accept > best
            cand = best_cost + w - p1
            if cand > best_cost and cand < second_best:
                second_best = cand

    print(second_best if second_best != float('inf') else -1)

if __name__ == "__main__":
    solve()
