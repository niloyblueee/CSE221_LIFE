from collections import deque
import sys

input = sys.stdin.readline

def knight_min_moves(N, x1, y1, x2, y2):
    if (x1, y1) == (x2, y2):
        return 0

    moves = [
        (2, 1), (2, -1), (-2, 1), (-2, -1),
        (1, 2), (1, -2), (-1, 2), (-1, -2)
    ]

    # distance array: -1 = unvisited
    dist = [[-1] * (N + 1) for _ in range(N + 1)]
    dist[x1][y1] = 0
    queue = deque([(x1, y1)])

    while queue:
        r, c = queue.popleft()
        for dr, dc in moves:
            nr, nc = r + dr, c + dc
            if 1 <= nr <= N and 1 <= nc <= N and dist[nr][nc] == -1:
                dist[nr][nc] = dist[r][c] + 1
                if (nr, nc) == (x2, y2):
                    return dist[nr][nc]
                queue.append((nr, nc))

    return -1


if __name__ == "__main__":
    N = int(input())
    x1, y1, x2, y2 = map(int, input().split())
    print(knight_min_moves(N, x1, y1, x2, y2))
