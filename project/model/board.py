from project.board.board_functions import create_empty_board


class Board:
    def __init__(self, board_size) -> None:
        super().__init__()
        self.inner_board = create_empty_board(board_size, None)

    def __len__(self):
        return 7

    def __getitem__(self, key):
        return self.inner_board[key]

    def set_flag(self, x, y):
        self.inner_board[x][y].set_flag()

    def click(self, x, y):
        self.inner_board[x][y].set_clicked()
