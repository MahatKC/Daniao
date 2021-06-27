import unittest 
from railfence import rail_fence
from onetimepad import one_time_pad
from columnar import columnar


class railfence_tests(unittest.TestCase):
    def test_rail_fence(self):
        pass
        self.assertEqual(rail_fence("hermes"), "daniao")
class onetimepad_tests(unittest.TestCase):
    def test_onetimepad(self):
        pass
        self.assertEqual(one_time_pad("hermes"),"daniao")
class columnar_tests(unittest.TestCase):
    def test_columnar(self):
        pass
        self.assertEqual(columnar("hermes"))


if __name__ == "__main__":
    unittest.main()