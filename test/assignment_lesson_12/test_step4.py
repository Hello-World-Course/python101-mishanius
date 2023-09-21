import sys
from unittest import mock

from test_base.test_base import AssignmentTester, Message
from test_base.test_decorator import devin_test_decorator


class Step4(AssignmentTester):

    def tearDown(self):
        try:
            del sys.modules['src.ui.user_interaction']
        except KeyError:
            pass

    @devin_test_decorator
    @mock.patch('builtins.input', side_effect=["i" for _ in range(1000)])
    def test_board_functions_create_empty_board(self, *args, message):
        # test
        import project.board.board_functions as board_functions

        expected_result = [["_" for _ in range(2)] for _ in range(2)]
        real_result = board_functions.create_empty_board(2, "_")
        # verify
        message.explanation = {'value': 'CODE_MISMATCH'}
        self.assertEqualWithMessage(real_result, expected_result, msg=message)

    @devin_test_decorator
    @mock.patch('builtins.input', side_effect=['Dan', '9', '40'])
    def test_coordinate_conversion_1(self, *args, message):
        # test
        import project.ui.board_ui as test_file

        expected_result = (322, 0)
        real_result = test_file.convert_coords("322A")
        # verify
        message.explanation = {'value': 'CODE_MISMATCH'}
        self.assertEqualWithMessage(real_result, expected_result, msg=message)

    @devin_test_decorator
    @mock.patch('builtins.input', side_effect=['Dan', '9', '40'])
    def test_coordinate_conversion_2(self, *args, message):
        # test
        import project.ui.board_ui as test_file
        expected_result = (4, 0)
        real_result = test_file.convert_coords("4A")
        # verify
        message.explanation = {'value': 'CODE_MISMATCH'}
        self.assertEqualWithMessage(real_result, expected_result, msg=message)

    @devin_test_decorator
    @mock.patch('builtins.input', side_effect=["i" for _ in range(1000)])
    def test_board_functions_draw_board(self, *args, message):
        # test
        import project.board.board_functions as board_functions
        import project.ui.board_ui as board_ui
        board = board_functions.create_empty_board(2, "_")

        expected_result = '   A B \n0 |_|_|\n1 |_|_|\n'
        real_result = board_ui.draw_board(board, 20)
        # verify
        message.explanation = {'value': 'CODE_MISMATCH'}
        self.assertEqualWithMessage(real_result, expected_result, msg=message)
