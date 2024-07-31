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
    def test_1_name(self, mock_input, message):
        # test
        import project.ui.user_interaction as user_interaction
        expected_result = True
        real_result = user_interaction.is_name_valid('Alon')
        # verify
        message.explanation = {'value': 'CODE_MISMATCH'}
        self.assertEqualWithMessage(real_result, expected_result, msg=message)

    @devin_test_decorator
    def test_1_name_2(self, mock_input, message):
        # test
        import project.ui.user_interaction as user_interaction
        expected_result = False
        real_result = user_interaction.is_name_valid('A')
        # verify
        message.explanation = {'value': 'CODE_MISMATCH'}
        self.assertEqualWithMessage(real_result, expected_result, msg=message)

    @devin_test_decorator
    def test_1_name_3(self, mock_input, message):
        # test
        import project.ui.user_interaction as user_interaction
        expected_result = False
        real_result = user_interaction.is_name_valid('')
        # verify
        message.explanation = {'value': 'CODE_MISMATCH'}
        self.assertEqualWithMessage(real_result, expected_result, msg=message)

    @devin_test_decorator
    def test_2_board_size_1(self, mock_input, message):
        # test
        import project.ui.user_interaction as user_interaction
        expected_result = False
        real_result = user_interaction.is_board_size_valid(0)
        # verify
        message.explanation = {'value': 'CODE_MISMATCH'}
        self.assertEqualWithMessage(real_result, expected_result, msg=message)

    @devin_test_decorator
    def test_2_board_size_2(self, mock_input, message):
        # test
        import project.ui.user_interaction as user_interaction
        expected_result = False
        real_result = user_interaction.is_board_size_valid(-1)
        # verify
        message.explanation = {'value': 'CODE_MISMATCH'}
        self.assertEqualWithMessage(real_result, expected_result, msg=message)

    @devin_test_decorator
    def test_2_board_size_3(self, mock_input, message):
        # test
        import project.ui.user_interaction as user_interaction
        expected_result = True
        real_result = user_interaction.is_board_size_valid(7)
        # verify
        message.explanation = {'value': 'CODE_MISMATCH'}
        self.assertEqualWithMessage(real_result, expected_result, msg=message)

    @devin_test_decorator
    def test_3_number_of_mines_1(self, mock_input, message):
        # test
        import project.ui.user_interaction as user_interaction
        expected_result = False
        real_result = user_interaction.is_number_of_mines_valid(5, 0)
        # verify
        message.explanation = {'value': 'CODE_MISMATCH'}
        self.assertEqualWithMessage(real_result, expected_result, msg=message)

    @devin_test_decorator
    def test_3_number_of_mines_2(self, mock_input, message):
        # test
        import project.ui.user_interaction as user_interaction
        expected_result = False
        real_result = user_interaction.is_number_of_mines_valid(5, 13)
        # verify
        message.explanation = {'value': 'CODE_MISMATCH'}
        self.assertEqualWithMessage(real_result, expected_result, msg=message)

    @devin_test_decorator
    def test_3_number_of_mines_3(self, mock_input, message):
        # test
        import project.ui.user_interaction as user_interaction
        expected_result = True
        real_result = user_interaction.is_number_of_mines_valid(5, 7)
        # verify
        message.explanation = {'value': 'CODE_MISMATCH'}
        self.assertEqualWithMessage(real_result, expected_result, msg=message)

    @devin_test_decorator
    @mock.patch('sys.stdout', new_callable=io.StringIO)
    @mock.patch('builtins.input', side_effect=['D', '9', '40'])
    def test_full_interaction_wrong_name_verify_return(self, mock_input, mock_stdout, message):
        # test
        import project.ui.user_interaction as user_interaction
        real_result = user_interaction.register_user()
        # verify
        expected_result = (None, None, None)
        self.assertEqualWithMessage(real_result, expected_result, msg=message)

    @devin_test_decorator
    @mock.patch('sys.stdout', new_callable=io.StringIO)
    @mock.patch('builtins.input', side_effect=['D', '9', '40'])
    def test_full_interaction_wrong_name_verify_output(self, mock_input, mock_stdout, message):
        # test
        import project.ui.user_interaction as user_interaction
        user_interaction.register_user()
        # verify
        expected_result = "Your name is too short\n"
        real_result = mock_stdout.getvalue()
        self.assertEqualWithMessage(real_result, expected_result, msg=message)

    @devin_test_decorator
    @mock.patch('sys.stdout', new_callable=io.StringIO)
    @mock.patch('builtins.input', side_effect=['Dan', '0', '40'])
    def test_full_interaction_wrong_board_size_verify_return(self, mock_input, mock_stdout, message):
        # test
        import project.ui.user_interaction as user_interaction
        real_result = user_interaction.register_user()
        # verify
        expected_result = (None, None, None)
        self.assertEqualWithMessage(real_result, expected_result, msg=message)

    @devin_test_decorator
    @mock.patch('sys.stdout', new_callable=io.StringIO)
    @mock.patch('builtins.input', side_effect=['Dan', '0', '40'])
    def test_full_interaction_wrong_board_size_verify_output(self, mock_input, mock_stdout, message):
        # test
        import project.ui.user_interaction as user_interaction
        user_interaction.register_user()
        # verify
        expected_result = "Dan, you have entered illegal board size\n"
        real_result = mock_stdout.getvalue()
        self.assertEqualWithMessage(real_result, expected_result, msg=message)

    @devin_test_decorator
    @mock.patch('sys.stdout', new_callable=io.StringIO)
    @mock.patch('builtins.input', side_effect=['Dan', '9', '41'])
    def test_full_interaction_wrong_mines_verify_return(self, mock_input, mock_stdout, message):
        # test
        import project.ui.user_interaction as user_interaction
        real_result = user_interaction.register_user()
        # verify
        expected_result = (None, None, None)
        self.assertEqualWithMessage(real_result, expected_result, msg=message)

    @devin_test_decorator
    @mock.patch('sys.stdout', new_callable=io.StringIO)
    @mock.patch('builtins.input', side_effect=['Dan', '9', '41'])
    def test_full_interaction_wrong_mines_verify_output(self, mock_input, mock_stdout, message):
        # test
        import project.ui.user_interaction as user_interaction
        user_interaction.register_user()
        # verify
        expected_result = "Dan, you have entered illegal number of mines\n"
        real_result = mock_stdout.getvalue()
        self.assertEqualWithMessage(real_result, expected_result, msg=message)

    @devin_test_decorator
    @mock.patch('sys.stdout', new_callable=io.StringIO)
    @mock.patch('builtins.input', side_effect=['i' for i in range(1000)])
    def test_0_verify_no_input(self, mock_input, mock_stdout, message):
        message.explanation = {'value': "UNNECESSARY_INPUT"}
        try:
            import project.ui.user_interaction as user_interaction
            number_of_times_input_was_called = mock_input.call_count
        except Exception as e:
            # If we have exception it means that something is running in file
            number_of_times_input_was_called = 1
        # we don't want to show the fake input we provide here neto to prevent waiting
        message.input_values = None
        # This supposed to assertEqual and not assertEqualWithMessage on purpose
        self.assertEqual(0, number_of_times_input_was_called,
                         msg=message)