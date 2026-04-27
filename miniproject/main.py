import pygame
import sys

pygame.init()

WIDHT, HEIGHT = 800,800
SQUARE_SIZE = WIDHT//8

WHITE =(255,255,255)
BLACK = (0,0,0)
BROWN = (139,69,19)
YELLOW = (255,255,0)

screen = pygame.display.set_mode((WIDHT,HEIGHT))
pygame.display.set_caption("Chess Game") 

class ChessPiece:
    def __init__(self,color,type,image):
        self.color=color
        self.type = type
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image, (SQUARE_SIZE,SQUARE_SIZE))
        self.has_moved = False

board = [[None for _ in range(8)] for _ in range(8)]

current_player = 'white'

selected_piece = None
selected_pos = None

def init_board():
    for col in range(8):
        board[1][col] = ChessPiece ('black','pawn','images/black_pawn.png')
        board[6][col] = ChessPiece ('white','pawn','images/white_pawn.png')
    board[0][0] = board[0][7] = ChessPiece('black','rook','images/black_rook.png')
    board[7][0] = board[7][7] = ChessPiece('white', 'rook','images/white_rook.png')
    board[0][1] = board[0][6] = ChessPiece('black', 'knight', 'images/black_knight.png')
    board[7][1] = board[7][6] = ChessPiece('white', 'knight', 'images/white_knight.png')

    board[0][2] = board[0][5] = ChessPiece('black', 'bishop', 'images/black_bishop.png')
    board[7][2] = board[7][5] = ChessPiece('white', 'bishop', 'images/white_bishop.png')

    board[0][3] = ChessPiece('black', 'queen', 'images/black_queen.png')
    board[7][3] = ChessPiece('white', 'queen', 'images/white_queen.png')

    board[0][4] = ChessPiece('black', 'king', 'images/black_king.png')
    board[7][4] = ChessPiece('white', 'king', 'images/white_king.png')

def draw_board():
    for row in range(8):
        for col in range(8):
            color = WHITE if (row + col) % 2 ==0 else BROWN
            pygame.draw.rect(screen,color,(col* SQUARE_SIZE ,row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
    
    if selected_pos:
        pygame.draw.rect(screen,YELLOW,(selected_pos[1]*SQUARE_SIZE,selected_pos[0]*SQUARE_SIZE,SQUARE_SIZE,SQUARE_SIZE))

def draw_piece():
    for row in range(8):
        for col in range(8):
            piece = board[row][col]
            if piece:
                screen.blit(piece.image,(col*SQUARE_SIZE, row*SQUARE_SIZE))

def get_valid_moves(piece, row, col):
    moves = []
    if piece.type == 'pawn':
        direction = -1 if piece.color == 'white' else 1
        if 0 <= row + direction < 8 and board[row + direction][col] is None:
            moves.append((row + direction, col))
            if (piece.color == 'white' and row == 6) or (piece.color == 'black' and row == 1):
                if board[row + 2*direction][col] is None:
                    moves.append((row + 2*direction, col))
        for dc in [-1, 1]:
            if 0 <= row + direction < 8 and 0 <= col + dc < 8:
                if board[row + direction][col + dc] and board[row + direction][col + dc].color != piece.color:
                    moves.append((row + direction, col + dc))

    elif piece.type == 'rook':
        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            r, c = row + dr, col + dc
            while 0 <= r < 8 and 0 <= c < 8:
                if board[r][c] is None:
                    moves.append((r, c))
                elif board[r][c].color != piece.color:
                    moves.append((r, c))
                    break
                else:
                    break
                r, c = r + dr, c + dc

    elif piece.type == 'knight':
        for dr, dc in [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]:
            r, c = row + dr, col + dc
            if 0 <= r < 8 and 0 <= c < 8 and (board[r][c] is None or board[r][c].color != piece.color):
                moves.append((r, c))

    elif piece.type == 'bishop':
        for dr, dc in [(1, 1), (1, -1), (-1, 1), (-1, -1)]:
            r, c = row + dr, col + dc
            while 0 <= r < 8 and 0 <= c < 8:
                if board[r][c] is None:
                    moves.append((r, c))
                elif board[r][c].color != piece.color:
                    moves.append((r, c))
                    break
                else:
                    break
                r, c = r + dr, c + dc

    elif piece.type == 'queen':
        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]:
            r, c = row + dr, col + dc
            while 0 <= r < 8 and 0 <= c < 8:
                if board[r][c] is None:
                    moves.append((r, c))
                elif board[r][c].color != piece.color:
                    moves.append((r, c))
                    break
                else:
                    break
                r, c = r + dr, c + dc

    elif piece.type == 'king':
        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                if dr == 0 and dc == 0:
                    continue
                r, c = row + dr, col + dc
                if 0 <= r < 8 and 0 <= c < 8 and (board[r][c] is None or board[r][c].color != piece.color):
                    moves.append((r, c))

    return moves


def is_check(color):
    king_pos = None
    for r in range(8):
        for c in range(8):
            if board[r][c] and board[r][c].color == color and board[r][c]=='king':
                king_pos = (r,c)
                break
            if king_pos:
                break

    for r in range(8):
        for c in range(8):
            piece = board[r][c]
            if piece and piece.color != color:
                if king_pos in get_valid_moves(piece,r,c):
                    return True
        

    return False       

def is_game_over():
    for r in range(8):
        for c in range(8):
            piece = board[r][c]
            if piece and piece.color == current_player:
                valid_moves = get_valid_moves(piece,r,c)
                for move in valid_moves:
                    temp = board[move[0]][move[1]]
                    board[move[0]][move[1]] = piece
                    board[r][c]= None
                    check = is_check(current_player)
                    board[r][c]= piece
                    board[move[0]][move[1]] =temp
                    if not check:
                        return False
    return True

def handle_click(pos):
    global selected_piece, selected_pos, current_player
    col = pos[0] // SQUARE_SIZE
    row = pos[1] // SQUARE_SIZE

    if selected_piece is None:
        piece = board[row][col]
        if piece and piece.color == current_player:
            selected_piece = piece
            selected_pos = (row, col)
    else:
        if (row, col) in get_valid_moves(selected_piece, selected_pos[0], selected_pos[1]):
            board[row][col] = selected_piece
            board[selected_pos[0]][selected_pos[1]] = None
            selected_piece.has_moved = True

            if selected_piece.type == 'pawn' and (row == 0 or row == 7):
                board[row][col] = ChessPiece(selected_piece.color, 'queen', f'images/{selected_piece.color}_queen.png')

            current_player = 'black' if current_player == 'white' else 'white'

            if is_game_over():
                if is_check(current_player):
                    print(f"Checkmate! {current_player.capitalize()} loses.")
                else:
                    print("Stalemate!")

        selected_piece = None
        selected_pos = None

def main():
    init_board()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                handle_click(pygame.mouse.get_pos())
        draw_board()
        draw_piece()
        pygame.display.flip()
        
if __name__ == "__main__":
    main()