# 🐍 Python standard library
import unittest
import os.path

# 🐍 External libraries
from pandas.testing import assert_frame_equal
import pandas as pd

# 🐍 Local module imports
# None


class TestDataWithPandas(unittest.TestCase):
    def setUp(self):
        path = os.path.join("..", "..", "data", "pleistocene_hub", "data.tsv")
        self.df = pd.read_csv(path, sep="\t").sort_values(by="name")

    def test_head_tail(self):
        path = os.path.join("samples", "head_tail.tsv")
        df = pd.read_csv(path, sep="\t").sort_values(by="name")

        head_difference = assert_frame_equal(df.head(), self.df.head())
        self.assertEqual(head_difference, None)

        tail_difference = assert_frame_equal(df.tail(), self.df.tail())
        self.assertEqual(tail_difference, None)


if __name__ == "__main__":
    unittest.main()
