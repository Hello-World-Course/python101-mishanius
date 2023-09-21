import io
import sys
from unittest import mock

from test_base.test_base import AssignmentTester
from test_base.test_decorator import devin_test_decorator


class TestUi(AssignmentTester):

    def tearDown(self):
        try:
            del sys.modules['src.ui.user_interaction']
        except KeyError:
            pass

    @devin_test_decorator
    def test_name(self, message):
        import project.ui.user_interaction as test_file

        message.expectedResult = True
        message.realResult = test_file.is_name_valid('Alon')
        message.explanation = {'value': 'INPUT_REQUEST_MISMATCH', 'params': {'order': 0}}
        self.assertEqualWithMessage(message.expectedResult, message.realResult, msg=message)

        message.expectedResult = False
        message.realResult = test_file.is_name_valid('A')
        message.explanation = {'value': 'INPUT_REQUEST_MISMATCH', 'params': {'order': 1}}
        self.assertEqualWithMessage(message.expectedResult, message.realResult, msg=message)

        message.expectedResult = False
        message.realResult = test_file.is_name_valid('')
        message.explanation = {'value': 'INPUT_REQUEST_MISMATCH', 'params': {'order': 2}}
        self.assertEqualWithMessage(message.expectedResult, message.realResult, msg=message)

    @devin_test_decorator
    def test_board_size(self, message):
        import project.ui.user_interaction as test_file

        message.expectedResult = False
        message.realResult = test_file.is_board_size_valid(0)
        message.explanation = {'value': 'INPUT_REQUEST_MISMATCH', 'params': {'order': 0}}
        self.assertEqualWithMessage(message.expectedResult, message.realResult, msg=message)

        message.expectedResult = False
        message.realResult = test_file.is_board_size_valid(-1)
        message.explanation = {'value': 'INPUT_REQUEST_MISMATCH', 'params': {'order': 1}}
        self.assertEqualWithMessage(message.expectedResult, message.realResult, msg=message)

        message.expectedResult = True
        message.realResult = test_file.is_board_size_valid(7)
        message.explanation = {'value': 'INPUT_REQUEST_MISMATCH', 'params': {'order': 2}}
        self.assertEqualWithMessage(message.expectedResult, message.realResult, msg=message)

    @devin_test_decorator
    def test_number_of_mines(self, message):
        import project.ui.user_interaction as test_file

        message.expectedResult = False
        message.realResult = test_file.is_number_of_mines_valid(0, 5)
        message.explanation = {'value': 'INPUT_REQUEST_MISMATCH', 'params': {'order': 0}}
        self.assertEqualWithMessage(message.expectedResult, message.realResult, msg=message)

        message.expectedResult = False
        message.realResult = test_file.is_number_of_mines_valid(13, 5)
        message.explanation = {'value': 'INPUT_REQUEST_MISMATCH', 'params': {'order': 1}}
        self.assertEqualWithMessage(message.expectedResult, message.realResult, msg=message)

        message.expectedResult = True
        message.realResult = test_file.is_number_of_mines_valid(7, 5)
        message.explanation = {'value': 'INPUT_REQUEST_MISMATCH', 'params': {'order': 2}}
        self.assertEqualWithMessage(message.expectedResult, message.realResult, msg=message)

    @devin_test_decorator
    @mock.patch('sys.stdout', new_callable=io.StringIO)
    @mock.patch('builtins.input', side_effect=['Dan', '9', '40'])
    def test_full_interaction(self, mock_input, mock_stdout, message):
        import project.ui.user_interaction as test_file

        message.expectedResult = ('Dan', 9, 40)
        message.realResult = test_file.register_user()
        message.explanation = {'value': 'INPUT_REQUEST_MISMATCH', 'params': {'order': 0}}
        self.assertEqualWithMessage(message.expectedResult, message.realResult, msg=message)
