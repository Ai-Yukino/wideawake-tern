# 🐍 Python standard library
import unittest
from os.path import join

# 🐍 External libraries
import polars as pl

# 🐍 Local module imports
from ai.testing import assert_frame_subset


class TestHub(unittest.TestCase):
    def setUp(self):
        self.hub = pl.scan_csv(join("..", "..", "data", "hub.tsv"), sep="\t")
        self.sample = pl.scan_csv(join("samples", "hub.tsv"), sep="\t")

    def test_shape(self):
        self.assertEqual(self.hub.shape, (1331, 6))

    def test_subset(self):
        self.assertEqual(assert_frame_subset(self.sample, self.hub), None)


if __name__ == "__main__":
    unittest.main()
