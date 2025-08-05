def solve():

    n = int(input())
    x, y = map(int, input().split())

    valid_moves = []


    moves = [
        (0, 1),   # Up
        (0, -1),  # Down
        (-1, 0),  # Left
        (1, 0),   # Right
        (-1, 1),  # Top-left
        (1, 1),   # Top-right
        (-1, -1), # Bottom-left
        (1, -1)   # Bottom-right
    ]

    for dx, dy in moves:
        new_x = x + dx
        new_y = y + dy


        if 1 <= new_x <= n and 1 <= new_y <= n:
            valid_moves.append((new_x, new_y))

    valid_moves.sort()

    print(len(valid_moves))

    for move_x, move_y in valid_moves:
        print(f"{move_x} {move_y}")

if __name__ == "__main__":
    solve()