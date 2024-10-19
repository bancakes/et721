"""
Delvin Gonzlez
Sep 30, unit testing 'input' data
"""
import unittest
import unittest.mock 
import patch
import io
import studentgrade

class TestMainFunction(unittest.TestCase):
    # test with valid inputs
    @patch('builtins.input', side_effect = ['3','85','90','75'])
    @patch('sys.stdout', new_callable=io.StringIO)

    def test_valid_input(self, mock_stdout, mock_input):
        # call the function 'main()' from 'studentgrade.py'
        studentgrade.main()

        # retrieve the capture output
        output = mock_stdout.getvalue()

        # check if the printed output is as expected 
        self.assertIn("The class average is 78.50", output)
     
     # test with valid inputs
    @patch('builtins.input', side_effect = ['-1','85','72'])
    @patch('sys.stdout', new_callable=io.StringIO)

    def test_invalid_and_valid_input(self, mock_stdout, mock_input):
        # call the function 'main()' from 'studentgrade.py'
        studentgrade.main()

        # retrieve the capture output
        output = mock_stdout.getvalue()

        # check if the printed output is as expected 
        self.assertIn("Invalid input.\n", output)

     # test with valid inputs
    @patch('builtins.input', side_effect = ['2','105','82','-10','7'])
    @patch('sys.stdout', new_callable=io.StringIO)

    def test_invalid_grade(self, mock_stdout, mock_input):
        # call the function 'main()' from 'studentgrade.py'
        studentgrade.main()

        # retrieve the capture output
        output = mock_stdout.getvalue()

        # check if the printed output is as expected 
        self.assertIn("Grade must be between 0 and 100.", output)
        self.assertIn("The class average is 76.00.", output)

if __name__ == "__main__":
    unittest.main()