# 🐍 Python standard library
import unittest
from os.path import join

# 🐍 External libraries
import polars as pl

# 🐍 Local module imports
from ai.testing import assert_frame_subset


class TestHub(unittest.TestCase):
    def setUp(self):
        self.availability = pl.scan_csv(
            join("..", "..", "data", "tsv", "availability.tsv"), sep="\t"
        )
        self.samples = pl.scan_csv(join("samples", "tsv", "availability.tsv"), sep="\t")

    def test_shape(self):
        self.assertEqual(self.availability.collect().shape, (1331, 7))

    def test_subset(self):
        self.assertEqual(
            assert_frame_subset(self.samples, self.availability),
            None,
        )


if __name__ == "__main__":
    unittest.main()
