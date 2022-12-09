
def is_on_board(x, y, board):
    return 0 <= x < len(board) and 0 <= y < len(board)

def safe_set_value(x, y, value, board):
    if is_on_board(x, y, board):
        board[x][y] = value
        return True
    else:
        return False

def create_empty_board(board_size):
    return [[None]*board_size for _ in range(board_size)]
