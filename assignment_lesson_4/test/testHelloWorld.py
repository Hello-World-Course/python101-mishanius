import importlib
import io
import json
import unittest
from contextlib import redirect_stdout


class AssignmentOneTest(unittest.TestCase):

    def assertFileImport(self, fileName):
        message = {
            "functionName": None,
            "file": fileName,
            "args": None,
            "expectedResult": str("Hello World I love Python!\n"),
            "realResult": None,
            "exception": None
        }
        try:
            output_holder = io.StringIO()
            with redirect_stdout(output_holder):
                importlib.import_module(fileName, package=None)
                print_out = output_holder.getvalue()
                message["realResult"] = str(print_out)
        except Exception as e:
            message["exception"] = str(e)
        self.assertEqual(print_out, "Hello World I love Python!\n", msg=f"@@@PREFIX@@@{json.dumps(message)}@@@SUFFIX@@@")

    def test_execute_std_out(self):
        self.assertFileImport("assignment_lesson_4.helloWorld")