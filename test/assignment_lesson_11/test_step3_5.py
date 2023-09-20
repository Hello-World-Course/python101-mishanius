import sys

from test_base.test_base import AssignmentTester
from test_base.test_decorator import devin_test_decorator


class TestUi(AssignmentTester):

        def tearDown(self):
            try:
                del sys.modules['project.ui.user_interaction']
            except KeyError:
                pass

        @devin_test_decorator
        def test_command_parsing(self, message):
            # test
            import project.ui.board_ui as board_ui

            expected_result = ("flag", ['4A'])
            real_result = board_ui.parse_cmd('flag 4A')
            # verify
            message.explanation = {'value': 'CODE_MISMATCH'}
            self.assertEqualWithMessage(real_result, expected_result, msg=message)

        @devin_test_decorator
        def test_command_parsing_2(self, message):
            # test
            ######
            import project.ui.board_ui as board_ui
            expected_result = ("test", ['1', '23', '4', '5', '67', '8'])
            real_result = board_ui.parse_cmd('test 1 23 4 5 67 8')
            # verify
            message.explanation = {'value': 'CODE_MISMATCH'}
            self.assertEqualWithMessage(real_result, expected_result, msg=message)

        @devin_test_decorator
        def test_is_on_board_1(self, message):
            # test
            ######
            import project.board.board_functions as board_functions
            board = [[None for _ in range(10)] for _ in range(10)]
            expected_result = True
            real_result = board_functions.is_on_board(0, 9, board)
            # verify
            message.explanation = {'value': 'CODE_MISMATCH'}
            self.assertEqualWithMessage(real_result, expected_result, msg=message)

        @devin_test_decorator
        def test_is_on_board_2(self, message):
            # test
            ######
            import project.board.board_functions as board_functions
            board = [[None for _ in range(10)] for _ in range(10)]
            expected_result = False
            real_result = board_functions.is_on_board(0, -9, board)
            # verify
            message.explanation = {'value': 'CODE_MISMATCH'}
            self.assertEqualWithMessage(real_result, expected_result, msg=message)

        @devin_test_decorator
        def test_is_on_board_3(self, message):
            # test
            ######
            import project.board.board_functions as board_functions
            board = [[None for _ in range(10)] for _ in range(10)]
            expected_result = False
            real_result = board_functions.is_on_board(90, 5, board)
            # verify
            message.explanation = {'value': 'CODE_MISMATCH'}
            self.assertEqualWithMessage(real_result, expected_result, msg=message)

        @devin_test_decorator
        def test_is_on_board_4(self, message):
            # test
            ######
            import project.board.board_functions as board_functions
            board = [[None for _ in range(10)] for _ in range(10)]
            expected_result = False
            real_result = board_functions.is_on_board(10, 9, board)
            # verify
            message.explanation = {'value': 'CODE_MISMATCH'}
            self.assertEqualWithMessage(real_result, expected_result, msg=message)

        @devin_test_decorator
        def test_is_on_board_5(self, message):
            # test
            ######
            import project.board.board_functions as board_functions
            board = [[None for _ in range(10)] for _ in range(10)]
            expected_result = True
            real_result = board_functions.is_on_board(9, 9, board)
            # verify
            message.explanation = {'value': 'CODE_MISMATCH'}
            self.assertEqualWithMessage(real_result, expected_result, msg=message)

        @devin_test_decorator
        def test_safe_set_value_1(self, message):
            # test
            ######
            import project.board.board_functions as board_functions
            board = [[None for _ in range(10)] for _ in range(10)]
            expected_result = True
            real_result = board_functions.safe_set_value(0, 5, 9, board)
            # verify
            message.explanation = {'value': 'CODE_MISMATCH'}
            self.assertEqualWithMessage(real_result, expected_result, msg=message)

        @devin_test_decorator
        def test_safe_set_value_2(self, message):
            # test
            ######
            import project.board.board_functions as board_functions
            board = [[None for _ in range(10)] for _ in range(10)]
            board_functions.safe_set_value(0, 5, 9, board)
            expected_result = 9
            real_result = board[0][5]
            # verify
            message.explanation = {'value': 'CODE_MISMATCH'}
            self.assertEqualWithMessage(real_result, expected_result, msg=message)

        @devin_test_decorator
        def test_safe_set_value_3(self, message):
            # test
            ######
            import project.board.board_functions as board_functions
            board = [[None for _ in range(10)] for _ in range(10)]
            expected_result = False
            real_result = board_functions.safe_set_value(0, 10, 9, board)
            # verify
            message.explanation = {'value': 'CODE_MISMATCH'}
            self.assertEqualWithMessage(real_result, expected_result, msg=message)
