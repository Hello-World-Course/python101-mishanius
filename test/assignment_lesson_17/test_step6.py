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
        # test
        import project.ui.terminal as test_file
        terminal = test_file.Terminal()
        commands_dict = terminal.get_available_commands()
        expected_result = ['click', 'flag', 'exit', 'help']
        real_result = list(commands_dict.keys())
        # verify
        self.assertEqualWithMessage(real_result, expected_result, msg=message)

    @devin_test_decorator
    @mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_help_function(self, mock_stdout, message):
        # test
        import project.ui.terminal as test_file
        terminal = test_file.Terminal()
        terminal.help()
        # verify
        expected_result = HELP_TEXT
        real_result = mock_stdout.getvalue()
        message.explanation = {'value': 'OUTPUT_MISMATCH'}
        self.assertEqualWithMessage(real_result, expected_result, msg=message)

    @devin_test_decorator
    @mock.patch('builtins.input', side_effect=['Amit', '8', '10', 'help', 'click 3A', 'click 4A', 'flag 5A', 'exit'])
    def test_running_loop(self, mock_input, message):
        # test
        import project.ui.terminal as test_file
        terminal = test_file.Terminal()
        # verify
        self.assertRaisesWithMessage(terminal.init_game, error=SystemExit, msg=message)

    @devin_test_decorator
    def test_generate_random_mines_locations_len(self, message):
        # test
        import project.model.board as test_file
        board = test_file.Board(10)
        locations = board.generate_random_mines_locations(5)
        real_result = len(locations)
        # verify
        self.assertEqualWithMessage(real_result, 5, msg=message)

    @devin_test_decorator
    def test_generate_random_mines_locations_unique(self, message):
        # test
        import project.model.board as test_file
        board = test_file.Board(10)
        locations = board.generate_random_mines_locations(5)
        real_result = len(set(locations))
        # verify
        self.assertEqualWithMessage(real_result, 5, msg=message)

    @devin_test_decorator
    def test_generate_random_mines_locations_random(self, message):
        # test
        import project.model.board as test_file
        board = test_file.Board(10)
        locations = board.generate_random_mines_locations(5)
        locations2 = board.generate_random_mines_locations(5)
        real_result = locations == locations2
        # verify
        self.assertEqualWithMessage(real_result, False, msg=message)

    @devin_test_decorator
    def test_generate_random_mines_locations_random(self, message):
        # test
        import project.model.board as test_file
        board = test_file.Board(10)

        is_ok = True
        # run the test 100 times
        for i in range(100):
            locations = board.generate_random_mines_locations(5)
            # check mines are on board
            for x, y in locations:
                if not 0 <= x < 10 or not 0 <= y < 10:
                    is_ok = False

        real_result = is_ok
        # verify
        self.assertEqualWithMessage(real_result, True, msg=message)

    @devin_test_decorator
    def test_set_mines(self, message):
        # test
        import project.model.board as test_file
        from project.model.mine import Mine
        board = test_file.Board(4)
        board.generate_random_mines_locations = lambda a: [(1, 0), (3, 1)]
        board.set_mines(2)
        # check that the cell is really a mine
        real_result = type(board[1][0]) == Mine and type(board[3][1]) == Mine
        # verify
        self.assertEqualWithMessage(real_result, True, msg=message)

    @devin_test_decorator
    def test_set_mines_value(self, message):
        # test
        import project.model.board as test_file
        board = test_file.Board(4)
        board.generate_random_mines_locations = lambda a: [(1, 0), (3, 1)]
        board.set_mines(2)
        # check that neighbor cells got a value
        real_result = [board[0][0].get_value(),
                       board[0][1].get_value(),
                       board[2][0].get_value(),
                       board[1][1].get_value(),
                       board[2][1].get_value(),
                       board[3][0].get_value(),
                       board[2][2].get_value(),
                       board[3][2].get_value()]
        # verify
        self.assertEqualWithMessage(real_result, [1, 1, 2, 1, 2, 1, 1, 1], msg=message)

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
