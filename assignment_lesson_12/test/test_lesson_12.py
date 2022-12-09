<<<<<<< HEAD
import json
=======
>>>>>>> origin/assignment_lesson_12
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

    def assertFunctionCall(self, file, functionName, args, expectedResult):
        message = {
            "functionName": functionName,
            "file": file.__name__,
            "args": args,
            "expectedResult": str(expectedResult),
            "realResult": None,
            "exception": None
        }
        real_result = None
        try:
            real_result = getattr(file, functionName)(*args)
            message["realResult"] = str(real_result)
        except Exception as e:
            message["exception"] = str(e)
        self.assertEqual(expectedResult, real_result, msg=f"@@@PREFIX@@@{json.dumps(message)}@@@SUFFIX@@@")

    @mock.patch('builtins.input', side_effect=["i" for _ in range(1000)])
    def test_board_functions_create_empty_board(self, *args):
        import project.game.board_functions as board_functions
        self.assertFunctionCall(board_functions, "create_empty_board", [2], [[1 for _ in range(2)] for _ in range(2)])

    @mock.patch('builtins.input', side_effect=['Dan', '9', '40'])
    def test_coordinate_conversion(self, *args):
        import project.ui.board_ui as test_file
        self.assertFunctionCall(test_file, "convert_coords", ["23A"], (21, 0))

    @mock.patch('builtins.input', side_effect=["i" for _ in range(1000)])
    def test_board_functions_draw_board(self, *args):
        import project.game.board_functions as board_functions
        import project.ui.board_ui as board_ui
        board = board_functions.create_empty_board(2, None)
        drawn_board = board_ui.draw_board(board, 20)
        self.assertEqual(drawn_board, '   A B \n0 |_|_|\n1 |_|_|\n')
