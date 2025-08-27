from main import suma,resta

import unittest


class TestPrueba(unittest.TestCase):
    def test_suma(self):
        self.assertEqual(suma(2,3), 5)
class TestResta(unittest.TestCase):
    def test_resta(self):
        self.assertEqual(resta(5,2), 3)



if __name__ == "__main__":
    unittest.main()