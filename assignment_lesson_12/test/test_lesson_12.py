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

    @mock.patch('builtins.input', side_effect=["i" for _ in range(1000)])
    def test_board_functions_create_empty_board(self, *args):
        import project.game.board_functions as board_functions
        board = board_functions.create_empty_board(2)
        self.assertEqual(board, [[None for _ in range(2)] for _ in range(2)])

    @mock.patch('builtins.input', side_effect=['Dan', '9', '40'])
    def test_coordinate_conversion(self, *args):
        import project.ui.board_ui as test_file
        self.assertEqual(test_file.convert_coords("23A"), (22, 0))
        self.assertEqual(test_file.convert_coords("4D"), (3, 3))

    @mock.patch('builtins.input', side_effect=["i" for _ in range(1000)])
    def test_board_functions_draw_board(self, *args):
        import project.game.board_functions as board_functions
        import project.ui.board_ui as board_ui
        board = board_functions.create_empty_board(2, None)
        drawn_board = board_ui.draw_board(board, 20)
        self.assertEqual(drawn_board, '   A B \n0 |_|_|\n1 |_|_|\n')