import io
import sys
from unittest import mock

from test_base.test_base import AssignmentTester
from test_base.test_decorator import devin_test_decorator

EMPTY_BOARD = """   A B C D E F G H I 
0 |_|_|_|_|_|_|_|_|_|
1 |_|_|_|_|_|_|_|_|_|
2 |_|_|_|_|_|_|_|_|_|
3 |_|_|_|_|_|_|_|_|_|
4 |_|_|_|_|_|_|_|_|_|
5 |_|_|_|_|_|_|_|_|_|
6 |_|_|_|_|_|_|_|_|_|
7 |_|_|_|_|_|_|_|_|_|
8 |_|_|_|_|_|_|_|_|_|

"""


class TestStep5(AssignmentTester):

    def tearDown(self):
        try:
            del sys.modules['project.ui.user_interaction']
        except KeyError:
            pass

    @devin_test_decorator
    def test_mine(self, message):
        # test
        import project.model.mine as test_file
        mine = test_file.Mine(0, 0)
        expected_result = '*'
        real_result = mine.str_as_clicked()
        # verify
        self.assertEqualWithMessage(real_result, expected_result, msg=message)

    @devin_test_decorator
    def test_empty_cell(self, message):
        # test
        import project.model.empty_cell as test_file
        empty_cell = test_file.EmptyCell(0, 0)
        expected_result = ' '
        real_result = empty_cell.str_as_clicked()
        # verify
        self.assertEqualWithMessage(real_result, expected_result, msg=message)

    @devin_test_decorator
    def test_empty_cell_second(self, message):
        # test
        import project.model.empty_cell as test_file
        empty_cell = test_file.EmptyCell(0, 0)
        empty_cell.set_value(6)
        expected_result = 6
        real_result = empty_cell.str_as_clicked()
        # verify
        self.assertEqualWithMessage(real_result, expected_result, msg=message)

    @devin_test_decorator
    def test_board_length(self, message):
        # test
        import project.model.board as test_file
        b = test_file.Board(6)

        expected_result = 6
        real_result = len(b)
        # verify
        self.assertEqualWithMessage(real_result, expected_result, msg=message)

    @devin_test_decorator
    def test_board_get_item(self, message):
        # test
        import project.model.board as test_file
        import project.model.mine as mine_file
        board = test_file.Board(6)
        mine = mine_file.Mine(1, 1)
        board.inner_board[1][1] = mine

        expected_result = mine
        real_result = board[1][1]
        # verify
        self.assertEqualWithMessage(real_result, expected_result, msg=message)

    @devin_test_decorator
    def test_board_set_flag(self, message):
        # test
        import project.model.board as test_file
        import project.model.mine as mine_file
        board = test_file.Board(6)
        mine = mine_file.Mine(1, 1)
        board.inner_board[1][1] = mine
        board.set_flag(1, 1)

        expected_result = True
        real_result = board[1][1].is_flaged()
        # verify
        self.assertEqualWithMessage(real_result, expected_result, msg=message)

    @devin_test_decorator
    def test_board_click(self, message):
        # test
        import project.model.board as test_file
        import project.model.mine as mine_file
        board = test_file.Board(6)
        mine = mine_file.Mine(1, 1)
        board.inner_board[1][1] = mine
        board.click(1, 1)

        expected_result = True
        real_result = board[1][1].is_clicked()
        # verify
        self.assertEqualWithMessage(real_result, expected_result, msg=message)



    @devin_test_decorator
    def test_board_not_click(self, message):
        # test
        import project.model.board as test_file
        import project.model.mine as mine_file
        board = test_file.Board(6)
        mine = mine_file.Mine(1, 1)
        board.inner_board[1][1] = mine
        board.click(1, 1)
        expected_result = False
        real_result = board[0][0].is_clicked()
        # verify
        self.assertEqualWithMessage(real_result, expected_result, msg=message)

    @devin_test_decorator
    @mock.patch('sys.stdout', new_callable=io.StringIO)
    @mock.patch('builtins.input', side_effect=["f", "f", "f", "f", "Micael", "9", "40"])
    def test_terminal_init(self, mock_input, mock_stdout, message):
        # test
        import project.ui.terminal as test_file
        terminal = test_file.Terminal()
        terminal.init_game()
        # verify
        expected_result = "Your name is too short\nYour name is too short\nYour name is too short\nYour name is too short\n"

        real_result = mock_stdout.getvalue()
        self.assertEqualWithMessage(real_result, expected_result, msg=message)

    @devin_test_decorator
    @mock.patch('sys.stdout', new_callable=io.StringIO)
    @mock.patch('builtins.input', side_effect=["Micael", "9", "40"])
    def test_terminal_draw(self, mock_input, mock_stdout, message):
        # test
        import project.ui.terminal as test_file
        terminal = test_file.Terminal()
        terminal.init_game()
        terminal.draw()
        # verify
        expected_result = EMPTY_BOARD
        real_result = mock_stdout.getvalue()

        self.assertEqualWithMessage(real_result, expected_result, msg=message)
