import io
import sys
from unittest import mock

from test_base.test_base import Message, AssignmentTester
from test_base.test_decorator import devin_test_decorator


class TestUi(AssignmentTester):

    def tearDown(self):
        try:
            del sys.modules['project.ui.user_interaction']
        except KeyError:
            pass

    def execute_the_file(self, side_effect_args, test_file, message):
        name = None
        board_size = None
        number_of_mines = None
        message.args = side_effect_args
        try:
            name = test_file.name
            board_size = test_file.board_size
            number_of_mines = test_file.number_of_mines

        except Exception as e:
            message.exception = str(e)
        return name, board_size, number_of_mines, message

    side_effect_wrong_name = ['M', '9', '3']

    @devin_test_decorator
    @mock.patch('sys.stdout', new_callable=io.StringIO)
    @mock.patch('builtins.input', side_effect=side_effect_wrong_name)
    def test_step2_1_wrong_name(self, mock_input, mock_stdout, message):
        import project.ui.user_interaction as test_file
        name, board_size, number_of_mines, message = self.execute_the_file(TestUi.side_effect_wrong_name, test_file, message)

        message.expectedResult = None
        message.realResult = name
        message.explanation = {'value': "GLOBAL_VAR_MISMATCH", 'params': {'var_name': 'name'}}
        self.assertEqualWithMessage(message.realResult, message.expectedResult, msg=message)

        message.expectedResult = None
        message.realResult = board_size
        message.explanation = {'value': "GLOBAL_VAR_MISMATCH", 'params': {'var_name': 'board_size'}}
        self.assertEqualWithMessage(message.realResult, message.expectedResult, msg=message)

        message.expectedResult = None
        message.realResult = number_of_mines
        message.explanation = {'value': "GLOBAL_VAR_MISMATCH", 'params': {'var_name': 'number_of_mines'}}
        self.assertEqualWithMessage(message.realResult, message.expectedResult, msg=message)

        message.expectedResult = "Your name is too short\n"
        message.realResult = mock_stdout.getvalue()
        message.explanation = {'value': "STD_OUT_MISMATCH"}
        self.assertEqualWithMessage(message.realResult, message.expectedResult, msg=message)

    side_effect_wrong_board = ['Dan', '0', '0', '0']

    @devin_test_decorator
    @mock.patch('sys.stdout', new_callable=io.StringIO)
    @mock.patch('builtins.input', side_effect=side_effect_wrong_board)
    def test_step2_2_wrong_board_size(self, mock_input, mock_stdout, message):
        import project.ui.user_interaction as test_file
        name, board_size, number_of_mines, message = self.execute_the_file(TestUi.side_effect_wrong_board, test_file, message)

        message.expectedResult = 'Dan'
        message.realResult = name
        message.explanation = {'value': "GLOBAL_VAR_MISMATCH", 'params': {'var_name': 'name'}}
        self.assertEqualWithMessage(message.realResult, message.expectedResult, msg=message)

        message.expectedResult = None
        message.realResult = board_size
        message.explanation = {'value': "GLOBAL_VAR_MISMATCH", 'params': {'var_name': 'board_size'}}
        self.assertEqualWithMessage(message.realResult, message.expectedResult, msg=message)

        message.expectedResult = None
        message.realResult = number_of_mines
        message.explanation = {'value': "GLOBAL_VAR_MISMATCH", 'params': {'var_name': 'number_of_mines'}}
        self.assertEqualWithMessage(message.realResult, message.expectedResult, msg=message)

        message.expectedResult = "Dan you entered illegal board size\n"
        message.realResult = mock_stdout.getvalue()
        message.explanation = {'value': "STD_OUT_MISMATCH"}
        self.assertEqualWithMessage(message.realResult, message.expectedResult, msg=message)

    side_effect_wrong_board_negative = ['Dan', '-2', '0', '0', '0', '0']

    @devin_test_decorator
    @mock.patch('sys.stdout', new_callable=io.StringIO)
    @mock.patch('builtins.input', side_effect=side_effect_wrong_board_negative)
    def test_step2_3_wrong_board_size_negative(self, mock_input, mock_stdout, message):
        import project.ui.user_interaction as test_file
        name, board_size, number_of_mines, message = self.execute_the_file(
            TestUi.side_effect_wrong_board_negative, test_file, message
        )

        message.expectedResult = 'Dan'
        message.realResult = name
        message.explanation = {'value': "GLOBAL_VAR_MISMATCH", 'params': {'var_name': 'name'}}
        self.assertEqualWithMessage(message.realResult, message.expectedResult, msg=message)

        message.expectedResult = None
        message.realResult = board_size
        message.explanation = {'value': "GLOBAL_VAR_MISMATCH", 'params': {'var_name': 'board_size'}}
        self.assertEqualWithMessage(message.realResult, message.expectedResult, msg=message)

        message.expectedResult = None
        message.realResult = number_of_mines
        message.explanation = {'value': "GLOBAL_VAR_MISMATCH", 'params': {'var_name': 'number_of_mines'}}
        self.assertEqualWithMessage(message.realResult, message.expectedResult, msg=message)

        message.expectedResult = "Dan you entered illegal board size\n"
        message.realResult = mock_stdout.getvalue()
        message.explanation = {'value': "STD_OUT_MISMATCH"}
        self.assertEqualWithMessage(message.realResult, message.expectedResult, msg=message)

    side_effect_wrong_number_of_mines_too_low = ['Dan', '6', '0', '0', '0', '0', '0']

    @devin_test_decorator
    @mock.patch('sys.stdout', new_callable=io.StringIO)
    @mock.patch('builtins.input', side_effect=side_effect_wrong_number_of_mines_too_low)
    def test_step2_4_wrong_number_of_mines_too_low(self, mock_input, mock_stdout, message):
        import project.ui.user_interaction as test_file
        name, board_size, number_of_mines, message = self.execute_the_file(
            TestUi.side_effect_wrong_number_of_mines_too_low, test_file, message
        )

        message.expectedResult = 'Dan'
        message.realResult = name
        message.explanation = {'value': "GLOBAL_VAR_MISMATCH", 'params': {'var_name': 'name'}}
        self.assertEqualWithMessage(message.realResult, message.expectedResult, msg=message)

        message.expectedResult = 6
        message.realResult = board_size
        message.explanation = {'value': "GLOBAL_VAR_MISMATCH", 'params': {'var_name': 'board_size'}}
        self.assertEqualWithMessage(message.realResult, message.expectedResult, msg=message)

        message.expectedResult = None
        message.realResult = number_of_mines
        message.explanation = {'value': "GLOBAL_VAR_MISMATCH", 'params': {'var_name': 'number_of_mines'}}
        self.assertEqualWithMessage(message.realResult, message.expectedResult, msg=message)

        message.expectedResult = "Dan you entered illegal number of mines\n"
        message.realResult = mock_stdout.getvalue()
        message.explanation = {'value': "STD_OUT_MISMATCH"}
        self.assertEqualWithMessage(message.realResult, message.expectedResult, msg=message)

    side_effect_wrong_number_of_mines_too_high = ['Dan', '6', '19', '0', '0', '0', '0']

    @devin_test_decorator
    @mock.patch('sys.stdout', new_callable=io.StringIO)
    @mock.patch('builtins.input', side_effect=side_effect_wrong_number_of_mines_too_high)
    def test_step2_5_wrong_number_of_mines_too_high(self, mock_input, mock_stdout, message):
        import project.ui.user_interaction as test_file
        name, board_size, number_of_mines, message = self.execute_the_file(
            TestUi.side_effect_wrong_number_of_mines_too_high, test_file, message
        )

        message.expectedResult = 'Dan'
        message.realResult = name
        message.explanation = {'value': "GLOBAL_VAR_MISMATCH", 'params': {'var_name': 'name'}}
        self.assertEqualWithMessage(message.realResult, message.expectedResult, msg=message)

        message.expectedResult = 6
        message.realResult = board_size
        message.explanation = {'value': "GLOBAL_VAR_MISMATCH", 'params': {'var_name': 'board_size'}}
        self.assertEqualWithMessage(message.realResult, message.expectedResult, msg=message)

        message.expectedResult = None
        message.realResult = number_of_mines
        message.explanation = {'value': "GLOBAL_VAR_MISMATCH", 'params': {'var_name': 'number_of_mines'}}
        self.assertEqualWithMessage(message.realResult, message.expectedResult, msg=message)

        message.expectedResult = "Dan you entered illegal number of mines\n"
        message.realResult = mock_stdout.getvalue()
        message.explanation = {'value': "STD_OUT_MISMATCH"}
        self.assertEqualWithMessage(message.realResult, message.expectedResult, msg=message)

    side_effect_all_correct = ['Dan', '6', '1', '0', '0', '0', '0', '0']

    @devin_test_decorator
    @mock.patch('sys.stdout', new_callable=io.StringIO)
    @mock.patch('builtins.input', side_effect=side_effect_all_correct)
    def test_step2_6_all_correct(self, mock_input, mock_stdout, message):
        import project.ui.user_interaction as test_file
        name, board_size, number_of_mines, message = self.execute_the_file(
            TestUi.side_effect_all_correct, test_file, message
        )

        message.expectedResult = 'Dan'
        message.realResult = name
        message.explanation = {'value': "GLOBAL_VAR_MISMATCH", 'params': {'var_name': 'name'}}
        self.assertEqualWithMessage(message.realResult, message.expectedResult, msg=message)

        message.expectedResult = 6
        message.realResult = board_size
        message.explanation = {'value': "GLOBAL_VAR_MISMATCH", 'params': {'var_name': 'board_size'}}
        self.assertEqualWithMessage(message.realResult, message.expectedResult, msg=message)

        message.expectedResult = 1
        message.realResult = number_of_mines
        message.explanation = {'value': "GLOBAL_VAR_MISMATCH", 'params': {'var_name': 'number_of_mines'}}
        self.assertEqualWithMessage(message.realResult, message.expectedResult, msg=message)
