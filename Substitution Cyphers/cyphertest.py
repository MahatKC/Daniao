import unittest 
import caesar
from vigenere import vigenere

class caesar_tests(unittest.TestCase):
    def test_caesar_all_lower(self):
        self.assertEqual(caesar.rot_n("hermes", 22), "daniao")
    def test_caesar_all_upper(self):  
        self.assertEqual(caesar.rot_n("HERMES", 22), "DANIAO")
    def test_caesar_negative_n(self):
        self.assertEqual(caesar.rot_n("hermes",-4), "daniao")
    def test_caesar_identity(self):
        self.assertEqual(caesar.rot_n("hermes",0), "hermes")

class vigenere_tests(unittest.TestCase):
    def test_vigenere_standard(self):
        self.assertEqual(vigenere("hermes", "w"), "daniao")
    def test_vigenere_identity(self):
        self.assertEqual(vigenere("hermes","aaa"),"hermes")

if __name__ == "__main__":
    unittest.main()