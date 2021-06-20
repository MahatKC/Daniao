import unittest 
import caesar

class caesar_tests(unittest.TestCase):
    def test_hermes(self):
        self.assertEqual(caesar.rot_n("hermes", 22), "daniao")

if __name__ == "__main__":
    unittest.main()