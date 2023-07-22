import unittest
from translator import english_to_french, french_to_english

class TestForE2F(unittest.TestCase):
    def test_1(self):
        self.assertEqual(english_to_french("hello"), "bonjour")

class TestForF2E(unittest.TestCase):
    def test_2(self):
        self.assertEqual(french_to_english("bonjour"), "hello")

unittest.main()