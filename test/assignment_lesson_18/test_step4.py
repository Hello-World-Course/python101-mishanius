import sys
from unittest import mock

from test_base.test_base import AssignmentTester
from test_base.test_decorator import devin_test_decorator


class TestStep4(AssignmentTester):

    def tearDown(self):
        try:
            del sys.modules['src.ui.user_interaction']
        except KeyError:
            pass

    @devin_test_decorator
    @mock.patch('builtins.input', side_effect=["i" for _ in range(1000)])
    def test_board_functions_create_empty_board(self, *args, message):
        import project.board.board_functions as board

        message.expectedResult = [[None for _ in range(2)] for _ in range(2)]
        message.realResult = board.create_empty_board(2, None)
        message.explanation = {'value': 'INPUT_REQUEST_MISMATCH', 'params': {'order': 0}}
        self.assertEqualWithMessage(message.expectedResult, message.realResult, msg=message)

    @devin_test_decorator
    @mock.patch('builtins.input', side_effect=['Dan', '9', '40'])
    def test_coordinate_conversion(self, *args, message):
        import project.ui.board_ui as test_file

        message.expectedResult = (321, 26)
        message.realResult = test_file.convert_coords("322AA")
        message.explanation = {'value': 'INPUT_REQUEST_MISMATCH', 'params': {'order': 0}}
        self.assertEqualWithMessage(message.expectedResult, message.realResult, msg=message)

        message.expectedResult = (3, 0)
        message.realResult = test_file.convert_coords("4A")
        message.explanation = {'value': 'INPUT_REQUEST_MISMATCH', 'params': {'order': 1}}
        self.assertEqualWithMessage(message.expectedResult, message.realResult, msg=message)

    @devin_test_decorator
    @mock.patch('builtins.input', side_effect=["i" for _ in range(1000)])
    def test_board_functions_draw_board(self, *args, message):
        import project.board.board_functions as board
        import project.ui.board_ui as board_ui
        board = board.create_empty_board(2, None)

        message.expectedResult = '   A B \n0 |_|_|\n1 |_|_|\n'
        message.realResult = board_ui.draw_board(board, 20)
        message.explanation = {'value': 'INPUT_REQUEST_MISMATCH', 'params': {'order': 0}}
        self.assertEqualWithMessage(message.expectedResult, message.realResult, msg=message)

    @devin_test_decorator
    @mock.patch('builtins.input', side_effect=["i" for _ in range(1000)])
    def test_board_cant_draw(self, *args, message):
        import project.board.board_functions as board
        import project.ui.board_ui as board_ui
        board = board.create_empty_board(20, None)
        self.assertRaisesWithMessage(board_ui.draw_board, board, 2, error=ValueError, msg=message)
