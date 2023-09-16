import io
import sys
from unittest import mock

from test_base.test_base import AssignmentTester
from test_base.test_decorator import devin_test_decorator


class TestUi(AssignmentTester):
    def tearDown(self):
        try:
            del sys.modules['project.ui.user_interaction']
        except KeyError:
            pass

    @devin_test_decorator
    @mock.patch('builtins.input', side_effect=['Dan', '9', '40'])
    def test_1_name(self, mock_input, message):
        # test
        import project.ui.user_interaction as user_interaction
        expected_result = True
        real_result = user_interaction.is_name_valid('Alon')
        # verify
        message.explanation = {'value': 'INPUT_REQUEST_MISMATCH', 'params': {'order': 0}}
        self.assertEqualWithMessage(real_result, expected_result, msg=message)

    @devin_test_decorator
    @mock.patch('builtins.input', side_effect=['Dan', '9', '40'])
    def test_1_name_2(self, mock_input, message):
        # test
        import project.ui.user_interaction as user_interaction
        expected_result = False
        real_result = user_interaction.is_name_valid('A')
        # verify
        message.explanation = {'value': 'INPUT_REQUEST_MISMATCH', 'params': {'order': 1}}
        self.assertEqualWithMessage(real_result, expected_result, msg=message)

    @devin_test_decorator
    @mock.patch('builtins.input', side_effect=['Dan', '9', '40'])
    def test_1_name_3(self, mock_input, message):
        # test
        import project.ui.user_interaction as user_interaction
        expected_result = False
        real_result = user_interaction.is_name_valid('')
        # verify
        message.explanation = {'value': 'INPUT_REQUEST_MISMATCH', 'params': {'order': 2}}
        self.assertEqualWithMessage(real_result, expected_result, msg=message)

    @devin_test_decorator
    @mock.patch('builtins.input', side_effect=['Dan', '9', '40'])
    def test_2_board_size_1(self, mock_input, message):
        # test
        import project.ui.user_interaction as user_interaction
        expected_result = False
        real_result = user_interaction.is_board_size_valid(0)
        # verify
        message.explanation = {'value': 'INPUT_REQUEST_MISMATCH', 'params': {'order': 0}}
        self.assertEqualWithMessage(real_result, expected_result, msg=message)

    @devin_test_decorator
    @mock.patch('builtins.input', side_effect=['Dan', '9', '40'])
    def test_2_board_size_2(self, mock_input, message):
        # test
        import project.ui.user_interaction as user_interaction
        expected_result = False
        real_result = user_interaction.is_board_size_valid(-1)
        # verify
        message.explanation = {'value': 'INPUT_REQUEST_MISMATCH', 'params': {'order': 1}}
        self.assertEqualWithMessage(real_result, expected_result, msg=message)

    @devin_test_decorator
    @mock.patch('builtins.input', side_effect=['Dan', '9', '40'])
    def test_2_board_size_3(self, mock_input, message):
        # test
        import project.ui.user_interaction as user_interaction
        expected_result = True
        real_result = user_interaction.is_board_size_valid(7)
        # verify
        message.explanation = {'value': 'INPUT_REQUEST_MISMATCH', 'params': {'order': 2}}
        self.assertEqualWithMessage(real_result, expected_result, msg=message)

    @devin_test_decorator
    @mock.patch('builtins.input', side_effect=['Dan', '9', '40'])
    def test_3_number_of_mines_1(self,mock_input, message):
        # test
        import project.ui.user_interaction as user_interaction
        expected_result = False
        real_result = user_interaction.is_number_of_mines_valid(0, 5)
        # verify
        message.explanation = {'value': 'INPUT_REQUEST_MISMATCH', 'params': {'order': 0}}
        self.assertEqualWithMessage(real_result, expected_result, msg=message)

    @devin_test_decorator
    @mock.patch('builtins.input', side_effect=['Dan', '9', '40'])
    def test_3_number_of_mines_2(self, mock_input, message):
        # test
        import project.ui.user_interaction as user_interaction
        expected_result = False
        real_result = user_interaction.is_number_of_mines_valid(13, 5)
        # verify
        message.explanation = {'value': 'INPUT_REQUEST_MISMATCH', 'params': {'order': 1}}
        self.assertEqualWithMessage(real_result, expected_result, msg=message)

    @devin_test_decorator
    @mock.patch('builtins.input', side_effect=['Dan', '9', '40'])
    def test_3_number_of_mines_3(self, mock_input, message):
        # test
        import project.ui.user_interaction as user_interaction
        expected_result = True
        real_result = user_interaction.is_number_of_mines_valid(7, 5)
        # verify
        message.explanation = {'value': 'INPUT_REQUEST_MISMATCH', 'params': {'order': 2}}
        self.assertEqualWithMessage(real_result, expected_result, msg=message)

    @devin_test_decorator
    @mock.patch('sys.stdout', new_callable=io.StringIO)
    @mock.patch('builtins.input', side_effect=['Dan', '9', '40'])
    def test_full_interaction(self, mock_input, mock_stdout, message):
        # test
        import project.ui.user_interaction as user_interaction

        expected_result = ('Dan', 9, 40)
        real_result = user_interaction.register_user()
        # verify
        message.explanation = {'value': 'INPUT_REQUEST_MISMATCH', 'params': {'order': 0}}
        self.assertEqualWithMessage(real_result, expected_result, msg=message)
