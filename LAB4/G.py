def solve():
    n, m, k = map(int, input().split())

    if k <= 1:
        print("NO")
        return

    knight_positions = set()
    knight_list = []

    for _ in range(k):
        x, y = map(int, input().split())
        knight_positions.add((x, y))
        knight_list.append((x, y))

    # Define the 8 possible L-shaped moves for a knight
    knight_moves = [
        (1, 2), (1, -2),
        (-1, 2), (-1, -2),
        (2, 1), (2, -1),
        (-2, 1), (-2, -1)
    ]

    for x, y in knight_list:
        for dx, dy in knight_moves:
            attack_x = x + dx
            attack_y = y + dy

            # Check if the potential attack position is within the board
            if 1 <= attack_x <= n and 1 <= attack_y <= m:
                # Check if there is another knight at the attack position
                if (attack_x, attack_y) in knight_positions:
                    print("YES")
                    return

    # If the loop completes without finding any attacks
    print("NO")

if __name__ == "__main__":
    solve()