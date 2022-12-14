# 🐍 Python standard library
import unittest
from os.path import join

# 🐍 External libraries
import polars as pl

# 🐍 Local module imports
from ai.testing import assert_frame_subset


class TestHub(unittest.TestCase):
    def setUp(self):
        self.hub = pl.scan_csv(join("..", "..", "data", "tsv", "hub.tsv"), sep="\t")
        self.samples = pl.scan_csv(join("samples", "tsv", "hub.tsv"), sep="\t")

    def test_shape(self):
        self.assertEqual(self.hub.collect().shape, (1329, 5))

    def test_subset(self):
        self.assertEqual(assert_frame_subset(self.samples, self.hub), None)


if __name__ == "__main__":
    unittest.main()
