import unittest
from justify import justify_text

class TestJustifyText(unittest.TestCase):
    
    def test_basic_case(self):
        paragraph = "This is a sample text but a complicated problem to be solved, so we are adding more text to see that it actually works."
        width = 20
        expected = [
            "This  is  a   sample",
            "text      but      a",
            "complicated  problem",
            "to be solved, so  we",
            "are adding more text",
            "to   see   that   it",
            "actually      works."
        ]
        result = justify_text(paragraph, width)
        self.assertEqual(result, expected)

if _name_ == '_main_':
    unittest.main()