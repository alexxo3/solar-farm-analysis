import unittest
from src.utils import load_data

class TestUtils(unittest.TestCase):

    def test_load_data(self):
        data = load_data("data/solar_data.csv")
        self.assertFalse(data.empty)

if __name__ == "__main__":
    unittest.main()
