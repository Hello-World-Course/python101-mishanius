import sys
import unittest
from unittest import mock
import io


class TestUi(unittest.TestCase):

    def tearDown(self):
        try:
            del sys.modules['src.ui.user_interaction']
        except KeyError:
            pass

    @mock.patch('builtins.input', side_effect=['Dan', '9', '40'])
    def test_name(self, *args):
        import project.ui.user_interaction as test_file
        self.assertEqual(test_file.is_name_valid("Alon"), True)
        self.assertEqual(test_file.is_name_valid("A"), False)

    @mock.patch('builtins.input', side_effect=['Dan', '9', '40'])
    def test_board_size(self, *args):
        import project.ui.user_interaction as test_file
        self.assertEqual(test_file.is_board_size_valid(0), False)
        self.assertEqual(test_file.is_board_size_valid(-1), False)
        self.assertEqual(test_file.is_board_size_valid(7), True)

    @mock.patch('builtins.input', side_effect=['Dan', '9', '40'])
    def test_number_of_mines(self, *args):
        import project.ui.user_interaction as test_file
        self.assertEqual(test_file.is_number_of_mines_valid(0, 5), False)
        self.assertEqual(test_file.is_number_of_mines_valid(13, 5), True)
        self.assertEqual(test_file.is_number_of_mines_valid(7, 5), True)

    @mock.patch('sys.stdout', new_callable=io.StringIO)
    @mock.patch('builtins.input', side_effect=['Dan', '9', '40'])
    def test_full_interaction(self, mock_input, mock_stdout):
        import project.ui.user_interaction as test_file
        name, board_size, number_of_mines = test_file.register_user()
        self.assertEqual(name, 'Dan')
        self.assertEqual(board_size, 9)
        self.assertEqual(number_of_mines, 40)
