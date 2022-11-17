import io
import unittest
from contextlib import redirect_stdout


class AssignmentOneTest(unittest.TestCase):

    def test_execute_std_out(self):
        output_holder = io.StringIO()
        with redirect_stdout(output_holder):
            import assignment_lesson_4.helloWorld
            print_out = output_holder.getvalue()
            self.assertEqual(print_out, "Hello World I love Python!\n")
