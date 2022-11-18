import sys
import unittest
from unittest import mock
import io


class TestUi(unittest.TestCase):
    def tearDown(self):
        try:
            del sys.modules['project.ui.user_interaction']
        except KeyError:
            pass

    @mock.patch('sys.stdout', new_callable=io.StringIO)
    @mock.patch('builtins.input', side_effect=['M', '9', '3'])
    def test_step2_wrong_name(self, mock_input, mock_stdout):
        import project.ui.user_interaction as test_file
        self.assertEqual(test_file.name, None)
        self.assertEqual(test_file.board_size, None)
        self.assertEqual(test_file.number_of_mines, None)
        self.assertEqual(mock_stdout.getvalue(), "Your name is too short\n")

    @mock.patch('sys.stdout', new_callable=io.StringIO)
    @mock.patch('builtins.input', side_effect=['Dan', '0'])
    def test_step2_wrong_board_size(self, mock_input, mock_stdout):
        import project.ui.user_interaction as test_file
        self.assertEqual(test_file.name, 'Dan')
        self.assertEqual(test_file.board_size, None)
        self.assertEqual(test_file.number_of_mines, None)
        self.assertEqual(mock_stdout.getvalue(), "Dan you entered illegal board size\n")

    @mock.patch('sys.stdout', new_callable=io.StringIO)
    @mock.patch('builtins.input', side_effect=['Dan', '-2'])
    def test_step2_wrong_board_size_negative(self, mock_input, mock_stdout):
        import project.ui.user_interaction as test_file
        self.assertEqual(test_file.name, 'Dan')
        self.assertEqual(test_file.board_size, None)
        self.assertEqual(test_file.number_of_mines, None)
        self.assertEqual(mock_stdout.getvalue(), "Dan you entered illegal board size\n")

    @mock.patch('sys.stdout', new_callable=io.StringIO)
    @mock.patch('builtins.input', side_effect=['Dan', '6', '0'])
    def test_step2_wrong_number_of_mines_too_low(self, mock_input, mock_stdout):
        import project.ui.user_interaction as test_file
        self.assertEqual(test_file.name, 'Dan')
        self.assertEqual(test_file.board_size, 6)
        self.assertEqual(test_file.number_of_mines, None)
        self.assertEqual(mock_stdout.getvalue(), "Dan you entered illegal number of mines\n")

    @mock.patch('sys.stdout', new_callable=io.StringIO)
    @mock.patch('builtins.input', side_effect=['Dan', '6', '19'])
    def test_step2_wrong_number_of_mines_too_high(self, mock_input, mock_stdout):
        import project.ui.user_interaction as test_file
        self.assertEqual(test_file.name, 'Dan')
        self.assertEqual(test_file.board_size, 6)
        self.assertEqual(test_file.number_of_mines, None)
        self.assertEqual(mock_stdout.getvalue(), "Dan you entered illegal number of mines\n")

    @mock.patch('sys.stdout', new_callable=io.StringIO)
    @mock.patch('builtins.input', side_effect=['Dan', '6', '1'])
    def test_step2_all_correct(self, mock_input, mock_stdout):
        import project.ui.user_interaction as test_file
        self.assertEqual(test_file.name, 'Dan')
        self.assertEqual(test_file.board_size, 6)
        self.assertEqual(test_file.number_of_mines, 1)
