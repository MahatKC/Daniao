import unittest 
from railfence import rail_fence
from onetimepad import one_time_pad
from columnar import columnar

class railfence_tests(unittest.TestCase):
    def test_rail_fence_standard(self):
        self.assertEqual(rail_fence("hermes",2), "hreems")
    def test_rail_fence_identity_row(self):
        self.assertEqual(rail_fence("hermes",1), "hermes")
    def test_rail_fence_identity_column(self):
        self.assertEqual(rail_fence("hermes",6), "hermes")
    def test_rail_fence_higher_n(self):
        self.assertEqual(rail_fence("hermes",30), "hermes")
    def test_rail_fence_negative_n(self):
        self.assertEqual(rail_fence("hermes",-10), "")
    def test_rail_fence_zero_division(self):
        with self.assertRaises(ZeroDivisionError):
            rail_fence("hermes",0)
    def test_rail_fence_non_integer(self):
        with self.assertRaises(NameError):
            rail_fence("hermes","a")

class columnar_tests(unittest.TestCase):
    def test_columnar_standard(self):
        self.assertEqual(columnar("hermes","ab"),"hreems")
    def test_columnar_identity_row(self):
        self.assertEqual(columnar("hermes","a"),"hermes")
    def test_columnar_identity_column(self):
        self.assertEqual(columnar("hermes","abcdef"),"hermes")
    def test_columnar_identity_big_key(self):
        self.assertEqual(columnar("hermes","abcdefghijklmnopqrst"),"hermes")
    def test_columnar_unordered_key(self):
        self.assertEqual(columnar("attackpostponeduntiltwoamxyz", "dcabefg"),"ttnaaptmtsuoaodwcoixknlypetz")
    def test_columnar_unordered_key_tuple(self):
        self.assertEqual(columnar("attackpostponeduntiltwoamxyz", (4,3,1,2,5,6,7)),"ttnaaptmtsuoaodwcoixknlypetz")
    def test_columnar_unordered_key_list(self):
        self.assertEqual(columnar("attackpostponeduntiltwoamxyz", [4,3,1,2,5,6,7]),"ttnaaptmtsuoaodwcoixknlypetz")
    def test_columnar_empty_key(self):
        with self.assertRaises(ZeroDivisionError):
            columnar("hermes", "")
    def test_columnar_integer(self):
        with self.assertRaises(NameError):
            columnar("hermes",1234)

class onetimepad_tests(unittest.TestCase):
    def test_onetimepad_standard(self):
        self.assertEqual(one_time_pad("RAMSWARUPK","RANCHOBABA"),"iazudosuqk")
    def test_onetimepad_identity(self):
        self.assertEqual(one_time_pad("hermes","a"),"hermes")
    def test_onetimepad_caesar_case(self):
        self.assertEqual(one_time_pad("hermes","w"),"daniao")
    def test_onetimepad_empty_key(self):
        with self.assertRaises(ZeroDivisionError):
            one_time_pad("hermes", "")
    def test_onetimepad_invalid_key(self):
        with self.assertRaises(TypeError):
            one_time_pad("hermes", 2)
    
if __name__ == "__main__":
    unittest.main()