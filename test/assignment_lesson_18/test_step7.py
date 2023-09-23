from test_base.test_base import AssignmentTester
from test_base.test_decorator import devin_test_decorator

EXPECTED_BOARD_1_1 = """   A B C D 
0 |_|1| | |
1 |_|1| | |
2 |_|2|1| |
3 |_|_|1| |
"""

EXPECTED_BOARD_1_2 = """   A B C D 
0 |1|_|_|_|
1 |_|_|_|_|
2 |_|_|_|_|
3 |_|_|_|_|
"""

EXPECTED_BOARD_2 = """   A B C D 
0 | | | | |
1 | | | | |
2 |1|1| | |
3 |_|1| | |
"""


class TestStep7(AssignmentTester):

    @devin_test_decorator
    def test_click_with_visit(self, message):
        # test #
        #######
        import project.ui.terminal as test_file
        import project.ui.board_ui as board_ui
        from project.model.mine import Mine

        board = test_file.Board(4)
        board[1][0] = Mine(1, 0)
        board[3][1] = Mine(3, 1)
        # set cell values
        board[0][0].set_value(1)
        board[0][1].set_value(1)
        board[1][1].set_value(1)
        board[2][0].set_value(1)
        board[2][1].set_value(2)
        board[2][2].set_value(1)
        board[3][0].set_value(1)
        board[3][2].set_value(1)

        board.click(1, 2)
        result = board_ui.draw_board(board, 20)
        # verify
        message.explanation = {'value': 'MISMATCH'}
        self.assertEqualWithMessage(EXPECTED_BOARD_1_1, result, msg=message)

    @devin_test_decorator
    def test_visit_neighbors_1_1(self, message):
        # test #
        #######
        import project.ui.terminal as test_file
        import project.ui.board_ui as board_ui
        from project.model.mine import Mine

        board = test_file.Board(4)
        board[1][0] = Mine(1, 0)
        board[3][1] = Mine(3, 1)

        # set cell values
        board[0][0].set_value(1)
        board[0][1].set_value(1)
        board[1][1].set_value(1)
        board[2][0].set_value(1)
        board[2][1].set_value(2)
        board[2][2].set_value(1)
        board[3][0].set_value(1)
        board[3][2].set_value(1)

        board.visit_neighbors(board[1][2])
        result = board_ui.draw_board(board, 20)
        # verify
        message.explanation = {'value': 'MISMATCH'}
        self.assertEqualWithMessage(EXPECTED_BOARD_1_1, result, msg=message)

    @devin_test_decorator
    def test_visit_neighbors_1_2(self, message):
        # test #
        #######
        import project.ui.terminal as terminal
        import project.ui.board_ui as board_ui
        from project.model.mine import Mine

        board = terminal.Board(4)
        board[1][0] = Mine(1, 0)
        board[3][1] = Mine(3, 1)

        # set cell values
        board[0][0].set_value(1)
        board[0][1].set_value(1)
        board[1][1].set_value(1)
        board[2][0].set_value(1)
        board[2][1].set_value(2)
        board[2][2].set_value(1)
        board[3][0].set_value(1)
        board[3][2].set_value(1)

        board.visit_neighbors(board[0][0])
        result = board_ui.draw_board(board, 20)
        # verify
        message.explanation = {'value': 'MISMATCH'}
        self.assertEqualWithMessage(EXPECTED_BOARD_1_2, result, msg=message)

    @devin_test_decorator
    def test_visit_neighbors_2(self, message):
        # test
        #######
        import project.ui.terminal as test_file
        import project.ui.board_ui as board_ui
        from project.model.mine import Mine

        board = test_file.Board(4)
        board[3][0] = Mine(3, 0)

        # set cell values
        board[2][0].set_value(1)
        board[2][1].set_value(1)
        board[3][1].set_value(1)

        board.visit_neighbors(board[3][2])
        result = board_ui.draw_board(board, 20)
        # verify
        message.explanation = {'value': 'MISMATCH'}
        self.assertEqualWithMessage(EXPECTED_BOARD_2, result, msg=message)
