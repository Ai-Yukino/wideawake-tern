"""
Utilities functions to assist with unit tests
"""

# 🐍 Python standard library
# None

# 🐍 External libraries
import polars as pl
from polars.testing import assert_frame_equal

# 🐍 Local module imports
# None


def assert_frame_subset(left, right) -> None:
    """
    Raise detailed AssertionError if `left` is not a subset of `right`.

    Parameters
    ----------
    subset
        the supposed subset dataframe
    superset
        the supposed superset dataframe
    """

    assert_frame_equal(
        left.join(right, on=left.columns, how="anti"),
        pl.DataFrame(
            columns=[(name, t) for (name, t) in zip(left.columns, left.dtypes)]
        ).lazy(),
    )
