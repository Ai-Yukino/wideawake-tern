# 🐍 Python standard library
import unittest
from os.path import join

# 🐍 External libraries
import polars as pl

# 🐍 Local module imports
from ai.testing import assert_frame_subset


class TestHub(unittest.TestCase):
    def setUp(self):
        self.profiles = pl.scan_csv(
            join("..", "..", "data", "tsv", "profiles.tsv"), sep="\t"
        )
        self.samples = pl.scan_csv(join("samples", "tsv", "profiles.tsv"), sep="\t")

    def test_shape(self):
        self.assertEqual(self.profiles.collect().shape, (1331, 9))

    def test_subset(self):
        self.assertEqual(
            assert_frame_subset(self.samples, self.profiles),
            None,
        )


if __name__ == "__main__":
    unittest.main()

    # profiles = pl.scan_csv(join("..", "..", "data", "tsv", "profiles.tsv"), sep="\t")
    # samples = pl.scan_csv(join("samples", "tsv", "profiles.tsv"), sep="\t")

    # difference = samples.join(profiles, on=samples.columns, how="anti")

    # print_vns(difference)
