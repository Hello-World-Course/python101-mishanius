import unittest
from unittest import mock
import io


class TestUi(unittest.TestCase):
    @mock.patch('sys.stdout', new_callable=io.StringIO)
    @mock.patch('builtins.input', side_effect=['Michael', '9', '3'])
    def test_sanity(self, mock_input, mock_stdout):
        import project.ui.user_interaction as test_file
        self.assertEqual(len(mock_input.call_args_list), 3, msg="בפרק זה נדרש לקבל 3 קלטים בדיוק מהמשתמש, להשתמש 3 פעמים בפונקציה input")
        self.assertEqual(mock_input.call_args_list[0].args[0], "Hello, whats your name?")
        self.assertEqual(mock_input.call_args_list[1].args[0], "Michael, please choose board size:")
        self.assertEqual(mock_input.call_args_list[2].args[0],
                         "Michael, for board size 9, choose number of mines to allocate:")
        self.assertEqual(test_file.name, 'Michael')
        self.assertEqual(test_file.board_size, 9)
        self.assertEqual(test_file.number_of_mines, 3)
