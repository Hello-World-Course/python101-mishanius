from project.model.board import Board
from project.ui.board_ui import draw_board
from project.ui.user_interaction import register_user


class Terminal:
    def __init__(self) -> None:
        super().__init__()
        self.name = None
        self.current_board = None
        self.number_of_mines = None
        self.board_size = None

    def init_game(self):
        self.name, self.board_size, self.number_of_mines = register_user()
        if not self.name or not self.board_size or not self.number_of_mines:
            print("Failed to init game")
            return
        self.current_board = Board(self.board_size)

    def _create_string(self):
        return draw_board(self.current_board, 0)

    def draw(self):
        print(self._create_string())
