import random

from project.board.board_functions import create_empty_board
from project.model.empty_cell import EmptyCell


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
