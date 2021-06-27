import unittest 
import caesar
from vigenere import vigenere
from monoalphabetic import monoalpha
from playfair import play_fair

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

class monoalphabetic_tests(unittest.TestCase):
    def test_monoalphabetic_standard(self):
        self.assertEqual(monoalpha("hermes","wxyzabcdefghijklmnopqrstuv"),"daniao")
    def test_monoalphabetic_identity(self):
        self.assertEqual(monoalpha("hermes","abcdefghijklmnopqrstuvwxyz"),"hermes")
    def test_monoalphabetic_upper_lower(self):
        self.assertEqual(monoalpha("heRMEs","wxyzAbcdefghijklmNOpqrstuv"), "daNIAo")

class playfair_tests(unittest.TestCase):
    def test_playfair_standard(self):
        self.assertEqual(play_fair("hermes","monarchy"),"cfnoil")
    def test_playfair_space_cypher(self):
        self.assertEqual(play_fair("Hide the gold in the tree stump","playfair example"),"Bmodzbxdnabekudmuixmmouvif")
    
if __name__ == "__main__":
    unittest.main()