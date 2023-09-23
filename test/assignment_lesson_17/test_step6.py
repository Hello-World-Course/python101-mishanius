import io
import sys
from unittest import mock

from test_base.test_base import AssignmentTester
from test_base.test_decorator import devin_test_decorator

HELP_TEXT = """-----------------------------HELP-------------------------------------------
to click a cell type: click <row_number><column_char>. example: "click 5A"
to flag a cell type: flag <row_number><column_letter>. example: "flag 5A"
to exit the game type: "exit"
board recommendations:
beginner: board size: 8, mines: 10
intermediate: board size: 16, mines: 40
expert: board size: 22, mines: 99
----------------------------------------------------------------------------
"""


class TestStep6(AssignmentTester):

    def tearDown(self):
        try:
            del sys.modules['project.ui.user_interaction']
        except KeyError:
            pass

    @devin_test_decorator
    def test_get_available_commands(self, message):
        import project.ui.terminal as test_file
        terminal = test_file.Terminal()
        commands_dict = terminal.get_available_commands()
        print(commands_dict)
        expected_result = ['click', 'flag', 'exit', 'help']
        real_result = list(commands_dict.keys())
        message.explanation = {'value': 'MISMATCH'}
        self.assertEqualWithMessage(real_result, expected_result, msg=message)

    @devin_test_decorator
    @mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_help_function(self, mock_stdout, message):
        import project.ui.terminal as test_file
        terminal = test_file.Terminal()
        terminal.help()

        expected_result = HELP_TEXT
        real_result = mock_stdout.getvalue()
        message.explanation = {'value': 'OUTPUT_MISMATCH'}
        self.assertEqualWithMessage(real_result, expected_result, msg=message)

    @devin_test_decorator
    @mock.patch('builtins.input', side_effect=[
        'Amit', '8', '10', 'help', 'click 3A', 'click 4a', 'flag 5A', 'exit'
    ])
    def test_running_loop(self, mock_input, message):
        import project.ui.terminal as test_file
        terminal = test_file.Terminal()
        self.assertRaisesWithMessage(terminal.init_game, error=SystemExit, msg=message)

    @devin_test_decorator
    def test_generate_random_mines_locations(self, message):
        # test
        import project.model.board as test_file
        board = test_file.Board(10)
        locations = board.generate_random_mines_locations(5)

        # verify len is 5
        message.explanation = {'value': 'WRONG_NUMBER_OF_MINES'}
        self.assertEqualWithMessage(5, len(locations), msg=message)

        # Mines are unique
        message.explanation = {'value': 'DUPLICATED_MINE_LOCATIONS'}
        self.assertEqualWithMessage(5, len(set(locations)), msg=message)

        # Mines are random
        message.explanation = {'value': 'MINES_ARE_NOT_RANDOM'}
        locations2 = board.generate_random_mines_locations(5)
        self.assertEqualWithMessage(True, locations2 != locations, msg=message)

        # Mines are on board
        is_ok = True
        for x, y in locations:
            if not 0 <= x < 10 or not 0 <= y < 10:
                is_ok = False
        message.explanation = {'value': 'MINES_ARE_OUT_OF_BOARD'}
        self.assertEqualWithMessage(True, is_ok, msg=message)

    @devin_test_decorator
    def test_set_mines(self, message):
        # test
        import project.model.board as test_file
        board = test_file.Board(4)
        board.generate_random_mines_locations = lambda a: [(1, 0), (3, 1)]
        board.set_mines(2)

        from project.model.mine import Mine
        # verify mines at place
        message.explanation = {'value': 'NOT_A_MINE', 'params': {'location': [1, 0]}}
        self.assertEqualWithMessage(True, type(board[1][0]) == Mine, msg=message)
        message.explanation = {'value': 'NOT_A_MINE', 'params': {'location': [3, 1]}}
        self.assertEqualWithMessage(True, type(board[3][1]) == Mine, msg=message)

        # verify mines at place
        message.explanation = {'value': 'CELL_VALUE_IS_WRONG', 'params': {'location': [0, 0]}}
        self.assertEqualWithMessage(board[0][0].get_value(), 1, msg=message)
        message.explanation = {'value': 'CELL_VALUE_IS_WRONG', 'params': {'location': [0, 1]}}
        self.assertEqualWithMessage(board[0][1].get_value(), 1, msg=message)
        message.explanation = {'value': 'CELL_VALUE_IS_WRONG', 'params': {'location': [2, 0]}}
        self.assertEqualWithMessage(board[2][0].get_value(), 2, msg=message)
        message.explanation = {'value': 'CELL_VALUE_IS_WRONG', 'params': {'location': [1, 1]}}
        self.assertEqualWithMessage(board[1][1].get_value(), 1, msg=message)
        message.explanation = {'value': 'CELL_VALUE_IS_WRONG', 'params': {'location': [2, 1]}}
        self.assertEqualWithMessage(board[2][1].get_value(), 2, msg=message)
        message.explanation = {'value': 'CELL_VALUE_IS_WRONG', 'params': {'location': [3, 0]}}
        self.assertEqualWithMessage(board[3][0].get_value(), 1, msg=message)
        message.explanation = {'value': 'CELL_VALUE_IS_WRONG', 'params': {'location': [2, 2]}}
        self.assertEqualWithMessage(board[2][2].get_value(), 1, msg=message)
        message.explanation = {'value': 'CELL_VALUE_IS_WRONG', 'params': {'location': [3, 2]}}
        self.assertEqualWithMessage(board[3][2].get_value(), 1, msg=message)

    @devin_test_decorator
    def test_mines_are_random(self, message):
        import project.model.board as test_file
        board = test_file.Board(10)
        board.set_mines(10)

        import project.model.mine as mine_test
        mine_locations_first = set()
        # count number of mines
        for i in range(100):
            if type(board[i // 10][i % 10]) == mine_test.Mine:
                mine_locations_first.add(i)

        board = test_file.Board(10)
        board.set_mines(10)
        mine_locations_second = set()
        # count number of mines
        for i in range(100):
            if type(board[i // 10][i % 10]) == mine_test.Mine:
                mine_locations_second.add(i)

        expected_result = True
        real_result = mine_locations_second != mine_locations_first
        message.explanation = {'value': 'MINES_NOT_RANDOM'}
        self.assertEqualWithMessage(real_result, expected_result, msg=message)
