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
        ######
        import project.model.mine as test_file
        mine = test_file.Mine(0,0)
        message.expectedResult = '*'
        message.realResult = mine.str_as_clicked()
        # verify
        self.assertEqualWithMessage(message.expectedResult, message.realResult, msg=message)

    @devin_test_decorator
    def test_empty_cell(self, message):
        import project.model.empty_cell as test_file
        empty_cell = test_file.EmptyCell(0,0)

        message.expectedResult = ' '
        message.realResult = empty_cell.str_as_clicked()
        self.assertEqualWithMessage(message.expectedResult, message.realResult, msg=message)

        empty_cell.val = 6
        message.expectedResult = '6'
        message.realResult = empty_cell.str_as_clicked()
        self.assertEqualWithMessage(message.expectedResult, message.realResult, msg=message)

    @devin_test_decorator
    def test_empty_cell(self, message):
        import project.model.empty_cell as test_file
        empty_cell = test_file.EmptyCell(0, 0)

        message.expectedResult = ' '
        message.realResult = empty_cell.str_as_clicked()
        self.assertEqualWithMessage(message.expectedResult, message.realResult, msg=message)

        empty_cell.val = 6
        message.expectedResult = '6'
        message.realResult = empty_cell.str_as_clicked()
        self.assertEqualWithMessage(message.expectedResult, message.realResult, msg=message)

    @devin_test_decorator
    def test_board_length(self, message):
        import project.model.board as test_file
        b = test_file.Board(6)

        message.expectedResult = 6
        message.realResult = len(b)
        message.explanation = {'value': 'CODE_MISMATCH'}
        self.assertEqualWithMessage(message.expectedResult, message.realResult, msg=message)

    @devin_test_decorator
    def test_board_get_item(self, message):
        import project.model.board as test_file
        import project.model.mine as mine_file
        board = test_file.Board(6)
        mine = mine_file.Mine(1,1)
        board.board[1][1] = mine

        message.expectedResult = mine
        message.realResult = board[1][1]
        message.explanation = {'value': 'CODE_MISMATCH'}
        self.assertEqualWithMessage(message.expectedResult, message.realResult, msg=message)

    @devin_test_decorator
    def test_board_set_flag(self, message):
        import project.model.board as test_file
        import project.model.mine as mine_file
        board = test_file.Board(6)
        mine = mine_file.Mine(1,1)
        board.board[1][1] = mine
        board.set_flag(1, 1)

        message.expectedResult = True
        message.realResult = board[1][1].is_flag
        message.explanation = {'value': 'CODE_MISMATCH'}
        self.assertEqualWithMessage(message.expectedResult, message.realResult, msg=message)

    @devin_test_decorator
    def test_board_click(self, message):
        import project.model.board as test_file
        import project.model.mine as mine_file
        board = test_file.Board(6)
        mine = mine_file.Mine(1, 1)
        board.board[1][1] = mine
        board.click(1, 1)

        message.expectedResult = True
        message.realResult = board[1][1].is_clicked
        message.explanation = {'value': 'CODE_MISMATCH'}
        self.assertEqualWithMessage(message.expectedResult, message.realResult, msg=message)

        message.expectedResult = False
        message.realResult = board[0][0].is_clicked
        message.explanation = {'value': 'CODE_MISMATCH'}
        self.assertEqualWithMessage(message.expectedResult, message.realResult, msg=message)

    @devin_test_decorator
    @mock.patch('sys.stdout', new_callable=io.StringIO)
    @mock.patch('builtins.input', side_effect=["f", "f", "f", "f", "Micael", "9", "40"])
    def test_terminal_init(self, mock_input, mock_stdout, message):
        import project.ui.terminal as test_file
        terminal = test_file.Terminal()
        terminal.init_game()

        message.expectedResult = "Your name is too short\nYour name is too short\nYour name is too short\nYour name is too short\n"
        message.realResult = mock_stdout.getvalue()
        message.explanation = {'value': 'CODE_MISMATCH'}
        self.assertEqualWithMessage(message.expectedResult, message.realResult, msg=message)

    @devin_test_decorator
    @mock.patch('sys.stdout', new_callable=io.StringIO)
    @mock.patch('builtins.input', side_effect=["Micael", "9", "40"])
    def test_terminal_draw(self, mock_input, mock_stdout, message):
        import project.ui.terminal as test_file
        terminal = test_file.Terminal()
        terminal.init_game()
        terminal.draw()

        message.expectedResult = EMPTY_BOARD
        message.realResult = mock_stdout.getvalue()
        message.explanation = {'value': 'CODE_MISMATCH'}
        self.assertEqualWithMessage(message.expectedResult, message.realResult, msg=message)
