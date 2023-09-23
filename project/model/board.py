from project.board.board_functions import create_empty_board
from project.model.empty_cell import EmptyCell


class Board:
    def __init__(self, board_size) -> None:
        super().__init__()
        self.inner_board = [[EmptyCell(row, col) for col, _ in enumerate(range(board_size))] for row, _ in enumerate(range(board_size))]

    def __len__(self):
        return len(self.inner_board)

    def __getitem__(self, key):
        return self.inner_board[key]

    def set_flag(self, x, y):
        self.inner_board[x][y].set_flag()

    def click(self, x, y):
        self.inner_board[x][y].set_clicked()

    def reveal_all(self):
        for i in self.inner_board:
            for j in i:
                j.set_clicked()
