import sys

from test_base.test_base import AssignmentTester
from test_base.test_decorator import devin_test_decorator


class TestUi(AssignmentTester):

    def setUp(self):
        self.board = [[None for _ in range(10)] for _ in range(10)]

    def tearDown(self):
        try:
            del sys.modules['src.ui.user_interaction']
        except KeyError:
            pass

    @devin_test_decorator
    def test_command_parsing(self, message):
        import project.ui.board_ui as test_file

        message.expectedResult = ("flag", ['4A'])
        message.realResult = test_file.parse_cmd('flag 4A')
        message.explanation = {'value': 'INPUT_REQUEST_MISMATCH', 'params': {'order': 0}}
        self.assertEqualWithMessage(message.expectedResult, message.realResult, msg=message)

        message.expectedResult = ("test", ['1', '23', '4', '5', '67', '8'])
        message.realResult = test_file.parse_cmd('test 1 23 4 5 67 8')
        message.explanation = {'value': 'INPUT_REQUEST_MISMATCH', 'params': {'order': 1}}
        self.assertEqualWithMessage(message.expectedResult, message.realResult, msg=message)

    @devin_test_decorator
    def test_is_on_board(self, message):
        import project.board.board_functions as test_file

        message.expectedResult = True
        message.realResult = test_file.is_on_board(0, 9, self.board)
        message.explanation = {'value': 'INPUT_REQUEST_MISMATCH', 'params': {'order': 0}}
        self.assertEqualWithMessage(message.expectedResult, message.realResult, msg=message)

        message.expectedResult = False
        message.realResult = test_file.is_on_board(0, -9, self.board)
        message.explanation = {'value': 'INPUT_REQUEST_MISMATCH', 'params': {'order': 1}}
        self.assertEqualWithMessage(message.expectedResult, message.realResult, msg=message)

        message.expectedResult = False
        message.realResult = test_file.is_on_board(90, 5, self.board)
        message.explanation = {'value': 'INPUT_REQUEST_MISMATCH', 'params': {'order': 2}}
        self.assertEqualWithMessage(message.expectedResult, message.realResult, msg=message)

        message.expectedResult = False
        message.realResult = test_file.is_on_board(10, 9, self.board)
        message.explanation = {'value': 'INPUT_REQUEST_MISMATCH', 'params': {'order': 3}}
        self.assertEqualWithMessage(message.expectedResult, message.realResult, msg=message)

        message.expectedResult = True
        message.realResult = test_file.is_on_board(9, 9, self.board)
        message.explanation = {'value': 'INPUT_REQUEST_MISMATCH', 'params': {'order': 3}}
        self.assertEqualWithMessage(message.expectedResult, message.realResult, msg=message)

    @devin_test_decorator
    def test_safe_set_value(self, message):
        import project.board.board_functions as test_file

        message.expectedResult = True
        message.realResult = test_file.safe_set_value(0, 5, 9, self.board)
        message.explanation = {'value': 'INPUT_REQUEST_MISMATCH', 'params': {'order': 0}}
        self.assertEqualWithMessage(message.expectedResult, message.realResult, msg=message)

        message.expectedResult = 9
        message.realResult = self.board[0][5]
        message.explanation = {'value': 'INPUT_REQUEST_MISMATCH', 'params': {'order': 1}}
        self.assertEqualWithMessage(message.expectedResult, message.realResult, msg=message)

        message.expectedResult = False
        message.realResult = test_file.safe_set_value(0, 10, 9, self.board)
        message.explanation = {'value': 'INPUT_REQUEST_MISMATCH', 'params': {'order': 1}}
        self.assertEqualWithMessage(message.expectedResult, message.realResult, msg=message)
