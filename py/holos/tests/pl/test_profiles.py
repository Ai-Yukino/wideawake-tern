# 🐍 Python standard library
import unittest
from os.path import join

# 🐍 External libraries
import polars as pl

# 🐍 Local module imports
from ai.testing import assert_frame_subset


class TestHub(unittest.TestCase):
    def setUp(self):
        self.hub = pl.scan_csv(join("..", "..", "data", "profiles.tsv"), sep="\t")
        self.sample = pl.scan_csv(join("samples", "profiles.tsv"), sep="\t")

    def test_shape(self):
        self.assertEqual(self.hub.collect().shape, (1331, 9))

    def test_subset(self):
        self.assertEqual(assert_frame_subset(self.sample, self.hub), None)


if __name__ == "__main__":
    unittest.main()
