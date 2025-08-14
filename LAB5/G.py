import sys
from collections import deque

def solve():
    R, H = map(int, sys.stdin.readline().split())
    grid = [sys.stdin.readline().strip() for _ in range(R)]

    max_diamonds = 0
    visited_overall = set()

    for r in range(R):
        for h in range(H):
            if grid[r][h] != '#' and (r, h) not in visited_overall:
                queue = deque([(r, h)])
                visited_component = set([(r, h)])
                
                current_diamonds = 0
                if grid[r][h] == 'D':
                    current_diamonds = 1

                while queue:
                    curr_r, curr_h = queue.popleft()

                    for dr, dh in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                        next_r, next_h = curr_r + dr, curr_h + dh

                        if 0 <= next_r < R and 0 <= next_h < H and grid[next_r][next_h] != '#' and (next_r, next_h) not in visited_component:
                            visited_component.add((next_r, next_h))
                            queue.append((next_r, next_h))
                            if grid[next_r][next_h] == 'D':
                                current_diamonds += 1
                
                # Update max_diamonds
                max_diamonds = max(max_diamonds, current_diamonds)
                
                # Mark all cells in this component as visited overall
                visited_overall.update(visited_component)

    print(max_diamonds)

if __name__ == "__main__":
    solve()