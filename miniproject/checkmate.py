def checkmate(board):
    if not board or not isinstance(board, str):
        return

    lines = [line.strip().replace('\\', '') for line in board.split('\n') if line.strip()]
    if not lines:
        return

    n = len(lines)
    for line in lines:
        if len(line) != n:
            print("Fail")
            return

    grid = [list(line) for line in lines]

    king_pos = None
    for r in range(n):
        for c in range(n):
            if grid[r][c] == 'K':
                king_pos = (r, c)
                break
        if king_pos: break

    if not king_pos:
        return

    kx, ky = king_pos

    def is_check(dx, dy, pieces):
        x, y = kx + dx, ky + dy
        while 0 <= x < n and 0 <= y < n:
            target = grid[x][y]
            if target != '.':
                return target in pieces
            x += dx
            y += dy
        return False

    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        if is_check(dx, dy, "RQ"):
            print("Success")
            return

    for dx, dy in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
        if is_check(dx, dy, "BQ"):
            print("Success")
            return

    for dx, dy in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
        px, py = kx + dx, ky + dy
        if 0 <= px < n and 0 <= py < n:
            if grid[px][py] == 'P':
                print("Success")
                return

    print("Fail")