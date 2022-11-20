import sys
import unittest
from unittest import mock
import io


class TestLesson(unittest.TestCase):

    def tearDown(self):
        try:
            del sys.modules['project.ui.user_interaction']
        except KeyError:
            pass

    @mock.patch('builtins.input', side_effect=['Dan', '9', '40'])
    def test_command_parsing(self, *args):
        import project.ui.board_ui as test_file
        self.assertEqual(test_file.parse_cmd("flag 4A"), ("flag", ['4A']))
        self.assertEqual(test_file.parse_cmd("test 1 23 4 5 67 8"), ("test", ['1', '23', '4', '5', '67', '8']))

    @mock.patch('builtins.input', side_effect=['Dan', '9', '40'])
    def test_is_on_board(self, *args):
        import project.game.board_functions as board_functions
        board = [[None for _ in range(10)] for _ in range(10)]
        self.assertEqual(board_functions.is_on_board(x=0, y=9, board=board), True)
        self.assertEqual(board_functions.is_on_board(x=0, y=-9, board=board), False)
        self.assertEqual(board_functions.is_on_board(x=90, y=5, board=board), False)
        self.assertEqual(board_functions.is_on_board(x=10, y=9, board=board), False)
        self.assertEqual(board_functions.is_on_board(x=9, y=9, board=board), True)

    @mock.patch('builtins.input', side_effect=['Dan', '9', '40'])
    def test_safe_set_value(self, *args):
        import project.game.board_functions as board_functions
        board = [[None for _ in range(10)] for _ in range(10)]
        self.assertEqual(board_functions.safe_set_value(0, 5, 9, board), True)
        self.assertEqual(board[0][5], 9)
        self.assertEqual(board_functions.safe_set_value(0, 10, 9, board), False)
        self.assertEqual(board[0][5], 9)