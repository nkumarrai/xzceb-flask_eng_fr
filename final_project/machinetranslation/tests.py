import unittest

from translator import english_to_french, french_to_english

class TestTranslator(unittest.TestCase):
    def test_e2f(self):
        self.assertEqual(english_to_french('hello'), 'bonjour')
        self.assertNotEqual(english_to_french('name'), 'bonjour')

    def test_f2e(self):
        self.assertEqual(french_to_english('bonjour'), 'hello')
        self.assertNotEqual(french_to_english('monsieur'), 'name')

if __name__ == '__main__':
    unittest.main()
