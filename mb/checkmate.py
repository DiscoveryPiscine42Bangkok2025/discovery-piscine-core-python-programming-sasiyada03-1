def checkmate(board):
    grid = board.split("\n")
    n = len(grid)

    
    king_pos = None
    for i in range(n):
        for j in range(len(grid[i])):
            if grid[i][j] == 'K':
                king_pos = (i, j)
                break
        if king_pos:
            break

    if not king_pos:
        return

    kx, ky = king_pos

    def check_direction(dx, dy, valid_pieces):
        x, y = kx + dx, ky + dy
        while 0 <= x < n and 0 <= y < len(grid[x]):
            if grid[x][y] != '.':
                if grid[x][y] in valid_pieces:
                    return True
                break
            x += dx
            y += dy
        return False

   
    directions_straight = [(1,0), (-1,0), (0,1), (0,-1)]
    for dx, dy in directions_straight:
        if check_direction(dx, dy, ['R', 'Q']):
            print("Success")
            return

    
    directions_diag = [(1,1), (1,-1), (-1,1), (-1,-1)]
    for dx, dy in directions_diag:
        if check_direction(dx, dy, ['B', 'Q']):
            print("Success")
            return

    pawn_dirs = [(-1, -1), (-1, 1)]
    for dx, dy in pawn_dirs:
        x, y = kx + dx, ky + dy
        if 0 <= x < n and 0 <= y < len(grid[x]):
            if grid[x][y] == 'P':
                print("Success")
                return

    print("Fail")

def checkmate(board):
    print("Test")
def main():
    board = """\
R...
.K..
..P.
....\
"""
    checkmate(board)

if __name__ == "__main__":
    main()