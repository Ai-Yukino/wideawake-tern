# 🐍 Python standard library
import unittest
from os.path import join
from itertools import chain

# 🐍 External libraries
from pandas.testing import assert_frame_equal
import pandas as pd

# 🐍 Local module imports
# None


class TestDataWithPandas(unittest.TestCase):
    def setUp(self):
        path = join("..", "..", "..", "data", "holocene_hub" + ".tsv")
        self.df = pd.read_csv(path, sep="\t")

        self.num_rows = 1337

    def test_head_tail(self):
        path = join("samples", "head_tail.tsv")
        df = pd.read_csv(path, sep="\t").set_index(
            chain(range(0, 5), range(self.num_rows - 5, self.num_rows))
        )

        head_difference = assert_frame_equal(df.head(), self.df.head())
        self.assertEqual(head_difference, None)

        tail_difference = assert_frame_equal(df.tail(), self.df.tail())
        self.assertEqual(tail_difference, None)


if __name__ == "__main__":
    unittest.main()
