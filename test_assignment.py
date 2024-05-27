import unittest
from assignment import justify_text  # Importing justify_text from assignment.py

class TestJustifyText(unittest.TestCase):

    def setUp(self):
        self.paragraph = "This is a sample text but a complicated problem to be solved, so we are adding more text to see that it actually works."

    def test_width_15(self):
        width = 15
        expected_output = [
            "This    is    a",
            "sample text but",
            "a   complicated",
            "problem  to  be",
            "solved,  so  we",
            "are adding more",
            "text   to   see",
            "that         it",
            "actually works."
        ]
        self.assertEqual(justify_text(self.paragraph, width), expected_output)

    def test_width_20(self):
        width = 20
        expected_output = [
            "This  is  a   sample",
            "text      but      a",
            "complicated  problem",
            "to be solved, so  we",
            "are adding more text",
            "to   see   that   it",
            "actually      works."     
        ]
        self.assertEqual(justify_text(self.paragraph, width), expected_output)

    def test_width_25(self):
        width = 25
        expected_output = [
            "This is a sample text but",
            "a complicated problem  to",
            "be  solved,  so  we   are",
            "adding more text  to  see",
            "that it  actually  works."
        ]
        self.assertEqual(justify_text(self.paragraph, width), expected_output)

    def test_width_30(self):
        width = 30
        expected_output = [
            "This is a sample  text  but  a",
            "complicated  problem   to   be",
            "solved, so we are adding  more",
            "text to see that  it  actually",
            "works.                        "
        ]
        self.assertEqual(justify_text(self.paragraph, width), expected_output)

if __name__ == '__main__':
    unittest.main()