# 🐍 Standard python library
import unittest
from os.path import join

# 🐍 External libraries
import pandas as pd

# 🐍 Local module imports
from ai.testing import assert_rows_subset


class TestDataWithPandas(unittest.TestCase):
    def setUp(self):
        path = join("..", "..", "..", "data", "profiles.tsv")
        self.df = pd.read_csv(path, sep="\t")

    def test_unordered(self):
        path = join("samples", "unordered.tsv")
        df = pd.read_csv(path, sep="\t")
        self.assertTrue(assert_rows_subset(df, self.df))
