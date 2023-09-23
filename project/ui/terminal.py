from project.model.board import Board
from project.ui.board_ui import draw_board, parse_cmd, convert_coords
from project.ui.user_interaction import register_user


EXPLANATION = """-----------------------------HELP-------------------------------------------
to click a cell type: click <row_number><column_char>. example: "click 5A"
to flag a cell type: flag <row_number><column_letter>. example: "flag 5A"
to exit the game type: "exit"
board recommendations:
beginner: board size: 8, mines: 10
intermediate: board size: 16, mines: 40
expert: board size: 22, mines: 99
----------------------------------------------------------------------------
"""

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

    def running_loop(self):
        while True:
            print(self.draw())
            cmd = input("Provide cmd")
            cmd, params = parse_cmd(cmd)
            self.get_available_commands()[cmd](self, *params)


    def get_available_commands(self):
        return {
            'click' : self.click,
            'flag' : self.flag,
            'exit': self.exit,
            'help': self.help
        }

    def click(self, *args):
        row, col = convert_coords(args[0])
        self.current_board[row][col].set_clicked()

    def flag(self, *args):
        row, col = convert_coords(args[0])
        self.current_board[row][col].set_flag()

    def exit(self, *args):
        self.current_board.reveal_all()
        print(self.draw())
        exit(0)

    def help(self, *args):
        print(EXPLANATION)

    def _create_string(self):
        return draw_board(self.current_board, 0)

    def draw(self):
        print(self._create_string())
