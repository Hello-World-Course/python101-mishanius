import random

from project.board.board_functions import create_empty_board, is_on_board
from project.model.empty_cell import EmptyCell
from project.model.mine import Mine


class Board:
    def __init__(self, board_size) -> None:
        super().__init__()
        self.board_size = board_size
        self.inner_board = [[EmptyCell(row, col) for col, _ in enumerate(range(board_size))] for row, _ in
                            enumerate(range(board_size))]

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

    def generate_random_mines_locations(self, number_of_mines):
        n = self.board_size
        cell_ids = random.sample(range(n * n), number_of_mines)
        return [(i // n, i % n) for i in cell_ids]

    def safe_inc_value(self, x, y):
        if is_on_board(x, y, self.inner_board) and type(self.inner_board[x][y]) == EmptyCell:
            current_val = 0 if self.inner_board[x][y].get_value() is None else self.inner_board[x][y].get_value()
            self.inner_board[x][y].set_value(current_val + 1)

    def set_mines(self, number_of_mines):
        coordinates = self.generate_random_mines_locations(number_of_mines)
        for x, y in coordinates:
            self.inner_board[x][y] = Mine(x, y)
            self.safe_inc_value(x, y - 1)
            self.safe_inc_value(x - 1, y - 1)
            self.safe_inc_value(x - 1, y)
            self.safe_inc_value(x - 1, y + 1)
            self.safe_inc_value(x, y + 1)
            self.safe_inc_value(x + 1, y + 1)
            self.safe_inc_value(x + 1, y)
            self.safe_inc_value(x + 1, y - 1)
